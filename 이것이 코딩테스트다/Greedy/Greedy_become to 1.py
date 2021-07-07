def solution(n, k):
    answer = 0

    while n!=1:
        if n%k == 0:
            n = n//k
            answer +=1
        else:
            n = n-1
            answer+=1
    print(answer)

n, k = map(int, input().split())
solution(n, k)