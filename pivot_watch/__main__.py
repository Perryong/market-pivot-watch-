import argparse
import json
import sys
import time
from pathlib import Path

from .app import ROOT, atomic_text, demo_fetch, json_text, load_state, run, write_outputs
from .core import DataError
from .providers import fetch


def main():
    parser = argparse.ArgumentParser(description="Read-only completed-4H pivot analysis")
    parser.add_argument("--config", type=Path, default=ROOT / "config.json")
    parser.add_argument("--state", type=Path, default=Path(".state/state.json"))
    parser.add_argument("--out", type=Path, default=Path("output"))
    parser.add_argument("--demo", action="store_true", help="Synthetic fixtures, isolated from live state")
    args = parser.parse_args()
    try:
        if args.demo and args.state == Path(".state/state.json"):
            raise DataError("Demo requires an explicit separate --state path")
        now = 1789516800 + 14460 if args.demo else time.time()
        config = json.loads(args.config.read_text(encoding="utf-8"))
        state = load_state(args.state)
        if state.get("demo", False) != args.demo and state["markets"]:
            raise DataError("Refusing to mix live and demo state")
        reports, state = run(config, state, now, demo_fetch if args.demo else fetch)
        state["demo"] = args.demo
        # Persist only after successful report/preset generation. Workflow must commit this file.
        write_outputs(args.out, reports, now)
        atomic_text(args.state, json_text(state))
        print((args.out / "report.md").read_text(encoding="utf-8"))
        return 2 if any("error" in r for r in reports) else 0
    except (DataError, OSError, ValueError, KeyError, TypeError) as exc:
        # No provider response bodies or arbitrary raw exceptions in logs.
        message = str(exc) if isinstance(exc, DataError) else "Invalid configuration or file operation failed"
        print("ERROR: " + message, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
