def answer(n, coins):
    coins.sort(reverse=True)
    answer = 0

    for coin in coins:
        if n == 0:
            print(answer)
            return None
        if n >= coin:
            div = n//coin
            n = n - (div)*coin
            answer += (div)
    print(answer)
    return None

def solution(n, coins):
    coins.sort(reverse=True)
    cnt = 0

    for coin in coins:
        cnt += n // coin
        n %= coin
    
    print(cnt)

n = int(input())
coins = [500, 100, 50, 10]
solution(n, coins)
