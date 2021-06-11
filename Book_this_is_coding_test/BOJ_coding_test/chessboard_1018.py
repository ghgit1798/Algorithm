m,n = map(int,input().split())
board = [ list(map(str, input())) for i in range(m)]

white = [
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W']
    ]
black = [
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B']
]

array = [ [j for j in range(i,i+10)] for i in range(1,6) ]

def solution(board, m, n):
    cnt_result = []
    for i in range(0, m-8+1):
        for j in range(0, n-8+1):

            # (i,j) 좌표 기준으로 8x8 체스판을 떼어옴
            result = []
            for k in range(i, i+8):
                result.append(board[k][j:j+8])

            # white, black 보드판과 다른 판 개수 체크
            w_cnt = 0
            b_cnt = 0
            for a in range(8):
                for b in range(8):
                    if white[a][b] != result[a][b]:
                        w_cnt += 1
                    if black[a][b] != result[a][b]:
                        b_cnt += 1

            cnt_result.append(w_cnt)
            cnt_result.append(b_cnt)
    return min(cnt_result)

print(solution(board,m,n))