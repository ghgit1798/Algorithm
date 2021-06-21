from collections import deque

def solution(progresses, speeds):
    '''
    Notes:
        1. progresses를 큐에 넣고 100이면 꺼낸다.
        2. 1일마다 speeds만큼 progresses를 더한다.
        3. 하루마다 1,2번을 반복한다.

    Args:
        progresses (list): 프로세스 진행도(int)를 담은 리스트
        speeds (list): 프로세스 효율(int)을 담은 리스트

    Returns:
        answer (list): 배포버전마다 완성된 프로세스 수를 담은 리스트 
    '''

    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        if cnt:
            answer.append(cnt)
        
        for i, speed in enumerate(speeds):
            progresses[i] += speed
        
    return answer
    

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))


