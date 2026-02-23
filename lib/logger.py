from datetime import datetime
import os

# Get absolute project path (one level above lib/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(BASE_DIR, "data", "user_logs.txt")


def log_action(action, log_file=LOG_PATH):
    """Append a user action with a timestamp to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Ensure data folder exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    with open(log_file, 'a') as file:
        file.write(f"{timestamp} - {action}\n")


def search_logs(keyword, log_file=LOG_PATH):
    """Search the log file for lines that match a keyword."""
    try:
        with open(log_file, 'r') as file:
            for line in file:
                if keyword.lower() in line.lower():
                    print(line.strip())
    except FileNotFoundError:
        print(f"Log file {log_file} not found.")


if __name__ == "__main__":
    log_action("User logged in")
    log_action("User viewed dashboard")
    log_action("User logged out")
