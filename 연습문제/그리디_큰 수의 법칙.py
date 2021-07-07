def answer(n,m,k, data):
    num = 0
    cnt = 0
    data.sort(reverse=True)

    big = data[0]
    small = data[1]

    while cnt != m:
        for i in range(k):
            if cnt == m:
                print(num)
                return None
            num += big
            cnt += 1
        if cnt == m:
            print(num)
            return None
        else:
            num += small
            cnt += 1
    print(num)

def solution(n,m,k,data):
    data.sort(reverse=True)

    first=data[0]
    second=data[1]

    result=0

    while True:
        for i in range(k):
            if m == 0:
                break
            result += first
            m -= 1
        if m == 0:
            break
        result += second
        m -= 1

    print(result)


n,m,k = map(int, input().split())
data = list(map(int, input().split()))
answer(n,m,k, data)
solution(n,m,k, data)