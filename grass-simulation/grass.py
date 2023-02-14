import os
import random


# Set of grass tiles
grass = set()
grass.add((0, 0))


def print_grass():
    bounds = 40
    land = []
    for y in range(-bounds, bounds):
        row = ""
        for x in range(-bounds, bounds):
            if (x, y) in grass:
                row += "g "
            else:
                row += ". "
        land.append(row)
    os.system('clear')
    for row in land:
        print(row)

N = 0
E = 1
S = 2
W = 3

def simulate_grass():
    global grass
    new_grass = set()
    for blade in grass:
        # choose random direction N E S W, which corresponds to 0 1 2 3        
        direction = random.randrange(4)
        if direction == N:
            new_position = (blade[0], blade[1] - 1)
        elif direction == E:
            new_position = (blade[0] + 1, blade[1])
        elif direction == S:
            new_position = (blade[0], blade[1] + 1)
        elif direction == W:
            new_position = (blade[0] - 1, blade[1])
        new_grass.add(new_position)
    grass.update(new_grass)


while True:
    print_grass()
    simulate_grass()
    input("Press enter to continue..")