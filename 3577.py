A = int(input())
B = int(input())
C = int(input())
r = str(A*B*C)
result = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(r)):
    result[int(r[i])] += 1
for j in range(10):
    print(result[j])