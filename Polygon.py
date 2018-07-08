import os

import convert
import sample
import read

mpath = sample.main_path
filepath = os.path.join(mpath, "input.txt")
print(convert.to_interval("1-5", str))  # Output [1, 2, 3, 4, 5]
print(convert.to_interval("5-2", int))  # Output [2, 3, 4, 5]
print(convert.to_interval("13-25", float))    # Output [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

print(str(type([123, 123])))