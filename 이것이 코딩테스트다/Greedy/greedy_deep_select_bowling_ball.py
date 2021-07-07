# 그리디 심화 문제 풀이: 볼링공 고르기
# 최대값 n = 1000, m = 10

# 문제 풀이
def solution(data):
    length = len(data)
    number = []
    sum = 0

    for i in range(length):
        cnt = 0
        for j in range(i, length):
            if data[i] != data[j]:
                cnt += 1
        number.append(cnt)
    
    for num in number:
        print(num)
        sum += num
    
    print(sum)

def answer(data, n,m):
    # 1부터 10까지의 무게를 담을 수 있는 리스트
    array = [0]*11
    
    for x in data:
        array[x] += 1
    
    result = 0
    # 1부터 m까지의 각 무게에 대하여 처리
    for i in range(1, m+1):
        # 각 무게에 해당하는 볼링공의 개수 카운트
        n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
        result += array[i] * n # B가 선택하는 경우의 수와 곱하기

    print(result)

 
n, m = map(int, input().split())
data = list(map(int, input().split()))

solution(data)