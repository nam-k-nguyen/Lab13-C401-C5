from __future__ import annotations

import argparse
import json

import httpx

from pathlib import Path

BASE_URL = "http://127.0.0.1:8000"
INCIDENTS_FILE = Path("data/incidents.json")


def get_incidents() -> dict[str, str]:
    if not INCIDENTS_FILE.exists():
        return {}
    return json.loads(INCIDENTS_FILE.read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", required=True, choices=get_incidents().keys())
    parser.add_argument("--disable", action="store_true")
    args = parser.parse_args()

    path = f"/incidents/{args.scenario}/disable" if args.disable else f"/incidents/{args.scenario}/enable"
    r = httpx.post(f"{BASE_URL}{path}", timeout=10.0)
    print(r.status_code, r.json())


if __name__ == "__main__":
    main()
