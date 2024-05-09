x = int(input())
y = int(input())

if x*y > 0:
    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y < 0:
        print(3)
elif x*y < 0:
    if x < 0:
        print(2)
    elif y < 0:
        print(4)
elif x==0 or y==0:
    x = int(input())
    y = int(input())