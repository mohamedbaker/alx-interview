#!/usr/bin/python3
"""
logs module contains a script that reads stdin
line by line and computes metrics
"""

import sys
import signal

# Dictionary stores the status codes counts
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0,
                      403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
line_count = 0


def print_statistics():
    """
    Print the statistics including total file size and status code counts
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))


def signal_handler(signum, frame):
    """
    Signal handler to print statistics on keyboard interruption (Ctrl+C)
    """
    print_statistics()
    sys.exit(0)


# Set up the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        if len(parts) < 7:
            continue

        # Extracting file size and status code
        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
        except ValueError:
            continue

        total_file_size += file_size

        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)

# Print statistics at the end of the input
print_statistics()
