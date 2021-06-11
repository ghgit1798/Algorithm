def solution(n,m, data):
    answer=0
    rlist = []

    for list_ in data:
        rlist.append(min(list_))
    
    answer = max(rlist)
    print(answer)

n,m = map(int, input().split())
data = [list(map(int, input().split())) for i in range(n)]
solution(n,m,data)