with open('input.txt', 'r') as fin:
    n, m, k = list(map(int, fin.readline().split()))
    limit = m
    reqL, reqR, b = [], [], [x for x in range(n)]
    for line in fin:
        reqL.append(int(line.split()[0]))
        reqR.append(int(line.split()[1]))



    reqL, reqR, b = zip(*sorted(zip(reqL, reqR, b)))
    reqL, reqR, b= list(reqL), list(reqR), list(b)
    print(reqL)
    print(reqR)
    print(b)

places = [0]*n
for i in range(1, n+1):
    for j in reqL:
        if j == i:
            for q in range(n):
                if n[q] == 0:
                    pass

