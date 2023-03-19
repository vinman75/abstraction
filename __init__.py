# abstraction/__init__.py
from game import create_objects, load_game_data
from player import Player
from config import game_data

game_data = load_game_data()
game_data, items, locations = create_objects(game_data)

def main(starting_location):
    print("Welcome to the adventure game!")
    player_name = input("What is your name? ")
    starting_location = locations[game_data["starting_location"]]
    player = Player(player_name, starting_location, locations, items)

    while True:
        command = input("Enter a command (inventory, look, inspect, move [N/S/E/W], take, combine, use, or quit): ").lower().split()
        if len(command) == 0:
            continue

        action = command[0]

        if action == "quit":
            print("Goodbye!")
            break
        elif action == "inventory":
            player.show_inventory()
        elif action == "look":
            player.look()
        elif action in ["inspect", "read", "use"]:
            item_name = ' '.join(command[1:]) if len(command) > 1 else None
            if item_name:
                item = next((i for i in player.inventory if i.name.lower() == item_name.lower()), None)
                if not item:  # If the item is not in the inventory, check the current location
                    item = next((i for i in player.location.items.values() if i.name.lower() == item_name.lower()), None)
                if item:
                    player.perform_action(action, item)
                else:
                    print(f"There is no {item_name} in your inventory or current location.")
            else:
                print(f"Please provide an item name to {action}.")
        elif action == "move":
            direction = command[1] if len(command) > 1 else None
            if direction and player.move(direction):
                print(f"You moved to {player.location.name}.")
            else:
                print(f"You can't move {direction} from here.")
        elif action == "take":
            item_name = ' '.join(command[1:]) if len(command) > 1 else None
            if item_name:
                player.take_item(item_name)
            else:
                print("Please provide an item name to pick up.")
        elif action == "combine":
            if len(command) > 2:
                item_name = command[1]
                target_name = command[2]
                player.combine_item(item_name, target_name)
            else:
                print("Please provide two item names to combine.")
        else:
            print("Invalid command. Please try again.")
            
if __name__ == "__main__":
    starting_location = game_data["starting_location"]
    main(starting_location)
