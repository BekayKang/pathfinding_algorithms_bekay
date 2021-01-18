import numpy as np
import heapq
import copy
import os
import imageio
import shutil
import matplotlib.pyplot as plt
from matplotlib import cm

# PriorityQueue
class PriorityQueue:
    def __init__(self):
        self.elements =[]

    def empty(self):
        return not self.elements

    def put(self, coordination, priority):
        heapq.heappush(self.elements, (priority, coordination))

    def get(self,):
        return heapq.heappop(self.elements)[1]

class dijkstra_algo:
    def __init__(self,mapsize,start_point,end_point,cost_map):
        self.map_size=mapsize
        self.start_point = start_point
        self.end_point = end_point
        self.cost_map = cost_map

    # Get neighbors of current position
    def get_neighbors(self,current):
        neighbors = set()
        # Down
        if current[0]+1<self.map_size[0]:
            neighbors.add((current[0]+1,current[1]))
        # Left
        if current[1]-1>=0:
            neighbors.add((current[0],current[1]-1))
        # Up
        if current[0]-1>=0:
            neighbors.add((current[0]-1,current[1]))
        # Right
        if current[1]+1<self.map_size[1]:
            neighbors.add((current[0],current[1]+1))

        return neighbors

    # Find the path
    def find_path(self,):
        frontier = PriorityQueue()
        frontier.put(self.start_point,0)

        came_from = dict()
        came_from[self.start_point]=None

        cost_value = dict()
        cost_value[self.start_point]=0


        # Searching Grid Map
        while not frontier.empty():
            current = frontier.get()
            if current == self.end_point:
                break
            neighbors = self.get_neighbors(current)
            for next in neighbors:
                new_cost = cost_value[current] + self.cost_map[next]
                if next not in cost_value or new_cost < cost_value[next]:
                    cost_value[next] = new_cost
                    frontier.put(next,new_cost)
                    came_from[next]=current

        # Reconstruction path --> (Backwards from the goal to the start)
        current = self.end_point
        path = []
        while current != self.start_point:
            path.append(current)
            current = came_from[current]
        path.append(self.start_point)
        path.reverse()

        return path

    def visualization(self,path):
        # Save the problem as a figure
        path_map = np.zeros((self.map_size[0],self.map_size[1],3))
        path_map[self.start_point[0],self.start_point[1],1]=255
        path_map[self.end_point[0],self.end_point[1],1]=255
        path_map[:,:,0]=self.cost_map

        os.makedirs('./temp_gif', exist_ok=True)
        images_gif=[]
        #initial
        plt.imshow(path_map, cmap=cm.OrRd)
        plt.imshow(self.cost_map,cmap=cm.coolwarm, alpha=0.4)
        plt.axis('off')
        plt.tight_layout()
        plt.savefig('./Problem.png',dpi=100)
        plt.savefig('./temp_gif/result' + str(0) +'.png',dpi=100)
        images_gif.append(imageio.imread('./temp_gif/result' + str(0) +'.png'))
        plt.close()
        for i,pos in enumerate(path):
            path_map[pos[0],pos[1]]=255
            plt.imshow(path_map, cmap=cm.OrRd)
            plt.imshow(self.cost_map,cmap=cm.coolwarm, alpha=0.4)
            plt.axis('off')
            plt.tight_layout()
            plt.savefig('./temp_gif/result' + str(i+1) +'.png',dpi=100)
            images_gif.append(imageio.imread('./temp_gif/result' + str(i+1) +'.png'))
            plt.close()
        imageio.mimsave('./Result_Dijkstra.gif',images_gif)

        shutil.rmtree('./temp_gif')
        return path
