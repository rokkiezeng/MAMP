# AI Memory Protocol

A lightweight, self-contained session memory protocol for AI agents.

**Problem solved**: Every AI conversation starts fresh. This protocol gives AI agents persistent, searchable memory using SQLite — zero dependencies, runs anywhere.

## Quick Start

```bash
python3 demo.py   # runs 5 demos, shows PASS/FAIL
```

## Features

- **Persistent sessions** — conversations survive restarts
- **Full-text search** — FTS5 powered, fast keyword search
- **Cross-session recall** — search memories across all sessions
- **Priority levels** — tag and filter by importance
- **SQLite backend** — stdlib + sqlite3 only, no external deps

## Usage

```python
from ai_memory_protocol_v1_1_5 import SessionManager

sm = SessionManager()
sid = sm.start_conversation()
sm.add_turn("user", "I prefer dark mode")
sm.add_turn("assistant", "Got it")
count = sm.search_count("dark mode")       # → 1
results = sm.search("dark mode", limit=5)   # → matching turns
s = sm.get_session_extended(sid)           # → full session
```

## Project Structure

```
ai_memory_protocol_v1.1.5.py   ← protocol implementation
demo.py                        ← run this first
CHANGELOG_v1.1.5.md           ← full changelog
iteration_guide.md            ← how we iterate
LICENSE                        ← MIT-0 (public domain equivalent)
```

## License

MIT-0 — free for any use, no attribution required.
