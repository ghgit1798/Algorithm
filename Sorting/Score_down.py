import sys

n = int(sys.stdin.readline().rstrip())

data = []
for i in range(n):
    student = sys.stdin.readline().rstrip().split()
    data.append((student[0], int(student[1])))

data = sorted(data, key = lambda var : var[1])

for var in data:
    print(var[0], end=' ')