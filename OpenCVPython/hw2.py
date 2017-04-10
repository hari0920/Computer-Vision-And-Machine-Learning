#inport necessary packages.
import numpy as np
import cv2
image2= np.array([[3, 1, 2, 1], [2, 2, 0, 2], [1, 2, 1, 1], [1, 0, 1, 2]], np.int32)
V=[0,1]
image=np.array([[1,2],[3,4]])

#visited= np.zeros(image.shape)# a visited array for each pixel with 1 for visited.
#we must preprocess the image segment to fit into the graph representation.

def neighbourhood(graph,i,j):
    if i > 0 and i < rows and j > 0 and j < cols:
        #graph[i, j] = [[i, j - 1], [i - 1, j], [i + 1, j], [i, j + 1]]
        graph = {(i, j): [] for j in range(j - 1, j + 1) for i in range(i - 1, i + 1) if image[i][j]in V}

temp=np.array([[1,2],[3,4]])
graph={}

#def neighbourhood_definition(image,graph):
[rows,cols]=temp.shape
for i in range(rows):
    for j in range(cols):
        neighbourhood(graph,i,j)

#neighbourhood_definition(temp,graph)
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

#neighbourhood_definition(temp,graph)
find_shortest_path(graph,[1,1],[2,2])







