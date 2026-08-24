import json
from datetime import datetime, timezone
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(API_URL, timeout=20)
response.raise_for_status()

print("status:", response.status_code)
print("content-type:", response.headers.get("Content-Type"))

payload = response.json()
print("top-level type:", type(payload).__name__)

with open("data/raw/api_snapshot.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, ensure_ascii=False)

print("retrieved_at_utc:", datetime.now(timezone.utc).isoformat())