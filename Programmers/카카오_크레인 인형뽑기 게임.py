from collections import deque

def solution(board, moves):
    ''' https://programmers.co.kr/learn/courses/30/lessons/64061

    Notes:
        1. stack 자료구조를 생성한다.
        2. moves에 해당하는 번호를 뽑아 stack에 넣는다.
        3. stack의 맨 위의 두 인형이 같으면 삭제하고 Count를 증가시킨다.

    Args:
        board (2d-list): 격자 상태를 나타내는 2차원 리스트
        moves (list): 인형 뽑는 순서(int)를 저장한 리스트

    Returns:
        answer (int): 터뜨린 인형 수
    
    '''
    answer = 0
    stack = deque()
    moves = deque(moves)

    while moves:
        idx = moves.popleft() - 1
        for i in range(len(board)):
            if board[i][idx]:
                stack.append(board[i][idx])
                board[i][idx] = 0
                break
        
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2

    return answer

board = [
        [0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]
        ]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
