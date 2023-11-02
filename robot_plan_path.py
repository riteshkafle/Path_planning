import argparse
from mbot_bridge.api import MBot

from src.graph import GridGraph, Cell
from src.graph_search import a_star_search, breadth_first_search, depth_first_search
from src.utils import generate_plan_file


def cells_to_poses(path, g):
    return [[*g.cell_to_pos(c.i, c.j), 0] for c in path]


def parse_args():
    parser = argparse.ArgumentParser(description="HelloRob Path Planning on the Robot.")
    parser.add_argument("-m", "--map", type=str, default="/home/mbot/current.map", help="Path to the map file.")
    parser.add_argument("--goal", type=float, nargs=2, default=[0, 0], help="Goal position.")
    parser.add_argument("-r", "--collision-radius", type=float, default=15, help="Collision radius (meters).")

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = parse_args()

    # Create the GridGraph using the robot map. HINT: You may want to set a new
    # value for the collision radius than the default.
    graph = GridGraph(args.map, collision_radius=args.collision_radius)
    goal = graph.pos_to_cell(*args.goal)

    # Initialize the MBot object.
    robot = MBot()
    # Get the current SLAM pose and convert it to a start cell.
    start_pose = robot.read_slam_pose()
    start = graph.pos_to_cell(*start_pose[:2])

    path = []
    # TODO: Call graph search function and put the result in path.

    # Send the path to the robot.
    print(f"Found path of length {len(path)}. Driving to the goal!")
    robot.drive_path(cells_to_poses(path, graph))

    # Genererate the path file for visualization.
    generate_plan_file(graph, start, goal, path)
