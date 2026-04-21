"""Build the architecture-focused GH-300 variant from the base gh-300.json.

Produces:
  courses/gh-300-architecture.json
  courses/gh-300-architecture-outline.md
  courses/gh-300-architecture-full.md

Strategy:
  1. Drop a curated set of demos / prompts (~37 min) that overlap or are smaller value.
  2. Insert a new "Under the Hood: How Copilot Works" chapter (37 min) right
     after Fundamentals, containing 6 sections of whiteboard-style narration:
       - Architecture Setup                       (3 min Narration)
       - Stateless LLM Core                       (8 min Narration)
       - Conversation Memory & Context Window     (8 min Narration)
       - RAG & Workspace Grounding                (7 min Narration)
       - Agents, Tools, and MCP                   (8 min Narration)
       - Architecture Reflection                  (3 min Prompt)
  3. Total stays at 180 minutes.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "courses" / "gh-300.json"
OUT_JSON = ROOT / "courses" / "gh-300-architecture.json"
OUT_OUTLINE = ROOT / "courses" / "gh-300-architecture-outline.md"
OUT_FULL = ROOT / "courses" / "gh-300-architecture-full.md"

# Section titles to remove from the base course (37 min total)
DROP_TITLES = {
    "Audience Check-In",                # 2 min Prompt
    "Demo Strategy Introduction",       # 3 min Narration
    "Terminal Inline Chat",             # 3 min Demo
    "Generate Sample Data with Inline Chat",  # 7 min Demo
    "Workflow Impact Check",            # 3 min Prompt
    "Plan Agent: Test Strategy",        # 8 min Demo
    "Testing Reflection",               # 2 min Prompt
    "Custom Instructions Demo",         # 6 min Demo
    "Responsible AI Risk Poll",         # 3 min Prompt
}

# ------------------------------------------------------------------
# New "Under the Hood" architecture chapter
# ------------------------------------------------------------------

ARCH_CHAPTER = {
    "title": "Under the Hood: How Copilot Works",
    "sections": [
        {
            "title": "Architecture Whiteboard Setup",
            "type": "Narration",
            "durationSeconds": 180,
            "instructions": (
                "### Focus\n"
                "Frame why a brief architecture deep-dive matters for using Copilot well.\n\n"
                "### Cover\n"
                "- Brief switch from product framing to mental model framing\n"
                "- Why understanding the architecture changes how you use the tool\n"
                "- Whiteboard ground rules: simplified diagrams, just enough detail\n"
                "- Roadmap: stateless LLM \u2192 conversation memory \u2192 RAG \u2192 agents/tools/MCP"
            ),
            "transcript": (
                "### Why Architecture Matters\n\n"
                "Before we go deeper into demos, I want to spend the next thirty-five minutes "
                "or so doing something a little different. We're going to whiteboard the "
                "architecture of how GitHub Copilot actually works under the hood. Not at "
                "the level of academic papers, but at the level a working developer needs "
                "in order to use the tool well and reason about its behavior.\n\n"
                "Why bother with this? Because almost every frustrating Copilot moment I "
                "see in the field traces back to a misunderstanding of one specific thing: "
                "people expect Copilot to behave like a human teammate who remembers, "
                "researches, and reasons continuously. It doesn't. It's a stateless model "
                "with a finite context window, augmented by a careful orchestration layer "
                "that fakes memory, retrieves relevant code, and runs tools. Once you see "
                "that picture clearly, the entire product makes sense. You stop being "
                "surprised when context is dropped, you understand why long conversations "
                "degrade, you know why workspace context matters, and you can debug your "
                "own prompts intelligently.\n\n"
                "Quick ground rules for this section. The diagrams I'll draw are deliberately "
                "simplified \u2014 I'm leaving out tokenizers, attention heads, transformer "
                "internals, vector index implementations, and a hundred other things that "
                "would be true but not useful to you today. We're aiming for the right mental "
                "model, not engineering completeness. If you want the full depth, every box "
                "I draw has a deep literature behind it that you can chase later.\n\n"
                "Here's our roadmap. First, the stateless LLM at the core \u2014 what it actually "
                "is, what it can and can't do. Second, conversation memory \u2014 how chat is "
                "faked on top of a stateless model, and what context windows and compaction "
                "really mean. Third, RAG and workspace grounding \u2014 how Copilot knows about "
                "your code without being trained on it. And fourth, agents, tools, and MCP \u2014 "
                "how the model goes from passively answering to actively doing work in your "
                "environment. Let's start at the center."
            ),
        },
        {
            "title": "The Stateless LLM Core",
            "type": "Narration",
            "durationSeconds": 480,
            "instructions": (
                "### Focus\n"
                "Establish the LLM as a stateless function: tokens in, tokens out.\n\n"
                "### Cover\n"
                "- Whiteboard: input box \u2192 model weights \u2192 output box\n"
                "- Training vs inference \u2014 frozen weights, no learning per request\n"
                "- Knowledge store = the weights, baked in at training time\n"
                "- Stateless: no memory between calls\n"
                "- Tokens, not characters; probabilistic next-token prediction\n"
                "- Implications: identical input \u2192 (mostly) identical output, no awareness of \u2018last time\u2019\n"
                "- Why this matters when you use the tool"
            ),
            "transcript": (
                "### The Model at the Center\n\n"
                "Let me draw the core picture. In the middle of the whiteboard I'll put a "
                "single box and label it 'LLM' \u2014 large language model. Inputs flow in from "
                "the left as a prompt. Outputs flow out to the right as generated text. "
                "That's it. That's the entire mathematical object at the heart of Copilot. "
                "Everything else \u2014 chat, agents, RAG, tools, MCP \u2014 is orchestration around "
                "this one box. If you only remember one thing from this whole architecture "
                "section, remember that picture: a single box in the middle, surrounded by "
                "plumbing.\n\n"
                "Inside the box are weights. Billions of numbers, learned during a training "
                "phase that happened months before you ever opened your editor. Training is "
                "where the model reads enormous amounts of text and code \u2014 we're talking "
                "trillions of tokens for the largest models \u2014 and adjusts those weights so "
                "that, given some input, it predicts plausible next tokens. The training "
                "data shapes everything: which programming languages the model is fluent "
                "in, which libraries it knows well, which patterns it has seen a million "
                "times versus only once. If a framework was popular on GitHub when training "
                "happened, the model is great at it. If it was niche, or new, or private, "
                "the model has weak coverage. That is a direct consequence of where the "
                "weights came from.\n\n"
                "Crucially, training is over by the time the model is deployed. The weights "
                "are frozen. When you use Copilot, you are running inference \u2014 forward "
                "passes through fixed weights. The model is not learning from your "
                "conversation. It is not improving overnight because you used it well "
                "yesterday. Improvements between model versions come from a whole new "
                "training run by the model vendor weeks or months later, not from your "
                "individual usage. The 'knowledge store' you may have read about is exactly "
                "these weights: a compressed, lossy, statistical representation of "
                "everything the model saw during training. It is not a database you can "
                "query exactly. It is a probability distribution baked into matrix "
                "multiplications.\n\n"
                "Now the most important property of this box, and the one most people miss: "
                "it is stateless. Each call is independent. The model has no memory of the "
                "previous request. None whatsoever. If I send the prompt 'what's my name?' "
                "twice in a row, the model has no idea I asked the same thing a second "
                "ago, and no idea what answer it gave the first time. Each inference is a "
                "completely clean slate. Two requests sent in parallel from two different "
                "users hit the exact same weights and produce results independent of one "
                "another. Statelessness isn't a bug or a limitation we'll fix later \u2014 it "
                "is a fundamental property of the architecture, and a deliberate one. It "
                "is what makes the system scalable: any inference server can handle any "
                "request, no session affinity, no shared state.\n\n"
                "A few more concepts to pin to the whiteboard so the rest of this section "
                "makes sense. First, tokens. The model doesn't see characters or words; it "
                "sees tokens, which are sub-word pieces produced by a tokenizer. 'GitHub "
                "Copilot' is maybe four tokens. A long Python identifier might be five. "
                "Whitespace and punctuation count. Common words are usually one token; "
                "rare words or unusual identifiers get split into multiple. This matters "
                "because every single thing we'll discuss \u2014 context windows, request "
                "costs, rate limits, latency \u2014 is measured in tokens, not lines or words "
                "or characters. When you hear that a model has a 200K context window, that "
                "means roughly 150,000 English words, but for code it is harder to predict "
                "because identifiers and symbols tokenize less efficiently than prose.\n\n"
                "Second, generation is probabilistic. Given an input, the model produces a "
                "probability distribution over the next token, samples from it, appends "
                "the chosen token to the input, and repeats. That is the entire generation "
                "loop. Roll, append, roll again. That is why two runs of the same prompt "
                "can produce different outputs, why Copilot sometimes hallucinates "
                "plausible-but-wrong code, and why phrasing your prompt slightly "
                "differently can shift the result a lot. The model isn't looking up an "
                "answer in a database; it is predicting what tokens are statistically "
                "likely to come next given everything in the input. There is a parameter "
                "called temperature that controls how much randomness is in the sampling, "
                "but the fundamental shape \u2014 distribution, sample, append \u2014 is always "
                "the same.\n\n"
                "Third, the model has no built-in concept of truth, only of plausibility. "
                "It generates what looks like a likely continuation given its training "
                "distribution. Sometimes that continuation is factually correct because "
                "the training data was correct and the pattern is well-represented. "
                "Sometimes it is confidently, fluently wrong. That is a hallucination, and "
                "it is a direct consequence of the architecture, not a passing flaw that "
                "will be patched out. Better models hallucinate less, but no model "
                "hallucinates zero, and you have to design your workflow around that fact.\n\n"
                "So what does this mean for you as a user? Three implications. One: "
                "anything you want the model to consider must be in the prompt at "
                "inference time. The model has no other way to know about it \u2014 there is "
                "no side channel, no memory, no background context. Two: there is no "
                "continuity between requests at the model level. Any continuity you "
                "experience is being reconstructed by the layer above the model, and we "
                "will see exactly how next. Three: outputs are statistical predictions "
                "over plausible token sequences, not lookups in an authoritative knowledge "
                "base, so independent verification is mandatory for anything that matters.\n\n"
                "All of that raises an obvious question. If the model is stateless and "
                "forgets everything between calls, how does chat work? How does Copilot "
                "remember what we just said three messages ago, or what file I attached "
                "five turns earlier? Let's draw that next."
            ),
        },
        {
            "title": "Conversation Memory and the Context Window",
            "type": "Narration",
            "durationSeconds": 480,
            "instructions": (
                "### Focus\n"
                "Show how stateful chat is reconstructed on top of a stateless model.\n\n"
                "### Cover\n"
                "- Each chat turn re-sends the entire conversation as the prompt\n"
                "- Context window: the maximum tokens the model can ingest per call\n"
                "- System prompt + history + current message + tool results all share the budget\n"
                "- What happens when the budget is exceeded: truncation, summarization, compaction\n"
                "- Why long conversations degrade (relevant context falls off the front)\n"
                "- Practical guidance: start fresh, summarize, keep prompts focused"
            ),
            "transcript": (
                "### Faking Memory\n\n"
                "Here's the trick that makes chat feel like a conversation: every single "
                "time you send a new message, the layer above the model packages up the "
                "entire prior conversation \u2014 your previous messages and the assistant's "
                "previous replies \u2014 prepends a system prompt that defines Copilot's role "
                "and behavior, appends your new question, and sends that whole bundle as "
                "one input to the stateless model. The model sees the full transcript "
                "every turn and continues it. To you it looks like the model 'remembers'. "
                "In reality, the conversation history is being re-fed from scratch on "
                "every single turn. There is no persistent memory anywhere in the model. "
                "The illusion of memory is constructed entirely by the orchestration "
                "layer.\n\n"
                "Let me draw that explicitly so it sticks. On the whiteboard I'll show "
                "three turns. Turn one: system prompt + user message #1 goes into the "
                "model, reply #1 comes out. Turn two: system prompt + user #1 + reply #1 "
                "+ user #2 goes in, reply #2 comes out. Turn three: system prompt + user "
                "#1 + reply #1 + user #2 + reply #2 + user #3 goes in, reply #3 comes "
                "out. Notice that by turn three we are sending five messages plus the "
                "system prompt as input, and the model has to read all of it just to "
                "continue the next reply. The bundle grows linearly with the conversation. "
                "By turn twenty, every single token of the previous nineteen turns is "
                "being re-sent on every request. Memory is reconstructed, not retained, "
                "and reconstruction has a cost.\n\n"
                "Now we run into a hard physical limit: the context window. The context "
                "window is the maximum number of tokens the model can ingest in a single "
                "call. Different models have different windows \u2014 a few thousand tokens "
                "for older models, hundreds of thousands or even millions for the newest "
                "frontier models \u2014 but every model has a ceiling, and going past that "
                "ceiling is not a soft warning, it is a hard error. Inside that ceiling, "
                "everything has to fit: the system prompt that defines Copilot's behavior "
                "and capabilities, every prior message in the conversation, your current "
                "question, any files or selections you attached, the contents of any "
                "@-mentions, and \u2014 critically, if you're in agent mode \u2014 the results of "
                "every single tool call the agent has made so far in this session. They "
                "all share one budget. A long agent run with lots of file reads and "
                "terminal output can blow through the context window surprisingly fast.\n\n"
                "What happens when the bundle is bigger than the window? The orchestration "
                "layer has to decide what to drop. There are a few common strategies, and "
                "good agent products use a mix of all of them. The simplest is truncation: "
                "cut the oldest messages off the front until the rest fits. Easy to "
                "implement, but the downside is that important early context just "
                "disappears. A smarter strategy is summarization \u2014 use the model itself, "
                "in a separate background call, to compress older turns into a short "
                "summary that preserves the essentials but takes a fraction of the "
                "tokens. This is what people usually mean when they say compaction. You "
                "may have seen Copilot or other assistants offer to 'summarize the "
                "conversation' or do it automatically when things get long. That is "
                "compaction in action. A third strategy is selective dropping \u2014 keeping "
                "the most semantically relevant messages and discarding noisy "
                "intermediate tool output, things like long file dumps the agent already "
                "acted on and no longer needs to re-read.\n\n"
                "All of these strategies are lossy. None of them are perfect, and there is "
                "no magic. The practical consequence is that long conversations degrade. "
                "The specific detail you established at message three may be silently "
                "gone by message thirty. The model isn't ignoring you on purpose; the "
                "relevant context literally is no longer in its input. People often "
                "interpret this as the model 'getting confused' or 'losing focus', which "
                "sounds anthropomorphic, but the real cause is mechanical: the input "
                "changed.\n\n"
                "So what should you do as a developer? Three habits make a huge "
                "difference. First, when you're starting a meaningfully different task, "
                "start a new chat. Don't keep one mega-thread going forever. Fresh "
                "context is cheaper, clearer, and more predictable than fighting "
                "compaction in a stale thread. Second, when a long conversation has "
                "accumulated useful decisions \u2014 the chosen library, the agreed-upon "
                "naming convention, the constraint you settled on \u2014 write them out "
                "yourself. A few crisp bullet points pinned at the top of a new chat is "
                "far more reliable than hoping compaction preserved them automatically. "
                "Third, prefer focused prompts over rambling ones. Every word in the "
                "prompt costs context budget that competes with your conversation "
                "history and any files you attached. Tight prompts leave more room for "
                "the model to actually consider what matters.\n\n"
                "OK \u2014 so now we have a stateless model, with reconstructed memory, "
                "bounded by a finite context window, with various lossy strategies for "
                "managing overflow. But how does Copilot answer specific questions about "
                "your private codebase, which it was almost certainly never trained on? "
                "That's the next box on the whiteboard."
            ),
        },
        {
            "title": "RAG and Workspace Grounding",
            "type": "Narration",
            "durationSeconds": 420,
            "instructions": (
                "### Focus\n"
                "Explain Retrieval-Augmented Generation as how Copilot grounds answers in your code.\n\n"
                "### Cover\n"
                "- The model wasn't trained on your private repo\n"
                "- RAG = retrieve relevant snippets at query time, inject them into the prompt\n"
                "- Workspace indexing: chunking files, computing embeddings, storing vectors\n"
                "- Embeddings: semantic similarity in vector space\n"
                "- At query time: embed the question, find nearest chunks, attach to prompt\n"
                "- Open tabs, recent edits, explicit @-mentions all influence retrieval\n"
                "- Why irrelevant context hurts and explicit context helps"
            ),
            "transcript": (
                "### Grounding in Your Code\n\n"
                "Here's a fundamental problem. The Copilot model was trained months ago, "
                "on public code that existed at that time. Your private repository \u2014 the "
                "one you actually work on every day, with your business logic, your "
                "team's conventions, your specific architecture \u2014 was almost certainly "
                "not in that training data. Even for public repositories, anything "
                "written or refactored after the training cutoff is invisible to the "
                "weights. So how can Copilot answer specific questions about your code? "
                "How does it know that your authentication service uses a particular "
                "pattern, or that your team prefers a specific library, or what the "
                "function three files over actually does? The model itself doesn't know "
                "any of that. It can't.\n\n"
                "The answer is RAG \u2014 Retrieval-Augmented Generation. Let me add a new box "
                "to the whiteboard, off to the side of the LLM. I'll label it 'retrieval'. "
                "The idea is simple but powerful: at the moment you ask a question, the "
                "system finds the most relevant pieces of your codebase, copies the "
                "actual text of those pieces into the prompt, and sends the augmented "
                "prompt to the model. The model isn't recalling your code from training "
                "\u2014 it's reading your code right there in the input, the same way it "
                "reads your question. The trained weights provide general code reasoning "
                "ability; retrieval provides the specific facts about your codebase. "
                "Together they answer questions that neither could answer alone.\n\n"
                "How does retrieval actually find the relevant pieces? The workspace gets "
                "indexed, usually in the background as you open and edit files. Files are "
                "split into chunks \u2014 typically along natural boundaries like functions, "
                "classes, or fixed-size sliding windows of lines. Each chunk is run "
                "through an embedding model, which is a different kind of neural network "
                "whose entire job is to convert text into a high-dimensional vector \u2014 a "
                "list of hundreds or thousands of numbers. The crucial property of "
                "embeddings is that texts which mean similar things end up at nearby "
                "points in vector space, even if they share no actual words. A function "
                "called handle_user_signup and a chunk that says 'register a new account' "
                "will end up close together. All these vectors get stored in an index "
                "optimized for fast nearest-neighbor lookup.\n\n"
                "When you ask a question \u2014 say, 'how does the signup endpoint validate "
                "duplicates?' \u2014 the system embeds your question into the same vector "
                "space, looks up the nearest chunks in the index, and grabs the top "
                "matches. Those chunks become extra context that gets appended to your "
                "prompt before it's sent to the LLM. The model then sees both your "
                "question and the relevant code from your actual repository, and can "
                "answer with specifics drawn from your real implementation rather than "
                "guessing from generic patterns. That's the entire RAG mechanism in one "
                "breath: chunk, embed, store, retrieve, augment, generate.\n\n"
                "Retrieval doesn't only run on explicit chat questions, by the way. "
                "Copilot is constantly using lighter-weight signals to decide what "
                "context to include in everything from inline suggestions to agent runs: "
                "which file you have open and where your cursor is, which tabs you have "
                "open, what you've recently edited, which symbols are referenced near "
                "where you're typing. Plus you have explicit knobs you can pull: "
                "@workspace to search across the whole project, @-mentions of specific "
                "files or symbols, dragging files into the chat panel, attaching whole "
                "folders. All of these are ways of nudging the retrieval system: 'pay "
                "attention to this, not that'.\n\n"
                "Two practical takeaways for everyday use. First, irrelevant context is "
                "actively harmful, not neutral. If your prompt drags in three files that "
                "have nothing to do with your question, you're spending precious context "
                "budget on noise, you're giving the model patterns to anchor on that "
                "aren't actually relevant, and you may be pushing genuinely relevant "
                "context out via compaction. Be deliberate about what you attach. More "
                "is not always better. Second, when you already know which file or "
                "function matters, tell Copilot explicitly. Don't make it guess via "
                "embedding similarity when you can just point at the right thing. A "
                "targeted @-mention or an explicit file attachment beats a vague "
                "workspace search nine times out of ten, both in accuracy and in cost.\n\n"
                "OK \u2014 stateless model, reconstructed memory inside a context window, "
                "RAG to ground answers in your actual code. We have everything we need "
                "to explain how chat works, both Ask Mode for questions and Inline Chat "
                "for scoped edits. But Copilot does more than chat \u2014 in Agent Mode, it "
                "actually builds and runs things in your environment. That's the last "
                "piece of the architecture, and it's where things get interesting."
            ),
        },
        {
            "title": "Agents, Tools, and MCP",
            "type": "Narration",
            "durationSeconds": 480,
            "instructions": (
                "### Focus\n"
                "Connect agent loops, function-calling tools, and MCP into one mental model.\n\n"
                "### Cover\n"
                "- The agent loop: model proposes \u2192 tool runs \u2192 result goes back to model \u2192 repeat\n"
                "- Tools = typed functions (read file, edit file, run terminal, search) the model can call\n"
                "- Function calling: model emits structured JSON, host executes it, returns observation\n"
                "- Plan Agent vs Agent Mode revisited as variations on the loop\n"
                "- MCP (Model Context Protocol): standard interface for plugging external tools/data\n"
                "- Why this matters: extensibility, vendor neutrality, your team's tools as first-class context\n"
                "- Closing synthesis: model + memory + RAG + tools = the real Copilot you use"
            ),
            "transcript": (
                "### From Answering to Doing\n\n"
                "So far the model has been a passive responder \u2014 you ask, it answers. "
                "Even with RAG, the system is reactive: question in, answer out, done. "
                "Agent Mode is fundamentally different: the model is now an active "
                "participant that can take actions in your environment, observe the "
                "results, and decide what to do next. To get there we add one more "
                "concept to the whiteboard \u2014 the agent loop \u2014 and one more category "
                "of components, the tools the agent can call.\n\n"
                "Picture this on the right side of the diagram. The model is in the "
                "middle. Around it I'll draw a circle of arrows. Step one: the model "
                "receives the user's request along with all the context we've already "
                "discussed \u2014 system prompt, conversation history, retrieved code chunks. "
                "Step two: instead of producing a final answer, the model decides 'I need "
                "more information' or 'I need to take an action', and it emits a "
                "structured request to call a tool. Step three: the orchestration layer "
                "\u2014 not the model \u2014 actually runs that tool against the real "
                "environment. Step four: the tool's result comes back as a new message in "
                "the conversation. Step five: the loop repeats. The model considers the "
                "new information, possibly calls another tool, and keeps going until it "
                "either has enough to produce a final answer or decides the task is "
                "complete. That loop \u2014 reason, act, observe, reason again \u2014 is the "
                "essence of an agent. Without it, you have a chatbot. With it, you have "
                "something that can actually do work.\n\n"
                "It is worth pausing on what makes this architecturally non-trivial. The "
                "model itself never executes anything. It cannot read your filesystem, "
                "cannot run a command, cannot touch the network. All it produces is text. "
                "What it produces, when it wants a tool to run, is a precisely formatted "
                "chunk of structured output \u2014 typically JSON \u2014 that names a tool and "
                "specifies its arguments. The host application parses that, runs the real "
                "function, and returns the output as the next message in the "
                "conversation. Every action you see Agent Mode take is going through that "
                "reason-and-route choreography.\n\n"
                "Tools are typed functions the model can invoke. Read this file. Edit "
                "these lines. Run this terminal command. Search the workspace for this "
                "string. List the files in this directory. Get errors from the language "
                "server. Each tool has a name, a one-line description that tells the "
                "model when to use it, and a strict input schema declaring its arguments "
                "and types. The model has been trained extensively on examples of "
                "producing structured JSON that conforms to such schemas. The host \u2014 "
                "VS Code, in our case \u2014 parses the JSON, validates it against the "
                "schema, runs the actual function with the supplied arguments, captures "
                "the output, and feeds it back into the conversation as the next turn. "
                "This pattern is sometimes called function calling or tool use, and it is "
                "how the model bridges from pure text generation to real-world effects "
                "on your machine.\n\n"
                "A subtle but important point: tool descriptions matter enormously. The "
                "model decides which tool to call partly based on how the tool describes "
                "itself. A vague description leads to a confused agent calling the wrong "
                "tool, or no tool when it should. A crisp description \u2014 'use this to "
                "read the contents of a file when you need to understand existing code "
                "before changing it' \u2014 leads to predictable, targeted behavior. If you "
                "ever build your own tools, treat the descriptions as part of the user "
                "interface, because to the model, they are.\n\n"
                "Plan Agent and Agent Mode that we covered earlier are both variations on "
                "this loop. Agent Mode runs the loop directly: model proposes, tool runs, "
                "model observes, repeat. Plan Agent inserts a planning phase first \u2014 the "
                "model is restricted to read-only tools and a planning output \u2014 then once "
                "you approve the plan, hands off to the full Agent Mode loop with write "
                "tools enabled. Same loop, different tool sets, different stopping "
                "conditions.\n\n"
                "Now the last box on the whiteboard, and probably the most important "
                "concept for the future of Copilot in your team: MCP. MCP stands for "
                "Model Context Protocol. It's an open standard that defines how external "
                "systems expose tools and data to AI assistants in a uniform way. Before "
                "MCP, every integration was bespoke \u2014 custom code, custom auth, custom "
                "schemas, locked to one vendor. With MCP, you write one server that "
                "exposes your system's capabilities, and any MCP-compatible assistant \u2014 "
                "Copilot included \u2014 can plug in and use it.\n\n"
                "Concretely: imagine your team has an internal database of architectural "
                "decisions, or a custom deployment system, or a private API. You stand up "
                "an MCP server that exposes those as tools \u2014 'list ADRs', 'deploy to "
                "staging', 'query the metrics service' \u2014 with proper schemas and "
                "permissions. You configure Copilot to connect to that server. Now "
                "Copilot in Agent Mode can call those tools as part of its work loop, "
                "the same way it calls 'read file' or 'run terminal'. Your team's "
                "internal systems become first-class context for the AI. That is the "
                "unlock that takes Copilot from a generic assistant to a deeply "
                "integrated team member that knows about your specific environment. The "
                "ecosystem of MCP servers is growing fast \u2014 there are public servers "
                "for GitHub itself, for various databases, for documentation systems, "
                "and any team can build their own.\n\n"
                "Let's pull it all together. Center of the whiteboard: a stateless LLM, "
                "frozen weights, probabilistic next-token prediction. Around it: a "
                "conversation memory layer that fakes statefulness by re-feeding history "
                "inside a finite context window, with compaction when things get long. To "
                "one side: a RAG system that indexes your workspace and pulls in relevant "
                "code chunks at query time. To the other side: an agent loop that lets "
                "the model call tools \u2014 built-in editor tools, terminal, search, plus "
                "anything your team exposes via MCP. That whole picture, working in "
                "concert, is the real GitHub Copilot. Every product feature you've seen "
                "today \u2014 inline suggestions, Inline Chat, Ask Mode, Agent Mode, Plan "
                "Agent, custom instructions \u2014 maps onto pieces of this diagram.\n\n"
                "Once you carry that picture in your head, you can predict Copilot's "
                "behavior, debug your own prompts, and design your team's customization "
                "and tooling investments deliberately. When a long agent run starts "
                "misbehaving, you'll think: context window is full, the early decisions "
                "got compacted out, time to start a fresh chat with a written summary. "
                "When a chat answer is wrong about your code, you'll think: retrieval "
                "pulled the wrong chunks, let me explicitly point at the right file. "
                "When you're planning team tooling investments, you'll think: a "
                "well-designed MCP server for our internal systems will compound across "
                "every developer, every day, in every Copilot session. That is the "
                "payoff of taking thirty-five minutes for architecture in the middle of "
                "a product session \u2014 turning a black box into a system you can reason "
                "about."
            ),
        },
        {
            "title": "Architecture Reflection",
            "type": "Prompt",
            "durationSeconds": 180,
            "instructions": (
                "### Focus\n"
                "Brief audience interaction to consolidate the architecture material.\n\n"
                "### Cover\n"
                "- Chat prompt: \"Which piece changed your mental model most?\"\n"
                "- Reaction check: Does the agent loop now make sense? (thumbs-up = yes)\n"
                "- Tease MCP investment for teams\n"
                "- Bridge into Responsible AI section"
            ),
            "transcript": (
                "### Quick Reflection\n\n"
                "Quick check before we move on. Drop in the chat: which piece of that "
                "architecture changed your mental model the most? Was it the stateless "
                "LLM with frozen weights? The fact that chat memory is just re-fed "
                "history inside a finite context window? Compaction quietly dropping "
                "your early decisions when the conversation gets long? RAG using "
                "embeddings to ground answers in your real code? The agent loop with "
                "tool calls? MCP as an open standard for plugging in your team's "
                "systems? I'm genuinely curious which concept is the biggest update for "
                "this audience.\n\n"
                "And a quick reaction check \u2014 thumbs up if the agent loop now makes "
                "intuitive sense to you, surprised face if it's still murky and you'd "
                "want me to recap a piece before we move on.\n\n"
                "Great \u2014 lots of thumbs, and I see RAG and MCP coming up most often in "
                "the chat as the biggest mental-model shifts. That tracks with what I "
                "see in the field. Both of those are exactly where I'd encourage your "
                "team to invest next: deliberate workspace context and good custom "
                "instructions to get the most out of RAG, and one or two MCP servers for "
                "the internal systems your developers actually use every day. That is "
                "how you compound Copilot's value over time, well beyond what installing "
                "it out of the box gives you.\n\n"
                "With the architecture clearly in our heads, the next conversation about "
                "responsible use lands very differently \u2014 because now you understand "
                "exactly why hallucinations happen, why context matters, and why "
                "validation is mandatory. Let's go there."
            ),
        },
    ],
}

# ------------------------------------------------------------------
# Build the variant
# ------------------------------------------------------------------

def build():
    base = json.loads(SRC.read_text(encoding="utf-8"))

    # Drop sections by title
    dropped = []
    new_chapters = []
    for ch in base["chapters"]:
        kept = []
        for sec in ch["sections"]:
            if sec.get("title") in DROP_TITLES:
                dropped.append((ch["title"], sec["title"], sec["durationSeconds"]))
                continue
            kept.append(sec)
        if kept:
            new_chapters.append({"title": ch["title"], "sections": kept})

    # Insert architecture chapter after the Fundamentals chapter
    insert_after_title = "GitHub Copilot Fundamentals & Product Model"
    insert_idx = next(
        i for i, ch in enumerate(new_chapters) if ch["title"] == insert_after_title
    )
    new_chapters.insert(insert_idx + 1, ARCH_CHAPTER)

    variant = {
        "title": "GH-300 GitHub Copilot \u2014 Architecture Edition",
        "chapters": new_chapters,
    }
    OUT_JSON.write_text(json.dumps(variant, indent=2, ensure_ascii=False), encoding="utf-8")

    # Pacing summary
    total = 0
    for ch in new_chapters:
        for s in ch["sections"]:
            total += s["durationSeconds"]
    print(f"Variant total: {total // 60} min ({total} s)")
    print(f"Dropped {len(dropped)} sections totaling {sum(d[2] for d in dropped) // 60} min:")
    for ch_t, sec_t, d in dropped:
        print(f"  - {ch_t} / {sec_t} ({d // 60} min)")
    print(f"Inserted architecture chapter with {len(ARCH_CHAPTER['sections'])} sections "
          f"totaling {sum(s['durationSeconds'] for s in ARCH_CHAPTER['sections']) // 60} min")

    return variant


def fmt_dur(s):
    m, sec = divmod(s, 60)
    return f"{m} min" if sec == 0 else f"{m}m {sec}s"


def write_markdown(variant):
    total = sum(s["durationSeconds"] for ch in variant["chapters"] for s in ch["sections"])

    # Outline
    lines = [f"# {variant['title']}", ""]
    lines.append(f"**Total duration:** {fmt_dur(total)}  ")
    lines.append(f"**Chapters:** {len(variant['chapters'])}  ")
    lines.append(f"**Sections:** {sum(len(c['sections']) for c in variant['chapters'])}")
    lines.append("")
    lines.append("---")
    lines.append("")
    for i, ch in enumerate(variant["chapters"], 1):
        ch_total = sum(s["durationSeconds"] for s in ch["sections"])
        lines.append(f"## {i}. {ch['title']}")
        lines.append("")
        lines.append(f"_Chapter duration: {fmt_dur(ch_total)}_")
        lines.append("")
        for j, sec in enumerate(ch["sections"], 1):
            lines.append(f"### {i}.{j} {sec['title']}")
            lines.append("")
            lines.append(f"- **Type:** {sec['type']}")
            lines.append(f"- **Duration:** {fmt_dur(sec['durationSeconds'])}")
            lines.append("")
            instr = sec.get("instructions", "").strip()
            if instr:
                lines.append(instr)
                lines.append("")
        lines.append("---")
        lines.append("")
    OUT_OUTLINE.write_text("\n".join(lines), encoding="utf-8")

    # Full
    lines = [f"# {variant['title']} \u2014 Full Transcript", ""]
    lines.append(f"**Total duration:** {fmt_dur(total)}")
    lines.append("")
    lines.append("---")
    lines.append("")
    for i, ch in enumerate(variant["chapters"], 1):
        ch_total = sum(s["durationSeconds"] for s in ch["sections"])
        lines.append(f"## {i}. {ch['title']}")
        lines.append("")
        lines.append(f"_Chapter duration: {fmt_dur(ch_total)}_")
        lines.append("")
        for j, sec in enumerate(ch["sections"], 1):
            lines.append(f"### {i}.{j} {sec['title']}")
            lines.append("")
            lines.append(
                f"**Type:** {sec['type']}  |  **Duration:** {fmt_dur(sec['durationSeconds'])}"
            )
            lines.append("")
            instr = sec.get("instructions", "").strip()
            if instr:
                lines.append("#### Delivery Notes")
                lines.append("")
                lines.append(instr)
                lines.append("")
            transcript = sec.get("transcript", "").strip()
            if transcript:
                lines.append("#### Transcript")
                lines.append("")
                lines.append(transcript)
                lines.append("")
            lines.append("---")
            lines.append("")
    OUT_FULL.write_text("\n".join(lines), encoding="utf-8")


def pacing_check(variant):
    WPM = {"Narration": 140, "Demo": 90, "Prompt": 100}
    issues = []
    for ch in variant["chapters"]:
        for s in ch["sections"]:
            if s["type"] == "Pause":
                continue
            text = s.get("transcript", "")
            words = len(re.sub(r"[#*_`>-]", " ", text).split())
            target = WPM.get(s["type"], 140)
            expected = int(target * s["durationSeconds"] / 60)
            if expected == 0:
                continue
            ratio = words / expected
            status = "ok"
            if ratio < 0.7:
                status = "TOO SHORT"
            elif ratio > 1.25:
                status = "TOO LONG"
            print(
                f"  {s['type']:10} {s['durationSeconds']//60:2d}m  "
                f"words={words:4d}  expected={expected:4d}  {status}  "
                f"{s['title']}"
            )
            if status != "ok":
                issues.append((s["title"], words, expected, status))
    print()
    print(f"{len(issues)} pacing issues" if issues else "All sections within pacing tolerance.")


if __name__ == "__main__":
    v = build()
    write_markdown(v)
    print("\nPacing check:")
    pacing_check(v)
    print(f"\nWrote: {OUT_JSON}")
    print(f"Wrote: {OUT_OUTLINE}")
    print(f"Wrote: {OUT_FULL}")
