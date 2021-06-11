import sys

n = int(sys.stdin.readline().rstrip())
input_list = [sys.stdin.readline().rstrip().split() for x in range(n)]
input_list = [(y, enum) for enum,y in enumerate(input_list, 1)]

def solution(input_list):
    input_list.sort(key = lambda value: (int(value[0][0]), value[1]))

solution(input_list)
for answer in input_list:
    print(answer[0][0], answer[0][1])


# ==============1차 시도===============
# 실패 이유 : 입력받을 때 나이가 문자로 입력되었다.
# [(['21', 'Junkyu'], 1), (['21', 'Dohyun'], 2), (['20', 'Sunyoung'], 3)]
# 따라서 '21'과 '20'을 비교하는 과정에서 문제가 발생했다.
# 이것을 int로 바꿔주니 문제 없이 통과되었다.
# 숫자 개념으로 비교할 때는 반드시 형변환을 실시해주자.
# import sys

# n = int(sys.stdin.readline().rstrip())
# input_list = [sys.stdin.readline().rstrip().split() for x in range(n)]
# input_list = [(x,y) for x,y in enumerate(input_list, 1)]

# def solution(input_list):
#     input_list.sort(key = lambda value: (value[1][0], value[0]))

# solution(input_list)
# for answer in input_list:
#     print(answer[1][0], answer[1][1])