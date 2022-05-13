import json

if __name__ == "__main__":
    data = {"width": 800, "height": 600, "fps": 60}
    with open("data.json", "w") as f:
        json.dump(data, f, indent=5)
