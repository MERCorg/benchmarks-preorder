import argparse
import json
import sys

def combine(left, right):
    for key, value in left.items():
        if type(value) is dict:
            for k, v in value.items():
                if type(value[k]) is float:
                    value[k] = v + right[key][k]

def average(results, number_of_inputs):
    for key, value in results.items():
        if type(value) is dict:
            for k, v in value.items():
                if type(value[k]) is float:
                    value[k] = v / number_of_inputs


def main():
    # Parse some configuration options
    parser = argparse.ArgumentParser(
        prog="merge.py",
        epilog="",
    )

    parser.add_argument("inputs", nargs="+")
    args = parser.parse_args()

    results = None
    for file in args.inputs:
        print(f"Loading {file}")
        # writing the dictionary data into the corresponding JSON file
        with open(file, "r", encoding="utf-8") as json_file:
            result = json.load(json_file)

            if results is None:
                results = result
            else:
                combine(results, result)

    # Take the average of all the results
    average(results, len(args.inputs))

    json.dump(results, sys.stdout, indent=4)
                                

if __name__ == "__main__":
    main()