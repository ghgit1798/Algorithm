def solution(n, times):
    answer = 0
    left, right = 0, min(times)*n

    while left<=right:
        mid = (left+right)//2
        cnt = 0
        for t in times:
            cnt += mid//t
        if cnt < n:
            left = mid+1
        else:
            right = mid-1
            answer = mid
    return answer