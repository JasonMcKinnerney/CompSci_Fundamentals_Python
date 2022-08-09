from typing import Any

MILLION = 1000000
PLANETS_FILE1 = "planets1.dat"
STATUS_FILE1 = "status1.dat"
PLANETS_FILE2 = "planets2.dat"
STATUS_FILE2 = "status2.dat"
OUTPUT_FILE = "planets_out.dat"

def convert_millions(planets):
    for planet in planets:
        length = len(planets[planet])
        for i in range(length):
            planets[planet][i] *= MILLION


def mark_planets(planets, stat):
    idx = 0
    for planet in planets:
        if stat[idx]:
            planets[planet].append("planet")
        else:
            planets[planet].append("dwarf")
        idx += 1


def display_planets(planets):
    print("{:>10}{:>10}{:>15}{:>15}{:>15}".format("planet","status","nearest","furthest","average",))
    print("-----------------------------------------------------------------")
    for planet in planets:
        length = len(planets[planet]) - 1
        print("{:>10}{:>10}".format(planet, planets[planet][length]), end="")
        for i in range(length):
            print("{:>15,}".format(planets[planet][i]), end="")
        print()
    print()


def planets_list(planets, stat):
    pl = []
    idx = 0
    for planet in planets:
        if stat[idx]:
            pl.append(planet)
        idx += 1
    return pl


def furthest(planets, greatest=True):
    idx = 1 if greatest else 0 
    maximum = 0
    for planet in planets:
        if planets[planet][idx] > maximum:
            far = planet
            maximum = planets[planet][idx]
    return far


def closest(planets, least=True):
    idx = 0 if least else 1
    minimum = planets[list(planets)[0]][idx]
    close = list(planets)[0]
    for planet in planets:
        if planets[planet][idx] < minimum:
            close = planet
            minimum = planets[planet][idx]
    return close

def load_planets(sol):
    with open(PLANETS_FILE1, "r") as f:
        for line in f:
            line = line.rstrip('\n')
            if len(line) > 0:
                li = line.split(',')
                sol[li[0]] = li[1:]
    for planet in sol:
        for i in range(len(sol[planet])):
            sol[planet][i] = int(sol[planet][i])

def load_status(sol, status):
    with open(STATUS_FILE1, "r") as s:
        temp = {}
        for line in s:
            line = line.rstrip('\n')
            if len(line) > 0:
                k, v = line.split(',')
                if v == 'True':
                    temp[k] = True
                else:
                    temp[k] = False
        for key in sol:
            status.append(temp[key])

def cap_every_other(string):
    ret = ''
    i = True
    for char in string:
        if i:
            ret += char.lower()
        else:
            ret += char.upper()
        if char != ' ':
            i = not i
    return ret


def save_planets(sol):
    with open(OUTPUT_FILE, "w") as s:
        for planet in sol:
            for i in range(len(sol[planet])):
                sol[planet][i] = str(sol[planet][i])
        for k, v in sol.items():
            i = cap_every_other(k)
            s.write(f"{i},{','.join(v)}\n")
# CODE HERE
# ###################################################
# write the definition for load_planets()C
# write the definition for load_status()C
# write the definition for cap_every_other()
# write the definition for save_planets(()
# ###################################################


def main():
    
    sol = {}
    status = []
    load_planets(sol)
    load_status(sol, status)

    # #######################
    # create an empty dictionary called sol
    # create an empty list called status
    # call load_planets() and pass it sol
    # call load_status() and pass it sol and status
    # #######################
    
    # at this point, you should be in the same state you were in when the
    # sol dictionary and status list was given to you in previous assignments
    
    # ##################################
    # do not alter anything between here...
    print()
    print("The closest by nearest distance is:", closest(sol))
    print("The closest by furthest distance is:", closest(sol, False))
    print("The furthest by nearest distance is:", furthest(sol, False))
    print("The furthest by furthest distance is:", furthest(sol))
    print("The list of all planets is:", planets_list(sol, status))
    print()
    convert_millions(sol)
    mark_planets(sol, status)
    display_planets(sol)
    # ... and here
    # ##################################

    save_planets(sol)

    # #######################
    
main()
