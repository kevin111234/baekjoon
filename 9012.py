import sys

n = int(sys.stdin.readline())

for i in range(n):
    stack = []
    b = False
    a = str(sys.stdin.readline())
    for j in range(len(a)):
        if a[j] == "(":
            stack.append(1)
        elif a[j] == ")":
            if len(stack) > 0:
                stack.pop(0)
            else:
                print("NO")
                b = True
                break
    if len(stack)>0:
        print("NO")
    elif not b:
        print("YES")