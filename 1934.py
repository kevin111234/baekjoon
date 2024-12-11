cnt=int(input())
result=[]
for i in range(cnt):
    inp=input().split(" ")
    a=int(inp[0])
    b=int(inp[1])
    while b > 0:
        a, b = b, a % b
    k=a
    a=int(inp[0])
    b=int(inp[1])
    result.append(a * b / k)
for j in range(cnt):
    print(int(result[j]))