# 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수
x = int(input())
y = int(input())
# 풀이 1
if x > 0 and y > 0 :
    print(1)
elif x < 0 and y < 0 :
    print(3)
elif x < 0 and y > 0 :
    print(2)
else :
    print(4)

#풀이 2
quad1 = x > 0 and y > 0
quad2 = x < 0 and y > 0
quad3 = x < 0 and y < 0

if quad1 :
    print(1)
elif quad2 :
    print(2)
elif quad3 :
    print(3)
else :
    print(4)
