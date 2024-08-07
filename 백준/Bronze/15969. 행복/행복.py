a = int(input())
b = list(map(int, input().split()))

max = 0
min = 1000

#초ㅣ댓값 최솟값 찾ㅣ for문으로 찾아야되는데
for i in range(a):
    if(b[i] >= max):
        max = b[i]
#print(max) 

for i in range(a):
    if(b[i] < min):
        min = b[i]  
#print(min)


#최댓값-최ㅅ값
print(max-min)