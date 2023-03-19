# abstraction/locations.py
class Location:
    def __init__(self, name, descriptions, items, neighbors, effect_states):
        self.name = name
        self.descriptions = descriptions
        self.items = items
        self.neighbors = neighbors
        self.effect_state = 0  # Initialize the effect_state to 0
        self.effect_states = effect_states

    def update_effect_state(self, new_state):
        self.effect_state = new_state

    def get_description(self):
        return self.descriptions[self.effect_state]

