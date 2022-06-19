import re
import numpy as np

n = int(input())
b = str(input())
arr = []
a = ''
if 1 <= n <= 100:
        a = re.findall("[A-Za-z]{2}",b)
        for i in a:
            if i == 'FS':
                arr.append(1)
            elif i == 'SF':
                arr.append(1)
            else:
                arr.append(0)

print(arr)
if not np.any(arr):
    print("NO")
else:
    print("YES")

