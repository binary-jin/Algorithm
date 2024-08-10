#2024-08-10 1부터 n까지의 합

#1. n을 입력 받기
n = int(input())
result = 0

#2. n까지의 합 출력 -> for문을 1부터 n+1까지로하기
for i in range(1, n+1):
    result += i

print(result)
