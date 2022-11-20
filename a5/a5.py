from network import Graph


# get data from file
def getfiledata(filename):
    with open(filename) as file:
        lines = file.read().split("\n")

        while "" in lines:
            lines.remove("")

        connections = []

        for line in lines:
            connections.append(
                [int(line.split(" ")[0]),
                 int(line.split(" ")[1])])

        return connections


graphlist = []

for i in range(5):
    # graph object list
    curgraph = []
    # read from file
    data = getfiledata(f"huepfburg{i}.txt")
    graph = Graph(data)
    # add to object
    curgraph.append(data[:])
    # get all paths
    sashapaths = graph.BFS(1, 2)
    mikapaths = graph.BFS(2, 1)

    meetups = {}

    # sort paths
    # for each node all the paths from sasha and mika will be collected which
    # lead to it. then it will check for the shortest of them
    # or if there is a path
    for node in graph.nodes:
        meet = {
            "node": node,
            "sasha": [],
            "mika": [],
            "sashashortest": None,
            "mikashortest": None
        }
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

    # search for the shortest
    shortlength = None
    shortest = None
    for node in graph.nodes:
        if meetups[node]["sasha"] and meetups[node]["mika"]:
            if shortlength == None:
                shortlength = max(len(meetups[node]["sashashortest"]),
                                  len(meetups[node]["mikashortest"]))
                shortest = [
                    meetups[node]["sashashortest"],
                    meetups[node]["mikashortest"]
                ]

            if max(len(meetups[node]["sashashortest"]),
                   len(meetups[node]["mikashortest"])) < shortlength:
                shortlength = max(len(meetups[node]["sashashortest"]),
                                  len(meetups[node]["mikashortest"]))
                shortest = [
                    meetups[node]["sashashortest"],
                    meetups[node]["mikashortest"]
                ]

    # add to list collection
    curgraph.append(shortest)

    # print, e. g. python a5.py >> solution.txt (on linux)
    print(f"---huepfburg{i}.txt---")
    print(shortlength - 1)
    print("Sasha:", shortest[0])
    print("Mika:", shortest[1])
    # append to global list to visualize each of them at the end
    graphlist.append(curgraph)

# visualization
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import get_backend

for b in range(5):
    G = nx.DiGraph()
    graphn = b
    G.add_edges_from(graphlist[graphn][0])

    # sasha edges
    sedges = []
    for i in range(len(graphlist[graphn][1][0])):
        if i < len(graphlist[graphn][1][0]) - 1:
            sedges.append(
                [graphlist[graphn][1][0][i], graphlist[graphn][1][0][i + 1]])

    # mika edges
    medges = []
    for i in range(len(graphlist[graphn][1][1])):
        if i < len(graphlist[graphn][1][1]) - 1:
            medges.append(
                [graphlist[graphn][1][1][i], graphlist[graphn][1][1][i + 1]])

    restedges = [
        edge for edge in G.edges()
        if (edge not in sedges and edge not in medges)
    ]

    pos = nx.kamada_kawai_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'))
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=restedges, arrows=True)
    nx.draw_networkx_edges(G,
                           pos,
                           edgelist=medges,
                           edge_color='y',
                           arrows=True)
    nx.draw_networkx_edges(G,
                           pos,
                           edgelist=sedges,
                           edge_color='r',
                           arrows=True)

    # print(get_backend()) find out backend
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()
    plt.show()
