# define classes to form a network

class Graph:
    def __init__(self, connections) -> None:
        self.connections = connections[:]
        self.connections.sort(key=lambda x: x[0])
        self.nodes = {}

        # generate dictionary where each node is a key
        # and all nodes it has connections to are stored
        # in a list as the value
        for i in range(len(self.connections)):
            if self.connections[i][0] in self.nodes:
                self.nodes[self.connections[i][0]].append(self.connections[i][1])
            else:
                self.nodes[self.connections[i][0]] = [self.connections[i][1]]

        # check which nodes are not connected
        # this will add the same nodes multiple times
        unconnected = []
        for i in self.nodes:
            for j in self.nodes[i]:
                if not (j in self.nodes):
                    unconnected.append(j)
        
        # why is there a 44 in the first file?
        # this will set each unconnected note to an empty list
        # it will set each multiple times as said above
        for i in unconnected:
            self.nodes[i] = []


    def BFS(self, vertex, target):
        # https://en.wikipedia.org/wiki/Breadth-first_search to understand better
        queque = []
        paths = []
        marks = []
        # queque holds all vertices
        queque.append([vertex])
        # holds all paths
        paths.append([vertex])
        # mark vertices so no loops occur
        marks.append(vertex)

        while queque:
            path = queque.pop(0)

            node = path[-1]
            if node == target:
                return { "direct": path, "indirect": paths }
            
            for adjacent in self.nodes[node]:
                if not (adjacent in marks):
                    marks.append(adjacent)
                    newpath = path[:]
                    newpath.append(adjacent)
                    
                    paths.append(newpath)
                    queque.append(newpath)
        
        return { "direct": None, "indirect": paths }
