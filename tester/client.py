
import requests
import time

class APIClient:
    def __init__(self, base_url="https://api.agify.io", timeout=3):
        self.base_url = base_url
        self.timeout = timeout

    def get(self, endpoint="/", params=None):
        url = f"{self.base_url}{endpoint}"

        last_exc = None
        for attempt in range(2):  # 1 retry max
            start = time.time()
            try:
                resp = requests.get(url, params=params, timeout=self.timeout)
                latency = (time.time() - start) * 1000

                if resp.status_code == 429:
                    time.sleep(1)
                    continue

                return resp, latency
            except requests.exceptions.Timeout as e:
                last_exc = e
        return None, None
