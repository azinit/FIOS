n, X, P = int(input()), 0, 0
a = [int(input()) for i in range(n)]
a.sort(reverse=True)
for i in range(n):
    if a[i] % 26 == 0:
        P = i
        break

for i in range(0, n-1):
    if i > P:
        break
    elif a[i] % 26 == 0:
        X = max(X, a[i]*a[i-1]) if i != 0 else max(X, a[0]*a[1])
        continue
    elif a[i] % 13 == 0:
        k = 2
    elif a[i] % 2 == 0:
        k = 13
    else:
        k = 26

    for j in range(n):
        if a[j] % k == 0 and i != j:
            X = max(X, a[i]*a[j])
            break

print(X)