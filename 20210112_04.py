total_apples, get_apples = [int(x) for x in input().split()]
s = input()

count_r = s.count('R')
if count_r < get_apples:
  print(-1)
else:
  left_ps = 0
  right_ps = len(s) - 1

  left_wl = 0
  right_wl = 0

  eat_apple = 0
  turn_right = False
  total_steps = 0

  while eat_apple < get_apples :    
    if turn_right == False:
      total_steps = total_steps + 1;
      if s[left_ps] == "R":
        eat_apple = eat_apple + 1
        total_steps = total_steps - right_wl;  
        right_ps = right_ps - right_wl
        right_wl = 0      
        left_ps += 1   
        left_wl = 0        
      else:
        left_wl += 1
        left_ps += 1
        turn_right = True
        continue

    if turn_right == True:
      total_steps = total_steps + 1;
      if s[right_ps] == "R":
        eat_apple = eat_apple + 1
        total_steps = total_steps - left_wl;
        left_ps = left_ps - left_wl
        left_wl = 0
        right_ps -= 1        
        right_wl = 0
      else:
        right_wl += 1
        right_ps -= 1
        turn_right = False

  print(total_steps)












# pass 3 test case 1, 3, 4
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
