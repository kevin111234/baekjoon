a=0
for i in range(5):
    b = int(input())
    if b < 40:
        a+=40
    else:
        a+=b
print(int(a/5))