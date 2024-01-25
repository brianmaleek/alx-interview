#!/usr/bin/python3
import sys
from collections import defaultdict


def process_log_lines():
    """
    Process log lines from stdin and compute metrics.

    This function reads log lines from standard input, computes file size,
    and counts occurrences of status codes. It prints the metrics after
    every 10 lines or on KeyboardInterrupt.

    Raises:
        KeyboardInterrupt: If the user interrupts the program with Ctrl+C.
    """
    status_codes = defaultdict(int)
    file_size = 0
    counter = 0

    try:
        for line in sys.stdin:
            counter += 1
            parsed_line = line.split()
            file_size += int(parsed_line[-1])
            status_codes[parsed_line[-2]] += 1

            if counter == 10:
                print("File size: {}".format(file_size))
                for key, value in sorted(status_codes.items()):
                    print("{}: {}".format(key, value))
                counter = 0

    except KeyboardInterrupt:
        print("File size: {}".format(file_size))
        for key, value in sorted(status_codes.items()):
            print("{}: {}".format(key, value))
        raise

    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        print("{}: {}".format(key, value))


if __name__ == "__main__":
    process_log_lines()
