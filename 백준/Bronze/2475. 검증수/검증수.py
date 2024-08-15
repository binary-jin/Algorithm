#2024-08-15
#5개의 숫자를 공백을 기준으로 입력 받기
a, b, c, d, e = map(int, input().split())

#각 숫자를 제곱한 수들의 합을 10으로 나눈 나머지 값을 출력해야함
#그럼 일단 각 숫자들을 제곱하기
a2 = a*a
b2 = b*b
c2 = c*c
d2 = d*d
e2 = e*e

#제곱한 걸 더해야함
sum = a2+b2+c2+d2+e2

#더한 걸 10으로 나눈 나머지 값 출력
result = sum%10
print(result)