'''
🧩 Mini Project (1 hour) — Log File Analyzer
w
🎯 Goal:

Build a tool that reads a server log file, detects errors, and generates a summary.

✅ Enhancements:

Save results to a summary file (log_summary.txt)

Use a generator to stream large log files line-by-line

Add color-coded terminal output for INFO, WARNING, ERROR

'''
import os

# File path
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "system_log.txt")

def analyze_log(filename):
    try:
        with open(filename, "r") as f:
            total_lines = 0
            error_count = 0
            warning_count = 0

            for line in f:
                total_lines += 1
                if "ERROR" in line:
                    error_count += 1
                elif "WARNING" in line:
                    warning_count += 1

        print(f"Total lines: {total_lines}")
        print(f"Errors found: {error_count}")
        print(f"Warnings found: {warning_count}")

    except FileNotFoundError:
        print("Log file not found!")
    except Exception as e:
        print(f"Unexpected error: {e}")

# --- Test it ---
analyze_log(file_path)
