h, m = map(int, input().split())

if m-45 >= 0:
    print(h, m-45)
elif m-45 < 0:
    if h == 0:
        print(23, m+60-45)
    else:    
        print(h-1, m+60-45)
elif h<0 or h>23 or m<0 or m>59:
    h, m = map(int, input().split())