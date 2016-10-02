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
        awt += wt - at
    return awt / len(lines)


def average_response_time(lines):
    awt, at = 0, 0
    wt = lines[0][0]
    for index in range(1, len(lines)):
        at = lines[index][0]
        wt += (lines[index - 1][1])
        awt += wt - at
    return awt / len(lines)


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
    return att / len(lines)


def average_time(jobs_list, name):
    awt = average_wait_time(jobs_list)
    art = average_response_time(jobs_list)
    att = average_turnaround_time(jobs_list)
    print(name + " " + str(round(att, 1)) + " " +
          str(round(art, 1)) + " " + str(round(awt, 1)))

def sjf(lines):
    jobs = sorted(lines, key=lambda lines: lines[0])
    for index in range(0, len(jobs)):
        ct = (jobs[index][1] + jobs[index][0])
        jobs[index].append(ct)
    jobs = sorted(jobs, key=lambda jobs: jobs[2])
    for index in range(0, len(jobs)):
        del jobs[index][2]
    average_time(jobs, 'SJF')


def fcfs(lines):
    jobs = sorted(lines, key=lambda lines: lines[0])
    average_time(jobs, 'FCFS')


def rr(lines):
    jobs = sorted(lines, key=lambda lines: lines[1] if lines[1] <= 2 else lines[0])
    average_time(jobs, 'RR')

fcfs(input_values)
sjf(input_values)
rr(input_values)
