def answer(n,m,data):
    result = 0
    rlist = []

    for arr in data:
        rlist.append(min(arr))
    
    print(max(rlist))

n,m = map(int, input().split())
data = [list(map(int, input().split())) for i in range(n)]
answer(n,m,data)
