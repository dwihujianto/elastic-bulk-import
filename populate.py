#!/usr/bin/env python3
filepath = 'accounts2.json'
metadata = '{"index": {"_index": "bank_account", "_type": "account"}}'
with open(filepath, mode="r", encoding="utf-8") as my_file:
    for line in my_file:
        print(metadata)
        print(line.rstrip("\n"))
