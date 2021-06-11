# My solution
def answer(n, data):
    data.sort(reverse=True)
    rlist = []

    i=0
    k=len(data)

    while i < k:
        tlist=[]
        group_cnt=data[i]
        for j in range(group_cnt):
            tlist.append(data[i])
            i = i+1
        if group_cnt == len(tlist):
            rlist.append(tlist)
    
    print(len(rlist))
    print(rlist)

    return None
    
# solution
def solution(data):
    data.sort()
    result = 0 # 총 그룹 수
    count = 0 # 현재 그룹에 포함된 모험가의 수

    for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
        count += 1 # 현재 그룹에 해당 모험가를 포함시키기
        if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
            result += 3 # 총 그룹 증가시키기
            count = 0 # 현재 그룹에 포함된 모험가의 수 초기화
    
    print(result) # 총 그룹의 수 출력

n = int(input())
data = list(map(int, input().split()))
answer(n, data)