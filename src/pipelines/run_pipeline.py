from src.core.processor import analyze_logs

def run_pipeline(task):
    if task == "log_analysis":
        with open("data/sample_logs.txt", "r") as f:
            logs = f.readlines()

        result = analyze_logs(logs)

        print("Log Summary:")
        for k, v in result.items():
            print(f"{k}: {v}")

        if result["ERROR"] > 1:
            print("ALERT: High number of errors detected!")

    else:
        raise ValueError("Unknown task")