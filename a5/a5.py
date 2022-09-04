from network import Graph

# get data from file
def getfiledata(filename):
    with open(filename) as file:
        lines = file.read().split("\n")

        while "" in lines:
            lines.remove("")

        connections = []

        for line in lines:
            connections.append([
                int(line.split(" ")[0]),
                int(line.split(" ")[1])
            ])

        return connections


for i in range(5):
    data = getfiledata(f"huepfburg{i}.txt")
    graph = Graph(data)
    sashapaths = graph.BFS(1, 2)
    mikapaths = graph.BFS(2, 1)
    
    meetups = {}

    for node in graph.nodes:
        meet = {"node": node, "sasha": [], "mika": [], "sashashortest": None, "mikashortest": None}
        sashashortest = None
        for path in sashapaths["indirect"]:
            if path[-1] == node:
                meet["sasha"].append(path)
                
                if sashashortest == None:
                    sashashortest = path

                if len(path) < len(sashashortest):
                    sashashortest = path
        
        meet["sashashortest"] = sashashortest

        mikashortest = None
        for path in mikapaths["indirect"]:
            if path[-1] == node:
                meet["mika"].append(path)
                
                if mikashortest == None:
                    mikashortest = path

                if len(path) < len(mikashortest):
                    mikashortest = path

        meet["mikashortest"] = mikashortest

        meetups[node] = meet

    shortlength = None
    shortest = None
    for node in graph.nodes:
        if meetups[node]["sasha"] and meetups[node]["mika"]:
            if shortlength == None:
                shortlength = max(len(meetups[node]["sashashortest"]), len(meetups[node]["mikashortest"]))
                shortest = [meetups[node]["sashashortest"], meetups[node]["mikashortest"]]

            if max(len(meetups[node]["sashashortest"]), len(meetups[node]["mikashortest"])) < shortlength:
                shortlength = max(len(meetups[node]["sashashortest"]), len(meetups[node]["mikashortest"]))
                shortest = [meetups[node]["sashashortest"], meetups[node]["mikashortest"]]

    print(f"---huepfburg{i}.txt---")
    print(shortlength - 1)
    print("Sasha:", shortest[0])
    print("Mika:", shortest[1])
