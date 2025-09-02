import statistics
import os

import data_generator as dg


def average_score(data):
    scores = [rec["score"] for rec in data]
    return statistics.mean(scores)


def age_distribution(data):
    dist = {"18-30": 0, "31-50": 0, "51-70": 0}
    for rec in data:
        if rec["age"] <= 30:
            dist["18-30"] += 1
        elif rec["age"] <= 50:
            dist["31-50"] += 1
        else:
            dist["51-70"] += 1
    return dist


def top_scores(data, n=5):
    sorted_data = sorted(data, key=lambda x: x["score"], reverse=True)
    return sorted_data[:n]


def ensure_data_file():
    if not os.path.exists("data.json"):
        print("No data.json found, generating new dataset...")
        dataset = dg.generate_dataset(100)
        dg.save_dataset(dataset)
    return dg.load_dataset()


def report():
    data = ensure_data_file()
    print("--- Data Analysis Report ---")
    print(f"Total records: {len(data)}")
    print(f"Average score: {average_score(data):.2f}")
    print("Age distribution:")
    for group, count in age_distribution(data).items():
        print(f"  {group}: {count}")
    print("Top scorers:")
    for rec in top_scores(data):
        print(f"  ID={rec['id']}, Name={rec['name']}, Score={rec['score']}")


if __name__ == "__main__":
    report()
