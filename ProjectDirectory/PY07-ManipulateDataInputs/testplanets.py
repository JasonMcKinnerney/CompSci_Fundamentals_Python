MILLION = 1000000
PLANETS_FILE1 = "planets1.dat"
STATUS_FILE1 = "status1.dat"
PLANETS_FILE2 = "planets2.dat"
STATUS_FILE2 = "status2.dat"
OUTPUT_FILE = "planets_outTEST.dat"
sol = {}
status = []

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
    print(sol)







def load_status(sol, status):
    with open(STATUS_FILE1, "r") as s:
        for line in s:
            line = line.rstrip('\n')
            if len(line) > 0:
                k, v = line.split(',')
                if k in sol:
                    sol[k].append(v)
    for key in sol:
        status.append(sol[key][3])
    for k, v in sol.items():
        v.pop()
    idx = 0
    while idx < len(status):
        if status[idx] == 'True':
            status[idx] = True
        else:
            status[idx] = False
        idx +=1

def load_status(sol, status):
    with open(STATUS_FILE1, "r") as s:
        temp = {}
        for line in s:
            line = line.rstrip('\n')
            k, v = line.split(',')
            if v == 'True':
                temp[k] = True
            else:
                temp[k] = False
        for key in sol:
            status.append(temp[key])
        print(status)







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



load_planets(sol)
#load_status(sol, status)

statustest(sol, status)
print(status)
print(sol)
#save_planets(sol)