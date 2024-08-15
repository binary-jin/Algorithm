#2024-08-15
#1. a, b를 한 줄에 입력받음
a, b = map(int, input().split())

#2. A＠B = (A+B)×(A-B) 의 결과를 출력
result = (a+b)*(a-b)
print(result)