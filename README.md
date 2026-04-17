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
- **Auto-record mode** — captures turns automatically without manual add_turn()

## Usage

```python
import sys
sys.path.insert(0, '.')
from importlib.util import spec_from_file_location, module_from_spec
spec = spec_from_file_location("mamp", "ai_memory_protocol_v1.1.8.py")
mod = module_from_spec(spec)
spec.loader.exec_module(mod)

# Manual mode
sm = mod.SessionManager()
sm.start_conversation()
sm.add_turn("user", "I prefer dark mode")
sm.add_turn("assistant", "Got it")

# Auto mode (v1.1.8) — auto-captures turns
sm = mod.SessionManager(auto_record=True)
sm.start_conversation()
# ... turns captured automatically ...
sm.stop()
```

Or use `demo.py` as a working reference.

## Project Structure

```
ai_memory_protocol_v1.1.8.py   ← protocol implementation
demo.py                        ← working demo (reference)
CHANGELOG.md                   ← full changelog
iteration_guide.md             ← how we iterate
LICENSE                        ← MIT-0
```

## License

MIT-0 — free for any use, no attribution required.
