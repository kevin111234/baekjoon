a = int(input())
i = 2
while True:
    if a>=i: 
        if a%i == 0:
            print(i)
            a=a/i
        else:
          i += 1
    elif a<i:
        break