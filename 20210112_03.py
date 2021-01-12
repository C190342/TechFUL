s = [int(x) for x in input().split()]
count_V = 0
count_H = 0
cut = []
for i in range(s[1]):
  cut = [x for x in input().split()]
  if cut[1] == 'V':
    count_V += 1
  else:
    count_H += 1
res = (count_V + 1) * (count_H + 1)
print(res)
