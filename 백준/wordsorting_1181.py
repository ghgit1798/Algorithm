import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for i in range(n)]

def solution(words):
    result = list(set(words))
    result.sort(key = lambda word : (len(word), word))
    return result

result = solution(words)
for answer in result:
    print(answer)