import sys

class Queue:
    def __init__(self):
        self.queue = []
    def push(self, x):
        self.queue.append(x)
    def pop(self):
        if len(self.queue) !=0:
            print(self.queue.pop(0))
        else:
            print(-1)
    def size(self):
        print(len(self.queue))
    def empty(self):
        if len(self.queue) == 0:
            print(1)
        else:
            print(0)
    def front(self):
        if len(self.queue) == 0:
            print(-1)
        else:
            print(self.queue[0])
    def back(self):
        if len(self.queue) == 0:
            print(-1)
        else:
            print(self.queue[-1])

n = int(input())
command = [sys.stdin.readline().rstrip().split() for x in range(n)]
queue = Queue()
for cmd in command:
    if len(cmd) == 2:
        queue.push(cmd[1])
    elif cmd[0] == 'front':
        queue.front()
    elif cmd[0] == 'back':
        queue.back()
    elif cmd[0] == 'size':
        queue.size()
    elif cmd[0] == 'pop':
        queue.pop()
    elif cmd[0] == 'empty':
        queue.empty()
    else:
        print('잘못된 입력입니다.')
