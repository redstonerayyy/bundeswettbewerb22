# generate images
from PIL import Image

# Note: the random module does not generate true random numbers
# but they should be sufficient for this program
from random import randint
import random
from crystal import Crystal, printarr, makeoptions
from merge import mergecrystaltofield

random.seed(10)

# main code

# config
amountofc = 5 
# not this amount will grown, 
# it will generate as many crystal origins which can be denied by
# other crystals
xsize = 40
ysize = 40

# generate field
field = []

for i in range(ysize):
    field.append([])
    for j in range(xsize):
        field[i].append([])

printarr(field)


options = makeoptions([xsize - 1, ysize - 1], 5, 3, 10) # -1 because it is inclusive

crystals = []

for i in range(amountofc):
    crystals.append(Crystal(i, options))

for crystal in crystals:
    if crystal.applytick(5): # if it generated something we can merge it
        field = mergecrystaltofield(field, crystal)
















# width = 20
# height = 20
# data = []

# def getpix():
#     return randint(0, 255)

# for i in range(width * height):
#     data.append((getpix(), getpix(), getpix()))

# img = Image.new('RGB', (width, height))
# img.putdata(data)
# img.save('image.png')