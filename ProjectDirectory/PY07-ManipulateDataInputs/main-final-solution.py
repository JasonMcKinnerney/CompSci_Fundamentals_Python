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


def display_panets(planets):
    print("{:>10}{:>10}{:>15}{:>15}{:>15}".format("planet","status","nearest","furthest","avererage",))
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

def load_planets(planets):
    #pf = open(PLANETS_FILE1,"r")
    pf = open(PLANETS_FILE2,"r")
    for line in pf:
        line = line[:-1]
        if len(line):
            line = line.split(",")
            planets[line[0]] = [int(line[1]), int(line[2]), int(line[3])]
    pf.close()

def load_status(planets, stat):
    #sf = open(STATUS_FILE1,"r")
    sf = open(STATUS_FILE2,"r")
    temp = {}
    for line in sf:
        line = line[:-1]
        if len(line):
            line = line.split(",")
            if line[1] == "True":
                temp[line[0]] = True
            else:
                temp[line[0]] = False
    sf.close()
    for planet in planets:
        stat.append(temp[planet])

def cap_every_other(instr):
    outstr = ""
    i = 0
    instr = instr.lower()
    for ch in instr:
        if i%2:
            outstr += ch.upper()
        else:
            outstr += ch
        i += 1
    return outstr

def save_planets(planets):
    po = open(OUTPUT_FILE,"w")
    for planet in planets:
        line = cap_every_other(planet) + "," + str(planets[planet][0]) + "," + str(planets[planet][1]) + "," + str(planets[planet][2]) + "," + planets[planet][3] + "\n"
        po.write(line)
    po.close()

def main():
    
    sol = {}
    status = []
    load_planets(sol)
    load_status(sol, status)

    # do not alter anything between here...
    # ##################################
    print()
    print("The closest by nearest distance is:", closest(sol))
    print("The closest by furthest distance is:", closest(sol, False))
    print("The furthest by nearest distance is:", furthest(sol, False))
    print("The furthest by furthest distance is:", furthest(sol))
    print("The list of all planets is:", planets_list(sol, status))
    print()
    convert_millions(sol)
    mark_planets(sol, status)
    display_panets(sol)
    # ... and here
    # ##################################
    save_planets(sol)
    
main()
