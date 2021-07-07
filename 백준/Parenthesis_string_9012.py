import sys

n = int(sys.stdin.readline().rstrip())
exlist = [sys.stdin.readline().rstrip() for x in range(n)]

def solution(ps):
    stack = list()
    for i in range(len(ps)):
        if ps[i] == '(':
            stack.append(ps[i])
        if ps[i] == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                print('NO')
                return
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')

for ps in exlist:
    solution(ps)

# 그런데 스택을 리스트로 구현해도 될까?
# 큐처럼 넣고 빼는 과정에서 성능저하는 없을까?
# 그냥 사용해도 괜찮다. 따로 스택 자료구조를 제공하지 않는다.

# =================1차 시도=================
# 실패 이유 : NO를 출력해야 하는데 No를 출력했다..