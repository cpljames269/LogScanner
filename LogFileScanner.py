import re
import csv
from collections import defaultdict
from pathlib import Path

FAILED_LOGIN_PATTERN = re.compile(
    r"Failed password.*from (?P<ip>\d+\.\d+\.\d+\.\d+)"
)

SUCCESS_LOGIN_PATTERN = re.compile(
    r"Accepted password.*from (?P<ip>\d+\.\d+\.\d+\.\d+)"
)

def parse_log_file(log_path):
    failed_logins = defaultdict(int)
    successful_logins = defaultdict(int)
    total_lines = 0

    with open(log_path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            total_lines += 1

            failed_match = FAILED_LOGIN_PATTERN.search(line)
            if failed_match:
                ip = failed_match.group("ip")
                failed_logins[ip] += 1
                continue

            success_match = SUCCESS_LOGIN_PATTERN.search(line)
            if success_match:
                ip = success_match.group("ip")
                successful_logins[ip] += 1

    return total_lines, failed_logins, successful_logins


def write_csv_report(total_lines, failed_logins, successful_logins):
    output_file = Path("log_summary.csv")

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["Metric", "Value"])
        writer.writerow(["Total Log Lines", total_lines])
        writer.writerow([])

        writer.writerow(["Failed Login Attempts"])
        writer.writerow(["Source IP", "Count"])
        for ip, count in sorted(
            failed_logins.items(), key=lambda x: x[1], reverse=True
        ):
            writer.writerow([ip, count])

        writer.writerow([])
        writer.writerow(["Successful Logins"])
        writer.writerow(["Source IP", "Count"])
        for ip, count in successful_logins.items():
            writer.writerow([ip, count])

    return output_file


def print_summary(total_lines, failed_logins, successful_logins):
    print("\n=== Log Analysis Summary ===\n")
    print(f"Total log lines processed: {total_lines}\n")

    print("Failed Login Attempts:")
    if failed_logins:
        for ip, count in sorted(
            failed_logins.items(), key=lambda x: x[1], reverse=True
        ):
            print(f"  {ip}: {count} attempts")
    else:
        print("  None detected")

    print("\nSuccessful Logins:")
    if successful_logins:
        for ip, count in successful_logins.items():
            print(f"  {ip}: {count} logins")
    else:
        print("  None detected")


if __name__ == "__main__":
    log_file = Path("auth.log")

    if not log_file.exists():
        print("Log file not found. Place an auth.log file in this directory.")
        exit(1)

    total_lines, failed_logins, successful_logins = parse_log_file(log_file)

    print_summary(total_lines, failed_logins, successful_logins)
    output = write_csv_report(total_lines, failed_logins, successful_logins)

    print(f"\nReport written to {output}")
