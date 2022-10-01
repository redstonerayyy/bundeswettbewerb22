# calculate some times
beforework = 9 * 60 # he starts at 9, so plus 540 minutes
afterwork = 7 * 60 # he ends at 17, so plus 420 minutes until the next day
noworktime = afterwork + beforework # time between to working intervalls
worktime = 8 * 60 # time he works

# read from file
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

# using nice sorting lambdas from STO
def sortbystarttime(arr):
    arr.sort(key=lambda x: x[0]) # sort array by first element of tasks [start, duration]

def sortbyduration(arr):
    arr.sort(key=lambda x: x[1]) # sort array by second element of tasks [start, duration]

def gettaskaverage(finishedtasks):
    _sum = 0
    for task in finishedtasks:
        print(task[-1]) 
        _sum += task[-1]

    return _sum / len(finishedtasks)