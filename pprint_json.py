import json
import sys


def load_data(filepath):
    with open(filepath) as json_file:
        my_json = json.load(json_file)
    return my_json


def pretty_print_json(json_data):
    print(json.dumps(json_data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    my_json = load_data(sys.argv[1])
    pretty_print_json(my_json)
