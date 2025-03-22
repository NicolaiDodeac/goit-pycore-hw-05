from collections import Counter

def count_logs_by_level(logs: list) -> dict:
    return Counter(log["level"] for log in logs)

def parse_log_line(line: str) -> dict:
    date, time, level, *message = line.strip().split()
    return {
        "date": date,
        "time": time,
        "level": level,
        "message": " ".join(message)
    }


def load_logs(file_path: str) -> list:
    logs = []
    with open(file_path, "r", encoding="utf-8") as file:
         for line in file:
            parsed = parse_log_line(line)
            if parsed:
                logs.append(parsed)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_list = list(filter(lambda log: log["level"].lower() == level.lower(), logs))
    return filtered_list


def count_logs_by_level(logs: list) -> dict:
    return Counter(log["level"] for log in logs)


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")