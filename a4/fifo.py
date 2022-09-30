from util import *
import math

# simulate fifo job scheduling

def fifo(tasks):
    # sort list
    sortedtasks = sortbystarttime(tasks)
    
    minute = beforework # current minute
    day = 0 # current day
    minuteofday = 0 # minute of day
    finishedtasks = [] # store with info on how long it took
    workduration = 0
    currenttask = sortedtasks.pop(0)

    # repeat until all tasks are done
    while sortedtasks or currenttask:
        start = [minute, day, minuteofday] # save start time

        # calculate time task needs
        days = math.floor(currenttask[1] / worktime)
        minutes = currenttask[1] / worktime - math.floor(currenttask[1] / worktime)

        # minutes of day left
        minutesleftofday = worktime - minuteofday
        
        # check how to calculate

        # subtract remaining minutes of day from minutes,
        # add minutes from a day, if its to small
        # if no day, the task can be finished on the same day
        minutediff = minutes - minutesleftofday

        # more minutes in day left than task needs
        if minutediff < 0:
            # get more minutes from a day
            if days > 0:
                days -= 1
                minutediff += worktime
                minutes = minutediff
                minuteofday = 0
                day += 1

            # can't get minutes, no more day
            else:
                # TASK FINISHED
                minuteofday += minutes
                minute += minutes

        elif minutediff == 0:
            minuteofday = 0
            minutes = 0

        else:
            # > 0 either normal or by adding a day
            # subtract the remaining minutes of the day
            # then calculate, as the remaining minutes
            # can't be longer than a day
            minutes -= minutesleftofday

        day += days
        minutes += minutes

        end = [minute, day, minuteofday]
        # add 1 two days and set minute to zero again afterwards