# Velocity [bit/sec]
V = 512
# Block volume [bit]
V0 = 2048
# Service data volume [bit]
d = 12
# Service data difference [bit]
dd = 13
# File volume [Kb]
file = 64
# Petya time [sec]
tp = 1079
# Vasya time [sec]
tv = 1061

file *= 1024*8
am = file // V0

difVolume = V*((V0 + d + dd)*tp - (V0 + d)*tv)
k = (V0 + d)*(V0 + d + dd)
# N1 = difVolume / k
N1 = 6
N2 = 6
# N2 = ((V0 + d)*N1 - (V*(tp-tv)+am*dd))/dd
print('N1: %s' % N1)
print('Check: t = ()*() ?')
print((V0+d)*(am+N1+N2) / V)
print(tp)
print((V0+d + dd)*(am + N2) / V)
print(tv)