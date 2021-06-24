from collections import deque

def solution(participant, completion):
    '''
    Notes: 
    - 해당 풀이는 deque 사용 시 시간초과 문제가 발생하는 문제가 있었다.
    - 시간복잡도 계산 시 O(N^2)일 경우 통과가 안되도록 설계되어 있는 듯 하다.
    
        1. participant, completion을 Queue에 넣는다.
        2. completion을 꺼내 participant에 있으면 participant에서 제거한다.
        3. completion 요소가 없어질때까지 반복하고 남아있는 participant를 반환한다.
    
    Args:
        participant (list): 참가자 리스트
        completion (list): 완주자 리스트
    
    Returns:
        answer (str): 완주하지 못한 참가자 이름
        
    '''

    answer = ''
    participant = deque(participant)
    completion = deque(completion)
  
    while completion:
        one = completion.popleft()
        if one in participant:
            participant.remove(one)

    answer = list(participant)
    return answer[0]

def best_solution1(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p
   
    return participant[-1]

def best_solution2(participant, completion):
    answer = '' 
    temp = 0 
    dic = {} 
    for part in participant: 
        dic[hash(part)] = part 
        temp += int(hash(part)) 

    for com in completion: 
        temp -= hash(com)

    answer = dic[temp]
    return answer


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))