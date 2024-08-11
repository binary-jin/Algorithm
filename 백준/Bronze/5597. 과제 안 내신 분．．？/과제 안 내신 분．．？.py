#2024-08-11
#input에 있는 숫자 중에 순서대로 나열했을 때 없는 숫자 두 개를 찾고 그걸 작은 순서대로 나오게 함
list_num = []

for i in range(1, 29):
    nums = int(input())
    list_num.append(nums)
#일단 그럼 input의 숫자들을 리스트로 먼저 만듬 -> 리스트에 집어넣는 append 검색 후 사용
#list_num만들어졌으니 오름차순으로 정렬
list_num.sort()

#없는 값을 찾아야되는데... 어차피 30까지로 정해져있으니까 30까지인 다른 list를 만들어서 그 리스트랑 값을 비교해서 없는 값을 찾기?
list_num2 = []
for i in range(1, 31):
    list_num2.append(i)

result_list = [] #결과값을 리스트로 만들기 위해 리스트 하나 만듬

#리스트 두개 비교하는 방법 검색 후 사용
for i in list_num2:
    if i not in list_num:
        result_list.append(i)

print(min(result_list))
print(max(result_list))