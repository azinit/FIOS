import font

intA = 12
intB = 5
timeA = 64
timeB = 32
memA = 12
memB = 6

memory = [8, 8, 8, 8, 8, 8, 16, 16, 16, 32, 32]
processes = [[0] * len(memory)][0]
seq = []


worktime = 1
reqA = 0
reqB = 0
while True:
    print('Tact {}: {}'.format(font.beige + str(worktime) + font.end, seq))
    print('Processes : {}'.format(font.green + str(processes) + font.end))
    if (worktime-1) % intA == 0:
        for pos in range(0, len(memory)):
            if memory[pos] >= intA and processes[pos] == 0:
                processes[pos] = timeA
                break
        else:
            print()
            print(font.red2 + 'Error occured from A{}'.format(reqA+1) + font.end)
            exit()
        reqA += 1
        print(font.yellow + 'A: Request №{} for {} to {}'.format(reqA, worktime, worktime + timeA) + font.end)
        seq.append('A{}'.format(reqA))
    elif (worktime-1) % intB == 0:
        for pos in range(0, len(memory)):
            if memory[pos] >= intB and processes[pos] == 0:
                processes[pos] = timeB
                break
        else:
            print()
            print(font.red2 + 'Error occured from B{}'.format(reqB + 1) + font.end)
            exit()
        reqB += 1
        print(font.blue + 'B: Request №{} for {} to {}'.format(reqB, worktime, worktime + timeB) + font.end)
        seq.append('B{}'.format(reqB))

    for i in range(0, len(processes)):
        processes[i] = processes[i] - 1 if processes[i] > 0 else processes[i]

    worktime += 1
