
import statistics
from datetime import datetime

from tester.client import APIClient
from tester import tests

def run_all_tests():
    client = APIClient()
    test_funcs = [
        ("status_ok", tests.test_status_ok),
        ("json_format", tests.test_json_format),
        ("schema_fields", tests.test_schema_fields),
        ("types", tests.test_types),
        ("invalid_input_empty_name", tests.test_invalid_input_empty_name),
        ("numeric_name", tests.test_numeric_name),
    ]

    results = []
    latencies = []
    passed = 0
    failed = 0

    for name, func in test_funcs:
        try:
            resp, latency = client.get("/", params={"name": "michael"})
            if latency is not None:
                latencies.append(latency)
            func(client)
            results.append({"name": name, "status": "PASS", "latency_ms": latency})
            passed += 1
        except AssertionError as e:
            results.append({"name": name, "status": "FAIL", "details": str(e)})
            failed += 1

    if not latencies:
        latencies = [0]

    return {
        "api": "Agify",
        "timestamp": datetime.now().isoformat(),
        "summary": {
            "passed": passed,
            "failed": failed,
            "error_rate": failed / len(test_funcs),
            "latency_ms_avg": statistics.mean(latencies),
            "latency_ms_p95": statistics.quantiles(latencies, n=20)[-1],
        },
        "tests": results,
    }
