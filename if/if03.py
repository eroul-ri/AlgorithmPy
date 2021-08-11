# 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수
a = int(input())
# 풀이 1
is4 = a % 4 == 0
is100 = a % 100 != 0
is400 = a % 400 == 0
if is4 and is100 or is400 :
    print(1)
else :
    print(0)