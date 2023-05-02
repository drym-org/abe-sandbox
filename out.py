#!/usr/bin/env python

import click
from payments import record_payment

DESTINATION_DIR = "abe/payouts"


@click.command(
    help=(
        "Record a new payout."
    )
)
@click.argument("whom")
@click.argument("amount")
def main(whom, amount):
    filename = record_payment(whom, amount, DESTINATION_DIR)
    print(f"Recorded payout of ${amount} to {whom} in {filename}")


if __name__ == '__main__':
    main()
