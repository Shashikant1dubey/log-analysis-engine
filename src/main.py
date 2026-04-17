import argparse
from src.pipelines.run_pipeline import run_pipeline

def main():
    parser = argparse.ArgumentParser(description="Log Processing Engine")
    parser.add_argument("--task", type=str, required=True)

    args = parser.parse_args()
    run_pipeline(args.task)

if __name__ == "__main__":
    main()
