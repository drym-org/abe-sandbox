#!/usr/bin/env python

import os
from uuid import uuid4


def _unique_name():
    return uuid4().hex[:7]


def record_payment(whom, amount, path):
    unique_id = _unique_name()
    filename = unique_id + ".txt"
    filename = os.path.join(path, filename)
    with open(filename, 'w') as f:
        f.write(",".join([whom, unique_id, amount, "dummydate"]))
    return filename
