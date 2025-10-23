# Labyrinth

A simple 2D maze environment where an agent (blue dot) finds its way from the top left corner (blue square) to the goal
at the bottom right corner (red square). 
The objective is to find the shortest path from the start to the goal.

### Instalation
Make sure to install `gym==0.15.7`.  
Note that there is a newer package called `Gymnasium`, but this project has not yet been migrated to it.

### Maze manual
Run the `maze_manual.py` file.

#### Arguments
You can specify the language and maze configuration when running the script:
```bash
python maze_manual.py [--lang {en,fr,it,de}]
```
<!-- [--maze MAZE_NAME] -->

- `--lang`: sets the language (`en`, `fr`, `it`, or `de`). Default is `'it'`.  
<!-- - `--maze`: selects the maze environment. Default is `'maze-sample-10x10-loop-v0'`. -->

#### Controls

- Navigate the maze using the arrow keys.
- Show/hide the walls with `o` key. 
- Show/hide the latest value function approximation with `v` key.
- Show/hide the greish walls with `w` key (if `o` option is not active).

Once the game is closed, a GIF will be generated at te `gif` folder. Open it with your favourite browser.

_Note:_ Each time you run the script, all previously generated figures in the `fig` folder, 
as well as the GIF, will be deleted.





