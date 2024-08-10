#2024-08-10 사칙연산 결과값 출력
#1. 두 자연수 a,b 입력 받기 -> 한 줄에 입력 받아야함
a, b = map(int, input().split())

#2. a+b
print(a+b)

#3. a-b
print(a-b)

#4. a*b
print(a*b)

#5. a/b
#/ -> 소수점 아래까지 나옴 // -> 소수점 아래 버리고 정수만 나옴
print(a//b)

#6. a%b
print(a%b)
