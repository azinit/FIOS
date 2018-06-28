with open('input.txt', 'r') as fin:
    n = int(fin.readline())
    strs = []
    for line in fin:
        strs.append(line.rstrip())

# print(n, strs)

nums = []
for num in strs:
    cell = str(ord(num[0])) + '.' + num[1:3:] + '.' + str(ord(num[3])) + '.' + num[4:6:] + '.' + str(ord(num[6]))
    nums.append(cell)

# print(nums)
result = ''
for i in range(0, n):
    if str(nums[i]).find('??') > -1:
        if i == 0:
            k = '00'
        else:
            for j in range(5):
                if j != 1:
                    a = int(nums[i-1].split('.')[j])
                    b = int(nums[i].split('.')[j])
                    if j == 0 and a < b:
                        k = '00'
                        break
                    else:
                        if a < b:
                            k = (strs[i - 1][1:3:])
                            break
            else:
                k = int(strs[i-1][1:3:]) + 1
                k = '0' + str(k) if k < 10 else str(k)
        nums[i] = str(nums[i]).replace('??', k)
        strs[i] = str(strs[i]).replace('??', k)
    else:
        if i != 0 and strs[i] == strs[i-1]:
            result = 'NO'
if not result:
    temp = 'YES' + '\n'
    for i in strs:
        temp += i + '\n'
    temp = temp[:len(temp)-1:]
    result = temp

with open('output.txt', 'w') as fout:
    fout.write(result)