from audioop import add


beforework = 9 * 60
afterwork = 7 * 60
nowork = afterwork + beforework
work = 8 * 60

def gettasks(filename):
    with open(filename) as file:
        lines = file.read().split("\n")
        while "" in lines:
            lines.remove("")

        tasks = []
        for line in lines:
            tasks.append(line.split(" "))

        for task in tasks:
            task[0] = int(task[0])
            task[1] = int(task[1])

        return tasks

def sortbystarttime(arr):
    arr.sort(key=lambda x: x[0]) # sort array by first element of tasks [start, duration]

def sortbyduration(arr):
    arr.sort(key=lambda x: x[1]) # sort array by second element of tasks [start, duration]

def sortbywaitingtime(arr, minute):
    arr.sort(key=lambda x: minute - x[0])

def starttime():
    # by starttime
    # it is not really clear if tasks
    # are listed in the minute or after it
    # passed same with when it is finished
    # but an error of 1 or 2 is ok
    minute = beforework
    finishedtasks = []
    tasklist = []
    workduration = 0
    noworktime = 540

    while len(finishedtasks) < len(tasks):
        for i in range(work):
            # add tasks
            for j in range(len(tasks)):
                if (tasks[j][0] <= minute) and (j >= (len(finishedtasks) + len(tasklist))):
                    tasklist.append(tasks[j])
            
            
            # check if tasks is finished
            if tasklist: # prevent indexerror when empty
                if tasklist[0][1] <= workduration:
                    finishedtasks.append([
                        tasklist[0][0],
                        tasklist[0][1],
                        minute - tasklist[0][0] # time to finish it
                    ])
                    del tasklist[0]
                    workduration = 0
                    # sorting by starttime not necessary as tasks is already sorted this way
                
            # sort again
            if tasklist:
                workduration += 1
            minute += 1
            # print(minute)

        minute += nowork # skip night and freetime
        noworktime += nowork


    printstats(finishedtasks)

def durationtime():
    # by starttime
    # it is not really clear if tasks
    # are listed in the minute or after it
    # passed same with when it is finished
    # but an error of 1 or 2 is ok
    minute = beforework
    finishedtasks = []
    tasklist = []
    workduration = 0
    noworktime = 540

    while len(finishedtasks) < len(tasks):
        for i in range(work):
            # add tasks
            for j in range(len(tasks)):
                if (tasks[j][0] <= minute) and (j >= (len(finishedtasks) + len(tasklist))):
                    tasklist.append(tasks[j])
            
            if workduration < 2: # only sort if there is no ongoing task
                sortbyduration(tasklist)

            # check if tasks is finished
            if tasklist: # prevent indexerror when empty
                if tasklist[0][1] <= workduration:
                    finishedtasks.append([
                        tasklist[0][0],
                        tasklist[0][1],
                        minute - tasklist[0][0] # time to finish it
                    ])
                    del tasklist[0]
                    workduration = 0
                    # sorting by starttime not necessary as tasks is already sorted this way
                
            # sort again
            if tasklist:
                workduration += 1
            minute += 1
            # print(minute)

        minute += nowork # skip night and freetime
        noworktime += nowork


    printstats(finishedtasks)

def optimized(jobcount = 0):
    # by starttime
    # it is not really clear if tasks
    # are listed in the minute or after it
    # passed same with when it is finished
    # but an error of 1 or 2 is ok
    minute = beforework
    finishedtasks = []
    tasklist = []
    workduration = 0
    noworktime = 540
    busytime = 0
    fastjobs = 0

    while len(finishedtasks) < len(tasks):
        for i in range(work):
            # add tasks
            for j in range(len(tasks)):
                if (tasks[j][0] <= minute) and (j >= (len(finishedtasks) + len(tasklist))):
                    tasklist.append(tasks[j])
            
            # a task was finished
            if workduration < 2: # only sort if there is no ongoing task
                sortbyduration(tasklist)
                copy = tasklist[:]
                sortbywaitingtime(copy, minute)
                if copy:
                    if jobcount:
                        if fastjobs > jobcount: # if this is lower, less highs, if higher better average
                            el = tasklist.pop(tasklist.index(copy[-1]))
                            tasklist.insert(0, el)
                            fastjobs = 0
                    
                    else:
                        if (minute - copy[-1][1]) > busytime:
                            el = tasklist.pop(tasklist.index(copy[-1]))
                            tasklist.insert(0, el)
                    

            # check if tasks is finished
            if tasklist: # prevent indexerror when empty
                if tasklist[0][1] <= workduration:
                    finishedtasks.append([
                        tasklist[0][0],
                        tasklist[0][1],
                        minute - tasklist[0][0] # time to finish it
                    ])
                    busytime += tasklist[0][1] # do this before element gets deleted
                    fastjobs += 1
                    # print(busytime)
                    # print(copy)
                    del tasklist[0]
                    workduration = 0
                    # sorting by starttime not necessary as tasks is already sorted this way
                
            # sort again
            if tasklist:
                workduration += 1
            minute += 1
            # print(minute)

        minute += nowork # skip night and freetime
        noworktime += nowork

    printstats(finishedtasks)


def printstats(finishedtasks):
    addedwaitingtime = 0
    hightest = -1
    highs = []
    for i in finishedtasks:
        addedwaitingtime += i[2]
        if i[2] > hightest:
            hightest = i[2]
            highs.insert(0, i)

    average = addedwaitingtime / len(finishedtasks)
    print("Taskcount:", len(finishedtasks))
    print("Average:", average)
    print("Hightest:", hightest)
    
    belowaverage = 0
    half = 0
    for i in finishedtasks:
        if i[2] < average:
            belowaverage += 1
    
        if i[2] < hightest / 2:
            half += 1
            
    print("Below Average:", belowaverage)
    print("Below Half of Hightest:", half)
    print("")


for i in range(5):
    # get two lists
    tasks = gettasks(f"fahrradwerkstatt{i}.txt")
    sortbystarttime(tasks)

    print(f"---fahrradwerkstatt{i}.txt---")
    print("-----------------------------")
    print("--optimized with fcount 30--")
    optimized(30)
    print("--optimized with fcount 10--")
    optimized(10)
    print("--optimized with busytime switcher--")
    optimized()
    print("--SJF--")
    durationtime()
    print("--FIFO--")
    starttime()
    print("")
    print("---------------------------------")
    print("---------------------------------")
    print("")
