def solution(clothes):
    ''' https://programmers.co.kr/learn/courses/30/lessons/42578
    Notes:
        1. 딕셔너리에 key, value를 저장한다.
        2. key별 해당하는 길이 +1 을 계산한다.
        3. key별 길이 + 1값을 전부 곱한 뒤 -1을 뺀다.
    
    Args:
        clohtes (list): key, value를 담은 리스트들을 저장한 리스트

    Returns:
        answer (int): 스파이의 의상 조합 개수
    
    '''
    answer = 0
    kv = dict()

    for v, k in clothes:
        if k in kv:
            kv[k].append(v)
        else:
            kv[k] = [v]
    
    mul = 1
    for k in kv.keys():
        mul *= len(kv[k])+1
    
    answer = mul - 1
    return answer

# clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))



