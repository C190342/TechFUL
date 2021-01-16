s = int(input())
str_input = input().split()
sum_str = 0

for i in range(s):
  sum_str += ord(str_input[i])
print(sum_str)

# 入力値             3
#                    A A B 

# 期待される出力値    196

# ASCIIコード表に照らし合わせると10進法表記で'A'は65,'B'は66です。
#そのため、65+65+66=196である 196を出力するのが正解です。
