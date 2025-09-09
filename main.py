import json

from model import run_model
from postprocessing import run_data_postprocessing


def read_data() -> list:
    with open("data.json", "r") as file:
        data = json.load(file)
    return data


def main():
    print("Starting data pipeline")
    data = read_data()
    data = run_model(data)
    data = run_data_postprocessing(data)
    return data

if __name__ == "__main__":
    main()
