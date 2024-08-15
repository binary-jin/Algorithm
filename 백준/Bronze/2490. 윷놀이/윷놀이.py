#2024-08-15
a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())
i, j, k, l = map(int, input().split())

#각 줄마다 1의 개수를 세어서 if문으로 나눔
#1의 개수를 어떻게 셀 것인가???....
#if문으로 각 숫자를 비교해서 1이면 list에 넣고 list의 개수로 1의 개수를 판별!!!
list_1 = [a, b, c, d]
list_2 = [e, f, g, h]
list_3 = [i, j, k, l]

list_new1 = []
list_new2 = []
list_new3 = []

for i in range(0, 4):
    if(list_1[i] == 1):
        list_new1.append(list_1[i])

for i in range(0, 4):
    if(list_2[i] == 1):
        list_new2.append(list_2[i])

for i in range(0, 4):
    if(list_3[i] == 1):
        list_new3.append(list_3[i])


if(len(list_new1)==1):
    print("C")
if(len(list_new1)==2):
    print("B")
if(len(list_new1)==3):
    print("A")
if(len(list_new1)==4):
    print("E")
if(len(list_new1)==0):
    print("D")

if(len(list_new2)==1):
    print("C")
if(len(list_new2)==2):
    print("B")
if(len(list_new2)==3):
    print("A")
if(len(list_new2)==4):
    print("E")
if(len(list_new2)==0):
    print("D")

if(len(list_new3)==1):
    print("C")
if(len(list_new3)==2):
    print("B")
if(len(list_new3)==3):
    print("A")
if(len(list_new3)==4):
    print("E")
if(len(list_new3)==0):
    print("D")