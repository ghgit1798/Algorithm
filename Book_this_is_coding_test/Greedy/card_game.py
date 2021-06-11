# 이 문제의 핵심은 각 행의 최소값을 구한 뒤, 행 별로 가장 큰 값을 구하는 것이다.

n,m = map(int, input().split())

data = [list(map(int, input().split())) for i in range(n)]

result = min(data[0])

for i in range(m):
    result = max(result, min(data[i]))


print(result)


# n * m 행렬에서 각 row의 최솟값 중 가장 큰 값에 해당하는 row 찾기
# 이 문제의 핵심은 각 행의 최소값들을 구하고, 그 중 가장 큰 행을 찾는 것이다.

# n,m = map(int, input().split())
#
# data = [list(map(int, input().split())) for i in range(n)]
#
# print(f'data는 {data}')
#
# max_row = 0
# for i in range(m):
#     if min(data[max_row]) < min(data[i]):
#         max_row = i
#
# print(max_row+1)