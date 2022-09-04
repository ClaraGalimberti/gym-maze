import sys
import time
import numpy as np
import math
import random

import gym
import gym_maze


def translate_action(action):
    if action == 'w':
        a = 'N'
    elif action == 's':
        a = 'S'
    elif action == 'a':
        a = 'W'
    elif action == 'd':
        a = 'E'
    elif action == 'p':
        a = 'close'
    elif action == 'o':
        a = 'solution'
    else:
        a = 4
    return a


class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchUnix()
            # self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


# class _GetchWindows:
#     def __init__(self):
#         import msvcrt
#
#     def __call__(self):
#         import msvcrt
#         return msvcrt.getch()


getch = _Getch()


if __name__ == "__main__":

    # Initialize the "maze" environment
    env = gym.make("maze-sample-5x5-v0")

    MAZE_SIZE = tuple((env.observation_space.high + np.ones(env.observation_space.shape)).astype(int))
    MAX_T = np.prod(MAZE_SIZE, dtype=int) * 100

    print("Maze size: %d %d -- Max t: %d" % (MAZE_SIZE[0], MAZE_SIZE[1], MAX_T))

    env.reset()
    env.render()
    i = 0
    total_reward = 0
    print("Starting game...")
    while i < MAX_T:
        action = 4
        while action == 4:
            try:
                ch = getch()
            except:
                ch = input()
            else:
                ch = input()
            action = translate_action(ch)
        print("Your action is: %s \t||\t The current reward is: %.4f" % (action, total_reward))
        if action == 'close':
            sys.exit()
        if action == 'solution':
            env.render(mode='solution')
            time.sleep(1)
            sys.exit()
        # execute the action
        obv, reward, done, _ = env.step(action)
        total_reward += reward
        env.render()
        i = i+1
        if env.is_game_over():
            sys.exit()

        if done:
            print("Finished after %f time steps with total reward = %.4f."
                  % (i, total_reward))
            # Reset the environment
            obv = env.reset()
            env.render()

        elif i >= MAX_T - 1:
            print("Timed out at %d with total reward = %f."
                  % (i, total_reward))

    print("Time out!")
    print("Closing game...")
    sys.exit()
