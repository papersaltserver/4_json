import json
import sys
from pprint import pprint


def load_data(filepath):
    with open(filepath) as f:
        my_json = json.load(f)
    return my_json


def pretty_print_json(data):
    pprint(data)


if __name__ == '__main__':
    my_json = load_data(sys.argv[1])
    pretty_print_json(my_json)
