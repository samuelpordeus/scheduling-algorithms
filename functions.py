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
    if flag == True:
        return 2.0
    return 2.0

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


def average_time(jobs_list, name):
    awt = average_wait_time(jobs_list)
    att = average_turnaround_time(jobs_list)
    if name == 'RR':
        art = average_response_time_rr(jobs_list)
    else:
        art = average_response_time(jobs_list)
    print(name + " " + str(round(att, 1)) + " " + str(round(art, 1)) + " " + str(round(awt, 1)))


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
            # jobs.sort(key=lambda jobs: jobs[0])
            time += 1
    average_time(process, 'SJF')


def fcfs(lines):
    jobs = sorted(lines, key=lambda lines: lines[0])
    average_time(jobs, 'FCFS')


def rr(lines):
    process = []
    jobs = sorted(lines, key=lambda jobs: (jobs[0]))
    for index in range(len(jobs)):
        jobs[index].append(2.0)
        jobs[index][2] -= jobs[index][1]
    jobs = sorted(lines, key=lambda jobs: jobs[2] if jobs[2] > 0 else jobs[0])
    # print(jobs)
    while jobs:
        jobs[0][2] -= jobs[0][1]
        if jobs[0][2] > 0:
            process.append(jobs[0])
            print(process)
            del jobs[0]
        else:
            process.append(jobs[0])
            break
    average_time(jobs, 'RR')

fcfs(input_values)
sjf(input_values)
rr(input_values)
