#2024-08-15
#첫째 줄에 숫자 하나를 입력 받는데 범위가 있음!
n = int(input())

if(n<0 or n>12):
    n = int(input())

result = 1
for i in range(1, n):
    result = (n-i)*result

if(n==0):
    print(1)
else:
    print(result*n)