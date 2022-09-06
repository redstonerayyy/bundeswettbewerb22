def getcontainers(filename):
    with open(filename) as file:
        lines = file.readlines()
        while "" in lines: # remove empty
            lines.remove("")
        # get container info
        containers = []
        for i in lines:
            cons = i.split(" ")
            while "" in cons: # remove empty
                cons.remove("")
            # parse int from list
            # left container is bigger than right? they don't say
            # anyway easy to switch, maybe finding out when testing
            containers.append([int(cons[0]), int(cons[1])])
        
        return containers

for k in range(4):
    # main code
    rules = getcontainers(f"container{k}.txt")
    
    # get list of all containers
    allcontainers = []
    for rule in rules:
        for i in rule:
            allcontainers.append(i)
    
    # remove doubles by making it a set
    allcontainers = set(allcontainers)

    # dependence dict, container as key and all that are smaller than it as value
    dependence = {}

    # add to dependence
    for rule in rules:
        if rule[0] in dependence:
            dependence[rule[0]].append(rule[1]) # 0 bigger than 1
        else:
            dependence[rule[0]] = [rule[1]]

    
    print(f"----container{k}.txt----")
    
    # iterate over the tree for each container
    # using BFS. mark each container
    for container in dependence:
        smaller = { container }
        queque = [container]
        checked = []
        while queque:
            con = queque.pop(0)
            checked.append(con)
            for c in dependence[con]:
                smaller.add(c)
                if c in dependence:
                    queque.append(c)

        if len(smaller) == len(allcontainers):
            print(f"largest is container: {container}")
