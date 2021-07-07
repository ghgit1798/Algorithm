def answer(n, k):
    cnt=0

    while n != 1:
        if n%k == 0:
            n = n//k
            cnt += 1
        else:
            n = n-1
            cnt += 1

    print(cnt)

n,k = map(int, input().split())
answer(n,k)