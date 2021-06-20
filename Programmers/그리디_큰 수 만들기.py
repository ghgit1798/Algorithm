def solution(number, k):
    '''
    Notes:
        1. stack에 값이 없거나, 더 작은 경우 넣는다.
        2. top에 위치한 값이 더 작으면 해당 값을 빼내고, k를 감소시킨다.
        3. k가 0이되면 남은 값들을 스택에 넣는다.
        4. 스택이 꽉 찼는데, k가 남아있다면 맨 위에서 k개를 꺼낸다.

    Args:
        number (str) : 주어진 숫자 (문자열로 주어짐)
        k (int) : 삭제할 숫자 개수

    Returns:
        answer (str) : 전체에서 k개를 삭제한 숫자 중 가장 큰 값
    '''

    answer = ''
    stack = []

    for i,num in enumerate(number):
        while stack and stack[-1]<num and k>0:
            stack.pop()
            k -= 1
        
        if k==0:
            stack += number[i:]
            break

        stack.append(num)
    

    stack = stack[:-k] if k != 0 else stack
    answer = ''.join(stack)

    return answer

# best solution
def best_solution(number, k):
    '''
    Notes:
        1. stack에서 값을 꺼내는 넣는 조건은 stack이 차있고 top 값이 num 보다 작고, k가 0보다 클 경우이다.
        2. k가 0이면 남은 값들을 stack에 넣고 반복문을 탈출한다.
        3. 1,2번 수행 후 num을 stack에 넣는다.
        4. 반복문 탈출 후 k가 0보다 크다면 k개만큼 stack 값을 제외한다.
    
    Args:
        number (str) : 숫자를 의미하는 문자열
        k (int) : 삭제할 숫자의 개수

    Returns:
        answer (str) : 가장 큰 수 반환
    '''

    stack = []

    for (i, num) in enumerate(number):
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1

        if k == 0:
            stack += number[i:]
            break

        stack.append(num)

    stack = stack[:-k] if k>0 else stack
    answer = ''.join(stack)
    return answer

number, k = input().split()
print(best_solution(number, int(k)))