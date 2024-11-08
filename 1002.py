n = int(input())
output = []
for i in range(n):
  a = input()
  b = a.split(" ")
  result = ""
  for k in range(len(b[1])):
    for j in range(int(b[0])):
      result += b[1][k]
  output.append(result)
for l in range(n):
  print(output[l])