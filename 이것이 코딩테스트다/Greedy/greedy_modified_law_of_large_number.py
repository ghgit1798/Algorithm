def solution(n, m, k, data):
    answer=0
    cnt=0
    data.sort(reverse=True)

    biggest = data[0]
    second = data[1]

    div = k+1
    sum = biggest*3 + second

    answer = sum*(m//div) + second*(m%div)
        
    return answer

n,m,k = map(int, input().split())
data = list(map(int, input().split()))
answer = solution(n,m,k,data)
print(answer)