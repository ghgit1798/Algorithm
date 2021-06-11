import sys

n = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
cards_set = list(set(cards))
cards.sort()

def solution(cards_set, cards, nums):
    hashmap = {}
    for x in cards:
        if x in hashmap:
            hashmap[x] += 1
        else:
            hashmap[x] = 1
    return hashmap

hashmap = solution(cards_set, cards, nums)s
for x in nums:
    if x in hashmap:
        print(hashmap[x], end=' ')
    else:
        print('0', end=' ')

# ==============1차 시도 시간 초과===============
# 이유는? 이진탐색을 사용하더라도 7log10 * 5*10^5으로 복잡도가 꽤 높다.
# 따라서 해쉬로 구현해야 할 듯하다.
# import sys

# n = int(sys.stdin.readline().rstrip())
# cards = list(map(int, sys.stdin.readline().rstrip().split()))
# m = int(sys.stdin.readline().rstrip())
# nums = list(map(int, sys.stdin.readline().rstrip().split()))
# cards_set = list(set(cards))

# cards.sort()
# cards_set.sort()
# cards_num = [cards_set[i] for i in range(len(cards_set))]
# counts_num = [cards.count(cards_set[i]) for i in range(len(cards_set))]

# def test(cards_num, num):
#     left, right = 0, len(cards_num)
#     while left <= right:
#         mid = (left+right)//2
#         if cards_num[mid] == num:
#             return mid
#         elif cards_num[mid] > num:
#             right = mid-1
#         else:
#             left = mid+1
#     return -1

# def solution(cards_num, counts_num, nums):
#     result = []
#     for i in range(len(nums)):
#         res = test(cards_num, nums[i])
#         if res == -1:
#             result.append(0)
#         else:
#             result.append(counts_num[res])
#     return result

# result = solution(cards_num, counts_num, nums)
# for x in result:
#     print(x, end=' ')
