class Game:
    current_state = None
    end_state = lambda _: False

    def __init__(self, initial_state=None):
        """Set up initial state."""
        self.current_state = initial_state


    def update(self, last_state):
        """Returns the next game state."""
        return last_state # default


    def draw(self, state):
        """Draw the current game state."""


    def end_state(self, state):
        return False

    def run(self, end_state=None):
        end_state = end_state or self.end_state
        self.draw(self.current_state)
        while not end_state(self.current_state):
            self.current_state = self.update(self.current_state)
            self.draw(self.current_state)
        # exit
