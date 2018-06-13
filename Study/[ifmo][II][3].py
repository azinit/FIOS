import read

path = "E:\Work\FIRI\FIOS\Study\ifmo_3.txt"
content = read.from_file(path).split('\r\n')
content[0] = content[0][1::]
content = list(map(lambda x: str(x).split(), content.copy()))

seq = list(map(lambda x: int(x[0]), content))
names = list(map(lambda x: x[1], content))
disp = list(map(lambda x: int(x[2])*int(x[3]) % 11, content))
result = []
c = 0

print(disp)
print()
print()
# print(seq)
# print(names)

while c != 2:
    result.append(seq[0])
    displace = disp[seq[0] - 1]
    # displace = 10
    print('{}. {} - Displace: {}'.format(seq[0], names[seq[0]-1], displace))
    print(seq)
    c = c + 1 if seq[0] == 1 else c
    for i in range(0, 11):
        seq[i] -= displace
        seq[i] = seq[i] if seq[i] > 0 else seq[i] + 11
    #    print(seq)
    input()

print(result)