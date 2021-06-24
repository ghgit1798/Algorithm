from collections import deque

def solution(prices):
    '''
    Notes:
        1. 1번째 가격을 꺼낸다.
        2. 2번째, 3번째... 주식 가격보다 작은 가격을 만날때까지 +1초
        3. 2번 결과 seconds를 저장한다.
            - prices의 최대길이는 100,000
            - price의 최대값은 10,000
    Args:
        prices (list): 주식 가격(int)을 담은 리스트

    Returns:
        answer (list): 주식이 떨어지지 않은 초를 담은 리스트
    '''
    
    answer = []
    
    


    return answer

prices = [1,2,3,2,3]
print(solution(prices))