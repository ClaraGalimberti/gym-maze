import sys
import time
import numpy as np
import math
import random

import gym
import gym_maze


if __name__ == "__main__":

    # Initialize the "maze" environment
    env = gym.make("maze-sample-5x5-v0")

    MAZE_SIZE = tuple((env.observation_space.high + np.ones(env.observation_space.shape)).astype(int))
    MAX_T = np.prod(MAZE_SIZE, dtype=int) * 100

    print("Maze size: %d %d -- Max t: %d" % (MAZE_SIZE[0], MAZE_SIZE[1], MAX_T))

    obv, done = env.reset()
    env.render()
    i = 0
    total_reward = 0
    print("Starting game...")
    while i < MAX_T:
        while True:
            action = env.maze_view.get_input_key()
            if action is not None:
                break

        if action == 'solution':
            env.render(mode='solution')
            time.sleep(2)
            break
        if env.valid_action(action):  # execute the action
            obv, reward, done, _ = env.step(action)
            total_reward += reward
            env.render()
            i = i+1

        if env.is_game_over():
            print("Game over! \nBye :)")
            break

        if done:
            print("Finished after %f time steps with total reward = %.4f."
                  % (i, total_reward))
            # Reset the environment
            obv, done = env.reset()
            env.render()

        print("Your action is: %s \t||\t The current reward is: %.4f" % (action, total_reward))

    else:
        print("Timed out at %d with total reward = %f." % (i, total_reward))

    print("Closing game...")
