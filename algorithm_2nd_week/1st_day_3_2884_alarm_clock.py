HOUR, MIN = input().split()
hour, min = int(HOUR), int(MIN)

# 1번 방식
if hour >= 1:
    if min >= 45:
        min = min - 45
    else:
        min = 60 + (min - 45)
        hour = hour - 1
elif hour == 0:
    if min >= 45:
        min = min - 45
    else:
        min = 60 + (min - 45)
        hour = 23

print(hour, min)

#2번식
if min >= 45:
    min = min - 45
else:
    min = 60 + (min - 45)
    if hour >= 1:
        hour = hour -1
    elif hour == 0:
        hour = 23

print(hour, min)

     
