n = int(input())
for i in range(n):
    a, b = map(int,input().split(" "))
    c = list(map(int,input().split(" ")))
    result = 1
    while c:
        if c[0] < max(c):
            c.append(c.pop(0))
        else:
            if b == 0: break

            c.pop(0)
            result += 1
        
        b = b-1 if b>0 else len(c) -1
    
    print(result)