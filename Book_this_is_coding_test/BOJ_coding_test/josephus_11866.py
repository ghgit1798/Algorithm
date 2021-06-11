import sys
from collections import deque

n, target = map(int, sys.stdin.readline().rstrip().split())
data = deque()
for i in range(1, n+1):
    data.append(i)

def solution(target, data):
    result = []
    i = 1
    while data:
        if i==target:
            result.append(data.popleft())
            i = 1
        else:
            data.append(data.popleft())
            i += 1
    return result

result = solution(target, data)
print('<', end='')
for i in range(len(result)):
    if i == len(result)-1:
        print(result[i], end='')
    else:
        print(result[i], end=', ')
print('>', end='')
        