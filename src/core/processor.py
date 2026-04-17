def analyze_logs(log_lines):
    summary = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    for line in log_lines:
        for level in summary:
            if line.startswith(level):
                summary[level] += 1

    return summary