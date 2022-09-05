from crystal import Crystal

# works on the reference passed to it
def mergecrystaltofield(field : list, crystal : Crystal):
    offset = [
        crystal.position[0] - crystal.middle[0],
        crystal.position[1] - crystal.middle[0]
    ]

    for y in range(len(crystal.form)):
        for x in range(len(crystal.form[0])):
            try:
                # prevent negative indices
                if (y + offset[1] < 0) or (x + offset[0] < 0):
                    raise IndexError("raised to prevent adding to end of list")

                if crystal.formmarks[y][x]:
                    field[y + offset[1]][x + offset[0]].append([crystal.id, crystal.form[y][x]])
            
            except IndexError:
                pass
    
    return field

def emptyfield(ysiz, xsiz):
    # generate field
    field = []

    for y in range(ysiz):
        field.append([])
        for x in range(xsiz):
            field[y].append([])

    return field