#2024-08-10 별 찍기
n = int(input())

#for문 돌려서 1부터 n+1까지 -> 별은 *, **, *** 한 개씩 증가 앞에 공백은 n에서 하나씩 줄어듬
for i in range(1, n+1):
    spaces = " "*(n-i)
    starts = "*" * i
    print(spaces + starts)