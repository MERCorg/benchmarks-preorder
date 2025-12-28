import json
import re
import argparse

# working (current: x, max: y) (hits: 82780, misses: 1311765, size: 3, max: 3306)
INNER_ANTICHAIN_REGEX=re.compile(r"\[debug\]\s*Inner antichain: working \(current: (\d+), max: (\d+)\).\n\[debug\]\s*antichain \(hits: (\d+), misses: (\d+), size: (\d+), max: (\d+)\)\n")
OUTER_ANTICHAIN_REGEX=re.compile(r"\[debug\]\s*Outer antichain: working \(current: (\d+), max: (\d+)\).\n\[debug\]\s*antichain \(hits: (\d+), misses: (\d+), size: (\d+), max: (\d+)\)\n")

def main():
    # Parse some configuration options
    parser = argparse.ArgumentParser(
        prog="run_examples.py",
        description="Prepares the examples specifications for testing",
        epilog="",
    )

    parser.add_argument(
        "result_path", action="store", type=str
    )
    args = parser.parse_args()

    with open(args.result_path, "r", encoding="utf-8") as f:
        results = json.load(f)
            
        for (key, result) in results.items():
            if "timeout" not in key:
                time = result['time']
                max_antichain_inner = 0
                misses_antichain_inner = 0
                hits_antichain_inner = 0

                max_antichain_outer = 0
                misses_antichain_outer = 0
                hits_antichain_outer = 0

                for match in re.finditer(INNER_ANTICHAIN_REGEX, result['stderr']):
                    misses_antichain_inner = max(misses_antichain_inner, int(match.groups()[2]))
                    hits_antichain_inner = max(hits_antichain_inner, int(match.groups()[3]))
                    max_antichain_inner = max(max_antichain_inner, int(match.groups()[5]))

                for match in re.finditer(OUTER_ANTICHAIN_REGEX, result['stderr']):
                    misses_antichain_outer = max(misses_antichain_outer, int(match.groups()[2]))
                    hits_antichain_outer = max(hits_antichain_outer, int(match.groups()[3]))
                    max_antichain_outer = max(max_antichain_outer, int(match.groups()[5]))

                print(f"{key}: {time}, {result["stdout"]}, {misses_antichain_inner}, {hits_antichain_inner}, {max_antichain_inner}, {misses_antichain_outer}, {hits_antichain_outer}, {max_antichain_outer}")

if __name__ == "__main__":
    main()