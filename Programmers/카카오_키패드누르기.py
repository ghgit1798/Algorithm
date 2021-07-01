def solution(numbers, hand):
    '''
    Notes:
        1. 왼손, 오른손 현재 위치를 저장하는 자료구조 생성
        2. 1,4,7이면 왼손을 3,6,9면 오른손으로 입력
        3. 2,5,8,0이면 왼손, 오른손과의 거리 계산 후 작은 손 선택
        4. 왼손, 오른손 거리가 같을 경우 hand의 선택에 따라 선택
    
    Args:
        numbers (list): 입력할 키패드 숫자(int)를 담은 리스트
        hand (str): 왼, 오른손 잡이를 나타내는 문자열
    
    Returns:
        answer (str): 사용한 손 순서를 담은 리스트

    '''
    
    answer = ''
    pad = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ['*',0,'#']
    ]

    l = [3, 0]
    r = [3, 2]

    for n in numbers:
        for i, p in enumerate(pad):
            if n in p:
                target = [i, p.index(n)]
                break
        if n in [1,4,7]:
            l = target
            answer += 'L'
        elif n in [3,6,9]:
            r = target
            answer += 'R'
        elif n in [2,5,8,0]:
            print(f'n={n}, l={l}, r={r}, target={target}')
            lp = [abs(target[0]-l[0]), abs(target[1]-l[1])]
            rp = [abs(target[0]-r[0]), abs(target[1]-r[1])]
            
            if sum(lp) < sum(rp):
                l = target
                answer += 'L'
            elif sum(lp) > sum(rp):
                r = target
                answer += 'R'
            elif sum(lp) == sum(rp):
                if hand=='left':
                    l = target
                    answer += 'L'
                else:
                    r = target
                    answer += 'R'

            # if abs(sum(l)-sum(target)) < abs(sum(r)-sum(target)):
            #     l = target
            #     answer += 'L'
            # elif abs(sum(l)-sum(target)) > abs(sum(r)-sum(target)):
            #     r = target
            #     answer += 'R'
            # elif abs(sum(l)-sum(target)) == abs(sum(r)-sum(target)):
            #     if hand=='left':
            #         l = target
            #         answer += 'L'
            #     else:
            #         r = target
            #         answer += 'R'
        print(n, target, l, r, answer)
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))