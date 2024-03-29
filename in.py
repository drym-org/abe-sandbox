#!/usr/bin/env python

import click
from payments import record_payment

DESTINATION_DIR = "abe/payments"


@click.command(
    help=(
        "Record a new payment."
    )
)
@click.argument("whom")
@click.argument("amount")
def main(whom, amount):
    filename = record_payment(whom, amount, DESTINATION_DIR)
    print(f"Recorded payment of ${amount} from {whom} in {filename}")


if __name__ == '__main__':
    main()
