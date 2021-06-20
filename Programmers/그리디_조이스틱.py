def solution(name):
    ''' Programmers 조이스틱 문제풀이 - Greedy
    
    Notes:
        1. 'A' 문자가 아닌 곳으로 이동하기까지 왼쪽, 오른쪽 이동 횟수를 계산 후 최소값을 더한다.
        2. 왼쪽 or 오른쪽 이동 후, 문자 완성을 위해 'A'에서부터 문자까지, 'Z'에서부터 문자까지 횟수를 계산 후 최솟값을 더한다.
        3. 모든 위치를 다 방문하여 문자열을 완성 시 종료한다.
        - 파이썬에서 리스트는 음수로도 indexing이 가능하다.
        - 가운데 중간 지점에서부터 계산하는 것이 아닌 주어진 조건 'A'부터 혹은 뒤에서 'Z'부터 계산할 것

    Args:
        name (str) : 완성할 문자열

    Returns:
        answer (int) : 조이스틱 이동횟수

    '''
    
    idx, answer = 0
    name_cnt = [min(ord(i)-ord('A'), 1+ord('Z')-ord(i))  for i in name]

    while True:
        answer += name_cnt[idx]
        name_cnt[idx] = 0
        left, right = 1,1

        if sum(name_cnt) == 0:
            break

        if name_cnt[idx] == 0:
            while name_cnt[idx-left] != 0:
                left += 1
            while name_cnt[idx+right] != 0:
                right += 1
        
        answer += left if left < right else left
        idx += -left if left < right else right

    return answer


def best_solution(name):
    make_name = [min(ord(i) - ord('A'), ord('Z')-ord(i)+1) for i in name]
    idx, answer = 0,0
    while True:
        answer += make_name[idx]
        make_name[idx] = 0
        if sum(make_name) == 0:
            break
        left, right = 1,1
        while make_name[idx - left] == 0:
            left += 1
        while make_name[idx + right] == 0:
            right += 1
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer

name = input()
print(solution(name))



