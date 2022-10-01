from numpy import sort
from util import *
import math

# simulate fifo job scheduling

def fifo(tasks):
    # sort list
    sortedtasks = tasks[:] 
    sortbystarttime(sortedtasks)
    
    gminute = beforework # current minute
    day = 0 # current day
    minuteofday = 0 # minute of day
    finishedtasks = [] # store with info on how long it took
    currenttask = sortedtasks.pop(0)

    # repeat until all tasks are done
    while sortedtasks or currenttask:
        # adjust time if the current task is not matching it
        if gminute >= currenttask[0]:
            pass
        else:
            gminute = currenttask[0]
            taskdays =  math.floor(currenttask[0] / (noworktime + worktime))
            tasktimeleft = currenttask[0] % (noworktime + worktime)
            mindiff = tasktimeleft - (worktime - minuteofday)
            if mindiff < 0:
                minuteofday += tasktimeleft

            elif mindiff == 0:
                minuteofday = 0
                day += 1

            else: # > 0
                if mindiff >= worktime:
                    minuteofday = 0
                    day += 2

                else:
                    minuteofday = mindiff
                    day += 1

            day += taskdays



        start = [gminute, day, minuteofday] # save start time

        # calculate time task needs
        days = math.floor(currenttask[1] / worktime)
        minutes = currenttask[1] % worktime

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
                # set new minutes
                minutediff += worktime
                minutes = minutediff
                
                # set time
                minuteofday = minutes
                day += days
                # add to minutes
                gminute += days * (noworktime + worktime) + minutes + minutesleftofday

            # can't get minutes, no more day
            else:
                # TASK FINISHED
                # set time
                minuteofday += minutes
                # add to minutes
                gminute += minutes

        elif minutediff == 0:
            if days > 0:
                # set time
                day += days
                minuteofday = minutes

                # add to minutes
                gminute += days * (noworktime + worktime) + minutes
                

            else:
                # set time
                # time is set at the bottom
                # add to minutes
                gminute += minutes

        else:
            # > 0 either normal or by adding a day
            # subtract the remaining minutes of the day
            # then calculate, as the remaining minutes
            # can't be longer than a day
            minutes -= minutesleftofday
            # set time
            day += days + 1
            minuteofday = minutes 
            # add to minutes
            gminute += days * (noworktime + worktime) + minutes + noworktime

        end = [gminute, day, minuteofday]

        # store in list
        finishedtasks.append([currenttask[:], start[:], end[:], end[0] - currenttask[0]])

        # add 1 too days and set minute to zero again afterwards
        if minutediff == 0:
            day += 1
            minuteofday = 0

        # add new task
        if sortedtasks:
            currenttask = sortedtasks.pop(0)
        else:
            break

    return finishedtasks