import json

from model import run_model


def read_data() -> list:
    with open("data.json", "r") as file:
        data = json.load(file)
    return data


def main():
    print("Starting data pipeline")
    data = read_data()
    data = run_model(data)
    return data

if __name__ == "__main__":
    main()
