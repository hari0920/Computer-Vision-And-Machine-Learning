#import packages
import numpy as np

image = np.array([[3, 1, 2, 1], [2, 2, 0, 2], [1, 2, 1, 1], [1, 0, 1, 2]], np.int32)
#temp=np.array([[1,2,2,2],[3,4,4,5]],np.int32)
V = [0, 1]
A = np.array(image) #copy


[rows, cols] = A.shape
N = rows * cols
for i in range(rows):
    for j in range(cols):
        if image[i, j] in V:
            A[i, j] = 1  # passable
        else:
            A[i, j] = 0  # not passable
#print A

def in_bounds(id):
    (x, y) = id
    return 0 <= x < rows and 0 <= y < cols


def accessible(id1):
    (x,y)=id1
    return A[x,y] ==1

# empty dictionary
adjLists_dict = {}
# insert (vertex, list) pairs into dictionary
for x in range(rows):
    for y in range(cols):
        if A[x,y]==1:
            #temp = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
            temp = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1),
                    (x - 1, y + 1)]
            temp = filter(in_bounds, temp)
            temp = filter(accessible,temp)
            adjLists_dict[x, y]=temp
# testing
#print adjLists_dict

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        #print node
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


s = (3,0)
e = (0,3)
#find_shortest_path(adjLists_dict, s, e)
path_found=find_shortest_path(adjLists_dict,s,e)
print path_found
print len(path_found)