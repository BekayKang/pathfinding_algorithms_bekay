from algorithms.astar_algorithm import astar_algo
from algorithms.breath_first_algorithm import breath_first_algo
from algorithms.dijkstra_algorithm import dijkstra_algo
import numpy as np

if __name__ == '__main__':
    # A* Algorithm
    # Define Map
    start_point = (0,0)
    end_point = (9,9)
    map_size = (10,10)
    map = np.zeros((map_size[0], map_size[1]))

    # Generate wall
    wall_point = [[2,0],[2,1],[2,2],[0,2],[0,5],[0,6],[1,4],[1,6],[2,4],[2,6],[2,8],[2,9],
    [3,4],[3,6],[3,8],[4,1],[4,2],[4,3],[4,4],[5,8],[6,0],[6,1],[6,2],[6,4],[6,5],[6,6],[7,2],[7,5],[7,8],
    [8,3],[8,5],[8,7],[9,7]]
    for pos in wall_point:
        map[pos[0], pos[1]]=255

    # BFS Algorithm
    bfs = breath_first_algo(map_size,start_point,end_point,map) # Actually Map is not a considered parameter in BFS
    bfs_path = bfs.find_path()
    bfs.visualization(bfs_path)

    # A* Algorithm
    dijkstra = dijkstra_algo(map_size,start_point,end_point,map)
    dijkstra_path = dijkstra.find_path()
    dijkstra.visualization(dijkstra_path)

    # A* Algorithm
    astar = astar_algo(map_size,start_point,end_point,map)
    astar_path = astar.find_path()
    astar.visualization(astar_path)