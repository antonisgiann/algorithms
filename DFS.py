def DFS(graph,start,end,path=[],shortestpath=[]):
    #initialize the path and check if you are at the destination
    if path == []:
        path = path + [start]
        if start.getName() == end.getName():
            return path
    #move to the next node
    for node in graph.childrenOf(start):
        #check if you have visited the node already
        if node not in path:
            currentpath = path.copy()
            currentpath.append(node)
        #check if the node is the final destination
            if node.getName() == end.getName():
                #check if this is the first arrival at the destination 
                #or if you have found a faster path
                if shortestpath == [] or len(currentpath) < len(shortestpath):
                    shortestpath = currentpath.copy()
        #if this is not the destination call DFS again
            else:
                shortestpath = DFS(graph,node,end,currentpath,shortestpath)
    return shortestpath

