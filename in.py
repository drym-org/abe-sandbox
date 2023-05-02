#!/usr/bin/env python

import os
import click
from uuid import uuid4

DESTINATION_DIR = "abe/payments"


def _unique_name():
    return uuid4().hex[:7]


def record_payment(whom, amount):
    unique_id = _unique_name()
    filename = unique_id + ".txt"
    filename = os.path.join(DESTINATION_DIR, filename)
    with open(filename, 'w') as f:
        f.write(",".join([whom, unique_id, amount, "dummydate"]))
    return filename


@click.command(
    help=(
        "Record a new payment."
    )
)
@click.argument("whom")
@click.argument("amount")
def main(whom, amount):
    filename = record_payment(whom, amount)
    print(f"Recorded payment of ${amount} from {whom} in {filename}.")


if __name__ == '__main__':
    main()
