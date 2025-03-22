import sys
from log_utils import *

def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до лог-файлу.")
        return

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        logs = load_logs(file_path)
    except FileNotFoundError:
        print("Файл не знайдено.")
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        print(f"\nДeталі логів для рівня '{level_filter.upper()}':")
        for log in filter_logs_by_level(logs, level_filter):
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()

#! commands: 

# python task_3/main.py task_3/logs.txt
# python task_3/main.py task_3/logs.txt debug