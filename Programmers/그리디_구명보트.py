def solution(people, limit):
    ''' https://programmers.co.kr/learn/courses/30/lessons/42885

    Notes:
        1. 가장 무거운 사람을 먼저 태운 후 가벼운 사람을 태워 나간다.
        2. 리스트 요소를 삭제 하는 연산 대신 indexing으로 대체한다.

    Args:
        people (list): 구조할 사람의 체중(int)들이 담긴 리스트
        limit (int): 구명보트의 최대 무게

    Returns:
        cnt (int): 필요한 최소 구명보트 수
    '''
    
    people.sort(reverse=True)
    cnt = 0

    left, right = 0, len(people)-1

    while left <= right:
        boat = people[left]
        cnt += 1
        left += 1
        
        while boat <= limit:
            if left > right:
                return cnt
            small = people[right]
            boat += small
            right -= 1
        right += 1

    return cnt

def worst_solution(people, limit):
    people.sort(reverse=True)
    cnt = 0

    while people:
        boat = people.pop(0)
        cnt += 1
        
        while boat <= limit:
            if len(people) == 0:
                return cnt
            small = people.pop()
            boat += small
        people.append(small)
    return cnt


people = [70,50,80,50]
limit = 100
print(solution(people, limit))


