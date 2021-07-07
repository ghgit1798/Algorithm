def solution(n, m, k, data):
    answer=0
    cnt=0
    data.sort(reverse=True)

    biggest = data[0]
    second = data[1]

    for i in range(m):
        if cnt == k:
            answer += second
            cnt = 0
        else:
            answer += biggest
            cnt += 1
        
    return answer

n,m,k = map(int, input().split())
data = list(map(int, input().split()))
answer = solution(n,m,k,data)
print(answer)