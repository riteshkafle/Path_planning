# Project 3: Path Planning - Python (F23)

Template code for Project 3 (Path Planning) in Python.
See [project instructions](https://hellorob.org/projects/p3) for more details.

## Testing your code on example maps

This repository includes a helper script to visualize plan outputs compatible with the
[navigation web app](https://hellorob.org/nav-app/). A tutorial is available [here](https://hellorob.org/tutorials/app).
You can run this file on your laptop (as long as you have Python 3 installed). To do so, do:
```bash
python path_planner_cli.py -m [PATH/TO/MAP] --start [START_i START_j] --goal [GOAL_i GOAL_j]
```
The map can be any map in the `data/` folder. You can also make your own or use maps from the robot to test! The start and goal should be represented by cell indices. You can also upload maps to the web app so that you can choose good start and goal cells to test. To test a different algorithm, you can pass `--algo [astar | bfs | dfs]`. The default is `bfs`.

This script will generate the file `out.planner`, which you can upload to the web app.

Use `python path_planner_cli.py -h` to show usage.

## Planning on the robot

To run your code on the robot, you will first need to have [made a map and be localized in it](https://hellorob.org/mbot/mapping).
Then, on the robot, do:
```bash
python robot_plan_path.py --goal [GOAL_x GOAL_y]
```
The goal is an x and y position in meters. Use the robot's web app to pick a good goal by clicking the cell you want to navigate to and noting its coordinates.

You will likely want to change the default collision radius. You can do this with argument `-r [RADIUS]`.

Use `python robot_plan_path.py -h` to show usage.
