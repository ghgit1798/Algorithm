def solution(n, lost, reverse):
    answer=0

    for n in lost:
        if n in reverse:
            reverse.delete(n)
    
    


    return answer