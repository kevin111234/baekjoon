n = int(input())
i = 0
cnt = 0
while True:
    if n-i>0:
        i += 1
        n = n-i
        cnt += 1
    else:
        print(cnt)
        break