# GH-300 GitHub Copilot

**Total duration:** 180 min  
**Chapters:** 9  
**Sections:** 28

---

## 1. Welcome & Session Framing

_Chapter duration: 10 min_

### 1.1 Welcome and Scale Delivery Norms

- **Type:** Narration
- **Duration:** 4 min

### Focus
Set a warm tone and establish scale delivery norms for a large audience.

### Cover
- Welcome global audience
- Confirm 3-hour session duration with two 10-minute breaks
- Microphones muted, cameras optional
- Chat for guided prompts only — no open-mic Q&A
- Moderator handles chat questions
- Teams reactions: thumbs-up = yes, surprised = no

### 1.2 Session Positioning

- **Type:** Narration
- **Duration:** 4 min

### Focus
Position GH-300 as foundational Copilot understanding. Demo-led, no labs.

### Cover
- GH-300 = foundational GitHub Copilot understanding
- Demo-led storytelling — no labs, no environment setup, no breakout rooms
- Copilot supports developers — does not replace thinking
- Focus on daily developer workflows, not syntax mastery or configuration
- AZ-2007 = deeper developer execution follow-on
- Scripted, repeatable demos throughout

### 1.3 Audience Check-In

- **Type:** Prompt
- **Duration:** 2 min

### Focus
Gauge audience composition and Copilot experience.

### Cover
- Chat prompt: "What's your role today? Developer / Lead / Manager"
- Reaction check: Used GitHub Copilot before? (thumbs-up = yes)
- Acknowledge the diversity and set inclusive expectations
- Transition to fundamentals

---

## 2. GitHub Copilot Fundamentals & Product Model

_Chapter duration: 28 min_

### 2.1 What Is GitHub Copilot

- **Type:** Narration
- **Duration:** 7 min

### Focus
Build a clear mental model of what GitHub Copilot is and where it fits in developer work.

### Cover
- AI coding assistant — write code faster with less effort
- Proven productivity impact (GitHub blog research)
- Works across VS Code, JetBrains, Xcode, and github.com
- Not just autocomplete — a full AI pair programmer
- Individual AND team productivity benefits
- Part of the developer's daily flow: Idea → Code → Test → Document → Review → Iterate

### 2.2 Copilot Interaction Modes

- **Type:** Narration
- **Duration:** 11 min

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

### 2.3 Project Overview with Ask Mode

- **Type:** Demo
- **Duration:** 7 min

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

### 2.4 Interaction Mode Poll

- **Type:** Prompt
- **Duration:** 3 min

### Focus
Quick engagement to anchor the fundamentals.

### Cover
- Chat prompt: "Do you rely more on suggestions or chat today?"
- Acknowledge the mix
- Transition to Responsible AI section

---

## 3. Responsible AI & Validation Mindset

_Chapter duration: 26 min_

### 3.1 Copilot Output Is a Starting Point

- **Type:** Narration
- **Duration:** 10 min

### Focus
Establish that Copilot output requires human validation and review.

### Cover
- Copilot suggestions are starting points, not final answers
- LLMs predict probable code based on patterns — they don't understand intent
- Four key risks: incorrect logic, security gaps, bias, over-reliance
- Developer accountability remains exactly the same
- AI-generated code must meet the same quality bar as human-written code
- Copilot does not replace code review, testing, or engineering judgment

### 3.2 Validation Workflow Demo

- **Type:** Demo
- **Duration:** 13 min

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

### 3.3 Responsible AI Risk Poll

- **Type:** Prompt
- **Duration:** 3 min

### Focus
Engage audience on perceived risks and reinforce validation mindset.

### Cover
- Reaction poll: Biggest risk? Security / Logic / Bias / Over-reliance
- Acknowledge all four are real and interconnected
- Reinforce: mitigation is always review, test, validate
- Bridge to break with energy

---

## 4. Break 1

_Chapter duration: 10 min_

### 4.1 Break

- **Type:** Pause
- **Duration:** 10 min

### 10-Minute Break

- Clearly state return time on screen
- Restart exactly on time to protect demo flow
- Display break countdown or "Back at HH:MM" slide

---

## 5. Core Developer Workflows

_Chapter duration: 35 min_

### 5.1 Demo Strategy Introduction

- **Type:** Narration
- **Duration:** 3 min

### Focus
Frame the demo block — what they'll see and why.

### Cover
- Remind audience we're continuing with the Mergington High School project
- Live, scripted demos — narrating thinking and decisions
- Focus on where Copilot saves time and what still requires human judgment
- If anything breaks, we switch to screenshots — never troubleshoot live

### 5.2 Terminal Inline Chat

- **Type:** Demo
- **Duration:** 3 min

### Focus
Show Copilot's terminal inline chat for command recall.

### Cover
- Open a new terminal tab (keep debugger running)
- Use Ctrl+I to invoke terminal inline chat
- Prompt: "How can I create and publish a new Git branch called accelerate-with-copilot?"
- Show Copilot generating the exact git commands
- Press Run to execute directly
- Highlight: Copilot helps with commands you've forgotten, keeping you in flow

### 5.3 Bug Fix with Inline Suggestions

- **Type:** Demo
- **Duration:** 8 min

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

### 5.4 Generate Sample Data with Inline Chat

- **Type:** Demo
- **Duration:** 7 min

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

### 5.5 Agent Mode: Build a Feature

- **Type:** Demo
- **Duration:** 11 min

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

### 5.6 Workflow Impact Check

- **Type:** Prompt
- **Duration:** 3 min

### Focus
Engage audience on demo impact before the break.

### Cover
- Thumbs up reaction: "Would these workflows help you tomorrow?"
- Chat prompt: "Where do you lose the most time today?"
- Acknowledge responses and bridge to break
- Preview: testing and quality workflows after the break

---

## 6. Break 2

_Chapter duration: 10 min_

### 6.1 Break

- **Type:** Pause
- **Duration:** 10 min

### 10-Minute Break

- Clearly state return time on screen
- Restart exactly on time to protect demo flow
- Display break countdown or "Back at HH:MM" slide

---

## 7. Testing & Quality Workflows

_Chapter duration: 23 min_

### 7.1 Copilot for Testing Overview

- **Type:** Narration
- **Duration:** 5 min

### Focus
Position Copilot's role in improving code quality, not just development speed.

### Cover
- Testing is where Copilot provides enormous value
- Four areas: test generation, fixing failures, code explanation/review, security-aware thinking
- Copilot accelerates the mechanics of testing — doesn't replace test strategy
- Quality is what separates professional developers from code generators

### 7.2 Plan Agent: Test Strategy

- **Type:** Demo
- **Duration:** 8 min

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

### 7.3 Test Generation and Fix Cycle

- **Type:** Demo
- **Duration:** 8 min

### Focus
Show the complete test cycle: generation → run → failure → diagnosis → fix → green.

### Cover
- Show the generated test file with pytest tests in AAA pattern
- Walk through one test case structure: Arrange (setup), Act (API call), Assert (verify)
- Run the tests — show results
- If a test fails, use Copilot to diagnose and fix
- Show the passing test suite — all green
- Emphasize: Copilot helps you get to green faster, doesn't skip testing

### 7.4 Testing Reflection

- **Type:** Prompt
- **Duration:** 2 min

### Focus
Quick audience engagement on testing experience.

### Cover
- Reaction poll: Tests easier with Copilot? (thumbs-up = yes)
- Chat prompt: "What part of testing slows you down most?"
- Bridge to code review and customization section

---

## 8. Streamline Code Review & Customization

_Chapter duration: 18 min_

### 8.1 Copilot for Commits and Pull Requests

- **Type:** Demo
- **Duration:** 6 min

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

### 8.2 Customizing Copilot for Your Team

- **Type:** Narration
- **Duration:** 6 min

### Focus
Introduce the four levels of Copilot customization.

### Cover
- **Repository custom instructions** (.github/copilot-instructions.md): project context applied to every chat request
- **Instruction files** (.github/instructions/*.instructions.md): targeted rules for specific files/directories via applyTo
- **Prompt files** (.github/prompts/*.prompt.md): reusable slash-command workflows for common tasks
- **Custom agents** (.github/agents/*.agent.md): specialized chat experiences with their own personality and tools
- Key message: customization makes Copilot understand YOUR project, not just generic code
- These scale team consistency without relying on wikis nobody reads

### 8.3 Custom Instructions Demo

- **Type:** Demo
- **Duration:** 6 min

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

---

## 9. Wrap Up & Next Steps

_Chapter duration: 20 min_

### 9.1 Key Takeaways

- **Type:** Narration
- **Duration:** 7 min

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

### 9.2 Next Steps and Resources

- **Type:** Narration
- **Duration:** 7 min

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

### 9.3 Closing Interaction

- **Type:** Prompt
- **Duration:** 6 min

### Focus
End on a forward-looking, energizing note with audience engagement.

### Cover
- Chat prompt: "One workflow you'll try Copilot on this week"
- Read out and acknowledge several responses
- Thank learners for their time and engagement
- Share feedback/survey link if applicable
- End exactly on time
- Final message: happy coding with your new AI pair programmer

---
