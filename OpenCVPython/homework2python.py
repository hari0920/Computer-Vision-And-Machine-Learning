#import packages
import numpy as np

#inputs to function
image = np.array([[3, 1, 2, 1], [2, 2, 0, 2], [1, 2, 1, 1], [1, 0, 1, 2]], np.int32)
temp=np.array([[1,2,2,2],[3,4,4,5]],np.int32)
V = [1, 0]
start = (3,0)
end = (0,3)
def final_function(image,V,start,end,k):
    A = np.array(image) #copy of the original
    [rows, cols] = A.shape
    N = rows * cols
    #passable and non-passable areas
    for i in range(rows):
        for j in range(cols):
            if image[i, j] in V:
                A[i, j] = 1  # passable
            else:
                A[i, j] = 0  # not passable
    #print A
    #check if within bounds
    def in_bounds(id):
        (x, y) = id
        return 0 <= x < rows and 0 <= y < cols
    #check if accessible
    def accessible(id1):
        (x,y)=id1
        return A[x,y] ==1

    # empty dictionary for adjacency representation
    adjLists_dict = {}
    # insert (vertex, list) pairs into dictionary
    for x in range(rows):
        for y in range(cols):
            if A[x,y]==1:
                if(k==4):
                    temp = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
                    temp = filter(in_bounds, temp)
                    temp = filter(accessible,temp)
                    adjLists_dict[x, y]=temp
                elif(k==8):
                    temp = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1),(x + 1, y+1), (x-1, y - 1), (x + 1, y-1), (x-1, y + 1)]
                    temp = filter(in_bounds, temp)
                    temp = filter(accessible,temp)
                    adjLists_dict[x, y]=temp
                elif(k==12):
                     #check for 4-path, then if not, then go for diagonal.
                     temp = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]# 4-path
                     temp = filter(in_bounds, temp)
                     temp = filter(accessible,temp)# check the accessibility of 4-neighbours
                     temp2 = [(x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]
                     temp2 = filter(in_bounds, temp2)
                     temp2 = filter(accessible, temp2)
                     if len(temp)>0: #accessible , then use 4
                        adjLists_dict[x, y] = temp
                     elif len(temp)==0 and len(temp2)>0:#not accessible, so go diagonal.
                        adjLists_dict[x, y] = temp2
    # testing
    print adjLists_dict

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

    path_found=find_shortest_path(adjLists_dict,start,end)
    if path_found==None:
        print "No path"
        return path_found,0
    else:
        print path_found
        print len(path_found)-1
        return path_found,len(path_found)-1

final_function(image,V,start,end,8)
