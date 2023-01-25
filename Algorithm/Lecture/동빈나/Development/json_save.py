import json

# 사전 자료형 데이터 선언
user = {
    "id" : "gildong",
    "password" : "1!2@3#4$",
    "age" : 30,
    "hobby" : ["football", "programming"],
}
# JSON 데이터로 변환하여 파일로 저장
with open("user.json", "w", encoding="UTF-8") as file:
    json_data = json.dump(user, file, indent=4)