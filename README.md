Log Parser – Security Event Extraction

This Python project is a simple log parser designed to extract security-relevant events from authentication logs. It identifies failed and successful login attempts, groups events by source IP, and produces both a console summary and a CSV report.

A sample log file (auth.log) is included for testing and demonstration purposes.

Features

Parses authentication logs for:

Failed login attempts

Successful logins

Aggregates events by source IP

Outputs results:

Console summary for immediate review

CSV report (log_summary.csv) for further analysis

Lightweight, self-contained, and easy to extend

Sample Log File

The included auth.log contains fake usernames and IP addresses for testing:

Usernames like FakeUser222, NotReal777, MadeUp1829

IP addresses in reserved documentation ranges (203.0.113.*, 198.51.100.*, 10.*.*.*)

Mix of failed and successful login events

20 sample entries to demonstrate parser functionality

This allows you to test the script without exposing real data.

Installation

Clone the repository:

git clone https://github.com/cpljames269/log-parser.git
cd log-parser


Ensure Python 3 is installed

Install any dependencies (standard library only for now; no extra packages required)

Usage

Place your log file in the same directory as log_parser.py. By default, the script expects:

auth.log


Run the script:

python log_parser.py


Expected output:

Console summary of failed and successful login attempts

log_summary.csv in the same folder containing aggregated data

Example Output (Console)
=== Log Analysis Summary ===

Total log lines processed: 20

Failed Login Attempts:
  203.0.113.45: 3 attempts
  198.51.100.22: 2 attempts
  ...

Successful Logins:
  10.0.0.12: 1 logins
  10.0.0.15: 1 logins
  ...
Report written to log_summary.csv
