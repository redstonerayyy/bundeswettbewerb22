# define classes to form a network

class Graph:
    def __init__(self, connections) -> None:
        self.connections = connections[:]
        self.connections.sort(key=lambda x: x[0])
        self.nodes = {}


        for i in range(len(self.connections)):
            if self.connections[i][0] in self.nodes:
                self.nodes[self.connections[i][0]].append(self.connections[i][1])
            else:
                self.nodes[self.connections[i][0]] = [self.connections[i][1]]

        unconnected = []
        for i in self.nodes:
            for j in self.nodes[i]:
                if not (j in self.nodes):
                    unconnected.append(j)
        
        # why is there a 44 in the first file?
        for i in unconnected:
            self.nodes[i] = []


    def BFS(self, vertex, target):
        queque = []
        paths = []
        marks = []
        queque.append([vertex])
        paths.append([vertex])
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
