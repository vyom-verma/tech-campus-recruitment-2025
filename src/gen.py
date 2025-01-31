import random
import datetime

# Log levels and sample messages
LOG_LEVELS = ["INFO", "ERROR", "WARN"]
LOG_MESSAGES = {
    "INFO": ["User logged in", "File uploaded successfully", "Service started"],
    "ERROR": ["Failed to connect to the database", "Unexpected server error", "Timeout occurred"],
    "WARN": ["Disk space running low", "Memory usage is high", "Network latency detected"]
}

# Function to generate random log entries
def generate_log_entries(num_entries=100000):
    start_date = datetime.datetime(2024, 1, 1, 0, 0, 0)
    log_entries = []
    
    for _ in range(num_entries):
        # Generate random timestamp within the last year
        random_days = random.randint(0, 364)
        random_seconds = random.randint(0, 86399)
        log_time = start_date + datetime.timedelta(days=random_days, seconds=random_seconds)
        
        # Select a random log level and message
        log_level = random.choice(LOG_LEVELS)
        log_message = random.choice(LOG_MESSAGES[log_level])
        
        # Format log entry
        log_entry = f"{log_time.strftime('%Y-%m-%d %H:%M:%S')} {log_level} {log_message}"
        log_entries.append(log_entry)
    
    return log_entries

# Write log entries to a file
def write_logs_to_file(filename="generated_logs.log", num_entries=1000):
    log_entries = generate_log_entries(num_entries)
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(log_entries))
    print(f"Generated {num_entries} log entries in {filename}")

# Run the script
write_logs_to_file()
