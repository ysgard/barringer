#!/usr/bin/env python3

# barringer.py
#
# A script to produce a randome hireling for Dungeon World, based on
# following a series of selections from random tables.

import random
import sys

HIRELING_TABLE = "hireling.tbl"


class Row:
    def __init__(self):
        self.weight = 0
        self.val = ""


class Table:
    def __init__(self):
        self.rows = []


class Tables:
    def __init__(self):
        self.tabledict = {}


# Load the hireling table into memory
def read_table(table=HIRELING_TABLE):
    with open(table, 'r') as f:
        lead = f.readline().rstrip()
        tables = Tables()
        for line in f:
            clean_line = line.rstrip()
            if clean_line == "":
                cur_table = ""
            elif cur_table == "":
                cur_table = clean_line
                tables.tabledict[cur_table] = Table()
            else:
                row = Row()
                row.weight = int(clean_line[0:clean_line.find(' ')])
                row.val = clean_line[clean_line.find(' ') + 1:len(clean_line)]
                tables.tabledict[cur_table].rows.append(row)
    return (lead, tables)


# Get a weighted random row from a given table
def get_row(tables, table_name):
    t = tables.tabledict[table_name]
    total_weight = 0
    for i in t.rows:
        total_weight += i.weight
    random_num = random.SystemRandom().randint(1, total_weight)
    current_weight = 0
    for i in t.rows:
        current_weight += i.weight
        if random_num <= current_weight:
            return i.val


def gen_hireling(count=1):
    # Initialize RNG
    random.seed(random.SystemRandom().randint(1, 65000))
    (lead, tables) = read_table()
    vars = {}
    # Parse the lead, looking up the values in the tables
    while lead.find('{') > -1:
        pass
    print(lead)


if __name__ == "__main__":
    if len(sys.argv) < 1 or len(sys.argv) > 2:
        print("Usage: python {} [count]").format(sys.argv[0])
    if len(sys.argv) > 1:
        gen_hireling(sys.argv[1])
    else:
        gen_hireling()
