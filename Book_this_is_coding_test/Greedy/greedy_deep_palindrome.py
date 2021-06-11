import copy 

# my solution
def answer(data):
    length = len(data)
    zero = [0 for i in range(length)]
    one = [1 for i in range(length)]
    zeroCnt=0
    oneCnt=0
    checkCnt=False

    tmp = copy.deepcopy(data)
    while tmp != zero:
        for i in range(len(tmp)):
            if tmp[i] == 0:
                continue
            elif (tmp[i] == 1) & (i+1 == len(tmp)):
                tmp[i] = 0
                zeroCnt+=1
            elif (tmp[i] == 1) & (tmp[i+1] == 0):
                tmp[i] = 0
                zeroCnt+=1
            else:
                tmp[i] = 0
    
    tmp = copy.deepcopy(data)
    while tmp != one:
        for i in range(len(tmp)):
            if tmp[i] == 1:
                continue
            elif (tmp[i] == 0) & (i+1 == len(tmp)):
                tmp[i] = 1
                oneCnt+=1
            elif (tmp[i] == 0) & (tmp[i+1] == 1):
                tmp[i] = 1
                oneCnt+=1
            else:
                tmp[i] = 1
    
    print(min(zeroCnt, oneCnt))

    return None

# solution
def solution(data):
    count0 = 0 # 전부 0으로 바뀌는 경우
    count1 = 1 # 전부 1로 바뀌는 경우

    if data[0] == '1':
        count0 += 1
    else:
        count1 += 1

    for i in range(len(data)-1):
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

    print(min(count0, count1))

s = list(map(int, input()))
answer(s)