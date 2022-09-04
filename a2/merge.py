from crystal import Crystal

# works on the reference passed to it
def mergecrystaltofield(field : list, crystal : Crystal):
    offset = [
        crystal.position[0] - crystal.middle[0],
        crystal.position[1] - crystal.middle[0]
    ]

    print(crystal.position[0], crystal.middle[0])
    print(crystal.position[1], crystal.middle[1])
    print(offset)

    for y in range(len(crystal.form)):
        for x in range(len(crystal.form[0])):
            try:
                field[y + offset[1]][x + offset[0]].append([crystal.id, crystal.form[y][x]])
            except IndexError:
                pass
    
    return field