s = int(input())
str_input = []
str_output = []
count_find = 0
str_find = '"'

for i in range(s):
  str_input.append(input())

for i in range(len(str_input)):
  count_find = str_input[i].count(str_find)
  if count_find > 1:
    str_out = str_input[i].split('"')
    for i in range(len(str_out)-1):
      if i%2 ==1:
        str_output.append(str_out[i])
for i in range(len(str_output)):
  print(str_output[i])
