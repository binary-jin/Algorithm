#2024-08-10 시험 성적
#1. score input으로 받음
score = int(input())

#2. 각 점수마다 if문으로 경우를 나눠서 결과값 출력
if 90<=score<=100:
    print("A")
elif 80<=score<=89:
    print("B")
elif 70<=score<=79:
    print("C")
elif 60<=score<=69:
    print("D")
else:
    print("F")