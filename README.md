# CuePilot

A **glanceable presentation timing assistant** for instructors delivering structured sessions. Built as a Tauri v2 native desktop app, designed to live on a secondary monitor.

## What It Does

CuePilot answers four questions at a glance during any presentation:

- **Where am I?** — Current chapter and section
- **How much time?** — Countdown timer with overtime tracking
- **What's next?** — Upcoming section preview
- **Am I on track?** — Schedule drift indicator

The UI is optimized for **<1 second visual parsing** with zero cognitive overhead.

## Pages

| Page | Purpose |
|------|---------|
| **Course Selection** | Grid of courses from local storage and GitHub |
| **Timer** | Two-panel view: countdown + section instructions |
| **Editor** | Three-panel course authoring with drag-and-drop |

## Getting Started

**Prerequisites:** Node.js 18+, Rust toolchain (`x86_64-pc-windows-gnu`), Tauri CLI

```bash
npm install          # install dependencies
npm run tauri:dev    # start dev server + launch native window
npm run tauri:build  # build production executable → src-tauri/target/release/
```

## Features

- **Countdown timer** with automatic overtime (count-up) mode
- **Color-coded states** — green (on track), yellow (wrapping up), red (overtime)
- **Schedule drift** — shows how far ahead or behind you are for the full session
- **Auto-advance** — moves to the next section when time expires
- **Keyboard controls** — no mouse required during delivery
- **Course editor** — author courses in-app with drag-and-drop chapter/section reordering
- **Dual course sources** — local files (Rust backend) + `uweinside/goldfish-data` on GitHub

## Keyboard Shortcuts (Timer)

| Key | Action |
|-----|--------|
| `Space` | Pause / Resume |
| `→` | Next chapter |
| `←` | Previous chapter |
| `Escape` | Close notes panel |

## Tech Stack

- **Runtime**: Tauri v2 (Rust backend + WebView frontend)
- **Frontend**: Vanilla TypeScript + Vite (no UI framework)
- **Styling**: Custom CSS
- **Target**: Windows (MinGW/GNU toolchain)

See [ARCHITECTURE.md](ARCHITECTURE.md) for a detailed breakdown of the module structure, data model, and Tauri/Vite integration.

## License

MIT — © 2026 Uwe Baumann