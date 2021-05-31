import sys

M = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
N = int(sys.stdin.readline().rstrip())
B = list(map(int, sys.stdin.readline().rstrip().split()))
# 이진 탐색을 위한 정렬
A.sort()

def binary_search(A, x):
    left, right = 0, len(A)-1

    while left <= right:
        mid = (left+right)//2
        if x == A[mid]:
            return 1
        elif x < A[mid]:
            right = mid-1
        else:
            left = mid+1
    return 0

def solution(A, B):
    res = []
    for x in B:
        num = binary_search(A, x)
        res.append(num)
    return res

res = solution(A,B)
for x in res:
    print(x)


# =============== 시간 초과 ================
# 이유는 총 10^10 = 100억의 계산을 수행해야 하기 때문이다.
# B의 10만개 각각에 대해 A의 10만개에 속하는 지 확인해야 하기 때문
# Binarysearch를 사용하면 복잡도를 낮출 수 있지 않을까?
# 이진 탐색은 조건이 있다. 정렬되어 있을 것!

# import sys

# M = int(sys.stdin.readline().rstrip())
# A = list(map(int, sys.stdin.readline().rstrip().split()))
# N = int(sys.stdin.readline().rstrip())
# B = list(map(int, sys.stdin.readline().rstrip().split()))

# def solution(A, B):
#     res = []
#     for x in B:
#         if x in A:
#             res.append(1)
#         else:
#             res.append(0)
#     return res

# res = solution(A,B)
# for x in res:
#     print(x)