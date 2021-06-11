import sys

n = int(input())
locations = [list(map(int,sys.stdin.readline().rstrip().split())) for x in range(n)]

locations.sort(key = lambda location : (location[0], location[1]))

for x in locations:
    print(x[0], x[1])