jumin = "990120-1234567"
year = jumin[0:2]
month = jumin[2:4]
day = jumin[4:6]
birth_day = jumin[0:6] # jumin[:6]과 동일


if jumin[7] == "1":
    gender = "남"
else:
    gender = "여"

print("성별 : {0}".format(gender))
print("연 : {0}".format(year))
print("월 : {0}".format(month))
print("일 : {0}".format(day))
print("생년월일 : {0}".format(birth_day))
print("뒷자리 : {0}".format(jumin[7:14])) # jumin[7:]과 동일
print("뒷자리 : {0}".format(jumin[-7:])) # -7 ~ -1까지 (범위는 작은 숫자 ~ 큰 숫자) -> 맨 뒤에서 7번째부터 끝까지라는 의미