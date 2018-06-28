with open('input.txt', 'r') as fin:
    n, M, l, b = list(map(int, fin.readline().split()))
    X = [-l] + list(map(int, fin.readline().split())) + [M]
    X.sort()

# print(n, M, l, b)
# print(X)

result = 0
for i in range(0, n+1):
    # print(X[i+1], X[i])
    c = X[i+1] - X[i] - l - 2*b
    result = max(result, c)

with open('output.txt', 'w') as fout:
    fout.write(str(result))
