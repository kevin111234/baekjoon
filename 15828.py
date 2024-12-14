import sys

n = int(sys.stdin.readline())
stack = []

while True:
    a = int(sys.stdin.readline())
    if a > 0:
        if len(stack)<n:
            stack.append(a)
    if a == 0:
        if len(stack)>0:
            stack.pop(0)
    if a == -1:
        break

if len(stack) > 1:
    for i in range(len(stack)):
        print(stack[i], end=" ")
if len(stack) == 1:
    print(stack[0])
elif len(stack) == 0:
    print("empty")