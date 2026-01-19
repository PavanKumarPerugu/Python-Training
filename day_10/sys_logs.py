import random
from datetime import datetime, timedelta
import os

# File name
filename = "system_log.txt"

# File path
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, filename)

# Define log levels and sample messages
log_levels = ["INFO", "WARNING", "ERROR"]

messages = {
    "INFO": [
        "System boot completed successfully.",
        "Background service started.",
        "User login detected.",
        "Network connection established.",
        "Scheduled backup initiated.",
        "Configuration file loaded.",
        "Health check completed.",
        "Cache cleared successfully.",
        "Database connection stable.",
        "API server running normally."
    ],
    "WARNING": [
        "High memory usage detected.",
        "Disk space running low.",
        "Unusual network activity noticed.",
        "Configuration mismatch found.",
        "Slow response from database.",
        "Deprecated API call used.",
        "CPU temperature rising.",
        "Low battery warning.",
        "Temporary network instability.",
        "System time drift detected."
    ],
    "ERROR": [
        "Failed to connect to database.",
        "System crash detected in module X.",
        "Unauthorized access attempt blocked.",
        "File not found during operation.",
        "Memory allocation failed.",
        "Kernel panic occurred.",
        "Network interface unreachable.",
        "I/O error on disk device.",
        "Segmentation fault detected.",
        "Critical system service failed."
    ]
}

# Starting time for logs (simulate past 24 hours)
start_time = datetime.now() - timedelta(hours=24)

# Open file to write logs
with open(file_path, "w") as file:
    for i in range(500):
        # Generate random timestamp (within 24 hours)
        timestamp = start_time + timedelta(seconds=random.randint(0, 86400))
        
        # Randomly pick log level and message
        level = random.choice(log_levels)
        message = random.choice(messages[level])
        
        # Format line
        log_line = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {level} - {message}\n"
        
        # Write to file
        file.write(log_line)

print(f"✅ Generated '{filename}' with 500 log entries.")
