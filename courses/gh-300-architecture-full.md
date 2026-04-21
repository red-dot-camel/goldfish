# GH-300 GitHub Copilot — Architecture Edition — Full Transcript

**Total duration:** 180 min

---

## 1. Welcome & Session Framing

_Chapter duration: 8 min_

### 1.1 Welcome and Scale Delivery Norms

**Type:** Narration  |  **Duration:** 4 min

#### Delivery Notes

### Focus
Set a warm tone and establish scale delivery norms for a large audience.

### Cover
- Welcome global audience
- Confirm 3-hour session duration with two 10-minute breaks
- Microphones muted, cameras optional
- Chat for guided prompts only — no open-mic Q&A
- Moderator handles chat questions
- Teams reactions: thumbs-up = yes, surprised = no

#### Transcript

### Opening

Hello everyone, and welcome to GH-300 — GitHub Copilot. I'm really glad you're here today, and I want to thank you for carving out time from what I know are very busy schedules to join us for this session.

We're going to be together for about three hours, including two ten-minute breaks along the way. That's the time we need to cover everything from Copilot fundamentals, through live demos of real workflows, to practical techniques you can apply in your daily work starting tomorrow. So please settle in, grab a coffee or some water, and let's make the most of this time together.

Before we dive into the content, I want to set a few ground rules. With this many people in the session, we need to be deliberate about how we interact — otherwise things get chaotic very quickly. Don't worry, none of these rules are restrictive. They're just here to help us all get the most value from the session.

First rule: please keep your microphones muted throughout the session. With hundreds of people on the call, even a little background noise from each person adds up to a lot of distraction. So microphones stay off unless I explicitly ask for someone to unmute, which won't happen today.

You are very welcome to turn on your cameras if you'd like. I always appreciate seeing a few faces nodding along — or looking confused, which is also useful information — because it helps me know whether what I'm saying is landing. But cameras are completely optional. No pressure either way.

If you have questions at any point during the session, please drop them in the chat. I have a colleague moderating who will collect them, group similar ones together, and surface them to me at natural breaking points. So you don't need to wait for a Q&A section — ask whenever the question pops into your head, and we'll get to it. There are absolutely no silly questions. If something isn't clear, or if you want me to go deeper on a topic, or if you spot an inconsistency — ask. Chances are several other people are wondering the same thing.

We're also going to use Teams reactions for quick check-ins throughout the session. This lets me get a pulse from the audience without anyone needing to unmute. Let's agree on a simple convention: thumbs up means yes, and the surprised emoji means no. We'll use these for quick polls and confirmations as we go.

Let's actually test that right now — give me a thumbs up if you can hear me clearly and the audio is good on your end.

Great, I see those reactions rolling in. The audio is working, you're engaged, and we're off to a really good start. Let me tell you what we're going to cover.

---

### 1.2 Session Positioning

**Type:** Narration  |  **Duration:** 4 min

#### Delivery Notes

### Focus
Position GH-300 as foundational Copilot understanding. Demo-led, no labs.

### Cover
- GH-300 = foundational GitHub Copilot understanding
- Demo-led storytelling — no labs, no environment setup, no breakout rooms
- Copilot supports developers — does not replace thinking
- Focus on daily developer workflows, not syntax mastery or configuration
- AZ-2007 = deeper developer execution follow-on
- Scripted, repeatable demos throughout

#### Transcript

### Positioning

So what exactly is this session? Let me set expectations clearly so you know what you're getting into.

GH-300 is our foundational session on GitHub Copilot. The keyword there is foundational. We're going to build a solid understanding of what Copilot is, how it fits into your daily developer workflows, and most importantly, how to use it effectively and responsibly. By the end of today, you'll have a clear mental model of Copilot, you'll have seen it in action across realistic developer scenarios, and you'll know exactly what to try first when you go back to your own work.

This is a demo-driven session. That means I'll be sharing my screen and showing you real workflows, real code, real prompts, and real results. You'll see Copilot succeed, you'll see me critique its output, and you'll see how I refine my approach when the first response isn't quite what I wanted. The goal is to make this concrete and practical, not theoretical.

There are no labs today. You don't need to set anything up. You don't need to install Copilot, configure any environments, sign in to anything, or open any specific tools. You can just watch, absorb, and think about how each pattern applies to your own codebase and your own day-to-day work. If you want hands-on practice afterward, I'll point you to the right resources at the end — but during the session, your job is just to watch carefully and ask questions in the chat.

We also won't be doing breakout rooms or open-mic Q&A. With this audience size, breakouts become logistical chaos and open-mic Q&A burns through our time budget very quickly. This format is intentionally designed to be efficient and focused, so we can cover a lot of ground in our three hours together without losing momentum.

There's one key message I want you to carry through every section today, and I'll repeat it several times because it's that important: GitHub Copilot is a powerful assistant that supports your development work. It does not replace your thinking, your judgment, your domain expertise, or your engineering discipline. What it does is accelerate the things you already do well, and remove a lot of the tedious mechanical effort that gets in the way of the genuinely interesting parts of software engineering.

Now, if today's session leaves you wanting more — specifically, deeper hands-on execution where you actually build things yourself with Copilot, work through complex scenarios, and develop real muscle memory — that's what AZ-2007 is designed for. AZ-2007 is the longer, intensive, hands-on follow-on. Think of today as building the conceptual foundation that makes AZ-2007 productive and efficient. GH-300 is the understanding, AZ-2007 is the doing. Both have their place, and they complement each other well.

Alright, before we get into the content, let's quickly find out who's actually in the room.

---

## 2. GitHub Copilot Fundamentals & Product Model

_Chapter duration: 28 min_

### 2.1 What Is GitHub Copilot

**Type:** Narration  |  **Duration:** 7 min

#### Delivery Notes

### Focus
Build a clear mental model of what GitHub Copilot is and where it fits in developer work.

### Cover
- AI coding assistant — write code faster with less effort
- Proven productivity impact (GitHub blog research)
- Works across VS Code, JetBrains, Xcode, and github.com
- Not just autocomplete — a full AI pair programmer
- Individual AND team productivity benefits
- Part of the developer's daily flow: Idea → Code → Test → Document → Review → Iterate

#### Transcript

### What Is GitHub Copilot

So let's start at the beginning. What exactly is GitHub Copilot? Because depending on when you last looked at it, you might have a slightly outdated picture in your head.

The official definition is this: GitHub Copilot is an AI coding assistant that helps you write code faster and with less effort, allowing you to focus more of your energy on problem solving and collaboration. That's the one-line summary, but let me unpack what that actually means in practice, because that sentence is doing a lot of work.

'AI coding assistant' — that's the category. It's an assistant. Not a replacement, not an oracle. An assistant that sits alongside you while you work and helps with the parts of coding that benefit from speed and pattern recognition. Things like writing boilerplate, looking up syntax you've half-forgotten, generating tests, drafting documentation, exploring unfamiliar code. The assistant handles the mechanical work; you handle the thinking.

'Helps you write code faster and with less effort' — that's the immediate benefit. GitHub has published research quantifying Copilot's impact on developer productivity and happiness. The numbers are significant. Developers using Copilot complete tasks measurably faster, report higher satisfaction with their work, and spend less time on the kinds of repetitive boilerplate that typically drains energy without adding value. This isn't anecdotal — it's measured across thousands of developers in controlled studies. We've seen this play out across organizations of every size and across every industry.

'Focus more of your energy on problem solving and collaboration' — that's the deeper benefit, and arguably the more important one. The mechanical parts of coding consume cognitive energy. Even when you can do something quickly, doing it eats some of your finite mental budget for the day. When Copilot handles the routine work, you have more of that budget left over for the genuinely hard problems — architecture, design trade-offs, edge cases, debugging gnarly issues, mentoring teammates. The work that actually requires a human.

Now, when people first hear about Copilot, they often think it's just fancy autocomplete. Code suggestions that pop up as you type. And yes, that is one part of it — a meaningful part, actually — but it's much, much more than that. Copilot is a full AI pair programmer that can explain unfamiliar code, generate entire functions from a comment, draft and refine multi-step plans, write tests against existing implementations, fix bugs across multiple files, generate commit messages, and even operate autonomously to complete complex multi-step tasks while you watch.

Copilot also shows up in multiple places across your development environment. You can use it in VS Code, JetBrains IDEs, Visual Studio, Xcode, Eclipse, Neovim, and even directly on github.com. It's designed to be wherever you already work, fitting naturally into your existing workflow rather than forcing you to change tools or learn a new interface. You don't switch context to use Copilot; Copilot meets you exactly where you already are. That matters because tools that require you to leave your current environment tend to get used less, no matter how good they are.

Think about the typical developer flow: you start with an idea or a requirement, you write some code, you test it, you document it, you put it up for review, and you iterate based on feedback. Copilot can help you at every single stage of that cycle. Drafting code at the implementation stage, generating tests at the testing stage, drafting documentation, generating commit messages and PR descriptions, even helping with code review.

And it benefits not just your individual productivity but team productivity too — through shared context via custom instructions, consistent code patterns across the team, and dramatically faster onboarding to unfamiliar parts of your codebase. I want to emphasize that last point because it tends to be undervalued. When a new developer joins your team, Copilot can help them understand the existing codebase in minutes instead of days. When you yourself need to work on a part of the system you haven't touched in months, Copilot helps you get back up to speed quickly. This compounds across an entire team and over time becomes a significant productivity multiplier.

Let me show you exactly how that works by walking through the different ways you actually interact with Copilot day to day.

---

### 2.2 Copilot Interaction Modes

**Type:** Narration  |  **Duration:** 11 min

#### Delivery Notes

### Focus
Explain the five primary interaction modes developers use with Copilot.

### Cover
- **Inline suggestions**: Context-aware ghost text as you type, accept with Tab
- **Inline Chat** (Ctrl+I / Cmd+I): Scoped to current file or selection for targeted edits
- **Ask Mode**: Q&A about codebase, coding concepts, brainstorming ideas
- **Agent Mode**: Autonomous multi-step coding — the recommended default for daily work
- **Plan Agent**: Draft a reviewed plan before implementation, then hand off
- Context matters: nearby code, open tabs, explicit file references
- Prompts: be explicit, can always follow up to refine

#### Transcript

### Interaction Modes

Let me walk you through the five primary ways you'll interact with GitHub Copilot. Understanding these is the key to getting real value out of it, because each mode has a sweet spot — a specific kind of task where it excels — and using the wrong mode for the wrong task is one of the most common reasons people feel underwhelmed when they first try Copilot.

First, we have **inline suggestions**. These are AI-powered code suggestions that appear as you type — you'll see them as faint ghost text in your editor. They offer context-aware completions ranging from finishing the current line, to filling in the next few lines, to occasionally generating entire blocks of new code. When you see a suggestion you like, you press Tab to accept it. If you don't like it, you just keep typing and it disappears. There's no friction, no commitment, no menu to click through.

This is the most lightweight interaction — it happens naturally and automatically as you code. You'll find yourself using inline suggestions dozens or hundreds of times a day without consciously thinking about it. It becomes part of your typing rhythm. Some developers describe it as a quiet collaborator that just makes them faster without ever interrupting their flow. The key skill here is learning when to look at a suggestion versus when to just keep typing. With practice, this becomes instinctive.

Second is **Inline Chat**. You trigger this with Control-I on Windows or Linux, or Command-I on Mac. It opens a small interactive chat window scoped right to your current file or whatever text you have selected. This is fantastic for code explanations, debugging a specific function, or making targeted improvements to a focused block of code. Think of it as a quick, focused conversation about the code right in front of you.

A typical Inline Chat workflow: you highlight some code, press Control-I, and say 'refactor this for readability', or 'add error handling here', or 'why is this slow?' — and Copilot modifies just that selection or answers your question about it. The scope is narrow on purpose. You're not asking about the whole project, you're asking about this specific block. That focus tends to produce better, more targeted results.

Third, we have **Ask Mode**. This is optimized for answering questions — about your codebase, about coding concepts, about technologies in general. You're not asking Copilot to change anything in this mode, you're asking it to help you understand something. How does this function work? What's the best approach for solving this kind of problem? Explain this design pattern to me. What's the difference between these two libraries? Is there a Pythonic way to do this thing I'm doing in Java?

It's like having a knowledgeable colleague sitting next to you who you can ask anything, anytime, without feeling like you're interrupting their work or taking up their time. And because it has access to your codebase as context, the answers can be specific to your project, not generic textbook explanations.

Fourth — and this is the one I really want you to remember — is **Agent Mode**. This is the recommended default mode for most coding tasks. Agent Mode is where Copilot acts as an autonomous peer programmer. You give it a high-level request, and it breaks that request down into multi-step work. It discovers which files in your project are relevant. It makes coordinated edits across multiple files. It runs terminal commands and reads the output. It checks whether tests pass. It iterates until the task is actually complete.

If something breaks during the work, Agent Mode tries to fix it. If tests fail, it adjusts the code and reruns them. If a command produces an unexpected error, it reads the error and adjusts its approach. This is the powerhouse mode for daily development work. When people say Copilot dramatically changed their productivity, Agent Mode is almost always what they're talking about. The mental model shifts from 'autocomplete' to 'I have a teammate who can take work and complete it'.

Finally, there's **Plan Agent**. This is for when you want to be deliberate — to think before you code rather than diving straight in. Plan Agent researches your request, asks you clarifying questions if needed, and then drafts a structured implementation plan. You review and refine that plan together — you can change the approach, add constraints, push back on things you don't like — and when you're satisfied, you click one button to hand the plan off to Agent Mode for implementation. Plan first, build second.

This is particularly valuable for complex changes where you want to consider the approach before committing to writing code. Refactors, new features that touch multiple parts of the system, anything where the wrong direction would be costly to undo. Plan Agent forces a moment of reflection that's easy to skip when the AI is happily generating code immediately.

So to summarize the five modes in terms of when to use each one: inline suggestions for fast completions while you're typing, Inline Chat for targeted questions or edits on selected code, Ask Mode for broader questions and understanding, Agent Mode for building and implementing things, and Plan Agent for thinking and planning before building something complex.

Now, across all five of these modes, two things matter enormously: context and prompts. Get these right and Copilot feels magical. Get them wrong and Copilot feels mediocre. So let me touch on both.

For context, Copilot automatically considers the code near your cursor, your open editor tabs, and the overall structure of your project. In chat-based modes, you can also explicitly reference specific files by dragging them into the conversation, by using @-mentions, or by attaching whole folders. The more relevant context Copilot has, the better its output will be. Think of it like briefing a new colleague — the more relevant background you give them, the better their help will be. Conversely, dumping irrelevant context just confuses the model. Be intentional.

For prompts, being explicit and clear matters — but you don't need to get it perfect on the first try. Unlike traditional tools, you can always clarify with follow-up prompts. If the first result isn't quite right, just tell Copilot what to adjust. 'Make it more defensive', or 'use the existing logger instead of print statements', or 'this should be a class method, not standalone'. It's a conversation, not a one-shot command, and that's a fundamental shift from how we used to think about tools.

There are also additional techniques you can use to supplement Copilot's knowledge: chat participants, slash commands, custom instructions, prompt files, custom agents, and MCP tools that extend Copilot's capabilities. We won't go deep on all of those today, but know they exist for when you want to get more advanced. The basics will get you very far on their own.

That's a lot of concepts. Let me make this concrete with a quick live demo — I want to show you what Ask Mode looks like in action right now.

---

### 2.3 Project Overview with Ask Mode

**Type:** Demo  |  **Duration:** 7 min

#### Delivery Notes

### Focus
Demonstrate Ask Mode for rapid project onboarding — the first live demo of the session.

### Cover
- Open VS Code with the skills/getting-started-with-github-copilot project in a Codespace
- Open Copilot Chat in Ask Mode
- Prompt: "Please briefly explain the structure of this project. What should I do to run it?"
- Show Copilot's project explanation — FastAPI app, src/app.py, static files, activities data
- Run the application via debugger and show website on port 8000
- Show the Mergington High School activities page in browser
- Highlight: 30-second onboarding vs 20-minute file browsing
- This is the project we'll use for all demos today

#### Transcript

### Demo: Project Overview

Let me make this real. Rather than just tell you about these modes, let me show you Ask Mode in action right now — because there's a particular use case that I think is the perfect first thing to try with Copilot, and it's one of the most underrated.

Imagine you've just joined a new team, or you've been pulled in to help on a project you've never seen before. What's the first thing you'd normally do? Open files one by one, read through the structure, dig into the README if there is one, maybe look at recent commits, and try to piece together how everything connects. If the project is well-documented, that takes maybe twenty minutes. If it isn't, it can take hours, sometimes a full day before you feel oriented.

Let me show you a faster way. I'm switching to my browser now, where I have VS Code open in a GitHub Codespace. The project is already cloned, but I haven't opened any of the files yet. I can see them in the sidebar — there's a src folder, some configuration files, a requirements.txt — but I genuinely don't know what this project does. Let's pretend it's day one for me.

I'll open Copilot Chat by clicking the chat icon in the activity bar. I want to make sure I'm in Ask Mode — you can see the mode dropdown at the bottom of the chat input. It's set to Ask. Good.

Now I'll type a very simple prompt: 'Please briefly explain the structure of this project. What is it, what tech stack does it use, and what should I do to run it?'

I'll press Enter. Watch what happens. Copilot is searching through the project files, looking at the README if there is one, checking the source code, looking at the dependencies. And within a few seconds — there's the response.

Let me read what it tells me. This is a FastAPI application called Mergington High School. It's an extracurricular activities website where students at a fictional high school can browse available clubs and sign up for them. Tech stack: Python with FastAPI for the backend, plain HTML, JavaScript, and CSS for the frontend, no framework. The main backend code is in src/app.py, the static frontend files are in src/static. It explains the activities data model — each activity has a description, a schedule, a max participant count, and a list of currently signed-up students. It tells me dependencies are listed in requirements.txt, and it tells me exactly how to start the application: run uvicorn app:app, or use the included VS Code launch configuration.

Let me actually run it now to verify all of that. I'll open the Run and Debug panel, hit the green play button, and the debugger fires up. I see uvicorn starting in the terminal. I'll click on the link to open the browser on port 8000.

And there it is — the Mergington High School Extracurricular Activities page. We can see Chess Club with its schedule on Mondays and Fridays, Programming Class on Tuesdays and Thursdays, Gym Class. Each activity shows when it meets, how many spots are available, and lets students sign up by entering an email address.

So what just happened? Copilot compressed what might have been a twenty-minute exploration into a thirty-second conversation. I now understand the project's purpose, its tech stack, its file layout, its data model, and how to run it. And I have the app actually running in front of me. That's Ask Mode earning its keep on day one of any project, and it's something you can use literally tomorrow on any codebase you're new to.

We're going to keep using this same Mergington High School project for all of our demos today, so you'll get very familiar with it as we go.

---

### 2.4 Interaction Mode Poll

**Type:** Prompt  |  **Duration:** 3 min

#### Delivery Notes

### Focus
Quick engagement to anchor the fundamentals.

### Cover
- Chat prompt: "Do you rely more on suggestions or chat today?"
- Acknowledge the mix
- Transition to Responsible AI section

#### Transcript

### Quick Check

So you just saw Ask Mode in action — pretty powerful for something that took thirty seconds. Before we move on, I want to do a quick poll to get a sense of how you're already using Copilot today, if you are.

For those of you who have already used Copilot — drop in the chat: do you rely more on inline suggestions, or more on chat-based interactions like Ask Mode and Agent Mode? Or maybe a mix of both? Just type 'inline', 'chat', or 'mix' — nice and simple.

Let me give that a moment… and I see a really good spread coming in. Some of you are firmly in the inline suggestions camp — Tab, Tab, Tab all day long, never opening the chat panel. Some of you are all about chat, using it for explanations, refactoring, full feature building, basically running everything through Agent Mode. And quite a lot of you are using a mix, picking the right mode for each task as you go. That mix is actually the ideal approach — different tasks really do call for different modes.

What's interesting is that there's a typical adoption arc people follow. Most developers start with inline suggestions because they're the most familiar and least disruptive — it just feels like a smarter autocomplete, low risk, easy to try. Over time, as they get more comfortable, they start using Inline Chat for targeted edits. Then they discover Ask Mode and use it for explanations and learning. And eventually, Agent Mode becomes the go-to for anything beyond a single-line completion. Most people end up there within a few weeks of regular use.

We'll see all of these modes in action with more demos throughout the day. But first, let's move to something critically important — how to use all of this responsibly.

---

## 3. Under the Hood: How Copilot Works

_Chapter duration: 37 min_

### 3.1 Architecture Whiteboard Setup

**Type:** Narration  |  **Duration:** 3 min

#### Delivery Notes

### Focus
Frame why a brief architecture deep-dive matters for using Copilot well.

### Cover
- Brief switch from product framing to mental model framing
- Why understanding the architecture changes how you use the tool
- Whiteboard ground rules: simplified diagrams, just enough detail
- Roadmap: stateless LLM → conversation memory → RAG → agents/tools/MCP

#### Transcript

### Why Architecture Matters

Before we go deeper into demos, I want to spend the next thirty-five minutes or so doing something a little different. We're going to whiteboard the architecture of how GitHub Copilot actually works under the hood. Not at the level of academic papers, but at the level a working developer needs in order to use the tool well and reason about its behavior.

Why bother with this? Because almost every frustrating Copilot moment I see in the field traces back to a misunderstanding of one specific thing: people expect Copilot to behave like a human teammate who remembers, researches, and reasons continuously. It doesn't. It's a stateless model with a finite context window, augmented by a careful orchestration layer that fakes memory, retrieves relevant code, and runs tools. Once you see that picture clearly, the entire product makes sense. You stop being surprised when context is dropped, you understand why long conversations degrade, you know why workspace context matters, and you can debug your own prompts intelligently.

Quick ground rules for this section. The diagrams I'll draw are deliberately simplified — I'm leaving out tokenizers, attention heads, transformer internals, vector index implementations, and a hundred other things that would be true but not useful to you today. We're aiming for the right mental model, not engineering completeness. If you want the full depth, every box I draw has a deep literature behind it that you can chase later.

Here's our roadmap. First, the stateless LLM at the core — what it actually is, what it can and can't do. Second, conversation memory — how chat is faked on top of a stateless model, and what context windows and compaction really mean. Third, RAG and workspace grounding — how Copilot knows about your code without being trained on it. And fourth, agents, tools, and MCP — how the model goes from passively answering to actively doing work in your environment. Let's start at the center.

---

### 3.2 The Stateless LLM Core

**Type:** Narration  |  **Duration:** 8 min

#### Delivery Notes

### Focus
Establish the LLM as a stateless function: tokens in, tokens out.

### Cover
- Whiteboard: input box → model weights → output box
- Training vs inference — frozen weights, no learning per request
- Knowledge store = the weights, baked in at training time
- Stateless: no memory between calls
- Tokens, not characters; probabilistic next-token prediction
- Implications: identical input → (mostly) identical output, no awareness of ‘last time’
- Why this matters when you use the tool

#### Transcript

### The Model at the Center

Let me draw the core picture. In the middle of the whiteboard I'll put a single box and label it 'LLM' — large language model. Inputs flow in from the left as a prompt. Outputs flow out to the right as generated text. That's it. That's the entire mathematical object at the heart of Copilot. Everything else — chat, agents, RAG, tools, MCP — is orchestration around this one box. If you only remember one thing from this whole architecture section, remember that picture: a single box in the middle, surrounded by plumbing.

Inside the box are weights. Billions of numbers, learned during a training phase that happened months before you ever opened your editor. Training is where the model reads enormous amounts of text and code — we're talking trillions of tokens for the largest models — and adjusts those weights so that, given some input, it predicts plausible next tokens. The training data shapes everything: which programming languages the model is fluent in, which libraries it knows well, which patterns it has seen a million times versus only once. If a framework was popular on GitHub when training happened, the model is great at it. If it was niche, or new, or private, the model has weak coverage. That is a direct consequence of where the weights came from.

Crucially, training is over by the time the model is deployed. The weights are frozen. When you use Copilot, you are running inference — forward passes through fixed weights. The model is not learning from your conversation. It is not improving overnight because you used it well yesterday. Improvements between model versions come from a whole new training run by the model vendor weeks or months later, not from your individual usage. The 'knowledge store' you may have read about is exactly these weights: a compressed, lossy, statistical representation of everything the model saw during training. It is not a database you can query exactly. It is a probability distribution baked into matrix multiplications.

Now the most important property of this box, and the one most people miss: it is stateless. Each call is independent. The model has no memory of the previous request. None whatsoever. If I send the prompt 'what's my name?' twice in a row, the model has no idea I asked the same thing a second ago, and no idea what answer it gave the first time. Each inference is a completely clean slate. Two requests sent in parallel from two different users hit the exact same weights and produce results independent of one another. Statelessness isn't a bug or a limitation we'll fix later — it is a fundamental property of the architecture, and a deliberate one. It is what makes the system scalable: any inference server can handle any request, no session affinity, no shared state.

A few more concepts to pin to the whiteboard so the rest of this section makes sense. First, tokens. The model doesn't see characters or words; it sees tokens, which are sub-word pieces produced by a tokenizer. 'GitHub Copilot' is maybe four tokens. A long Python identifier might be five. Whitespace and punctuation count. Common words are usually one token; rare words or unusual identifiers get split into multiple. This matters because every single thing we'll discuss — context windows, request costs, rate limits, latency — is measured in tokens, not lines or words or characters. When you hear that a model has a 200K context window, that means roughly 150,000 English words, but for code it is harder to predict because identifiers and symbols tokenize less efficiently than prose.

Second, generation is probabilistic. Given an input, the model produces a probability distribution over the next token, samples from it, appends the chosen token to the input, and repeats. That is the entire generation loop. Roll, append, roll again. That is why two runs of the same prompt can produce different outputs, why Copilot sometimes hallucinates plausible-but-wrong code, and why phrasing your prompt slightly differently can shift the result a lot. The model isn't looking up an answer in a database; it is predicting what tokens are statistically likely to come next given everything in the input. There is a parameter called temperature that controls how much randomness is in the sampling, but the fundamental shape — distribution, sample, append — is always the same.

Third, the model has no built-in concept of truth, only of plausibility. It generates what looks like a likely continuation given its training distribution. Sometimes that continuation is factually correct because the training data was correct and the pattern is well-represented. Sometimes it is confidently, fluently wrong. That is a hallucination, and it is a direct consequence of the architecture, not a passing flaw that will be patched out. Better models hallucinate less, but no model hallucinates zero, and you have to design your workflow around that fact.

So what does this mean for you as a user? Three implications. One: anything you want the model to consider must be in the prompt at inference time. The model has no other way to know about it — there is no side channel, no memory, no background context. Two: there is no continuity between requests at the model level. Any continuity you experience is being reconstructed by the layer above the model, and we will see exactly how next. Three: outputs are statistical predictions over plausible token sequences, not lookups in an authoritative knowledge base, so independent verification is mandatory for anything that matters.

All of that raises an obvious question. If the model is stateless and forgets everything between calls, how does chat work? How does Copilot remember what we just said three messages ago, or what file I attached five turns earlier? Let's draw that next.

---

### 3.3 Conversation Memory and the Context Window

**Type:** Narration  |  **Duration:** 8 min

#### Delivery Notes

### Focus
Show how stateful chat is reconstructed on top of a stateless model.

### Cover
- Each chat turn re-sends the entire conversation as the prompt
- Context window: the maximum tokens the model can ingest per call
- System prompt + history + current message + tool results all share the budget
- What happens when the budget is exceeded: truncation, summarization, compaction
- Why long conversations degrade (relevant context falls off the front)
- Practical guidance: start fresh, summarize, keep prompts focused

#### Transcript

### Faking Memory

Here's the trick that makes chat feel like a conversation: every single time you send a new message, the layer above the model packages up the entire prior conversation — your previous messages and the assistant's previous replies — prepends a system prompt that defines Copilot's role and behavior, appends your new question, and sends that whole bundle as one input to the stateless model. The model sees the full transcript every turn and continues it. To you it looks like the model 'remembers'. In reality, the conversation history is being re-fed from scratch on every single turn. There is no persistent memory anywhere in the model. The illusion of memory is constructed entirely by the orchestration layer.

Let me draw that explicitly so it sticks. On the whiteboard I'll show three turns. Turn one: system prompt + user message #1 goes into the model, reply #1 comes out. Turn two: system prompt + user #1 + reply #1 + user #2 goes in, reply #2 comes out. Turn three: system prompt + user #1 + reply #1 + user #2 + reply #2 + user #3 goes in, reply #3 comes out. Notice that by turn three we are sending five messages plus the system prompt as input, and the model has to read all of it just to continue the next reply. The bundle grows linearly with the conversation. By turn twenty, every single token of the previous nineteen turns is being re-sent on every request. Memory is reconstructed, not retained, and reconstruction has a cost.

Now we run into a hard physical limit: the context window. The context window is the maximum number of tokens the model can ingest in a single call. Different models have different windows — a few thousand tokens for older models, hundreds of thousands or even millions for the newest frontier models — but every model has a ceiling, and going past that ceiling is not a soft warning, it is a hard error. Inside that ceiling, everything has to fit: the system prompt that defines Copilot's behavior and capabilities, every prior message in the conversation, your current question, any files or selections you attached, the contents of any @-mentions, and — critically, if you're in agent mode — the results of every single tool call the agent has made so far in this session. They all share one budget. A long agent run with lots of file reads and terminal output can blow through the context window surprisingly fast.

What happens when the bundle is bigger than the window? The orchestration layer has to decide what to drop. There are a few common strategies, and good agent products use a mix of all of them. The simplest is truncation: cut the oldest messages off the front until the rest fits. Easy to implement, but the downside is that important early context just disappears. A smarter strategy is summarization — use the model itself, in a separate background call, to compress older turns into a short summary that preserves the essentials but takes a fraction of the tokens. This is what people usually mean when they say compaction. You may have seen Copilot or other assistants offer to 'summarize the conversation' or do it automatically when things get long. That is compaction in action. A third strategy is selective dropping — keeping the most semantically relevant messages and discarding noisy intermediate tool output, things like long file dumps the agent already acted on and no longer needs to re-read.

All of these strategies are lossy. None of them are perfect, and there is no magic. The practical consequence is that long conversations degrade. The specific detail you established at message three may be silently gone by message thirty. The model isn't ignoring you on purpose; the relevant context literally is no longer in its input. People often interpret this as the model 'getting confused' or 'losing focus', which sounds anthropomorphic, but the real cause is mechanical: the input changed.

So what should you do as a developer? Three habits make a huge difference. First, when you're starting a meaningfully different task, start a new chat. Don't keep one mega-thread going forever. Fresh context is cheaper, clearer, and more predictable than fighting compaction in a stale thread. Second, when a long conversation has accumulated useful decisions — the chosen library, the agreed-upon naming convention, the constraint you settled on — write them out yourself. A few crisp bullet points pinned at the top of a new chat is far more reliable than hoping compaction preserved them automatically. Third, prefer focused prompts over rambling ones. Every word in the prompt costs context budget that competes with your conversation history and any files you attached. Tight prompts leave more room for the model to actually consider what matters.

OK — so now we have a stateless model, with reconstructed memory, bounded by a finite context window, with various lossy strategies for managing overflow. But how does Copilot answer specific questions about your private codebase, which it was almost certainly never trained on? That's the next box on the whiteboard.

---

### 3.4 RAG and Workspace Grounding

**Type:** Narration  |  **Duration:** 7 min

#### Delivery Notes

### Focus
Explain Retrieval-Augmented Generation as how Copilot grounds answers in your code.

### Cover
- The model wasn't trained on your private repo
- RAG = retrieve relevant snippets at query time, inject them into the prompt
- Workspace indexing: chunking files, computing embeddings, storing vectors
- Embeddings: semantic similarity in vector space
- At query time: embed the question, find nearest chunks, attach to prompt
- Open tabs, recent edits, explicit @-mentions all influence retrieval
- Why irrelevant context hurts and explicit context helps

#### Transcript

### Grounding in Your Code

Here's a fundamental problem. The Copilot model was trained months ago, on public code that existed at that time. Your private repository — the one you actually work on every day, with your business logic, your team's conventions, your specific architecture — was almost certainly not in that training data. Even for public repositories, anything written or refactored after the training cutoff is invisible to the weights. So how can Copilot answer specific questions about your code? How does it know that your authentication service uses a particular pattern, or that your team prefers a specific library, or what the function three files over actually does? The model itself doesn't know any of that. It can't.

The answer is RAG — Retrieval-Augmented Generation. Let me add a new box to the whiteboard, off to the side of the LLM. I'll label it 'retrieval'. The idea is simple but powerful: at the moment you ask a question, the system finds the most relevant pieces of your codebase, copies the actual text of those pieces into the prompt, and sends the augmented prompt to the model. The model isn't recalling your code from training — it's reading your code right there in the input, the same way it reads your question. The trained weights provide general code reasoning ability; retrieval provides the specific facts about your codebase. Together they answer questions that neither could answer alone.

How does retrieval actually find the relevant pieces? The workspace gets indexed, usually in the background as you open and edit files. Files are split into chunks — typically along natural boundaries like functions, classes, or fixed-size sliding windows of lines. Each chunk is run through an embedding model, which is a different kind of neural network whose entire job is to convert text into a high-dimensional vector — a list of hundreds or thousands of numbers. The crucial property of embeddings is that texts which mean similar things end up at nearby points in vector space, even if they share no actual words. A function called handle_user_signup and a chunk that says 'register a new account' will end up close together. All these vectors get stored in an index optimized for fast nearest-neighbor lookup.

When you ask a question — say, 'how does the signup endpoint validate duplicates?' — the system embeds your question into the same vector space, looks up the nearest chunks in the index, and grabs the top matches. Those chunks become extra context that gets appended to your prompt before it's sent to the LLM. The model then sees both your question and the relevant code from your actual repository, and can answer with specifics drawn from your real implementation rather than guessing from generic patterns. That's the entire RAG mechanism in one breath: chunk, embed, store, retrieve, augment, generate.

Retrieval doesn't only run on explicit chat questions, by the way. Copilot is constantly using lighter-weight signals to decide what context to include in everything from inline suggestions to agent runs: which file you have open and where your cursor is, which tabs you have open, what you've recently edited, which symbols are referenced near where you're typing. Plus you have explicit knobs you can pull: @workspace to search across the whole project, @-mentions of specific files or symbols, dragging files into the chat panel, attaching whole folders. All of these are ways of nudging the retrieval system: 'pay attention to this, not that'.

Two practical takeaways for everyday use. First, irrelevant context is actively harmful, not neutral. If your prompt drags in three files that have nothing to do with your question, you're spending precious context budget on noise, you're giving the model patterns to anchor on that aren't actually relevant, and you may be pushing genuinely relevant context out via compaction. Be deliberate about what you attach. More is not always better. Second, when you already know which file or function matters, tell Copilot explicitly. Don't make it guess via embedding similarity when you can just point at the right thing. A targeted @-mention or an explicit file attachment beats a vague workspace search nine times out of ten, both in accuracy and in cost.

OK — stateless model, reconstructed memory inside a context window, RAG to ground answers in your actual code. We have everything we need to explain how chat works, both Ask Mode for questions and Inline Chat for scoped edits. But Copilot does more than chat — in Agent Mode, it actually builds and runs things in your environment. That's the last piece of the architecture, and it's where things get interesting.

---

### 3.5 Agents, Tools, and MCP

**Type:** Narration  |  **Duration:** 8 min

#### Delivery Notes

### Focus
Connect agent loops, function-calling tools, and MCP into one mental model.

### Cover
- The agent loop: model proposes → tool runs → result goes back to model → repeat
- Tools = typed functions (read file, edit file, run terminal, search) the model can call
- Function calling: model emits structured JSON, host executes it, returns observation
- Plan Agent vs Agent Mode revisited as variations on the loop
- MCP (Model Context Protocol): standard interface for plugging external tools/data
- Why this matters: extensibility, vendor neutrality, your team's tools as first-class context
- Closing synthesis: model + memory + RAG + tools = the real Copilot you use

#### Transcript

### From Answering to Doing

So far the model has been a passive responder — you ask, it answers. Even with RAG, the system is reactive: question in, answer out, done. Agent Mode is fundamentally different: the model is now an active participant that can take actions in your environment, observe the results, and decide what to do next. To get there we add one more concept to the whiteboard — the agent loop — and one more category of components, the tools the agent can call.

Picture this on the right side of the diagram. The model is in the middle. Around it I'll draw a circle of arrows. Step one: the model receives the user's request along with all the context we've already discussed — system prompt, conversation history, retrieved code chunks. Step two: instead of producing a final answer, the model decides 'I need more information' or 'I need to take an action', and it emits a structured request to call a tool. Step three: the orchestration layer — not the model — actually runs that tool against the real environment. Step four: the tool's result comes back as a new message in the conversation. Step five: the loop repeats. The model considers the new information, possibly calls another tool, and keeps going until it either has enough to produce a final answer or decides the task is complete. That loop — reason, act, observe, reason again — is the essence of an agent. Without it, you have a chatbot. With it, you have something that can actually do work.

It is worth pausing on what makes this architecturally non-trivial. The model itself never executes anything. It cannot read your filesystem, cannot run a command, cannot touch the network. All it produces is text. What it produces, when it wants a tool to run, is a precisely formatted chunk of structured output — typically JSON — that names a tool and specifies its arguments. The host application parses that, runs the real function, and returns the output as the next message in the conversation. Every action you see Agent Mode take is going through that reason-and-route choreography.

Tools are typed functions the model can invoke. Read this file. Edit these lines. Run this terminal command. Search the workspace for this string. List the files in this directory. Get errors from the language server. Each tool has a name, a one-line description that tells the model when to use it, and a strict input schema declaring its arguments and types. The model has been trained extensively on examples of producing structured JSON that conforms to such schemas. The host — VS Code, in our case — parses the JSON, validates it against the schema, runs the actual function with the supplied arguments, captures the output, and feeds it back into the conversation as the next turn. This pattern is sometimes called function calling or tool use, and it is how the model bridges from pure text generation to real-world effects on your machine.

A subtle but important point: tool descriptions matter enormously. The model decides which tool to call partly based on how the tool describes itself. A vague description leads to a confused agent calling the wrong tool, or no tool when it should. A crisp description — 'use this to read the contents of a file when you need to understand existing code before changing it' — leads to predictable, targeted behavior. If you ever build your own tools, treat the descriptions as part of the user interface, because to the model, they are.

Plan Agent and Agent Mode that we covered earlier are both variations on this loop. Agent Mode runs the loop directly: model proposes, tool runs, model observes, repeat. Plan Agent inserts a planning phase first — the model is restricted to read-only tools and a planning output — then once you approve the plan, hands off to the full Agent Mode loop with write tools enabled. Same loop, different tool sets, different stopping conditions.

Now the last box on the whiteboard, and probably the most important concept for the future of Copilot in your team: MCP. MCP stands for Model Context Protocol. It's an open standard that defines how external systems expose tools and data to AI assistants in a uniform way. Before MCP, every integration was bespoke — custom code, custom auth, custom schemas, locked to one vendor. With MCP, you write one server that exposes your system's capabilities, and any MCP-compatible assistant — Copilot included — can plug in and use it.

Concretely: imagine your team has an internal database of architectural decisions, or a custom deployment system, or a private API. You stand up an MCP server that exposes those as tools — 'list ADRs', 'deploy to staging', 'query the metrics service' — with proper schemas and permissions. You configure Copilot to connect to that server. Now Copilot in Agent Mode can call those tools as part of its work loop, the same way it calls 'read file' or 'run terminal'. Your team's internal systems become first-class context for the AI. That is the unlock that takes Copilot from a generic assistant to a deeply integrated team member that knows about your specific environment. The ecosystem of MCP servers is growing fast — there are public servers for GitHub itself, for various databases, for documentation systems, and any team can build their own.

Let's pull it all together. Center of the whiteboard: a stateless LLM, frozen weights, probabilistic next-token prediction. Around it: a conversation memory layer that fakes statefulness by re-feeding history inside a finite context window, with compaction when things get long. To one side: a RAG system that indexes your workspace and pulls in relevant code chunks at query time. To the other side: an agent loop that lets the model call tools — built-in editor tools, terminal, search, plus anything your team exposes via MCP. That whole picture, working in concert, is the real GitHub Copilot. Every product feature you've seen today — inline suggestions, Inline Chat, Ask Mode, Agent Mode, Plan Agent, custom instructions — maps onto pieces of this diagram.

Once you carry that picture in your head, you can predict Copilot's behavior, debug your own prompts, and design your team's customization and tooling investments deliberately. When a long agent run starts misbehaving, you'll think: context window is full, the early decisions got compacted out, time to start a fresh chat with a written summary. When a chat answer is wrong about your code, you'll think: retrieval pulled the wrong chunks, let me explicitly point at the right file. When you're planning team tooling investments, you'll think: a well-designed MCP server for our internal systems will compound across every developer, every day, in every Copilot session. That is the payoff of taking thirty-five minutes for architecture in the middle of a product session — turning a black box into a system you can reason about.

---

### 3.6 Architecture Reflection

**Type:** Prompt  |  **Duration:** 3 min

#### Delivery Notes

### Focus
Brief audience interaction to consolidate the architecture material.

### Cover
- Chat prompt: "Which piece changed your mental model most?"
- Reaction check: Does the agent loop now make sense? (thumbs-up = yes)
- Tease MCP investment for teams
- Bridge into Responsible AI section

#### Transcript

### Quick Reflection

Quick check before we move on. Drop in the chat: which piece of that architecture changed your mental model the most? Was it the stateless LLM with frozen weights? The fact that chat memory is just re-fed history inside a finite context window? Compaction quietly dropping your early decisions when the conversation gets long? RAG using embeddings to ground answers in your real code? The agent loop with tool calls? MCP as an open standard for plugging in your team's systems? I'm genuinely curious which concept is the biggest update for this audience.

And a quick reaction check — thumbs up if the agent loop now makes intuitive sense to you, surprised face if it's still murky and you'd want me to recap a piece before we move on.

Great — lots of thumbs, and I see RAG and MCP coming up most often in the chat as the biggest mental-model shifts. That tracks with what I see in the field. Both of those are exactly where I'd encourage your team to invest next: deliberate workspace context and good custom instructions to get the most out of RAG, and one or two MCP servers for the internal systems your developers actually use every day. That is how you compound Copilot's value over time, well beyond what installing it out of the box gives you.

With the architecture clearly in our heads, the next conversation about responsible use lands very differently — because now you understand exactly why hallucinations happen, why context matters, and why validation is mandatory. Let's go there.

---

## 4. Responsible AI & Validation Mindset

_Chapter duration: 23 min_

### 4.1 Copilot Output Is a Starting Point

**Type:** Narration  |  **Duration:** 10 min

#### Delivery Notes

### Focus
Establish that Copilot output requires human validation and review.

### Cover
- Copilot suggestions are starting points, not final answers
- LLMs predict probable code based on patterns — they don't understand intent
- Four key risks: incorrect logic, security gaps, bias, over-reliance
- Developer accountability remains exactly the same
- AI-generated code must meet the same quality bar as human-written code
- Copilot does not replace code review, testing, or engineering judgment

#### Transcript

### Output Is a Starting Point

This is perhaps the most important section of today's entire session, and I want you to really internalize the message I'm about to deliver. If you take only one thing away from this whole three-hour session, please let it be this: every piece of code that GitHub Copilot generates is a starting point, not a final answer.

Let me explain why that framing matters so much. Copilot works by predicting what code is most likely to be helpful given your context and your prompt. Under the hood, it uses large language models trained on vast amounts of publicly available code. These models are remarkably good at recognizing patterns and generating plausible code that looks correct — but they are predicting. They don't truly understand your business logic, your security requirements, the specific edge cases in your system, the architectural decisions your team has made over the years, or the regulatory environment you operate in. They produce output that fits the patterns they've learned, and patterns are not the same as correctness for your specific situation.

The output can be impressive — sometimes remarkably so. You'll see Copilot generate entire functions that do exactly what you need, with appropriate error handling, sensible naming, even reasonable comments. And that quality is exactly what makes it dangerous to use uncritically. The polish of the output creates a false sense of confidence. Just because the code looks professional doesn't mean it's correct for your specific situation. Just because it compiles and runs doesn't mean it does the right thing on the inputs that actually matter.

Let me be very clear about the four key risks you need to keep in mind every time you accept code from Copilot. These aren't theoretical — every one of them shows up in real teams using these tools.

First risk: incorrect logic. Copilot can generate code that looks correct, compiles without errors, and even passes basic tests — but produces wrong results for certain inputs or edge cases. This is actually the most dangerous category of bug because it passes the initial gut check. The code runs, it returns sensible-looking values, it seems fine — but it's subtly wrong in ways that only show up in production. Maybe it handles the happy path perfectly but breaks on null inputs. Maybe the algorithm works for small datasets but has quadratic complexity that completely kills performance once you hit production scale. Maybe it gets the off-by-one wrong in a way that only matters at boundary conditions. Maybe the rounding is slightly off in a way that compounds over millions of transactions. Subtle wrongness is the worst kind of wrongness because it earns trust before it betrays it.

Second risk: security gaps. Copilot might generate code that works perfectly from a functional standpoint but doesn't follow security best practices. Missing input validation. Improper error handling that leaks internal details to attackers. Insecure defaults. SQL queries built by string concatenation that are wide open to injection attacks. Authentication checks that look right but have a logic error allowing bypass. Cryptographic operations using outdated algorithms or weak parameters. Logging sensitive data like passwords or tokens. The code does exactly what you asked, but it opens a door you didn't intend to open. Security is an area where 'it works' is a dangerously low bar — we need 'it works AND it can't be exploited'.

Third risk: bias. The models are trained on vast amounts of public code, which includes both excellent patterns and terrible anti-patterns, both modern best practices and outdated approaches that were once standard but have since been superseded. Copilot doesn't always reliably distinguish between them. It might suggest a deprecated API call, an inefficient algorithm where a better one exists, a pattern that was common five years ago but has since fallen out of favor for good reasons, or a coding style inconsistent with the rest of your codebase. The model reflects the statistical average of what it was trained on, weighted by what's most common, not necessarily what's actually best practice for your context.

And the fourth risk — and this is the human risk, the one that's actually hardest to manage — is over-reliance. When a tool generates code quickly and the code looks reasonable, there's a powerful, natural human tendency to accept it without thorough review. The faster the output comes, the less scrutiny we tend to apply, because applying scrutiny feels disproportionate to the effort it took to produce. This is a well-documented cognitive bias we all share, and Copilot's quality makes it worse, not better. Fight that tendency actively, every time you accept a suggestion. Slow down a beat. Read what was generated. Ask yourself if it does what you actually need.

Here's the bottom line, and I want this to land hard: your accountability as a developer does not change because you're using Copilot. Every line of code, whether you typed it character by character or whether Copilot suggested the entire block in one shot, goes through the same review standards, the same testing rigor, the same quality bar. Period. Your name is on the commit. Your team is responsible for the system. Your customers depend on the code working correctly. Copilot is a tool — an incredibly powerful one — but the engineering judgment, the responsibility, and the accountability are still yours and only yours.

Let me put this concretely. When a Copilot suggestion appears, develop a habit: pause for one extra second, read what was generated, and ask three quick questions. Does this actually do what I need? Does it handle the edge cases that matter for my system? Would I have written something equivalent if I had typed it from scratch? If any answer is no, you reject or refine. That one-second habit is the difference between Copilot accelerating your team and Copilot quietly degrading your codebase.

And one more useful framing: think of Copilot like a very fast, very confident, junior engineer who has read enormous amounts of code but has never actually shipped your specific system to production. Brilliant at producing first drafts. Not the person you trust to make the final call. You are. That mental model keeps you in the driver's seat where you belong. Let me show you what disciplined validation looks like in practice with a concrete demo.

---

### 4.2 Validation Workflow Demo

**Type:** Demo  |  **Duration:** 13 min

#### Delivery Notes

### Focus
Demonstrate: weak prompt → suboptimal output → refined prompt → validated result.

### Cover
- Open the Mergington High School project in VS Code
- Start with a vague prompt: "add a function to handle signups"
- Show the generated code — identify missing validation, no duplicate check, no capacity limit
- Refine the prompt with specific requirements
- Show the improved, validated output
- Walk through reviewing the result: logic correctness, HTTP status codes, error messages
- Emphasize the iterative prompt-review-refine cycle
- Trainer rule: never pause to troubleshoot — if demo fails, switch to narrated screenshots

#### Transcript

### Demo: Validation Workflow

Let me show you exactly what I mean with a live example, because this is the kind of thing that's much more powerful when you see it happen than when you hear about it. I'm switching back to VS Code now, with our same Mergington High School project from before.

Let me give you a quick refresher on the existing code. I'll open src/app.py. Up at the top here, we have an in-memory dictionary called activities, where each activity has a description, a schedule, a max_participants count, and a list of currently signed-up participants. Below that, there's a signup endpoint that takes an activity name and an email address. Right now, that endpoint is fairly minimal — it just appends the email to the participants list. Simple application, but realistic enough to demonstrate real workflows.

Now, let's pretend I want to extend this. I want a proper signup function that handles all the edge cases properly. I'm going to start with a deliberately vague prompt to show you what happens when you don't put effort into your prompt. In Copilot Chat, in Ask Mode, I'll type: 'add a function to handle signups.'

That's it. Three words of intent. Let me send it and see what comes back.

Look at what Copilot generates. At first glance, this looks fine. It creates a function called signup_for_activity. It takes activity name and email parameters. It checks if the activity exists. It appends the email to the participants list. It returns a success message. The code is clean, it's readable, it has a docstring. If I were just glancing at this, I might say 'great, let me paste that in and move on.'

But now let's put on our reviewer hat. This is the critical moment — not when the code is generated, but when we evaluate it. What's actually missing here?

Let me work through it. First, what happens if someone sends a signup request for an activity that doesn't exist? Like 'Underwater Basket Weaving'? Looking at this code… it does check, but it just returns an error message instead of an HTTP error code. That's not how a REST API should signal a bad request. A real client wouldn't know how to handle this.

Second issue: there's no check for duplicate signups at all. A student could sign up for Chess Club fifty times with the same email and the system would happily add them fifty times. That's clearly broken behavior.

And third: there's no enforcement of the max_participants limit. An activity designed for twelve students could end up with two hundred signups. The data model has the limit, but the function ignores it.

This is exactly the kind of output that I was warning about a few minutes ago. It looks right, but it isn't. It would pass a quick code review from someone glancing at the diff, and it would fail spectacularly the first time it hit production with real users behaving like real users.

So what do I do? Now watch what happens when I refine my prompt. Instead of starting from scratch, I'm going to clarify what I actually need. I'll say: 'Update the signup function to do three things. First, validate that the activity exists and return an HTTP 404 if not. Second, prevent duplicate signups by checking if the email is already in the participants list, and return an HTTP 400 with a clear error message if so. Third, enforce the max_participants limit and return an HTTP 400 with a capacity error if the activity is full.'

Notice how specific that is. Three concrete requirements, each with the desired HTTP status code. This is what a good prompt looks like — explicit about what you want and explicit about how it should behave.

Let me send it. And see the difference? The refined output uses HTTPException for each error case. Activity not found gives a 404 with the message 'Activity not found'. Duplicate signup gives a 400 with 'Student is already signed up'. At capacity gives a 400 with 'Activity is at capacity'. Each one has the correct HTTP status code and a clear, actionable error message that a client could parse and display to a user.

But here's the key point — I'm not done yet. Even with the refined output, my job as the developer continues. I now review this code myself. Let me trace through some scenarios. What happens if the activity exists, the student hasn't signed up yet, and we have capacity? Returns success, adds them — correct. What if the activity doesn't exist at all? 404 — correct. What about the duplicate check — is it comparing emails correctly, case-sensitively? Looking at it… yes, it's a direct membership check. Should I worry about case sensitivity? In our domain, emails are typically normalized to lowercase, so probably fine — but I should add that to my mental list of things to verify or write a test for.

This is the cycle: prompt, get output, review critically, refine if needed, validate the final result, and then test it. Every single time, without exception. Copilot wrote the code in seconds; my job is to make sure that code is actually correct for the situation. That's not optional, and it doesn't go away as Copilot gets better. The skill we're developing here is the skill of being a fast, critical reviewer of generated code.

---

## 5. Break 1

_Chapter duration: 10 min_

### 5.1 Break

**Type:** Pause  |  **Duration:** 10 min

#### Delivery Notes

### 10-Minute Break

- Clearly state return time on screen
- Restart exactly on time to protect demo flow
- Display break countdown or "Back at HH:MM" slide

---

## 6. Core Developer Workflows

_Chapter duration: 19 min_

### 6.1 Bug Fix with Inline Suggestions

**Type:** Demo  |  **Duration:** 8 min

#### Delivery Notes

### Focus
Demonstrate finding and fixing a bug using Ask Mode + inline suggestions.

### Cover
- Describe the bug: students can register for the same activity more than once
- Use Ask Mode: "#codebase Students are able to register twice for an activity. Where could this bug be coming from?"
- Show Copilot identifying src/app.py signup_for_activity function
- Navigate to the function, position cursor above the add-student line
- Type comment: `# Validate student is not already signed up`
- Show inline suggestion ghost text appearing with the fix
- Press Tab to accept
- Highlight: comment-driven development with Tab completion

#### Transcript

### Demo: Bug Fix

Now let's tackle a more substantial scenario — there's a real bug in our application. Students can register for the same activity more than once. If I sign up for Chess Club with my email, then sign up again with the same email, the system just adds me twice. Same email appearing twice in the participants list. That's clearly broken behavior — it doesn't match what anyone would expect from a signup form.

Let me show you two Copilot features working together to find and fix this. This is a really common pattern: use one mode to investigate, then switch to another mode to act.

First, I'll ask Copilot to help me locate the bug. I switch back to the Chat panel, make sure I'm in Ask Mode. Now, here's a useful trick — I'm going to use the #codebase reference. That tells Copilot to actually search through all the files in the workspace, not just the file I happen to have open. I type: 'Students are able to register twice for an activity. Where could this bug be coming from? #codebase'

Watch what Copilot does. It searches the project, identifies the relevant endpoint, and tells me clearly: the issue is in the signup_for_activity function in src/app.py. It even quotes the relevant lines. Looking at the code Copilot highlighted, we can see the problem clearly — the function just appends the email to the participants list without checking if it's already there. There's no duplicate prevention at all. Copilot located in seconds what might have taken me five or ten minutes to find by reading code on my own.

Now let me show you inline suggestions in action for the actual fix. I'll close the chat and navigate to the signup function. I want to position my cursor just above the line that adds the student to the participants list — that's where my validation needs to live. I'll add an empty line there.

Now, instead of typing the fix myself, I'm going to use a technique called comment-driven development. I'll type a comment that describes what I want: '# Validate that the student is not already signed up for this activity'. Then I press Enter to go to the next line.

Watch — see that ghost text appearing? That faint, lighter-colored suggestion? Copilot has read my comment, looked at the surrounding code, and generated the validation logic. It's an if-statement that checks whether the email is already in the participants list, and if so, raises an HTTPException with status 400 and a clear message: 'Student is already signed up for this activity'. That's exactly the right shape — right HTTP code, right message style, consistent with the rest of the codebase.

I'll just press Tab to accept it. Done. The bug is fixed. Let me quickly verify by trying to sign up the same email twice in the running website… first signup succeeds, second signup gets a clean error. Perfect.

This pattern is what we call comment-driven development. You describe your intent in a natural language comment as if you were leaving a note for a teammate, and Copilot fills in the implementation that satisfies the comment. It's one of the most natural and efficient ways to work with inline suggestions because it forces you to articulate your intent clearly before writing the code, and articulating intent is half of writing good code anyway. You think, you describe, Copilot implements, you review and accept or reject. Fast, focused, and safe.

---

### 6.2 Agent Mode: Build a Feature

**Type:** Demo  |  **Duration:** 11 min

#### Delivery Notes

### Focus
Demonstrate Agent Mode's autonomous multi-step capabilities across multiple files.

### Cover
- Switch to Agent Mode in Copilot Chat dropdown
- Add context: drag src/static/app.js, index.html, styles.css into chat
- Prompt: "Edit the activity cards to add a participants section showing signed-up students as a bulleted list. Make it pretty!"
- Show Copilot working autonomously across HTML, JS, and CSS
- Explain the Keep/Discard review workflow
- Verify updated website shows participants under each activity card
- Follow-up: fix registration page refresh bug with another prompt
- Highlight: one prompt, multi-file implementation, you review

#### Transcript

### Demo: Agent Mode

Now let's see the real powerhouse of Copilot — Agent Mode. This is where Copilot stops being a smart autocomplete and starts being something genuinely different: an autonomous peer programmer that takes work and completes it across multiple files while you watch.

I'll switch to Agent Mode using the dropdown at the bottom of the Chat panel. You can see the mode change — the input prompt now indicates Agent. Good.

Here's the scenario. Our website currently lists activities with their details — schedule, description, capacity. But it doesn't show who's actually signed up for each one. Students might want to see if their friends are in the same activity, teachers might want to see attendance at a glance, and right now there's no way to know without checking the API directly. Let's add a participants display.

First, I'll add some explicit context for the work. I'll drag the relevant files into the chat panel: the JavaScript file app.js, the HTML file index.html, and the CSS file styles.css. I'm telling Copilot: these are the files involved in the frontend display, focus on these. You can always provide context, but being explicit about what's relevant tends to produce sharper results.

Now I'll type my prompt: 'Hey Copilot, can you please edit the activity cards to add a participants section. It will show what participants are already signed up for that activity as a bulleted list. Remember to make it pretty!'

Notice how the prompt is conversational, not super-precise. I'm describing the user-facing outcome and trusting Agent Mode to figure out the implementation. Let me send it.

Watch what happens — this is the interesting part. Copilot is analyzing the three files, understanding the relationships between them, and now it's making coordinated changes across all of them. You can see the activity in the chat panel: it's reading files, planning edits, then proposing changes. It updates the HTML template structure to add a container for participants. It modifies the JavaScript to fetch participant data from the API and render it as a bulleted list under each card. And it adjusts the CSS to style the participant section consistently with the rest of the page — matching colors, spacing, typography.

This is the key difference with Agent Mode — it doesn't just edit one file. It understands how files relate to each other in your project, and it makes coordinated changes across them. One prompt, multiple file edits, all consistent. That's a fundamentally different mental model from autocomplete.

Now before I accept anything, let me check the website to see what it actually looks like. I'll refresh the page — and there we go. Each activity card now shows its participants listed underneath as a clean bulleted list. Chess Club shows michael@mergington.edu and daniel@mergington.edu. Programming Class shows emma@mergington.edu and sophia@mergington.edu. The styling is clean and consistent with the rest of the page — matching font, sensible spacing, nice indentation on the bullets.

The review workflow is important here. I can review each change individually using the Keep and Discard buttons next to each diff. I can accept everything at once if I'm confident, or I can go file by file, or hunk by hunk within a file. Even though Agent Mode is autonomous in producing the changes, I'm always in control of what actually gets applied to my codebase. That's by design.

Let me also show you the iterative nature of Agent Mode — because real development is rarely one-and-done. After playing with the new feature, I notice a usability bug. When I register a new student through the signup form, the page doesn't update automatically. I have to manually refresh the browser to see the new participant appear in the list. That's annoying.

I'll go back to the chat and continue the conversation: 'I've noticed a bug. When a participant is registered through the signup form, the page must be manually refreshed to see the change reflected on the activity card. Please fix this.'

Copilot identifies the issue in the JavaScript: the activity list isn't being re-fetched and re-rendered after a successful signup API call. It modifies the signup handler to call the activities-fetch function on success. I verify in the browser — sign up a new student, the participant list updates immediately. Bug fixed.

This is the Agent Mode workflow in a nutshell: give a clear instruction, let Copilot work across files, review the multi-file output, provide follow-up feedback in plain language if needed, iterate until it's right. It feels natural, like working with a colleague who happens to type incredibly fast and never gets tired of small revisions.

---

## 7. Break 2

_Chapter duration: 10 min_

### 7.1 Break

**Type:** Pause  |  **Duration:** 10 min

#### Delivery Notes

### 10-Minute Break

- Clearly state return time on screen
- Restart exactly on time to protect demo flow
- Display break countdown or "Back at HH:MM" slide

---

## 8. Testing & Quality Workflows

_Chapter duration: 13 min_

### 8.1 Copilot for Testing Overview

**Type:** Narration  |  **Duration:** 5 min

#### Delivery Notes

### Focus
Position Copilot's role in improving code quality, not just development speed.

### Cover
- Testing is where Copilot provides enormous value
- Four areas: test generation, fixing failures, code explanation/review, security-aware thinking
- Copilot accelerates the mechanics of testing — doesn't replace test strategy
- Quality is what separates professional developers from code generators

#### Transcript

### Testing Overview

Welcome back everyone, hope you got a chance to refill your coffee. Let's talk about testing — this is an area where Copilot genuinely shines, and where many developers tell me they see the biggest productivity gains from using it.

When we talk about developer productivity, the speed of writing application code is only part of the equation. Quality matters just as much, and arguably more. Code that ships fast but breaks in production is worse than code that ships a bit slower and works reliably. Testing is how we systematically ensure quality — it's how we know our code does what we think it does, and it's how we catch regressions when we change things later.

The challenge with testing is that it's often the part developers rush through, deprioritize, or skip entirely when they're under deadline pressure. Why? Because writing test boilerplate is tedious. Thinking through edge cases takes mental energy. The feedback loop of run, fail, fix, repeat can be slow and frustrating. And the immediate reward of writing a test is much smaller than the immediate reward of shipping a feature — even though the long-term value of the test is often much greater.

Copilot can help meaningfully in four key areas of testing work. Let me walk through each one.

First, generating tests. Writing the test setup, the assertions, the boilerplate scaffolding — all the mechanical work that eats up time without exercising your brain. Copilot can produce a complete, well-structured test for an existing function in seconds, including the imports, the fixtures, and multiple test cases for happy path and error conditions.

Second, fixing failing tests. When a test breaks, Copilot can read both the test and the implementation, diagnose what's wrong, and suggest corrections. This dramatically shortens the debug cycle, especially for tests where the failure isn't immediately obvious.

Third, explaining code. Helping you understand what existing code actually does, so you can write meaningful tests for it. This is particularly valuable when you inherit code from someone else or come back to your own code months later.

And fourth, security-aware thinking. Prompting you to consider edge cases, boundary conditions, and attack vectors you might overlook on your own. You can literally ask Copilot 'what edge cases am I missing for this function?' and get a useful list back.

Important caveat to put on top of all of this: Copilot accelerates the mechanics of testing. It does not replace your test strategy. You still need to decide what to test, what the acceptance criteria are, what edge cases matter for your specific domain, what level of coverage is appropriate, and what kinds of tests make sense — unit, integration, end-to-end. The thinking is yours, the typing is Copilot's. And critically, you still need to review the tests Copilot generates the same way you'd review any other code, because tests can have bugs too. Let me show you what this looks like in practice with a more deliberate workflow using Plan Agent produce a complete, well-structured test for an existing function in seconds, including the imports, the fixtures, and multiple test cases for happy path and error conditions.

Second, fixing failing tests. When a test breaks, Copilot can read both the test and the implementation, diagnose what's wrong, and suggest corrections. This dramatically shortens the debug cycle, especially for tests where the failure isn't immediately obvious.

Third, explaining code. Helping you understand what existing code actually does, so you can write meaningful tests for it. This is particularly valuable when you inherit code from someone else or come back to your own code months later.

And fourth, security-aware thinking. Prompting you to consider edge cases, boundary conditions, and attack vectors you might overlook on your own. You can literally ask Copilot 'what edge cases am I missing for this function?' and get a useful list back.

Important caveat to put on top of all of this: Copilot accelerates the mechanics of testing. It does not replace your test strategy. You still need to decide what to test, what the acceptance criteria are, what edge cases matter for your specific domain, what level of coverage is appropriate, and what kinds of tests make sense — unit, integration, end-to-end. The thinking is yours, the typing is Copilot's. And critically, you still need to review the tests Copilot generates the same way you'd review any other code, because tests can have bugs too. Let me show you what this looks like in practice with a more deliberate workflow using Plan Agent.

---

### 8.2 Test Generation and Fix Cycle

**Type:** Demo  |  **Duration:** 8 min

#### Delivery Notes

### Focus
Show the complete test cycle: generation → run → failure → diagnosis → fix → green.

### Cover
- Show the generated test file with pytest tests in AAA pattern
- Walk through one test case structure: Arrange (setup), Act (API call), Assert (verify)
- Run the tests — show results
- If a test fails, use Copilot to diagnose and fix
- Show the passing test suite — all green
- Emphasize: Copilot helps you get to green faster, doesn't skip testing

#### Transcript

### Demo: Test Cycle

Let me show you what Plan Agent and Agent Mode just built together. Here's the new tests directory in the file explorer, and inside it we have a test file with well-structured pytest tests following the Arrange-Act-Assert pattern.

Let me walk through one test case in detail so you can see the structure clearly. This is test_signup_for_activity. In the Arrange phase — marked with a comment — we create a test client using FastAPI's TestClient and prepare some test data: an activity name and an email address. In the Act phase, we make a single POST request to the signup endpoint with that data. In the Assert phase, we verify three things: the response status code is 200, the success message in the response body matches what we expect, and the participant was actually added to the activity's participants list. Three clear phases, easy to read, easy to maintain.

Looking through the rest of the file, there are tests for the happy path — successful signup, successful retrieval of the activities list. Tests for error cases — activity not found returning 404, duplicate signup returning 400, missing required fields returning 422 from FastAPI's validation. And tests for edge cases — hitting the max participants limit, signing up multiple students sequentially, retrieving activities when none exist.

Let me run the full test suite. I'll open the terminal and run pytest. We see the test runner spinning up, then results coming in. Mostly green checkmarks — but look, there's a failure. The test for duplicate signup expected a 400 status code but got a 200. That means our duplicate check isn't actually triggering in this test scenario.

This is the moment where Copilot really helps. Let me ask it about the failure. I copy the failure output, paste it into the chat, and ask: 'This test is failing — the duplicate signup check returned 200 instead of 400. Can you help me understand why and fix it?'

Copilot analyzes the failing test against the actual implementation and identifies the mismatch. It turns out that in our earlier demo we added the duplicate check, but the test setup is using a fresh test client and fresh state between each test — so the 'first' signup that's supposed to make the second one a duplicate isn't being executed. Copilot suggests the fix: make the duplicate test arrange phase explicitly do the first signup before the second one. I apply the fix, save the file, run the tests again — all green. Every test passes.

This is the real-world testing cycle, but accelerated. You generate tests with Copilot to save the boilerplate time. You run them against your implementation. When something fails, you use Copilot to help diagnose the failure and propose a fix. You verify everything passes. The whole loop that might take an hour manually takes maybe fifteen minutes with Copilot assisting — but critically, you're still the one validating that the tests are meaningful, that they exercise the right behaviors, and that they pass for the right reasons. Copilot makes you fast. You make sure the speed is going in the right direction.

---

## 9. Streamline Code Review & Customization

_Chapter duration: 12 min_

### 9.1 Copilot for Commits and Pull Requests

**Type:** Demo  |  **Duration:** 6 min

#### Delivery Notes

### Focus
Demonstrate Copilot's code review and PR workflow capabilities.

### Cover
- Stage changes in Source Control tab
- Generate commit message using sparkles icon — show Copilot reading the diff
- Commit and push to the accelerate-with-copilot branch
- Create a pull request on GitHub
- Use Copilot PR summary to generate description
- Request Copilot code review on the PR
- Show review comments Copilot adds
- Note: PR features require paid GitHub Copilot plans

#### Transcript

### Demo: PR Workflow

Let's take all the work we've done today — the bug fix, the new activities data, the participant display, the test suite — and get it properly committed and merged. This is where Copilot helps with the code review and pull request workflow, which is one of the most underrated parts of the product.

First, I'll go to the Source Control tab in VS Code. I can see all the files we've changed in this session listed under Changes. I'll stage them all by clicking the plus icon next to each file, or by clicking the plus next to the Changes header to stage everything at once.

Now normally you'd write a commit message yourself — summarizing what changed and why, in the present tense, following whatever convention your team uses. That takes time, and let's be honest, when you're tired or in a hurry, your commit messages get lazy. We've all written 'fixed stuff' or 'updates' or 'WIP' as commit messages we now regret.

Look at this sparkles icon next to the Message box. That's the Generate Commit Message button. I'll click it.

Copilot reads the entire diff — every file, every line that changed — and generates a descriptive, well-structured commit message. Let me read what it produced: 'Add duplicate signup validation, expand activities data, add participant display to activity cards, and add pytest test suite.' That's accurate, comprehensive, and follows good commit message conventions. I could tweak it if I wanted, but honestly it's already better than most commit messages I've written manually.

I'll commit and push to our accelerate-with-copilot branch from earlier. Now let me switch over to GitHub in the browser and create a pull request from that branch into main.

Here's where two more Copilot features come in. First, in the PR description area, I click the Copilot icon and select Summary. Copilot reads all the changes in the entire pull request — across every commit, every file — and generates a comprehensive, structured description. It includes what was added, what was fixed, what was changed, with references to specific files and functions where appropriate. For reviewers, this is incredibly valuable. Instead of opening the PR and trying to figure out what's going on, they get a guided tour right in the description.

Second, I can request an actual code review from Copilot itself. In the Reviewers section, I click the Request button next to the Copilot icon. Copilot scans the changes and adds review comments inline on specific lines — it might catch common mistakes, suggest improvements, flag potential issues, point out missing test coverage, or notice inconsistencies with the rest of the codebase.

One important note: these PR-level features — the summary generation and the Copilot code review — are part of paid GitHub Copilot plans. But even the commit message generation alone, which is much more broadly available, saves real time every single day. Multiply that across an entire team and an entire year and it adds up to a lot of time and a lot of better commit history.

---

### 9.2 Customizing Copilot for Your Team

**Type:** Narration  |  **Duration:** 6 min

#### Delivery Notes

### Focus
Introduce the four levels of Copilot customization.

### Cover
- **Repository custom instructions** (.github/copilot-instructions.md): project context applied to every chat request
- **Instruction files** (.github/instructions/*.instructions.md): targeted rules for specific files/directories via applyTo
- **Prompt files** (.github/prompts/*.prompt.md): reusable slash-command workflows for common tasks
- **Custom agents** (.github/agents/*.agent.md): specialized chat experiences with their own personality and tools
- Key message: customization makes Copilot understand YOUR project, not just generic code
- These scale team consistency without relying on wikis nobody reads

#### Transcript

### Customizing Copilot

Everything I've shown you so far works completely out of the box. You install Copilot, sign in, and you get all of those workflows immediately. But the real power of GitHub Copilot emerges when you customize it to understand your specific project, your team's standards, and your team's workflows. This is what takes Copilot from useful to indispensable.

There are four levels of customization available, and they form a layered system where each one adds more specificity than the one before it.

First, **repository custom instructions**. You create a single Markdown file at .github/copilot-instructions.md and describe your project in plain English. What it does, how it's structured, your coding standards, your key tools and frameworks, your conventions. This content is automatically included as context in every Copilot chat interaction within that repository, for every developer on the team. So Copilot stops being a generic assistant and starts understanding your specific project context. If your team uses a particular API pattern, or has naming conventions, or requires specific error handling, or has architectural rules — put it in that file. It's the simplest, highest-leverage customization you can do.

Second, **instruction files**. These live in the .github/instructions/ folder and use a front matter field called applyTo with glob patterns to target specific files or directories. For example, you could have one instruction file that only applies when Copilot is working on test files — with rules about your testing framework, your AAA convention, your fixture patterns. Another that applies only to your API layer with rules about authentication, error responses, and request validation. Another for your database models. Different standards for different parts of your codebase, applied automatically based on which file you're working on. This scales much better than putting everything in the single repo-level instructions file.

Third, **prompt files**. These are stored in .github/prompts/ and define reusable workflows that your whole team can access via slash commands in chat. Need to create a new component? Type /new-component and Copilot follows the prompt file's instructions for scaffolding a component the way your team does it. Need to scaffold a database migration? /new-migration. Need to write an architectural decision record? /new-adr. These encode your team's processes and ceremonies into repeatable, shareable prompts. New team members get up to speed faster because the institutional knowledge is encoded into the tool itself.

And fourth, **custom agents**. These go even further — they let you define entirely specialized chat experiences with their own personality, their own specific tool access, and their own response formats. A brainstorming agent that only generates ideas and explicitly refuses to write code. A security review agent that focuses exclusively on vulnerabilities and threat modeling. An architecture agent that evaluates design decisions against your standards. Each agent can be invoked separately and has a focused mission.

Here's why this matters at scale, and why I think customization is the underrated superpower. Every team has coding standards, conventions, and processes documented somewhere — usually in a wiki or a README that nobody reads after their first week, and that gets out of date over time. Copilot customization files encode those standards directly into the tool that developers use every single day. The standards are surfaced and applied automatically, consistently, without anyone having to remember to check the wiki or hunt down a doc. New hires onboard faster, code reviews flag fewer style issues, and the team's collective intelligence becomes self-reinforcing.

That's what takes Copilot from a helpful generic AI tool to an indispensable team member that genuinely understands your specific way of working.

---

## 10. Wrap Up & Next Steps

_Chapter duration: 20 min_

### 10.1 Key Takeaways

**Type:** Narration  |  **Duration:** 7 min

#### Delivery Notes

### Focus
Reinforce the three core messages from the session.

### Cover
- GH-300 builds GitHub Copilot fundamentals — the foundation for productive AI-assisted development
- Copilot accelerates every stage: onboarding, coding, testing, reviewing, committing
- Responsible use and validation are essential — assistant, not autopilot
- Recap interaction modes: Inline suggestions, Inline Chat, Ask Mode, Agent Mode, Plan Agent
- Recap demos: project intro, terminal help, bug fix, data generation, feature building, testing, PR workflow
- Recap customization: instructions, prompts, custom agents
- Copilot supports developers — it doesn't replace thinking

#### Transcript

### Key Takeaways

We're nearly at the end. Let me bring everything together with the three key messages from today's session, because if you remember nothing else from these three hours, I want you to remember these three things.

First, GH-300 has given you the fundamentals of GitHub Copilot. You now understand where Copilot appears across your tools, and the five primary ways you interact with it. Inline suggestions for fast completions while you type. Inline Chat for scoped edits on specific code blocks. Ask Mode for questions, exploration, and learning. Agent Mode for autonomous multi-step coding work. And Plan Agent for deliberate, planned changes where the approach matters.

You've seen each of these in action with the Mergington High School project. Ask Mode helped us onboard to the project in thirty seconds when we started — that was the first 'aha' moment of the day for many of you. Terminal inline chat remembered the git commands we'd forgotten. Inline suggestions fixed a duplicate signup bug with a single comment and a Tab press. Inline Chat generated realistic test data perfectly matching our existing schema. Agent Mode built a complete participant display feature across three files from a single conversational prompt, and then fixed a follow-up bug through natural conversation. Plan Agent designed a comprehensive test strategy that we then handed off to Agent Mode for implementation. Each mode shown in a realistic context, doing real work.

Second, you've seen how Copilot accelerates every single stage of the developer workflow. Onboarding to unfamiliar codebases, where it compresses days of exploration into minutes. Locating bugs by searching the codebase intelligently. Fixing bugs with comment-driven inline suggestions. Generating realistic data that matches your existing patterns. Building features that span multiple files. Writing comprehensive test suites with structured planning. Running the test-fix-rerun cycle. Creating meaningful commit messages and PR descriptions. Requesting code reviews. And customizing Copilot itself to understand your team's specific project, standards, and workflows through instructions, prompts, and agents.

This isn't just about writing code faster, though you will absolutely write code faster. It's about freeing up your mental energy for the genuinely hard problems that actually require a human. The architecture decisions. The design trade-offs. The edge cases that require domain expertise. The mentoring of junior teammates. The critical thinking. Let Copilot handle the implementation mechanics so you can focus on the work that makes you most valuable as an engineer.

And third — and this is the message I want you to remember above all the others, even above the productivity wins — responsible use and validation are non-negotiable. Every piece of code Copilot generates is a starting point, never a final answer. You review it critically. You test it thoroughly. You validate it against your real requirements, not just the ones you stated in the prompt. Your engineering judgment is what makes the output reliable, secure, and production-ready. Copilot is an assistant, not an autopilot. It accelerates you; it does not replace your judgment, your expertise, or your accountability. That distinction matters more as Copilot gets better, not less.

Let me reinforce a fourth implicit point that runs through everything today: Copilot rewards intentionality. The developers and teams who get the most value from it are the ones who choose the right mode for the task, write specific prompts, layer in customization that captures their team's standards, and review output with the same rigor they'd apply to a junior teammate's pull request. The developers who get the least value are the ones who treat it as autocomplete and accept whatever comes out. Same tool, completely different outcomes, depending entirely on how deliberately you use it.

If you carry just those three messages — fundamentals understood, every workflow stage accelerated, validation always required — plus that fourth principle of intentional use, you have everything you need to start using Copilot well and keep getting better at it over time.

One more thought before we move into next steps. The teams that succeed with Copilot treat it as a long-term capability they invest in, not a magic button they switch on. They share prompt patterns with each other. They review each other's customization files in pull requests. They talk about what worked and what didn't in retros. They onboard new hires to their team's Copilot conventions the same way they onboard them to their coding standards. The tool itself is the easy part. The team practice around the tool is what compounds over months and years into genuine, durable productivity gains. Plan for that practice from day one and you'll get far more out of Copilot than the team that just installs it and hopes for the best.

---

### 10.2 Next Steps and Resources

**Type:** Narration  |  **Duration:** 7 min

#### Delivery Notes

### Focus
Provide actionable next steps and position follow-on learning paths.

### Cover
- Challenge: apply Copilot to one real workflow this week
- GitHub Skills exercises for hands-on self-paced practice:
  - Getting Started with GitHub Copilot (Mergington High School project)
  - Customize Your GitHub Copilot Experience (instructions, prompts, agents)
  - Integrate MCP with Copilot (extend capabilities)
  - Expand Your Team with Copilot (Copilot Coding Agent)
- AZ-2007 as the deeper hands-on execution follow-on
- GitHub Copilot documentation and features reference
- Encourage experimentation and iteration

#### Transcript

### Next Steps

So what do you actually do after today, when this session ends and you go back to your normal work? Let me give you a concrete action plan, because the worst thing that could happen is you sit in this session for three hours, nod along, and then never actually try anything.

First, my challenge to you. This week — not next month, not 'when I have time', this week — pick one real workflow from your actual work and try using Copilot for it. Just one workflow, one time. That's it. Maybe it's writing tests for a module you've been putting off. Maybe it's refactoring a function that's gotten too complex. Maybe it's documenting an API you wrote six months ago and can barely remember. Maybe it's onboarding to a part of your codebase you've been quietly avoiding because it intimidates you. Maybe it's just generating a sensible commit message instead of writing 'updates' for the hundredth time.

Pick one specific thing. Try Copilot on it deliberately. See what happens. Be surprised by what works, take notes on what doesn't, and adjust. You'll be amazed how quickly Copilot becomes part of your natural workflow once you've crossed that initial threshold of just using it on something real. The hardest step is always the first one.

For hands-on practice beyond your daily work, I strongly recommend the GitHub Skills exercises. These are free, completely self-paced, and they run entirely in your browser using GitHub Codespaces — no setup required at all. You don't even need to install anything locally. Just log into GitHub, click Start, and you're in.

The most relevant exercises to what we covered today are: 'Getting Started with GitHub Copilot' — which uses the exact same Mergington High School project we demoed today. You'll go through the project onboarding, the bug fix, the data generation, the Agent Mode features, the testing workflow, and the PR process yourself, hands-on. It takes less than an hour and it's the perfect immediate follow-up to today's session.

The second one to try is 'Customize Your GitHub Copilot Experience' — where you build repository instructions, file-specific instructions with applyTo patterns, reusable prompt files with slash commands, and even your first custom agent. This is how you take what you learned today and make Copilot work specifically for your team's standards and conventions.

There are also exercises on integrating MCP tools to give Copilot extra capabilities beyond what's built in, and on using the Copilot Coding Agent to expand your team's capacity by having Copilot work autonomously on issues and create pull requests for you to review.

And if you want to go much, much deeper — that's AZ-2007. That's the intensive, hands-on, multi-day session where you build real things with Copilot, tackle complex realistic scenarios, and develop the muscle memory for AI-assisted development as a daily practice. Think of today as building the conceptual understanding that makes AZ-2007 productive and efficient. Today was the foundation. AZ-2007 is the structure built on top.

All the documentation for GitHub Copilot — features, interaction modes, customization options, advanced techniques — is available on docs.github.com. I encourage you to explore it, experiment freely, and iterate. The truth is that the more you use Copilot, the better you get at prompting it, and the more value you extract from every single interaction. There's a learning curve, but it's a steep curve in the good direction — you get noticeably better in days and weeks, not months.

A few specific resources to bookmark right now. The official documentation at docs.github.com/copilot is the canonical reference — every feature, every setting, every interaction mode is documented there with examples. The GitHub Copilot blog publishes regular updates on new capabilities, customer stories, and best practices, and it's worth checking once a week. The github.com/github/awesome-copilot repository on GitHub is a community-maintained collection of prompt files, custom instructions, and custom agents you can borrow from and adapt. Don't reinvent the wheel — many teams have already shared excellent customization patterns you can build on.

And one final practical tip. As you start using Copilot more deliberately, keep a small running list — just a Markdown file in your notes, or a thread in your team's chat — of the prompts and patterns that worked well. Over time that list becomes your personal Copilot playbook, and it becomes the source material for the customization files you'll eventually push into your team's repositories. Today's experiments become tomorrow's team standards. That's how you compound the value over time.

---

### 10.3 Closing Interaction

**Type:** Prompt  |  **Duration:** 6 min

#### Delivery Notes

### Focus
End on a forward-looking, energizing note with audience engagement.

### Cover
- Chat prompt: "One workflow you'll try Copilot on this week"
- Read out and acknowledge several responses
- Thank learners for their time and engagement
- Share feedback/survey link if applicable
- End exactly on time
- Final message: happy coding with your new AI pair programmer

#### Transcript

### Closing

Before we wrap up completely, I'd love to hear from you one more time. Drop in the chat: what's one specific workflow you plan to try Copilot on this week, in your actual real work? I'm genuinely curious to see the variety of answers, and stating it publicly here in the chat makes you slightly more likely to follow through. Behavioral psychology says so.

I'll give you a moment to type… and I see some great answers coming in already. Let me read a few that catch my eye. Testing — absolutely, that's where many people see the fastest and most measurable return on Copilot. Code review — a smart choice, especially the commit message generation and PR summary features which add up over time. Documentation — a fantastic one, Copilot is excellent at generating and updating docs and it's the kind of work most engineers actively dislike doing. Onboarding to a legacy codebase nobody understands anymore — brave choice, and Copilot will genuinely help you make sense of code nobody has touched in years. Refactoring — yes, Agent Mode is perfect for that kind of multi-file coordinated work.

Those are all excellent starting points, and I'm seeing a really good mix. Remember the key principle: you don't have to change everything at once. You don't have to overhaul your entire workflow. Start with one specific workflow this week, get genuinely comfortable with it, build your prompting intuition, and then expand from there. Copilot also gets better as you learn to work with it — better prompts, more relevant context, better results. It's a feedback loop, and every interaction is practice.

Thank you all sincerely for your time today. Three hours is a significant investment of your day, and I deeply appreciate that you spent it with me. I really hope you're walking away with both a solid conceptual understanding of GitHub Copilot and genuine excitement about how it can transform your daily development workflow.

If there's a feedback survey for this session in your follow-up email, please take just a few minutes to fill it out. Your specific input directly shapes how we improve these sessions for the people who come after you. Even one or two sentences of honest feedback is incredibly valuable for us.

Let me leave you with this final framing. GH-300 today gave you the fundamentals — the conceptual understanding. The GitHub Skills exercises will give you immediate hands-on practice this week. AZ-2007 will give you the deep execution skills if you want to go further. And your daily work itself, with deliberate practice, is what gives you real lasting mastery over time. Each layer builds on the previous one.

Alright, that's our session. Have a great rest of your day, take care, and happy coding with your new AI pair programmer. Goodbye everyone, and thanks again!

---
