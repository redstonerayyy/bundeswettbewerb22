from util import gettaskaverage, gettasks
from fifo import fifo

# main code
for i in range(1):
    tasks = gettasks(f"fahrradwerkstatt{i}.txt")
    results = fifo(tasks)
    print(gettaskaverage(results))