import json
import random
import string
from datetime import datetime, timedelta


def random_name(length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def random_date(start_days_ago=100, end_days_ago=1):
    start = datetime.now() - timedelta(days=start_days_ago)
    end = datetime.now() - timedelta(days=end_days_ago)
    delta = end - start
    random_days = random.randrange(delta.days + 1)
    return (start + timedelta(days=random_days)).strftime("%Y-%m-%d")


def generate_record(record_id: int) -> dict:
    return {
        "id": record_id,
        "name": random_name(),
        "age": random.randint(18, 70),
        "score": round(random.uniform(0, 100), 2),
        "created": random_date(),
    }


def generate_dataset(n: int = 50) -> list:
    return [generate_record(i) for i in range(1, n + 1)]


def save_dataset(data: list, filename: str = "data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


def load_dataset(filename: str = "data.json") -> list:
    with open(filename, "r") as f:
        return json.load(f)


if __name__ == "__main__":
    dataset = generate_dataset(100)
    save_dataset(dataset)
    print(f"Generated and saved {len(dataset)} records to data.json")


