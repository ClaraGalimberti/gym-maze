from setuptools import setup

setup(name="gym_maze",
      version="0.4",
      url="https://github.com/tuzzer/gym-maze",
      author="Matthew T.K. Chan",
      license="MIT",
      packages=["gym_maze", "gym_maze.envs"],
      package_data={
          "gym_maze.envs": ["maze_samples/*.npy"]
      },
      install_requires=['gym==0.15.7',
                        'pygame',
                        'numpy',
                        'pillow']
      )

# If pygame is not installing, run: brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
# or
# export CC='/usr/bin/gcc'
# export CFLAGS='-isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.8.sdk -I/opt/X11/include -arch i386 -arch x86_64'
# export LDFLAGS='-arch i386 -arch x86_64'
# export ARCHFLAGS='-arch i386 -arch x86_64'
