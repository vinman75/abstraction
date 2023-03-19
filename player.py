# abstraction/player.py
class Player:
    def __init__(self, name, location, locations, items):
        self.name = name
        self.location = location
        self.locations = locations
        self.inventory = []
        self.items = items
        self.effects_applied = set()

    def move(self, direction):
        if direction in self.location.neighbors:
            new_location_name = self.location.neighbors[direction]
            self.location = self.locations[new_location_name]
            return True
        else:
            return False

    def look(self):
        print(self.location.get_description())
        if self.location.items:
            print("You see the following items:")
            for item in self.location.items.values():
                print(f"- {item.name}")
        else:
            print("There are no items here.")


    def perform_action(self, action, item):
        if action in item.actions:
            action_data = item.actions[action]
            success_message = action_data.get("success_message", "")
            fail_message = action_data.get("fail_message", "")

            if "item_use" in action_data:
                target_item = self.items[action_data["item_use"]]
                if action == "use" and item.item_type == target_item.item_type:
                    print(success_message)
                    if "effects" in action_data:
                        self.apply_effects(action_data["effects"])
                else:
                    print(fail_message)
            else:
                print(success_message)
                if "effects" in action_data:
                    self.apply_effects(action_data["effects"])
        else:
            print(f"Cannot perform action {action} on {item.name}.")
            
    def update_location_description(self, target_location, new_description, item):
        if item.name not in self.locations[target_location].used_items:
            self.locations[target_location].new_description = new_description
            self.locations[target_location].used_items.add(item.name)    

    def apply_effects(self, effects):
        for effect in effects:
            if effect["effect_type"] == "update_effect_state":
                target_location_name = effect["target_location"]
                new_effect_state = effect["effect_state"]

                # Update the effect_state of the target location
                self.locations[target_location_name].update_effect_state(new_effect_state)


    def take_item(self, item_name):
        item = next((item for item_name_key, item in self.location.items.items() if item_name_key.lower() == item_name.lower()), None)
        if item:
            if not item.fixed:
                self.inventory.append(item)
                self.location.items.pop(item.name)
                print(f"You picked up the {item.name}.")
            else:
                print(f"You cannot take the {item.name}.")
        else:
            print(f"There is no {item_name} in this location.")

    def combine_item(self, item_name, target_name):
        item = next((i for i in self.inventory if i.name.lower() == item_name.lower()), None)
        target = next((i for i in self.inventory if i.name.lower() == target_name.lower()), None)

        if item and target:
            combine_action = item.actions.get("combine")
            if combine_action and combine_action["target_name"].lower() == target_name.lower():
                combined_item_name = combine_action["combined_item_name"]
                combined_item = self.items[combined_item_name]
                self.inventory.remove(item)
                self.inventory.remove(target)
                self.inventory.append(combined_item)
                success_message = combine_action.get("success_message")
                if success_message:
                    print(success_message)
            else:
                print("These items cannot be combined.")
        else:
            print("Both items must be in your inventory to combine them.")

    def show_inventory(self):
        if self.inventory:
            print("Inventory:")
            for item in self.inventory:
                print(f"- {item.name}")
        else:
            print("Your inventory is empty.")