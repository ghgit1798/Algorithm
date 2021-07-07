def solution(n, lost, reserve):
    ''' 프로그래머스-체육복 문제 풀이 (Greedy)
        
        Notes:
            1. 체육복 여벌은 자신 기준 앞, 뒤로만 빌려줄 수 있다는 것 주의
            2. 체육복 여벌이 있는데 도난 당한 경우를 먼저 고려할 것. 예외 처리 발생
        
        Args:
            n (int) : 학생 수
            lost (list) : 체육복을 잃어버린 학생 번호를 담은 리스트
            reserve (list) : 체육복 여벌을 가져온 학생 번호를 담은 리스트

        Returns:
            answer (int) : 체육 수업에 참여할 수 있는 최대 학생 수
    '''

    for l in lost:
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)
    
    answer = n - len(lost)

    for l in lost:
        for r in reserve:
            if abs(l-r) <= 1:
                answer += 1
                reserve.remove(r)
                break

    return answer

def best_solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)


n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))
print(solution(n, lost, reserve))