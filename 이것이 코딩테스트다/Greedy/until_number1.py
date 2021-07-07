# 이 문제는 최소 횟수를 구하는 것이다.
# 따라서 문제 해결의 핵심은 무조건 많이 나누는 것이 좋다.
# 왜냐하면 1씩 뺴는 것보다는 나누는 것이 1에 더 빠르게 도달하기 때문이다.

import sys

n, k = map(int, sys.stdin.readline().split())
cnt = 0

while True:
    if n == 1:
        break

    if n % k == 0:
        n = n//k
        cnt = cnt + 1
    else:
        n = n-1
        cnt = cnt + 1

print(f'성공 결과 :  {cnt}')
