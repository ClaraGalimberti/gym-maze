import sys
import time
import numpy as np
import math
import random
import argparse

import gym
import gym_maze


if __name__ == "__main__":

    # Argument parser
    parser = argparse.ArgumentParser(description="Maze environment language and configuration.")
    parser.add_argument(
        "--lang",
        type=str,
        default="it",
        choices=["en", "fr", "it", "de"],
        help="Language selection (default: 'it')."
    )
    # parser.add_argument(
    #     "--maze",
    #     type=str,
    #     default="maze-sample-10x10-loop-v0",
    #     help="Maze environment name (default: 'maze-sample-10x10-loop-v0')."
    # )

    args = parser.parse_args()

    lang = args.lang
    # maze_choice = args.maze

    # maze_choice = "maze-sample-5x5-v0"
    # maze_choice = "maze-sample-5x5-v1"
    # maze_choice = "maze-sample-7x7-v0"
    maze_choice = "maze-sample-10x10-loop-v0"
    # maze_choice = "maze-random-5x5-v0"
    # maze_choice = "maze-random-7x7-v0"
    # maze_choice = "maze-random-10x10-loop-v0"

    # Initialize the "maze" environment
    env = gym.make(maze_choice, lang=lang)

    MAZE_SIZE = tuple((env.observation_space.high + np.ones(env.observation_space.shape)).astype(int))
    MAX_T = np.prod(MAZE_SIZE, dtype=int) * 100

    print("Maze size: %d %d -- Max t: %d" % (MAZE_SIZE[0], MAZE_SIZE[1], MAX_T))

    obv, done = env.reset()
    env.render()
    i = 0
    total_reward = 0
    render_mode = "human"
    value_function_show = False
    wall_greyscale_show = False
    attempt_counter = 0
    env.save_screenshot("maze%03d.png" % attempt_counter, show_value_function=True, delete_previous=True)
    attempt_counter += 1
    print("Starting game...")
    while i < MAX_T:
        while True:
            action = env.maze_view.get_input_key()
            if action is not None:
                break

        if action == 'solution':
            if render_mode == "human":
                print("Maze with walls...")
                render_mode = "solution"
            else:
                print("Maze without walls...")
                render_mode = "human"
            env.render(mode=render_mode)
        if action == 'ValueFunction':
            if not value_function_show:
                value_function_show = True
                print("Maze with value function...")
                env.show_value_function('on')
            else:
                value_function_show = False
                print("Maze without value function...")
                env.show_value_function('off')
            env.render(mode=render_mode)
        if action == 'wall':
            if not wall_greyscale_show:
                wall_greyscale_show = True
                print("Maze with grayscale walls...")
                env.show_greyscale_wall('on')
            else:
                wall_greyscale_show = False
                print("Maze without grayscale walls...")
                env.show_greyscale_wall('off')
            env.render(mode=render_mode)

        if not done and env.valid_action(action):  # execute the action
            obv, reward, done, _ = env.step(action)
            total_reward += reward
            print("Action: %s \t||\t Reward: %.4f" % (action, total_reward))
            env.render(mode=render_mode, cost=total_reward)
            i = i+1
            if done:
                filename = "maze%03d.png" % attempt_counter
                attempt_counter += 1
                env.save_screenshot(filename, show_value_function=True)
                print("Finished after %f time steps with total reward = %.4f." % (i, total_reward))
                print("Press enter to continue...")

        if env.is_game_over():
            env.generate_gif()
            print("Game over! \nBye :)")
            break

        if done and action == 'enter':
            # Reset the environment
            obv, done = env.reset()
            total_reward = 0
            env.render(mode=render_mode)

    else:
        print("Timed out at %d with total reward = %f." % (i, total_reward))

    print("Closing game...")
