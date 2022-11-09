from gym.envs.registration import register


register(
    id='maze-v0',
    entry_point='gym_maze.envs:MazeEnvSample5x5',
    max_episode_steps=2000,
)

register(
    id='maze-sample-5x5-v0',
    entry_point='gym_maze.envs:MazeEnvSample5x5',
    max_episode_steps=2000,
)

register(
    id='maze-sample-5x5-v1',
    entry_point='gym_maze.envs:MazeEnvSample5x5loop',
    max_episode_steps=2000,
)

register(
    id='maze-random-5x5-v0',
    entry_point='gym_maze.envs:MazeEnvRandom5x5',
    max_episode_steps=2000,
    nondeterministic=True,
)

register(
    id='maze-sample-7x7-v0',
    entry_point='gym_maze.envs:MazeEnvSample7x7',
    max_episode_steps=3000,
)

register(
    id='maze-random-7x7-v0',
    entry_point='gym_maze.envs:MazeEnvRandom7x7',
    max_episode_steps=3000,
    nondeterministic=True,
)

register(
    id='maze-sample-10x10-v0',
    entry_point='gym_maze.envs:MazeEnvSample10x10',
    max_episode_steps=10000,
)

register(
    id='maze-random-10x10-v0',
    entry_point='gym_maze.envs:MazeEnvRandom10x10',
    max_episode_steps=10000,
    nondeterministic=True,
)

register(
    id='maze-sample-3x3-v0',
    entry_point='gym_maze.envs:MazeEnvSample3x3',
    max_episode_steps=1000,
)

register(
    id='maze-random-3x3-v0',
    entry_point='gym_maze.envs:MazeEnvRandom3x3',
    max_episode_steps=1000,
    nondeterministic=True,
)

register(
    id='maze-random-3x3-loop-v0',
    entry_point='gym_maze.envs:MazeEnvRandom3x3Loop',
    max_episode_steps=1000,
    nondeterministic=True,
)

register(
    id='maze-random-5x5-loop-v0',
    entry_point='gym_maze.envs:MazeEnvRandom5x5Loop',
    max_episode_steps=2000,
    nondeterministic=True,
)

register(
    id='maze-random-10x10-loop-v0',
    entry_point='gym_maze.envs:MazeEnvRandom10x10Loop',
    max_episode_steps=10000,
    nondeterministic=True,
)

register(
    id='maze-random-20x20-loop-v0',
    entry_point='gym_maze.envs:MazeEnvRandom20x20Loop',
    max_episode_steps=20000,
    nondeterministic=True,
)

register(
    id='maze-random-30x30-loop-v0',
    entry_point='gym_maze.envs:MazeEnvRandom30x30Loop',
    max_episode_steps=40000,
    nondeterministic=True,
)

register(
    id='maze-random-3x3-plus-v0',
    entry_point='gym_maze.envs:MazeEnvRandom3x3Plus',
    max_episode_steps=1000,
    nondeterministic=True,
)

register(
    id='maze-random-5x5-plus-v0',
    entry_point='gym_maze.envs:MazeEnvRandom5x5Plus',
    max_episode_steps=2000,
    nondeterministic=True,
)

register(
    id='maze-sample-100x100-v0',
    entry_point='gym_maze.envs:MazeEnvSample100x100',
    max_episode_steps=1000000,
)

register(
    id='maze-random-100x100-v0',
    entry_point='gym_maze.envs:MazeEnvRandom100x100',
    max_episode_steps=1000000,
    nondeterministic=True,
)

register(
    id='maze-random-10x10-plus-v0',
    entry_point='gym_maze.envs:MazeEnvRandom10x10Plus',
    max_episode_steps=1000000,
    nondeterministic=True,
)

register(
    id='maze-random-20x20-plus-v0',
    entry_point='gym_maze.envs:MazeEnvRandom20x20Plus',
    max_episode_steps=1000000,
    nondeterministic=True,
)

register(
    id='maze-random-30x30-plus-v0',
    entry_point='gym_maze.envs:MazeEnvRandom30x30Plus',
    max_episode_steps=1000000,
    nondeterministic=True,
)
