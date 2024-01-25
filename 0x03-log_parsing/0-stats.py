#!/usr/bin/python3
import sys
import re
from collections import defaultdict


LOG_PATTERN = r"(\d+\.\d+\.\d+\.\d+) - \[([^]]+)\] " \
             r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)'


def parse_line(line):
    """
    Parse a log line and return extracted information or None if invalid.

    Args:
        line (str): The log line to be parsed.

    Returns:
        tuple or None: A tuple containing parsed elements or None if invalid.
    """
    match = re.match(LOG_PATTERN, line)
    if match:
        return match.groups()
    return None


def print_statistics(total_size, status_counts):
    """
    Print the computed statistics.

    Args:
        total_size (int): The total file size.
        status_counts (dict): A dictionary mapping status codes to counts.
    """
    print(f"Total file size: {total_size}")
    for code, count in sorted(status_counts.items()):
        print(f"{code}: {count}")


def main():
    """
    Read log lines from stdin, compute and print statistics.
    """
    total_size = 0
    status_counts = defaultdict(int)

    try:
        for line in sys.stdin:
            ip, date, status_code, file_size = parse_line(line) or (None,) * 4
            if ip:  # Parsing successful
                total_size += int(file_size)
                status_counts[int(status_code)] += 1
                print_statistics(total_size, status_counts)  # Print regularly

    except KeyboardInterrupt:
        pass  # Handle Ctrl+C gracefully

    finally:
        print_statistics(total_size, status_counts)  # Always print final stats


if __name__ == "__main__":
    main()
