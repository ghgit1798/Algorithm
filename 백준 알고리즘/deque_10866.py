import sys

class Deque:
    def __init__(self):
        self.deque = []
    def push_front(self, x):
        self.deque.insert(0, x)
    def push_back(self, x):
        self.deque.append(x)
    def pop_front(self):
        if len(self.deque) == 0:
            print(-1)
        else:
            print(self.deque.pop(0))
    def pop_back(self):
        if len(self.deque) == 0:
            print(-1)
        else:
            print(self.deque.pop())
    def size(self):
        print(len(self.deque))
    def empty(self):
        if len(self.deque) == 0:
            print(1)
        else:
            print(0)
    def front(self):
        if len(self.deque)==0:
            print(-1)
        else:
            print(self.deque[0])
    def back(self):
        if len(self.deque) == 0:
            print(-1)
        else:
            print(self.deque[-1])

deque = Deque()

n = int(input())
commands = [sys.stdin.readline().rstrip().split() for x in range(n)]

def solution(commands):
    for cmd in commands:
        if len(cmd)==2 and cmd[0]=='push_back':
            deque.push_back(cmd[1])
        elif len(cmd)==2 and cmd[0]=='push_front':
            deque.push_front(cmd[1])
        elif cmd[0]=='pop_front':
            deque.pop_front()
        elif cmd[0]=='pop_back':
            deque.pop_back()
        elif cmd[0]=='size':
            deque.size()
        elif cmd[0]=='empty':
            deque.empty()
        elif cmd[0]=='front':
            deque.front()
        elif cmd[0]=='back':
            deque.back()
        else:
            print('잘못된 명령입니다.')

solution(commands)