def solution(s):
    answer = 0
    phone = {
        2 : 'ABC',
        3 : 'DEF',
        4 : 'GHI',
        5 : 'JKL',
        6 : 'MNO',
        7 : 'PQRS',
        8 : 'TUV',
        9 : 'WXYZ'
    }

    for a in s:
        for k, v in phone.items():
            if a in v:
                answer += k+1
                break

    return answer

s = input()
print(solution(s))