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
    return (awt / len(lines)) - 1

# 0 + 20 + 30 + 32 + 38 + 42 + 50

def average_response_time(lines):
    awt, at = 0, 0
    wt = lines[0][0]
    for index in range(1, len(lines)):
        at = lines[index][0]
        wt += (lines[index - 1][1])
        awt += wt - at
    return (awt / len(lines)) - 1


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
    return (att / len(lines)) - 1


def average_time(jobs_list, name):
    awt = average_wait_time(jobs_list)
    art = average_response_time(jobs_list)
    att = average_turnaround_time(jobs_list)
    print(name + " " + str(round(att, 1)) + " " +
          str(round(art, 1)) + " " + str(round(awt, 1)))


def sjf(lines):
    total_time = 0
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
            jobs.sort(key=lambda jobs:jobs[0])
            time += 1
    average_time(process, 'SJF')


def fcfs(lines):
    jobs = sorted(lines, key=lambda lines: lines[0])
    average_time(jobs, 'FCFS')


def rr(lines):
    jobs = sorted(lines, key=lambda lines: lines[1] if lines[1] >= 2 else lines[0])
    average_time(jobs, 'RR')

fcfs(input_values)
sjf(input_values)
rr(input_values)