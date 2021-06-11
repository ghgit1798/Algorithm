import sys
N = int(sys.stdin.readline().rstrip())

data = list(map(str, sys.stdin.readline().split()))

x,y = 1,1

for i in range(len(data)):
    direct = data[i]

    if direct == 'L' and y > 1:
        y = y-1
    if direct == 'R' and y < 5:
        y = y+1
    if direct == 'U' and x > 1:
        x = x-1
    if direct == 'D' and x < 5:
        x = x+1

print(x,y)