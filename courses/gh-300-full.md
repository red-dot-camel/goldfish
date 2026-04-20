# GH-300 GitHub Copilot — Full Transcript

**Total duration:** 180 min

---

## 1. Welcome & Session Framing

_Chapter duration: 10 min_

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

### 1.3 Audience Check-In

**Type:** Prompt  |  **Duration:** 2 min

#### Delivery Notes

### Focus
Gauge audience composition and Copilot experience.

### Cover
- Chat prompt: "What's your role today? Developer / Lead / Manager"
- Reaction check: Used GitHub Copilot before? (thumbs-up = yes)
- Acknowledge the diversity and set inclusive expectations
- Transition to fundamentals

#### Transcript

### Interaction

Before we get into the content, I'd love to know who's in the room today. Drop in the chat: what's your role? Developer, technical lead, engineering manager, or something else like product or evaluation? Just a word or two is fine.

And while answers come in — a quick reaction check. Thumbs up if you've used GitHub Copilot before, even briefly. Surprised face if this session is your very first introduction.

I'm watching the chat… great mix. Lots of developers, several leads, a handful of managers. Some of you are using Copilot daily already, some have tried it once or twice, a meaningful number are completely new to it. Perfect. This session is designed to meet you wherever you are.

For those already using Copilot, my goal is you pick up at least two or three new techniques you weren't using before. For brand new folks, you'll walk away with a clear picture of what Copilot does and exactly where to start. Alright — let's get into the fundamentals.

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

## 3. Responsible AI & Validation Mindset

_Chapter duration: 26 min_

### 3.1 Copilot Output Is a Starting Point

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

### 3.2 Validation Workflow Demo

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

### 3.3 Responsible AI Risk Poll

**Type:** Prompt  |  **Duration:** 3 min

#### Delivery Notes

### Focus
Engage audience on perceived risks and reinforce validation mindset.

### Cover
- Reaction poll: Biggest risk? Security / Logic / Bias / Over-reliance
- Acknowledge all four are real and interconnected
- Reinforce: mitigation is always review, test, validate
- Bridge to break with energy

#### Transcript

### Risk Poll

Let's do a quick poll while what we just saw is fresh in your minds. Using your Teams reactions, tell me — of the four risks I described, which one feels like the biggest concern for your team or your work?

Give me a thumbs up if you think it's security risks — the worry that Copilot will introduce vulnerabilities. A heart if it's incorrect logic — subtle bugs that make it through review. A clap if it's bias — outdated patterns or anti-patterns being suggested as if they were best practice. And a surprised face if it's over-reliance — the human tendency to accept what looks reasonable without truly reviewing it.

Let me watch the reactions roll in… interesting spread of answers. Looks like over-reliance and security are tied for the lead, with incorrect logic close behind, and bias coming in fourth. That's actually a very mature distribution of concerns — it suggests this audience is already thinking about this seriously.

Here's the truth, though: all four are real, and they're deeply interconnected. A security gap is often a form of incorrect logic. Over-reliance means you don't catch the bias when it shows up. Bias in suggestions feeds incorrect logic. They reinforce and compound each other. So you can't really pick one to worry about and ignore the rest.

The good news is that the mitigation strategy is the same regardless of which risk you're most worried about: review your code carefully, write tests that exercise edge cases, validate behavior against your real requirements, and treat AI output the same way you'd treat code from a fast but unfamiliar contractor. Copilot accelerates the writing. The engineering discipline stays with you, and arguably becomes more important, not less.

Alright, we've built a solid foundation now. You understand what Copilot is, you've seen the five interaction modes, you've watched Ask Mode in action, and you know how to think about Copilot's output responsibly. That's a great place to take our first break. We'll be back in ten minutes, and then we dive into the fun part — a series of live demos showing core developer workflows where Copilot really shines.

---

## 4. Break 1

_Chapter duration: 10 min_

### 4.1 Break

**Type:** Pause  |  **Duration:** 10 min

#### Delivery Notes

### 10-Minute Break

- Clearly state return time on screen
- Restart exactly on time to protect demo flow
- Display break countdown or "Back at HH:MM" slide

---

## 5. Core Developer Workflows

_Chapter duration: 35 min_

### 5.1 Demo Strategy Introduction

**Type:** Narration  |  **Duration:** 3 min

#### Delivery Notes

### Focus
Frame the demo block — what they'll see and why.

### Cover
- Remind audience we're continuing with the Mergington High School project
- Live, scripted demos — narrating thinking and decisions
- Focus on where Copilot saves time and what still requires human judgment
- If anything breaks, we switch to screenshots — never troubleshoot live

#### Transcript

### Demo Setup

Welcome back everyone, I hope you got a chance to stretch and refill your coffee. Now the real fun begins — we're going to spend the next thirty-five minutes doing live demos of core developer workflows, the kind of work you actually do every day.

We're continuing with the same Mergington High School project we explored earlier. You already saw Ask Mode give us a full project overview in thirty seconds, and you saw the validation workflow with prompt-refine-review. Now we'll go deeper. We'll get help in the terminal when our git memory fails us. We'll fix a real bug together using inline suggestions. We'll generate realistic sample data with Inline Chat. And we'll use Agent Mode to build a full feature across multiple files from a single prompt. Each demo highlights a specific Copilot pattern you can take back to your own work tomorrow.

A few things about how I'll run these demos. I'll narrate my thinking out loud throughout — why I'm choosing a particular Copilot mode for the task, what I'm looking for in the output as it streams in, where I'd push back on the suggestion, and where I need to apply my own engineering judgment. These are scripted, repeatable workflows, not random improvisation, so what you see should be reproducible if you try the same things later in the GitHub Skills exercise.

One ground rule for me: if something breaks during a demo, I'm not going to stop and try to debug it live. We've all been to those sessions where the presenter spends ten minutes troubleshooting a Codespace and the audience checks out completely. I won't do that to you. If anything misbehaves, I'll switch to screenshots or narrated storytelling and we'll keep moving. Our time together is too valuable for live debugging. Let's go.

---

### 5.2 Terminal Inline Chat

**Type:** Demo  |  **Duration:** 3 min

#### Delivery Notes

### Focus
Show Copilot's terminal inline chat for command recall.

### Cover
- Open a new terminal tab (keep debugger running)
- Use Ctrl+I to invoke terminal inline chat
- Prompt: "How can I create and publish a new Git branch called accelerate-with-copilot?"
- Show Copilot generating the exact git commands
- Press Run to execute directly
- Highlight: Copilot helps with commands you've forgotten, keeping you in flow

#### Transcript

### Demo: Terminal Help

Here's a small but useful way Copilot helps that people often overlook — it works right in the terminal too, not just in the editor.

Let me open a new terminal tab. I'm keeping the existing debug session running in the original terminal so our website stays live. Now, in this new tab, I want to create and publish a new git branch — but let's pretend I can't quite remember the exact git command syntax. We've all been there. You know roughly what you want to do, but the exact incantation slips your mind.

Instead of switching to a browser tab to search Stack Overflow, I press Control-I right here inside the terminal. That brings up Copilot's terminal inline chat — same shortcut as the editor inline chat, just contextually aware that I'm in a terminal.

I type: 'How can I create and publish a new Git branch called accelerate-with-copilot?'

Copilot gives me the exact commands. First git checkout -b accelerate-with-copilot to create and switch to the new branch. Then git push -u origin accelerate-with-copilot to publish it and set the upstream so future pushes are easier. I just press the Run button and it executes both commands right there in the terminal. No copy-paste, no context switching, no leaving my workspace.

This seems like a tiny thing, but think about how many times a day you Google a command you've used before but can't quite remember. Docker commands, git operations, npm scripts, kubectl commands, complex find or grep invocations. Each one of those is a tiny context switch that breaks your flow. Copilot keeps you in flow state by answering right where you're already working.

---

### 5.3 Bug Fix with Inline Suggestions

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

### 5.4 Generate Sample Data with Inline Chat

**Type:** Demo  |  **Duration:** 7 min

#### Delivery Notes

### Focus
Demonstrate Inline Chat for targeted, scoped code generation.

### Cover
- Explain Inline Chat vs Chat panel — scoped vs broad
- Find and highlight the activities dictionary in src/app.py
- Open Inline Chat with Ctrl+I on the selection
- Prompt: "Add 2 more sports, 2 more artistic, and 2 more intellectual activities"
- Show Copilot generating realistic sample data matching the existing pattern
- Accept changes with Keep button
- Refresh website to verify new activities appear
- Highlight: Copilot understood the data schema from context alone

#### Transcript

### Demo: Inline Chat for Data Generation

Let me show you Inline Chat now — this is different from the Chat panel because it's scoped to exactly the code you're looking at and selected. Different tool, different sweet spot.

In new projects — or when you're adding new features to an existing project — you very often need realistic sample data for testing or for making the UI feel populated. Manually writing out data structures with consistent formatting is tedious, slow, and unrewarding work. It's exactly the kind of task where Copilot shines.

Let me find the activities dictionary near the top of app.py. There it is — this is our in-memory database. Right now we have three entries: Chess Club, Programming Class, and Gym Class. Each one has the same shape: description, schedule, max_participants, and an empty participants list. Realistic but pretty thin.

Here's the technique. I'm going to highlight the entire activities dictionary — from the opening brace through all three existing entries to the closing brace. The reason I'm selecting all of it is to give Copilot maximum context about the structure I want it to follow. Without that selection, it would have to guess. With it, the pattern is right there.

Now I press Control-I, which brings up Inline Chat right here on my selection. Notice it's a small chat input attached to the selected code, not the side panel. Different mode, different scope.

I type: 'Add two more sports related activities, two more artistic activities, and two more intellectual activities. Use realistic schedules and reasonable participant limits.'

Watch what happens. Copilot is generating new entries. They appear inline, in a diff view so I can see exactly what's being added. Let me read through them: Basketball Team meeting Tuesdays and Thursdays after school. Swimming Club on Mondays and Wednesdays. Art Studio on Wednesdays. Drama Club on Tuesdays. Debate Team on Thursdays. Science Club on Fridays. Each one has a sensible description, a realistic schedule, and an appropriate max_participants count — twenty for sports, fifteen for arts, twenty-five for intellectual.

All of them follow the exact structure of the existing entries. All consistent with the pattern. All realistic, plausible data — nothing weird or out of place. And critically, I never had to specify the schema. Copilot understood it from the highlighted context, because that's exactly what selection-based context is for.

I'll click Accept to apply the changes, then refresh the website to verify. And there they are — all six new activities showing up in the page, mixed in with the original three, all displaying their schedules correctly. Beautiful.

The lesson here: Inline Chat is your go-to tool for targeted, scoped changes on the code right in front of you. The Chat panel is better when you need broader exploration, multi-file work, or you don't yet know which file is relevant. Pick the right tool for the right scope.

---

### 5.5 Agent Mode: Build a Feature

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

### 5.6 Workflow Impact Check

**Type:** Prompt  |  **Duration:** 3 min

#### Delivery Notes

### Focus
Engage audience on demo impact before the break.

### Cover
- Thumbs up reaction: "Would these workflows help you tomorrow?"
- Chat prompt: "Where do you lose the most time today?"
- Acknowledge responses and bridge to break
- Preview: testing and quality workflows after the break

#### Transcript

### Quick Check

Let me pause here and check in with you, because we just covered a lot of demo material. Give me a thumbs up if these workflows we just walked through — the project onboarding earlier, the bug fixing with inline suggestions, the data generation with Inline Chat, and the multi-file feature building with Agent Mode — would genuinely help you in your daily work. Be honest. Some of these might already be part of your workflow, others might feel new.

Fantastic response, lots of thumbs up rolling in. Now drop in the chat: where do you actually lose the most time today, in your real work? Is it writing boilerplate code? Debugging? Writing tests? Doing code review? Updating documentation? Onboarding to unfamiliar parts of the codebase? Just a word or two.

Let me read what's coming in… testing comes up a lot. Debugging too. Several people mentioning documentation. A surprising number mentioning code review. And a handful mentioning the slog of onboarding to legacy code. All very real pain points, and all areas where Copilot can genuinely help.

This is perfect timing, because after our break we're going to cover exactly those areas. We'll look at Plan Agent for designing a test strategy, full test generation including the fix-and-rerun cycle, then code review and PR workflows, and then customizing Copilot for your team's specific standards and conventions.

Let's take our second break now. Ten minutes, please be back right on time — we've got a lot of valuable content in the second half and I don't want to cut anything short.

---

## 6. Break 2

_Chapter duration: 10 min_

### 6.1 Break

**Type:** Pause  |  **Duration:** 10 min

#### Delivery Notes

### 10-Minute Break

- Clearly state return time on screen
- Restart exactly on time to protect demo flow
- Display break countdown or "Back at HH:MM" slide

---

## 7. Testing & Quality Workflows

_Chapter duration: 23 min_

### 7.1 Copilot for Testing Overview

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

### 7.2 Plan Agent: Test Strategy

**Type:** Demo  |  **Duration:** 8 min

#### Delivery Notes

### Focus
Demonstrate Plan Agent for designing a test approach before implementation.

### Cover
- Switch to Plan Agent mode in Copilot Chat
- Prompt: "I want to add backend FastAPI tests in a separate tests directory."
- Show Plan Agent drafting a plan — test files, structure, coverage areas
- Refine: "Use AAA (Arrange-Act-Assert) pattern" and "Use pytest, add to requirements.txt"
- Review the structured plan with updated constraints
- Click "Start Implementation" to hand off to Agent Mode
- Watch Agent Mode create test files and run them
- Highlight: deliberate planning leads to better implementation

#### Transcript

### Demo: Plan Agent for Testing

Let me show you Plan Agent in action — testing strategy is actually a perfect use case for Plan Agent because it's exactly the kind of work where you want to think carefully before you commit to writing code.

I'll switch to Plan Agent in the chat dropdown at the bottom of the panel. Notice the mode change. Now I'll type a relatively open prompt: 'I want to add backend FastAPI tests in a separate tests directory. I want good coverage of the signup endpoint behaviors we built earlier today.'

Watch what happens — and this is the key difference from Agent Mode. Plan Agent does NOT start writing code. Instead, it researches the project structure, looks at the existing endpoints, understands the data model, and starts drafting a plan. You can see it exploring the workspace in the activity log. It might also ask me clarifying questions: what testing framework do I want to use? What should the test file structure look like? Which endpoints need coverage first? Are there existing fixtures I should reuse?

Let me refine the plan with some specific requirements as it develops. I'll add: 'Let's use the Arrange-Act-Assert pattern — AAA — to structure each test, and please include a comment header in each test indicating which phase is which.' I'll also add: 'Make sure we use pytest specifically, and add it to requirements.txt with an appropriate version pin.'

Plan Agent updates the plan to incorporate these new constraints. Now I can see the structured approach laid out cleanly in the chat panel: which test files to create, what test cases each file should contain, what the AAA structure looks like for each test, what the directory layout should be. There are tests planned for the happy path — successful signup, successful retrieval of activities. Tests for error cases — activity not found returning 404, duplicate signup returning 400. And tests for edge cases — hitting the max participants limit, missing parameters, empty input.

I review the plan carefully. I'm satisfied with the coverage and the structure — it matches what I would have asked a junior engineer to do, but it's been generated and refined in under a minute. So I click the 'Start Implementation' button at the bottom of the plan.

Notice it switches automatically from Plan to Agent Mode. Now Copilot takes the plan I just approved and starts implementing it. It creates the tests directory, writes each test file, structures every test with the AAA comment markers I requested, adds pytest to requirements.txt with a sensible version pin, and even adds a brief README explaining how to run the tests.

This combination is genuinely powerful. For non-trivial changes — anything that touches multiple files or where the approach matters — you get the clarity of a reviewed plan combined with the speed of automated implementation. You thought first, you reviewed second, and Copilot built third. Compared to just blasting Agent Mode with a vague prompt and hoping for the best, this gives you much more control and much higher quality outputre tests planned for the happy path — successful signup, successful retrieval of activities. Tests for error cases — activity not found returning 404, duplicate signup returning 400. And tests for edge cases — hitting the max participants limit, missing parameters, empty input.

I review the plan carefully. I'm satisfied with the coverage and the structure — it matches what I would have asked a junior engineer to do, but it's been generated and refined in under a minute. So I click the 'Start Implementation' button at the bottom of the plan.

Notice it switches automatically from Plan to Agent Mode. Now Copilot takes the plan I just approved and starts implementing it. It creates the tests directory, writes each test file, structures every test with the AAA comment markers I requested, adds pytest to requirements.txt with a sensible version pin, and even adds a brief README explaining how to run the tests.

This combination is genuinely powerful. For non-trivial changes — anything that touches multiple files or where the approach matters — you get the clarity of a reviewed plan combined with the speed of automated implementation. You thought first, you reviewed second, and Copilot built third. Compared to just blasting Agent Mode with a vague prompt and hoping for the best, this gives you much more control and much higher quality output.

---

### 7.3 Test Generation and Fix Cycle

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

### 7.4 Testing Reflection

**Type:** Prompt  |  **Duration:** 2 min

#### Delivery Notes

### Focus
Quick audience engagement on testing experience.

### Cover
- Reaction poll: Tests easier with Copilot? (thumbs-up = yes)
- Chat prompt: "What part of testing slows you down most?"
- Bridge to code review and customization section

#### Transcript

### Quick Poll

Quick reaction check — thumbs up if you think testing would be significantly easier with Copilot assisting you the way you just saw.

That's a strong response. And honestly, this is one of the areas where the productivity impact is most tangible and most measurable. Teams I work with consistently report that test coverage goes up after they start using Copilot, simply because the boilerplate friction is so much lower.

Drop in the chat: what part of testing slows you down most today? Writing the initial tests? Knowing what to test? Debugging failures? Maintaining tests when code changes? I'm genuinely curious about the distribution.

Great variety of answers coming in. I see writing initial tests, edge case discovery, debugging flaky tests, maintaining tests as the implementation evolves. Copilot helps across all of those, especially as you get better at giving it specific prompts about your testing requirements. Let's now turn to code review, pull requests, and customization.

---

## 8. Streamline Code Review & Customization

_Chapter duration: 18 min_

### 8.1 Copilot for Commits and Pull Requests

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

### 8.2 Customizing Copilot for Your Team

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

### 8.3 Custom Instructions Demo

**Type:** Demo  |  **Duration:** 6 min

#### Delivery Notes

### Focus
Quickly demonstrate repository instructions and their effect on Copilot responses.

### Cover
- Show the Customize Your GitHub Copilot Experience project (Mergington homework website)
- Create .github/copilot-instructions.md with project description and coding guidelines
- Ask Copilot "Briefly explain this project" — show response shaped by instructions
- Show .github/instructions/assignments.instructions.md with applyTo: "assignments/**/*.md"
- Ask Copilot to update an assignment file — show it referencing both instruction files
- Show .github/prompts/new-assignment.prompt.md — invoke with /new-assignment
- Briefly mention custom agents (.github/agents/assignment-brainstorming.agent.md)
- Highlight: instructions change HOW Copilot works in your repo, prompts change WHAT tasks are available

#### Transcript

### Demo: Custom Instructions

Let me show you customization in practice. I'll switch to a different project for this demo — this is the Mergington High School homework assignment website, which comes from another GitHub Skills exercise called 'Customize Your GitHub Copilot Experience'. Same fictional school, different application: this one is for teachers to share homework assignments with students.

First, repository-level instructions. I create a file at .github/copilot-instructions.md. Inside it, I add a project description in plain English: this is an educational website for sharing homework assignments, here's the folder structure, assignments live in the assignments folder, each one follows a specific Markdown template, we maintain consistent visual styling across pages, and we use student-friendly language because our audience is high school students — nothing patronizing, but accessible.

Now when I ask Copilot 'Briefly explain this project,' watch how the response is completely shaped by these instructions. It doesn't give a generic web project answer. It talks about the educational purpose, the assignment structure, the student-friendly approach, the specific folder layout. It understood the context because we told it. Same project, before instructions versus after — night and day difference in the quality of its responses.

Next, targeted instructions. I create another file at .github/instructions/assignments.instructions.md. In the front matter at the top, I set applyTo to 'assignments/**/*.md' — so these rules only activate when Copilot is working on Markdown files inside the assignments directory. Then in the body, I specify the assignment template structure: required sections like 'Learning Objectives', 'Instructions', 'Submission Requirements', formatting standards, the heading hierarchy, and the tone we want.

When I open an actual assignment file and ask Copilot to update it to follow project standards, it automatically references both the general repo-level instructions AND the assignment-specific instructions. Two layers of context, automatically applied based on which file is open. I never had to remind it. That's the layered customization model in action.

I can also create a prompt file at .github/prompts/new-assignment.prompt.md that defines a reusable workflow. The prompt tells Copilot exactly what to do: gather assignment information from the user, create the directory structure, generate the README from the template, update the website navigation. My team invokes this with /new-assignment in the chat panel. Consistent, repeatable, and everyone on the team does it the same way — even teachers who aren't full-time developers.

And for teams that want to go even further, custom agents let you create specialized experiences — like a brainstorming agent that helps teachers come up with creative assignment ideas without writing any code at all. Just conversational ideation, focused on a single purpose.

Each customization tool builds on the one before it, giving you progressively finer-grained control over how Copilot behaves in your specific project and for your specific team.

---

## 9. Wrap Up & Next Steps

_Chapter duration: 20 min_

### 9.1 Key Takeaways

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

### 9.2 Next Steps and Resources

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

### 9.3 Closing Interaction

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
