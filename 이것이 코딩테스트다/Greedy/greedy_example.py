# 금액을 입력받았을 때, 최소한의 동전 개수로 거스름돈 돌려주기
n = int(input())

count = 0

# 동전의 종류
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    # 동전의 개수 추가
    count += n // coin
    # 남은 거스름돈 금액
    n %= coin

print(count)