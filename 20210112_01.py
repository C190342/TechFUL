s = [int(x) for x in input().split()]
res = 0
for i in s[::2]:
  res += i
print(res)
