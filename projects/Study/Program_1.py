def to_sec(time):
    hh, mm, ss = time[0]+time[1], time[3]+time[4], time[6]+time[7]
    hh, mm, ss = int(hh), int(mm), int(ss)
    total = hh*3600 + mm*60 + ss
    return total

def to_hms(sec):
    h, m, s = sec//3600, sec % 3600 //60, sec % 60
    h = str(h) if h >= 10 else '0' + str(h)
    m = str(m) if m >= 10 else '0' + str(m)
    s = str(s) if s >= 10 else '0' + str(s)
    return h + ':' + m + ':' + s

with open('input.txt', 'r') as fin:
    inp = fin.readline()
time = to_sec(inp)
if time == 0:
    result = '23:30:00'
else:
    a, b = time // 1800, time / 1800
    ctime = (a-1)*1800 if a == b else a*1800
    result = to_hms(ctime)

with open('output.txt', 'w') as fout:
    fout.write(result)
