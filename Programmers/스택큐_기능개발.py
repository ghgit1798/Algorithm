from collections import deque

def solution(progresses, speeds):
    '''
    Notes:
        1. progresses, speeds를 큐에 넣는다.
        2. progresses 0번째 값이 100이상이면 꺼낸다.
            - speeeds도 0번째부터 함께 꺼낸다.
        3. 1일마다 speeds만큼 progresses를 더한다.
        4. progresses 원소를 모두 꺼낼때까지 반복한다.

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

def best_solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))


