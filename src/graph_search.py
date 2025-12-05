import numpy as np
from collections import deque
import heapq

from .graph import Cell
from .utils import trace_path

def _valid_start_goal(graph, start, goal):
    if not graph.is_cell_in_bounds(start.i, start.j):
        return False
    if not graph.is_cell_in_bounds(goal.i, goal.j):
        return False
    if graph.check_collision(start.i, start.j):
        return False
    if graph.check_collision(goal.i, goal.j):
        return False
    return True



def breadth_first_search(graph, start, goal):
    
    graph.init_graph() 

    if not _valid_start_goal(graph, start, goal):
        return []

    # BFS 
    q = deque()
    q.append(start)
    graph.visited[start.j, start.i] = True
    graph.g_costs[start.j, start.i] = 0.0
    graph.parents[start.j][start.i] = None

    while q:
        current = q.popleft()
        graph.visited_cells.append(Cell(current.i, current.j))

        
        if current.i == goal.i and current.j == goal.j:
            return trace_path(goal, graph)

        for neighbor in graph.find_neighbors(current.i, current.j):
            if not graph.visited[neighbor.j, neighbor.i]:
                graph.visited[neighbor.j, neighbor.i] = True
                graph.parents[neighbor.j][neighbor.i] = (current.i, current.j)
                graph.g_costs[neighbor.j, neighbor.i] = graph.g_costs[current.j, current.i] + 1.0
                q.append(neighbor)

   
    return []



