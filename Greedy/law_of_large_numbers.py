# 큰 수의 법칙 문제
# n은 리스트 요소의 개수, m은 더하는 횟수, k는 연속해서 더할 수 있는 횟수
# 5 8 3
# 2 4 5 4 6
# 6+6+6+5+6+6+6+5 = 46

# 이 문제의 핵심은 가장 큰 수, 그 다음 큰 수를 찾는 것이다.

n, m, k  = map(int, input().split(' '))

data = list(map(int, input().split(' ')))

print(f'n, m, k는 {n}, {m}, {k}')
print(f'data는 {data}')

sum = 0

data.sort(reverse=False)

max1 = data[-1]
max2 = data[-2]

print(f'data는 {data}, max1={max1}, max2={max2}')

for i in range(m):
    if i % k == 0 and i != 0:
        sum += max2
    else:
        sum += max1

print(sum)
