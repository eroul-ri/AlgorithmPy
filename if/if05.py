h, m = map(int, input().split())

before = 45
time = h * 60 + m - before

minute = time % 60
hour = time // 60 % 24

print(hour, minute)
