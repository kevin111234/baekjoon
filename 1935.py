n = int(input())
s = str(input())
num = []
stack = []
for i in range(n):
    a = int(input())
    num.append(a)
for j in range(len(s)):
    if s[j] not in ("+", "-", "*", "/"):
        b = ord(s[j])-65
        stack.append(num[b])
    else:
        if len(stack) > 1:
            c = stack.pop(-1)
            d = stack.pop(-1)
            if s[j] == "+":
                stack.append(d+c)
            elif s[j] == "-":
                stack.append(d-c)
            elif s[j] == "*":
                stack.append(d*c)
            elif s[j] == "/":
                stack.append(d/c)
print(f"{stack[0]:.2f}")