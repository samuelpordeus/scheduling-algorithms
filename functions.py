input_values = []
file = open('entrada.txt')
for line in file.readlines():
    if '\n' in line or line:
        a, b = line.split()
        values = [float(a), float(b)]
        input_values.append(values)


def average_wait_time(lines):
    awt, at = 0, 0
    wt = lines[0][0]
    for index in range(1, len(lines)):
        at = lines[index][0]
        wt += lines[index - 1][1]
        # print(wt)
        awt += wt - at
    return (awt / len(lines))


def average_turnaround_time(lines):
    at, bt, ct = 0, 0, 0
    wt = lines[0][0]
    att = (lines[0][1] + lines[0][0]) - lines[0][0]
    for index in range(1, len(lines)):
        wt += lines[index - 1][1]
        at = lines[index][0]
        bt = lines[index][1]
        ct = wt + bt
        tt = ct - at
        att += tt
    return (att / len(lines))


def average_response_time(lines):
    awt, at = 0, 0
    wt = lines[0][0]
    for index in range(1, len(lines)):
        at = lines[index][0]
        wt += (lines[index - 1][1])
        awt += wt - at
    return (awt / len(lines))


def average_response_time_rr(lines):
    flag = True
    for index in range(0, len(lines)):
        if lines[index][2] > 0:
            flag = False
    if flag:
        return 2.0
    return 2.0


def average_time(jobs_list, name):
    awt = average_wait_time(jobs_list)
    att = average_turnaround_time(jobs_list)
    if name == 'RR':
        art = average_response_time_rr(jobs_list)
    else:
        art = average_response_time(jobs_list)
    print(name + " " + str(round(att, 1)) + " " +
          str(round(art, 1)) + " " + str(round(awt, 1)))


def sjf(lines):
    time = 0
    process = []
    jobs = sorted(lines, key=lambda jobs: (jobs[0], jobs[1]))
    while jobs:
        if time >= jobs[0][0]:
            process.append(jobs[0])
            time += jobs[0][1]
            del jobs[0]
            if jobs:
                jobs.sort(key=lambda jobs: jobs[1])
        else:
            time += 1
    average_time(process, 'SJF')


def fcfs(lines):
    jobs = sorted(lines, key=lambda lines: lines[0])
    average_time(jobs, 'FCFS')


def realocate(wait, ready, lines, time):
    for index in range(len(lines)):
        if lines[index][0] <= time:
            ready.append(lines[index])
        else:
            wait.append(lines[index])


def rr_turnaround_time(avt):
    avg = 0
    for index in range(len(avt)):
        avg += avt[index]
    print(round(avg / len(avt), 1))


def rr_debug_aux(lines):
    for index in range(len(lines)):
        lines[index].append(int(index))
        lines[index].append(0)


def rr_ready_wait(lines, wait, ready, time):
    for index in range(len(lines)):
        lines[index].append(lines[index][1])
        if lines[index][0] <= time:
            ready.append(lines[index])
        else:
            wait.append(lines[index])


def rr(lines):
    avt, wait, ready, avw, aux = [], [], [], [], []
    time = 0
    triggered = False
    quantum = 2
    sum_t, sum_w = 0, 0
    if lines[0][0] == 0:
        rr_ready_wait(lines, wait, ready, 0)
    else:
        time = lines[0][0]
        rr_ready_wait(lines, wait, ready, time)
    while len(avt) < len(lines):
        ready += [x for x in wait if x[0] <= time]
        wait = [x for x in wait if x[0] > time]
        if aux:
            ready.append(aux)
            aux = []
        if ready:
            if ready[0][2] > quantum:
                ready[0][2] -= quantum
                time += quantum
                aux = ready[0]
                del ready[0]
            else:
                time += ready[0][2]
                avt.append(time - ready[0][0])
                avw.append((time - ready[0][0]) - ready[0][1])
                del ready[0]
    for index in range(len(avt)):
        sum_t += avt[index]
    for index in range(len(avt)):
        sum_w += avw[index]

    print(round(avg/len(avt), 1))
fcfs(input_values)
sjf(input_values)
rr(input_values)