# abstraction/game.py
from config import game_data
from items import Item
from locations import Location


def load_game_data():
    return game_data

def create_objects(game_data):
    items = {}
    locations = {}

    for item_data in game_data["items"]:
        item = Item(
            item_data["name"],
            item_data["description"],
            actions=item_data.get("actions", {}),
            fixed=item_data.get("fixed"),
            item_type=item_data.get("item_type"), # Add this line
        )
        items[item.name] = item

    for location_data in game_data["locations"]:
        location_items = {item_name: items.get(item_name) for item_name in location_data["items"]}
        location = Location(
            location_data["name"],
            location_data["descriptions"],
            location_items,
            location_data["neighbors"],
            location_data["effect_states"],  # Add this line
        )
        locations[location.name] = location

    return game_data, items, locations