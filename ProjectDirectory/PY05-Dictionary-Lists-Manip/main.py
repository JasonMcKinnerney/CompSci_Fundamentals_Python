########################################
#Name: Jason McKinnerney
#Coding 07
#Passing by Reference - Using notes from last assignment, build 3 functions to create
#an organized and correct graph
########################################
MILLION = 1000000
#write a function called planets_list()
# pass it the planets dictionary and status list
# return the list of planets that are true planets
# base on the status list
#
# you may NOT use python methods; min, max, sum, or mean
# you must use a loop to do this
def planets_list(planets, stat):
    pl = []
    idx = 0
    for planet in planets:
        if stat[idx]:
            pl.append(planet)
        idx += 1
    return pl


# write a function called furthest()
# pass it the planets dictionary and an OPTIONAL boolean flag
# the flag decides if you use the CLOSEST distance or the FURTHEST
# distance to decide which planet is furthest
# in other words, use index 0 or 1 from the distance lists
# return the name of the furthest planet
#
# you may not use python methods; min, max, sum, or mean
# you must use a loop
def furthest(planets, greatest=True):
    idx = 1 if greatest else 0
    maximum = 0
    for planet in planets:
        if planets[planet][idx] > maximum:
            far = planet
            maximum = planets[planet][idx]
    return far


# write a function called closest()
# pass it the planets dictionary and an OPTIONAL boolean flag
# the flag decides if you use the CLOSEST distance or the FURTHEST
# distance to decide which planet is closest
# in other words, use index 0 or 1 from the distance lists
# return the name of the closest planet
#
# you may not use python methods; min, max, sum, or mean
# you must use a loop
def closest(planets, least=True):
    idx = 0 if least else 1
    minimum = planets[list(planets)[0]][idx]
    for planet in planets:
        if planets[planet][idx] < minimum:
            close = planet
            minimum = planets[planet][idx]
    return close


def convert_millions(sol):
    for planet in sol:
        for i in range(len(sol[planet])):
            sol[planet][i] *= MILLION


def mark_planets(planets, stat):
    idx = 0
    for planet in planets:
        if stat[idx]:
            planets[planet].append("Planet")
            idx += 1
        else:
            planets[planet].append("Dwarf")
            idx += 1


def display_planets(sol):
    print("{:>10} {:>10} {:>15} {:>15} {:>15}".format("planet", "status", "nearest", "furthest", "average"))
    print("{:-^69s}".format("-"))
    for planet in sol:
        print("{:>10} {:>10} {:>15,} {:>15,} {:>15,}".format(planet, sol[planet][3], sol[planet][0], sol[planet][1],sol[planet][2]))




def main():
    # do not modify this function except while coding to help you figure
    # out the functions you are writing. before you submit, main() must be
    # returned to exactly this state or the assignment is an automatic 0

    sol = {"Uranus": [2750, 3000, 2880], "Mercury": [46, 70, 57], "Earth": [147, 152, 150], "Venus": [107, 109, 108],
           "Mars": [205, 249, 228], "Saturn": [1350, 1510, 1430], "Jupiter": [741, 817, 779],
           "Pluto": [4440, 7380, 5910], "Neptune": [4450, 4550, 4500]}
    status = [True, True, True, True, True, True, True, False, True]
    # note that the "arrays" above are what are known as "parallel arrays"
    # this means that have values that relate to each other. The first "True"
    # in status relates to "Uranus" in sol. The second "True" to "Mercury", etc.

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


main()
