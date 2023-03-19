# abstraction/items.py
class Item:
    def __init__(self, name, description, actions, fixed, item_type):
        self.name = name
        self.description = description
        self.actions = actions
        self.fixed = fixed
        self.item_type = item_type
