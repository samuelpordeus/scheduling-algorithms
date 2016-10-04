from functions import fcfs, sjf, rr

input_values = []
file = open('entrada.txt')
for line in file.readlines():
    if '\n' in line or line:
        a, b = line.split()
        values = [float(a), float(b)]
        input_values.append(values)


def rr(lines):
    original = lines
    aux, ready, wait, avt, avw = [], [], [], [], []
    time = 0
    quantum = 2
    triggered = False
    index_aux = 0
    # rr_debug_aux(lines)
    for index in range(len(lines)):
        avw.append(0)
    for index in range(len(lines)):
        lines[index].append(index)
    if lines[0][0] != time:
        time = lines[0][0]
    for index in range(len(lines)):
        if lines[index][0] <= time:
            ready.append(lines[index])
        else:
            wait.append(lines[index])
    while ready:
        for index in range(len(wait)):
            if wait[index][0] <= time:
                if len(ready) > 1:
                    ready.insert(len(ready), wait[index])
                else:
                    ready.append(wait[index])
        wait = [x for x in wait if x[0] > time]


        if aux:
            ready.append(aux)
            aux = []
        print(ready[0][2], time)

        if ready[0][1] > quantum:
            time += quantum
            ready[0][1] -= quantum
            aux = ready[0]
            index_aux = ready[0][2]
            del ready[0]
        else:
            index_aux = ready[0][2]
            time += ready[0][1]
            triggered = True
            if len(ready[0]) > 3:
                avt.append((time - ready[0][2]))
                tt - bt - at
            else:
                avt.append((time - ready[0][0]))
                avw.append((time - avt.append))
            # print(time)
        if triggered:
            avw[index_aux] = (time - original[index_aux][1])
            avw.sort(key = lambda avw: avw)
            del ready[0]
            triggered = False
        if not ready:
            if aux:
                ready.append(aux)
                aux = []
            elif wait:
                ready.append(wait[0])
                del wait[0]

    rr_turnaround_time(avt)
    print(avt)
    print(avw)