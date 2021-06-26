def false_solution(phone_book):
    '''
        Notes:
            1. phone_book의 길이 만큼 앞에서 추출한다.
            2. 추출한 길이들을 set으로 저장한다.
            3. set의 길이와 phone_book의 길이가 다르다면, 중복된 접두어가 있으므로 False 반환
                - 문제점: 323, 1191, 1192의 경우 True이지만 False로 반환한다.
        Args:
            phone_book (list): 전화번호(str)들을 담은 리스트
        
        Returns:
            answer (bool): True or False    
    '''

    length = sorted(set([len(n) for n in phone_book]))
    phone_book.sort(key = len)

    for l in length:                
        hashResult=[num[:l] for num in phone_book]
        length = len(hashResult)

        if len(hashResult) != len(phone_book):
            return False
    
    return True

def solution_timeover(phone_book):
    '''
        풀이는 성공했으나 시간초과로 효율성 통과 X
    '''
    phone_book.sort(key=len)

    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
    return True


def best_solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

def best_solution2(phone_book):
    phone_book.sort()

    for p1, p2 in zip(phone_book, phone_book[1:]):
        print(p1, p2)
        if p2.startswith(p1):
            return False
    return True




phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123","456","789"]
# phone_book = ['11', '0', '111']
print(ssolution(phone_book))