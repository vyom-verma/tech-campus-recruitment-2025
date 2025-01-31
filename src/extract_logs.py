import sys
import os

def extract_logs(file_path, target_date, output_dir="output"):
    """Extract logs for a specific date from a large log file and save them to an output file."""
    
    os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists
    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    try:
        with open(file_path, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            for line in infile:
                if line.startswith(target_date):
                    outfile.write(line)

        print(f"Logs for {target_date} saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: Log file '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    log_file = "test.log"  # Ensure this file exists before running
    target_date = sys.argv[1]
    extract_logs(log_file, target_date)
