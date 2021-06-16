def solution(numbers):
    """ number를 받아 가장 큰 수를 정렬하는 함수
    
    Notes:
        1. 핵심은 숫자를 문자열로 반환한 뒤, 문자열 비교를 수행하는 것이다.
        2. 모든 숫자를 문자열로 비교하기 위해 문자열 곱셉을 수행하였다.
        3. 마지막에 0000과 같은 중복값을 제거하기 위해 int로 반환한 뒤 다시 string으로 반환하였다. 

    Args:
        numbers (list): int형 숫자를 담은 리스트

    Returns
        정렬한 값들을 string으로 연결한 문자열 반환

    """
    answer=''
    answer = sorted(list(map(str, numbers)), key=lambda x: x*5, reverse=True)

    return str(int(''.join(answer)))

q = [3, 30, 34, 5, 9]
print(solution(q))