import json

if __name__ == "__main__":
    data = [{"name": "Sasha", "score": 180}]
    with open("data.json", "w") as f:
        json.dump(data, f, indent=5)
