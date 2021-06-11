import sys

def solution():
    while True:
        input_value = str(sys.stdin.readline().rstrip())
        if input_value == '0':
            break
        target_value = input_value[::-1]
        if input_value == target_value:
            print("yes")
        else:
            print("no")
    return 0

solution()