#2024-08-10 근무 시간
#a b c 의 출퇴근시간이 h m s로 6개 숫자로 찍힘 각각의 일 근무시간 구하기
ahour, amin, asec, ahour2, amin2, asec2 = map(int, input().split())
bhour, bmin, bsec, bhour2, bmin2, bsec2 = map(int, input().split())
chour, cmin, csec, chour2, cmin2, csec2 = map(int, input().split())

#각 시간을 초로 바꿔서 계산하기? 
astart = ahour*3600 + amin*60 + asec
aend = ahour2*3600 + amin2*60 + asec2
bstart = bhour*3600 + bmin*60 + bsec
bend = bhour2*3600 + bmin2*60 + bsec2
cstart = chour*3600 + cmin*60 + csec
cend = chour2*3600 + cmin2*60 + csec2

#aend-astart해서 다시 시간으로 바꾸기
result1 = aend - astart
result2 = bend - bstart
result3 = cend - cstart

aresulthour = result1//3600
aresultmin = (result1%3600) // 60
aresultsec = (result1%3600) % 60
print(aresulthour, aresultmin, aresultsec)

bresulthour = result2//3600
bresultmin = (result2%3600) // 60
bresultsec = (result2%3600) % 60
print(bresulthour, bresultmin, bresultsec)

cresulthour = result3//3600
cresultmin = (result3%3600) // 60
cresultsec = (result3%3600) % 60
print(cresulthour, cresultmin, cresultsec)