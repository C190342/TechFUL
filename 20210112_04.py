sum_apple, take_apple = [int(x) for x in input().split()]
s = input()
tr_in = [i for i in s]
take_time = 0
j = 0
k = -1
find_str = 'R'
count_find_r = 0
count_r = s.count(find_str)
if count_r < take_apple:
  print(-1)
  
else:
  while True:
    take_time += 1
    if tr_in[j] == "R":
      count_find_r += 1
      j += 1
    elif tr_in[k] == "R":
      count_find_r += 1
      k -= 1
    else:
      if take_time==1:
        take_time +=1
      j += 1
      k -= 1
    
    if count_find_r == take_apple:
      break
  print(take_time)
