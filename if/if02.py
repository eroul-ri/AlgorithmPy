# 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F
a= int(input())
# 풀이 1
result = int(a / 10)

if result >= 9 :
    print('A')
elif result == 8 :
    print('B')
elif result == 7 :
    print('C')
elif result == 6 :
    print('D')
else :
    print('F')