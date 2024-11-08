n = int(input())
resultlist = []
for i in range(n):
  a = input()
  b = a.split(" ")
  result = float(b[0])
  for j in range(len(b)):
    if b[j] == "@":
      result *= 3
    elif b[j] == "%":
      result += 5
    elif b[j] == "#":
      result -= 7
  resultlist.append(result)

for l in range(len(resultlist)):
  print("{:.2f}".format(resultlist[l]))