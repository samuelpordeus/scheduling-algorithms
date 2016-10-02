from functions import fcfs, sjf, rr

input_values = []
file = open('entrada.txt')
for line in file.readlines():
    if '\n' in line or line:
        a, b = line.split()
        values = [float(a), float(b)]
        input_values.append(values)
fcfs(input_values)
sjf(input_values)
rr(input_values)
