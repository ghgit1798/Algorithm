def solution(citations):
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