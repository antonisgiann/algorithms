"""implementation of the breadth first search algorithm
   without weights on the edges
   From each node we can get the nodes we can go to 
   with the childrenOf() function.Each node is identifiend by
   a name which we get with the getName() function
   """
def BFS(graph,start,end):
    #create the first search path
    front = [start]
    paths=[front]
    #while there is a path for searching search
    while paths != []:
        #take the first searching path of the available paths
        tempPath= paths.pop(0)
        #create the next searching paths if there are some
        for node in graph.childrenOf(tempPath[-1]):
            path = tempPath + [node]
            paths.append(path)
            #check if you found your destination
            if node.getName() == end.getName():
                return path
    else:
        return None
            
        


