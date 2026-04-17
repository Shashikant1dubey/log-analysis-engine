from src.core.processor import analyze_logs

def test_analyze_logs():
    logs = [
        "INFO test",
        "ERROR fail",
        "WARNING warn",
        "ERROR again"
    ]

    result = analyze_logs(logs)

    assert result["INFO"] == 1
    assert result["ERROR"] == 2
    assert result["WARNING"] == 1