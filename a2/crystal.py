# Note: the random module does not generate true random numbers
# but they should be sufficient for this program
from random import randint
import random

def printarr(arr):
    for i in arr:
        print(i)
        
def makeoptions(
        sizeoffield : list, # x,y both inclusive
        maxtimeoffset : int, # in ticks 
        mingrowth : int, # growth per tick 
        maxgrowth: int
    ):

    return {
        "sizeoffield": sizeoffield,
        "maxtimeoffset": maxtimeoffset,
        "mingrowth": mingrowth,
        "maxgrowth": maxgrowth,
    }


# crystal class
class Crystal:
    def __init__(self, id, options) -> None:
        self.id = id

        self.position = [
            randint(0, options["sizeoffield"][0]), 
            randint(0, options["sizeoffield"][1])
        ] # x,y

        # tick when to start
        self.starttime = randint(0, options["maxtimeoffset"])

        # top, right, bottom, left
        self.growthfactors =  [
            randint(options["mingrowth"], options["maxgrowth"]),
            randint(options["mingrowth"], options["maxgrowth"]),
            randint(options["mingrowth"], options["maxgrowth"]),
            randint(options["mingrowth"], options["maxgrowth"])
        ]

        # simulate growing
        self.tick = None
        self.middle = None
        self.form = None
        self.formmarks = None

    def applytick(self, tick):
        # if tick < 1: return # only apply ticks bigger than 0

        if tick - self.starttime < 0:
            return False

        self.tick = tick - self.starttime
        tick -= self.starttime
        self.middle = [self.growthfactors[3] * self.tick, self.growthfactors[0] * tick] # left and top times tickcount
        
        # get widths
        xwidth = self.growthfactors[1] * self.tick + self.growthfactors[3] * self.tick + 1
        ywidth = self.growthfactors[0] * self.tick + self.growthfactors[2] * self.tick + 1

        self.xwidth = xwidth
        self.ywidth = ywidth

        # generate form
        self.form = []
        self.formmarks = []
        for i in range(ywidth):
            self.form.append([])
            self.formmarks.append([])
            for j in range(xwidth):
                self.form[i].append(-1)
                self.formmarks[i].append(True)

        # set middle to zero
        self.form[self.middle[1]][self.middle[0]] = 0 # access with y, x

        sharpness = 0 # makes it more slim
        threshhold = max([
            self.growthfactors[0] * self.growthfactors[1] * self.tick ** 2,
            self.growthfactors[1] * self.growthfactors[2] * self.tick ** 2,
            self.growthfactors[2] * self.growthfactors[3] * self.tick ** 2,
            self.growthfactors[3] * self.growthfactors[0] * self.tick ** 2,
        ]) // ((tick + sharpness ** 2) if (tick + sharpness ** 2) > 0 else 1) 

        # print(threshhold)
        
        adjust = 0 # offset middle values off the cordinate cross, not really useful
        # maybe somehow alter it to make crystals more interesting

        for i in range(ywidth):
            for j in range(xwidth):
                vec = [abs(j - self.middle[0]), abs(i - self.middle[1])]
                if (vec[0] == 0 and vec[1] != 0):
                    self.form[i][j] = vec[1] - adjust if vec[1] - adjust > 0 else 1
                elif (vec[0] != 0 and vec[1] == 0):
                    self.form[i][j] = vec[0] - adjust if vec[0] - adjust > 0 else 1
                else:
                    self.form[i][j] = vec[0] * vec[1]
                
                if self.form[i][j] >= threshhold :
                    if self.form[i][j] < 2:
                        continue
                    self.formmarks[i][j] = False 
        

        # print(xwidth, ywidth)
        # printarr(self.form)
        # printarr(self.formmarks)
        # self.printself(self.formmarks)
        return True
    
    def printself(self, arr):
        for i in arr:
            for j in i:
                if j:
                    print("O", end="")
                else:
                    print(" ", end="")
            print("")