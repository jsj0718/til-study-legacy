# 평탄화 함수 선언
def flatten(data):
    # 초기값 설정
    output = []
    # data 요소 (item) 반복
    for item in data:
        # item 유형이 리스트일 때
        if type(item) == list:
            # output에 더하기
            output += flatten(item)
        else:
            # item 유형이 리스트가 아닐 땐 append로 요소 추가
            output.append(item)
    # ouptut 반환
    return output

example=[[1,2,3],[4,[5,6]],7,[9,9]]
print(flatten(example))