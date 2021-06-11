import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
cards = [x for x in range(1,n+1)]
cards = deque(cards)

def solution(cards):
    while len(cards) > 1:
        cards.popleft()
        cards.append(cards.popleft())
    print(cards[0])

solution(cards)

# 2초 초과 - N 500000으로 대입 시 79초가 걸렸다.
# 병목 지점은 어디지?

# import sys

# n = int(sys.stdin.readline().rstrip())
# cards = [x for x in range(1,n+1)]

# def solution(cards):
#     while len(cards) > 1:
#         cards.pop(0)
#         cards.append(cards.pop(0))
#     print(cards[0])

# solution(cards)