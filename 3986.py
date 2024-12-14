n = int(input())
k = 0
for i in range(n):
    arr = []
    a = str(input())
    for i in range(len(a)):
        arr.append(a[i])
        if len(arr) > 1:
            if arr[-1] == arr[-2]:
                arr.pop(-1)
                arr.pop(-1)
    if len(arr) == 0:
        k += 1
print(k)