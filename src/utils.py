import json
from .graph import Cell


def trace_path(cell, graph):
    """Traces a path from the given cell through its parents."""
    path = []
    while cell is not None:
        path.append(Cell(cell.i, cell.j))
        cell = graph.get_parent(cell)
    # Reverse the path since it is from goal to start at this point.
    path.reverse()
    return path


def generate_plan_file(graph, start, goal, path, algo="", out_name="out.planner"):
    """Generates the planner file for visualization in the navigation web app.

    The app can be found at: hellorob.org/nav-app
    """
    print(f"Saving planning data to file: {out_name}")

    path_data = [[cell.i, cell.j] for cell in path]
    visited_cells_data = [[cell.i, cell.j] for cell in graph.visited_cells]

    plan = {
        "path": path_data,
        "visited_cells": visited_cells_data,
        "dt": [],
        "map": graph.as_string(),  # assuming mapAsString(graph) is equivalent to self.map_as_string()
        "start": [start.i, start.j],
        "goal": [goal.i, goal.j],
        "planning_algo": algo
    }

    with open(out_name, 'w') as outfile:
        json.dump(plan, outfile)
