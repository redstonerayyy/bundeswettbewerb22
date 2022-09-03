

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
    applied = [False] * len(rules)

    # start with first rule
    # if nothing connects to this, then there can not be
    # said with certainty, which is the biggest
    containers = rules[0][:]
    # keep count which rules are applied
    applied[0] = True

    # repeat until nothing was changed
    # then either all rules are fullfilled or
    # it is impossible to do so
    while True:
        change = False
        for i in range(len(rules)):
            if not applied[i]:
                # apply unapplied rules
                for j in range(len(containers)):
                    # search for a position which is either first or second of rule
                    if containers[j] in rules[i]:
                        # is first
                        if rules[i][0] == containers[j]:
                            if rules[i][1] in containers: # remove so no doubles
                                containers.remove(rules[i][1])
                            containers.insert(j + 1, rules[i][1]) # insert after
                        # is second
                        else:
                            if rules[i][0] in containers: # remove so no doubles
                                containers.remove(rules[i][0])
                            containers.insert(j, rules[i][0]) # insert before

                        # mark rule, change happened 
                        applied[i] = True
                        change = True
                        break
        # applieng rules over
        if not change:
            break

    print(f"----container{k}.txt----")
    print(containers)
    # returns True if all rules were applied
    print(min(applied))
