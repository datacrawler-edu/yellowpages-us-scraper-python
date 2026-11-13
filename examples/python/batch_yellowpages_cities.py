"""Run a separate small search per city, sequentially."""
import argparse
import json

from common import client_from_env, run_and_collect, sample_input


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--locations", nargs="+", default=["Austin, TX", "Dallas, TX"])
    parser.add_argument("--max-charge-usd", default="0.05", help="Spending cap for EACH city run")
    args = parser.parse_args()
    client = client_from_env()
    for city in args.locations:
        value = sample_input()
        value["locations"] = [city]
        result = run_and_collect(client, value, args.max_charge_usd)
        print(json.dumps({"location": city, **result}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
