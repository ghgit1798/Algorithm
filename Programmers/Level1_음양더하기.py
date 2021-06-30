def solution(absolutes, signs):
    ''' https://programmers.co.kr/learn/courses/30/lessons/76501
    '''
    answer = 0

    for n, s in zip(absolutes, signs):
        if s:
            answer += n
        else:
            answer -= n
    
    return answer


absolutes = [4,7,12]
signs = [True,False,True]
print(solution(absolutes, signs))