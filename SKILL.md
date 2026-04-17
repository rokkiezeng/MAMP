---
name: mamp
description: Mark AI Memory Protocol — persistent, searchable session memory for AI agents. SQLite-only, zero external dependencies.
author: LeoTseng
version: 1.1.6
license: MIT-0
security:
  credential_access: false  # Local SQLite only, no external services or credentials
  data_persistence: true     # Writes to a local .db file on disk
---

# MAMP — Mark AI Memory Protocol

Gives AI agents persistent, searchable memory using SQLite.

## When to Use

- User says "remember what I told you last time"
- Agent needs to recall facts across conversations
- User asks about past topics, preferences, or decisions
- Context window is filling up and older info needs to be summarized

## Core Concepts

- **Session** — a conversation, has an ID, survives restarts
- **Turn** — one message in a session (role: user/assistant)
- **Tag** — labels for a turn, e.g. ["finance", "important"]
- **Priority** — importance level: critical, normal, trivial

## Key Methods

```python
from importlib.util import spec_from_file_location, module_from_spec
spec = spec_from_file_location("mamp", "ai_memory_protocol_v1.1.6.py")
mod = module_from_spec(spec)
spec.loader.exec_module(mod)

# Default: writes to ./mark_memory.db in current directory
sm = mod.SessionManager()
# Or specify path explicitly (recommended):
sm = mod.SessionManager(db_path="./memory.db")
# Or via environment variable:
# export MARK_MEMORY_DB=/path/to/memory.db
# (overrides default and db_path parameter)

# Start a conversation
sid = sm.start_conversation()

# Add a message
sm.add_turn("user", "I prefer dark mode")
sm.add_turn("assistant", "Noted")

# Search across all sessions
count = sm.search_count("dark mode")
results = sm.search("dark mode", limit=5)

# Get full session
sess = sm.get_session_extended(sid)
# → {'total_turns': 2, 'turns': [...], 'meta': {...}}

# Tag and filter
sm.add_turn("user", "finance topic", tags=["finance"])
c = sm.search_count("topic", tag_filter=["finance"])
```

## What It Solves

AI forgets everything each conversation. MAMP makes memory persistent, searchable, and structured — without any external service, API key, or dependency beyond SQLite.

## Security Notes

**Default behavior — local directory only:**

- DB file written to `./mark_memory.db` in the current working directory
- No system directories are touched
- No log files, audit files, or hidden state files are written
- No network access, no external services

**Pass an explicit path to isolate data:**

```python
sm = mod.SessionManager(db_path="/your/specific/path/memory.db")
```

**Environment variable override:**

```bash
export MARK_MEMORY_DB=/your/specific/path/memory.db
```

This takes precedence over both the default and any `db_path` argument.

**Permissions awareness:**

- The DB file contains your conversation history in plaintext
- Ensure the directory has appropriate access controls
- If multiple agents run on the same host with the same path, they share memory — use different paths per agent to isolate

**No credentials stored:**

MAMP uses no API keys, tokens, or secrets. It is a pure local SQLite store.
