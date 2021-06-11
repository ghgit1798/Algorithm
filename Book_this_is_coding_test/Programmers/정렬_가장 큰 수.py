
def solution(numbers):
    answer=''
    nlist = [str(n) for n in numbers]

    # rlist = []
    # for n in nlist:
    #     rlist.append(n)
    #     for a in n:
    #         rlist.append(int(a))
    # rlist.sort(reverse=True)
    # for s in rlist:
    #     answer+=str(s)
    nlist.sort(key=lambda x: (str(x)[0] ), reverse=True)
    print(nlist)

    return answer

q = [3, 30, 34, 5, 9]
answer=solution(q)
print(answer)