# This class describe all the events in the game

class Event:
    def __init__(self, text, actions, effect):
        # Text for display
        self.text = text
        # List of actions that can be taken in response to the event
        self.actions = actions
        # immediate effect
        self.effect = effect

    # string representation
    def __str__(self):
        to_return = self.text + "\n"
        to_return += str(self.effect)
        to_return += "Your action: " + "\n"
        for index, action in enumerate(self.actions):
            to_return += str(index + 1) + ": " + action.text
            if index % 2 == 0:
                to_return += "\t"
            else:
                to_return += "\n"
        return to_return


