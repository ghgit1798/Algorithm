
import sys
import time

t = int(input())
case = [int(sys.stdin.readline().rstrip()) for x in range(t)]

st = time.time()
def fibonacci(n, cnt):
    if n == 0:
        cnt.append(0)
        return 0
    elif n == 1:
        cnt.append(1)
        return 1
    else:
        return fibonacci(n-1, cnt) + fibonacci(n-2, cnt)

def solution(cnt):
    zero = cnt.count(0)
    one = cnt.count(1)
    return zero, one

# 피보나치 값, 계산 결과값, 0개수 1개수
table = {}
for x in case:
    if x in table:
        
    cnt = []
    fibonacci(x, cnt)
    zero, one = solution(cnt)
    print(zero, one)

et = time.time()
print(et-st)

# =====================시간 초과======================
# 이유 : N이 40 이하이므로 피보나치 수열을 수행 과정에서 시간 초과
# import sys

# t = int(input())
# case = [int(sys.stdin.readline().rstrip()) for x in range(t)]

# def fibonacci(n, cnt):
#     if n == 0:
#         cnt.append(0)
#         return 0
#     elif n == 1:
#         cnt.append(1)
#         return 1
#     else:
#         return fibonacci(n-1, cnt) + fibonacci(n-2, cnt)

# def solution(cnt):
#     zero = cnt.count(0)
#     one = cnt.count(1)
#     return zero, one

# for x in case:
#     cnt = []
#     fibonacci(x, cnt)
#     zero, one = solution(cnt)
#     print(zero, one)