"""Export an existing Dataset without starting another Actor run."""
import argparse
import csv
from pathlib import Path

from common import client_from_env

FIELDS = ["ypid", "name", "phone", "website", "street", "city", "state", "zip", "rating", "reviewCount"]


def cell(value):
    if isinstance(value, str) and value.startswith(("=", "+", "-", "@", "\t", "\r")):
        return "'" + value
    return value


def export_dataset(client, dataset_id, destination):
    count = 0
    with destination.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS)
        writer.writeheader()
        for row in client.dataset(dataset_id).iterate_items(clean=True):
            writer.writerow({key: cell(row.get(key)) for key in FIELDS})
            count += 1
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset_id")
    parser.add_argument("--output", type=Path, default=Path("yellowpages-businesses.csv"))
    args = parser.parse_args()
    print(f"Exported {export_dataset(client_from_env(), args.dataset_id, args.output)} businesses to {args.output}")


if __name__ == "__main__":
    main()
