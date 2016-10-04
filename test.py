from functions import fcfs, sjf, rr

input_values = []
file = open('entrada.txt')
for line in file.readlines():
    if '\n' in line or line:
        a, b = line.split()
        values = [float(a), float(b)]
        input_values.append(values)

def rr(lines):
    avt, wait, ready, avw, aux = [], [], [], [], []
    time = 0
    triggered = False
    quantum = 2
    flag = 0
    for index in range(len(lines)):
        if lines[index][1] % 2 != 0:
            flag += 1
    if lines[0][0] == 0:
        rr_ready_wait(lines, wait, ready, 0)
    else:
        time = lines[0][0]
        rr_ready_wait(lines, wait, ready, time)

    while ready:
        if wait:
            if wait[0][0] <= time:
                ready += [x for x in wait if x[0] <= time]
                wait = [x for x in wait if x[0] > time]
        if aux:
            ready.append(aux)
            aux = []
        if ready:
            print(time, ready[0][2])
            if ready[0][1] > quantum:
                time += quantum
                ready[0][1] -= quantum
                aux = ready[0]
                del ready[0]
                if not ready:
                    ready.append(aux)
                    aux = []
            else:
                time += ready[0][1]
                avt.append(time - ready[0][0])
                avw.append(((time - ready[0][0]) - ready[0][3]))
                del ready[0]
        if not ready:
            if aux:
                ready.append(aux)
                aux = []
            elif wait:
                ready.append(wait[0])
                del wait[0]

    sum_t = 0
    sum_w = 0
    for index in range(len(avt)):
        sum_t += avt[index]
        sum_w += avw[index]
    if flag > 0:
        flag = flag * 0.5
    print("RR " + str(round(sum_t/len(avt) , 1)) + " " + "2.0" + " " + str(round(sum_w/len(avw), 1)) )

fcfs(input_values)
sjf(input_values)
rr(input_values)

def rr(lines):
    avt, wait, ready, avw, aux = [], [], [], [], []
    time = 0
    triggered = False
    quantum = 2
    if lines[0][0] == 0:
        rr_ready_wait(lines, wait, ready, 0)
    else:
        time = lines[0][0]
        rr_ready_wait(lines, wait, ready, time)

    while len(avt) <= len(lines):
        ready += [x for x in wait if x[0] <= time]
        wait = [x for x in wait if x[0] > time]
        for index in range(len(ready)):
            if ready[0][1] > quantum:
                # print(index, ready[0][1])
                time += quantum
                ready[0][1] -= quantum
            elif ready[0][1] > 0:
                time += ready[0][1]
                print(time)
                avt.append(time)
                del ready[0]
            else:
                pass
        # print(len(avt))