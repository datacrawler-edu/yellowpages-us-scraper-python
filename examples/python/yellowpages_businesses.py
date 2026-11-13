"""Start the small sample search and print the saved businesses."""
import argparse
import json
from pathlib import Path

from common import client_from_env, run_and_collect, sample_input


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--max-charge-usd", default="0.05")
    args = parser.parse_args()
    value = json.loads(args.input.read_text(encoding="utf-8")) if args.input else sample_input()
    print(json.dumps(run_and_collect(client_from_env(), value, args.max_charge_usd), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
