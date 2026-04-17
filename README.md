# Mark AI Memory Protocol (MAMP)

A lightweight, self-contained session memory protocol for AI agents.

**Problem solved**: Every AI conversation starts fresh. MAMP gives AI agents persistent, searchable memory using SQLite — zero external dependencies, runs anywhere.

## Quick Start

```bash
git clone <repo>
cd MAMP
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
import sys
sys.path.insert(0, '.')
from importlib.util import spec_from_file_location, module_from_spec
spec = spec_from_file_location("mamp", "ai_memory_protocol_v1.1.6.py")
mod = module_from_spec(spec)
spec.loader.exec_module(mod)

sm = mod.SessionManager('.')
sid = sm.start_conversation()
sm.add_turn("user", "I prefer dark mode")
sm.add_turn("assistant", "Got it")
count = sm.search_count("dark mode")       # → 1
results = sm.search("dark mode", limit=5)  # → matching turns
s = sm.get_session_extended(sid)           # → full session
```

Or use `demo.py` as a working reference.

## Project Structure

```
ai_memory_protocol_v1.1.6.py   ← protocol implementation
demo.py                        ← working demo (reference)
CHANGELOG.md           ← full changelog
iteration_guide.md             ← how we iterate
LICENSE                        ← MIT-0
```

## License

MIT-0 — free for any use, no attribution required.
