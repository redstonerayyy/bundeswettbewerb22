# generate images
from PIL import Image
import sys

# Note: the random module does not generate true random numbers
# but they should be sufficient for this program
from random import randint
import random
from crystal import Crystal, checkiffilled, printarr, makeoptions
from merge import mergecrystaltofield, emptyfield

# random.seed(10)

# main code

# python a2.py {amount} {xsize} {ysize} {offset} {mingrowth} {maxgrowth}
# python a2.py 2 20 20 0 2 10


# config
# not this amount will grown, 
# it will generate as many crystal origins which can be denied by
# other crystals

# get input with sys.argv
amountofc = 20
xsize = 200
ysize = 200
timeoffset = 4
mingrow = 1
maxgrow = 4
try:
    if sys.argv[1]:
        amountofc = int(sys.argv[1])

    if sys.argv[2]:
        xsize = int(sys.argv[2])

    if sys.argv[3]:
        ysize = int(sys.argv[3])

    if sys.argv[4]:
        timeoffset = int(sys.argv[4])

    if sys.argv[5]:
        mingrow = int(sys.argv[5])

    if sys.argv[6]:
        maxgrow = int(sys.argv[6])

except IndexError:
    pass

# make options
options = makeoptions([xsize - 1, ysize - 1], timeoffset, mingrow, maxgrow) # -1 because it is inclusive


# generate crystals
crystals = []

for i in range(amountofc):
    crystals.append(Crystal(i, options))

# perform growth for each tick and check when field is full
tick = 0
while True:
    field = emptyfield(ysize, xsize)
    for crystal in crystals:
        if crystal.applytick(tick): # if it generated something we can merge it
            field = mergecrystaltofield(field, crystal)

    if checkiffilled(field):
        break
    
    tick += 1


# polish field
for row in field:
    for i in range(len(row)):
        # sort and filter
        if len(row[i]) > 1:
            row[i].sort(key=lambda x: x[1])
            # first element has smallest strenth value
            row[i] = row[i][0][0]
        else:
            row[i] = row[i][0][0]


print(tick)
# generate image













colors = {}
for i in range(amountofc):
    colors[i] = randint(0, 255) 

data = []

for i in range(len(field)):
    for j in range(len(field[i])):
        data.append(colors[field[i][j]])

img = Image.new('L', (xsize, ysize))
img.putdata(data)
img.save('grayscale.png')