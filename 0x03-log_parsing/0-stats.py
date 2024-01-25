#!/usr/bin/python3
import sys
import re
from collections import defaultdict


def parse_line(line):
    """
    Parse a log line and extract relevant information.

    Args:
        line (str): Log line to be parsed.

    Returns:
        tuple: Tuple containing IP address, date, status code, and file size.
               If the line does not match the expected format, returns None.
    """
    ip_address_pattern = r'(\d+\.\d+\.\d+\.\d+)'
    date_pattern = r'\[([^]]+)\]'
    request_pattern = r'"GET /projects/260 HTTP/1\.1"'
    status_code_pattern = r'(\d+)'
    file_size_pattern = r'(\d+)'

    pattern = fr'{ip_address_pattern} - {date_pattern} {request_pattern}
    {status_code_pattern} {file_size_pattern}'

    match = re.match(pattern, line)
    if match:
        ip_address, date, status_code, file_size = match.groups()
        return ip_address, date, int(status_code), int(file_size)
    else:
        return None


def print_statistics(total_size, status_counts):
    """
    Print the computed statistics.

    Args:
        total_size (int): Total file size.
        status_counts (dict): Dictionary containing counts of
        each status code.
    """
    print(f"Total file size: {total_size}")
    for code in sorted(status_counts):
        print(f"{code}: {status_counts[code]}")


def main():
    """
    Read log lines from stdin, compute and print statistics at
    regular intervals or on Ctrl+C.
    """
    total_size = 0
    status_counts = defaultdict(int)
    lines_processed = 0

    try:
        for line in sys.stdin:
            log_data = parse_line(line)
            if log_data:
                _, _, status_code, file_size = log_data
                total_size += file_size
                status_counts[status_code] += 1
                lines_processed += 1

                if lines_processed % 10 == 0:
                    print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        pass  # Handle Ctrl+C gracefully

    finally:
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
