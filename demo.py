#!/usr/bin/env python3
"""Demo: AI Memory Protocol v1.1.5 - Run with stdlib + sqlite3 only."""

import sys
import os
import tempfile
import importlib

# Load the actual protocol
sys.path.insert(0, os.path.dirname(__file__))
from importlib.util import spec_from_file_location, module_from_spec
spec = spec_from_file_location("protocol", "ai_memory_protocol_v1.1.5.py")
mod = module_from_spec(spec)
spec.loader.exec_module(mod)

DB_PATH = tempfile.mktemp(suffix=".db")
SessionManager = mod.SessionManager


def test_basic_search():
    """DEMO 1: add turns + search_count"""
    sm = SessionManager(DB_PATH)
    sm.start_conversation()
    sm.add_turn("user", "I love finance and glass bottles")
    sm.add_turn("assistant", "Interesting hobby")
    import time; time.sleep(0.05)
    c1 = sm.search_count("finance")
    c2 = sm.search_count("glass")
    ok = c1 == 1 and c2 == 1
    print(f"  [1] search_count finance={c1} glass={c2}  {'PASS' if ok else 'FAIL'}")
    return ok


def test_session_extended():
    """DEMO 2: get_session_extended returns full turns"""
    sm = SessionManager(DB_PATH)
    sid = sm.start_conversation()
    sm.add_turn("user", "Hello world")
    sm.add_turn("assistant", "Hi there")
    import time; time.sleep(0.05)
    s = sm.get_session_extended(sid)
    ok = s.get("total_turns") == 2
    print(f"  [2] total_turns={s.get('total_turns')}  {'PASS' if ok else 'FAIL'}")
    return ok


def test_priority_persist():
    """DEMO 3: priority_levels survive restart"""
    sm = SessionManager(DB_PATH)
    sm.add_priority_level("critical", 999)
    sm2 = SessionManager(DB_PATH)
    levels = sm2.get_priority_levels()
    ok = "critical" in levels
    print(f"  [3] priority_levels persist: {list(levels.keys())}  {'PASS' if ok else 'FAIL'}")
    return ok


def test_merge_duplicate():
    """DEMO 4: merge_sessions duplicate strategy"""
    sm = SessionManager(DB_PATH)
    sid1 = sm.start_conversation()
    sid2 = sm.start_conversation()
    sm.add_turn("user", "msg A")
    sm.add_turn("user", "msg B")
    import time; time.sleep(0.05)
    sm.merge_sessions(sid2, sid1, conflict_strategy="duplicate")
    s = sm.get_session_extended(sid1)
    ok = s.get("total_turns", 0) >= 2
    print(f"  [4] merge duplicate total_turns={s.get('total_turns')}  {'PASS' if ok else 'FAIL'}")
    return ok


def test_tag_filter():
    """DEMO 5: search with tag_filter"""
    sm = SessionManager(DB_PATH)
    sm.start_conversation()
    sm.add_turn("user", "finance topic", tags=["finance"])
    sm.add_turn("user", "other topic", tags=["other"])
    import time; time.sleep(0.05)
    c = sm.search_count("topic", tag_filter=["finance"])
    ok = c >= 1
    print(f"  [5] tag_filter finance count={c}  {'PASS' if ok else 'FAIL'}")
    return ok


def main():
    print("=== AI Memory Protocol v1.1.5 Demo ===\n")

    results = [
        test_basic_search(),
        test_session_extended(),
        test_priority_persist(),
        test_merge_duplicate(),
        test_tag_filter(),
    ]

    print(f"\nDatabase: {DB_PATH}")
    print(f"Demo complete! ({sum(results)}/{len(results)}) PASS)")

    # Cleanup
    if os.path.exists(DB_PATH):
        os.unlink(DB_PATH)

    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
