"""Draw a flying nyan cat."""

import curses
from pyrsistent import m, inc
# from curses import halfdelay, beep, wrapper, error as c_err
from engine import Game

class NyanGame(Game):
    def __init__(self, initial_state=None):
        super().__init__(m(
            time=0,
            color=curses.COLOR_MAGENTA,
            background=curses.COLOR_GREEN
        ))

    def update(self, last_state):
        return last_state.transform(['time'], inc)

    def draw(self, state):
        time = state.get('time')
        print(" "*time + "nyan")

    def end_state(self, state):
        return state.get('time') == 5

game = NyanGame()
game.run()
