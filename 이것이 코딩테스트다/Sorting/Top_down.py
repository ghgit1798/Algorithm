import sys

num = int(sys.stdin.readline())

data = [int(sys.stdin.readline().rstrip()) for _ in range(num)]

data.sort(reverse=True)

for var in data:
    print(var, end=' ')