# Python For DevOps

A collection of Python scripts built while learning Python for real DevOps tasks — covering system monitoring, log analysis, API integration, AWS automation, and CLI tooling.

The focus is not on Python syntax alone, but on **thinking like a DevOps engineer** and solving real problems with code.

---

## Scripts

Scripts are listed in the order they were written, following the learning path from basics to AWS automation.

---

### System Health Monitoring

| Script | Description |
|--------|-------------|
| `system_health.py` | Prompts the user to enter threshold values for CPU, memory, and disk usage, then checks live system stats using `psutil` and prints a warning if any metric exceeds its threshold. |
| `utilities.py` | A shared utility module with two reusable helper functions — `read_file()` for reading any file line by line, and `write_json()` for serialising and saving a Python object as JSON. Meant to be imported by other scripts. |

---

### Log Analyzer – Progressive Builds

The log analyzer was built incrementally across multiple days, each version adding a new concept.

| Script | Description |
|--------|-------------|
| `log_analyzer.py` | First version — procedural approach. Reads `app.log`, counts `INFO`, `WARNING`, and `ERROR` lines using functions, prints a summary report to the terminal, and saves it to `log_summary.txt`. Includes suggestions if error/warning counts exceed thresholds. |
| `log_analyzer_oop.py` | OOP refactor of `log_analyzer.py`. Wraps all logic in a `LogAnalyzer` class with `read_logs()`, `count_logs()`, and `summary_file()` methods. Uses a `main()` function as the single entry point and the `if __name__ == "__main__"` guard. |
| `sample_log_analyzer.py` | Reference/sample version of the OOP log analyzer with full docstrings on every method. Also adds an `UNKNOWN` category for unclassified log lines and handles `FileNotFoundError` gracefully. |
| `log_analyzer_cli.py` | CLI version of the OOP log analyzer using `argparse`. Accepts `--file` (input log path) and `--out` (output report path) as command-line arguments, making it fully scriptable without editing the source. |

---

### API Integration

| Script | Description |
|--------|-------------|
| `api_data_fetcher.py` | Fetches live flight data from the AviationStack API using `requests`. Prompts the user for how many flights to display, formats departure times with `datetime`, and saves structured flight details to `Flight_Details.json`. |

---

### AWS Automation

| Script | Description |
|--------|-------------|
| `aws_resource_report.py` | Connects to AWS using `boto3` to list all EC2 instances (with names, IDs, and states) and all S3 buckets, then prints a combined report and saves it to `aws_report.json`. |
| `aws_demo.py` | Minimal OOP demo of AWS interaction — defines an `AWSUtils` class that connects to S3 via `boto3.client` and collects bucket names into a list via `show_buckets()`. |
| `s3_utitlites.py` | A more complete `AWSUtils` class covering S3 and EC2 operations — listing buckets, creating a bucket with a region constraint, uploading a file to a bucket, and listing EC2 regions. Demonstrates class-based AWS client management and the `if __name__ == "__main__"` pattern. |
| `try_s3.py` | Demonstrates module importing — imports `AWSUtils` from `s3_utitlites.py` and calls `show_buckets()`, showing how to split and reuse code across files. |

---

### Notes & Design Docs

| File | Description |
|------|-------------|
| `design.md` | Day 7 thinking-before-coding notes — walks through how to approach an unfamiliar problem (converting a Python script to a CLI tool) by reading docs, experimenting, and debugging before touching the code. |

---

## Usage

```bash
git clone <repo-url>
cd python-for-devops

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Running scripts:**

```bash
# Procedural / OOP versions
python log_analyzer.py
python log_analyzer_oop.py

# CLI version (with argparse)
python log_analyzer_cli.py --file app.log --out report.txt

# System health check
python system_health.py

# AWS automation (requires configured AWS credentials)
python aws_resource_report.py
```

> AWS scripts require valid credentials configured via `aws configure` or environment variables.

---

## Topics Covered

- Functions, modules & reusable utilities
- File I/O — reading logs, writing `.txt` and `.json` reports
- OOP — classes, `__init__`, methods, `self`
- `if __name__ == "__main__"` pattern
- Error handling with `try/except`
- CLI tooling with `argparse`
- HTTP APIs with `requests` and JSON parsing
- AWS automation with `boto3` — EC2 and S3
- Debugging with `pdb`
- DevOps mindset — designing before coding