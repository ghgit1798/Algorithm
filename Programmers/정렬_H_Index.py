def solution(citations):
    ''' 가장 큰 인용횟수부터 H-index 찾기

    Notes:
        1. target값의 최대값부터 1씩 내려온다.
        2. target값보다 크거나 같은 값을 bigList에 모은다.
        3. target값보다 작거나 같은 값을 smallList에 모은다.
        4. 다음 두 조건을 만족하면 최종 resultList에 target값을 추가한다.
            - bigList의 개수(target보다 많이 인용된 논문수)가 target값보다 크거나 같다.
            - smallList의 개수(tartget보다 적게 인용된 논문수)가 target값보다 작거나 같다.
        5. resultList 중 최대값을 구한다.

    Args:
        citations (List): int형 값들을 담고 있는 List
    
    Returns:
        answer (int) : H-index의 최대값으로 정수값

    '''

    resultList = []

    for target in range(len(citations), 0, -1):
        bigList = [big for big in citations if target <= big]
        smallList = [small for small in citations if target >= small]

        if (len(bigList)>=target) & (len(smallList)<=target):
            resultList.append(target)
        
        print(target)

    if len(resultList) >= 1:    
        answer = max(resultList)
        return answer
    else:
        return 0

citations = [0]
print(solution(citations))