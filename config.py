# abstraction/config.py
import yaml
import os

game_data = None

try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_path = os.path.join(base_dir, "data", "game_data.yaml")

    with open(yaml_path, "r") as file:
        yaml_data = yaml.safe_load(file)
        game_data = yaml_data["game_data"]
except Exception as e:
    print("An error occurred while reading the game_data.yaml file:", e)