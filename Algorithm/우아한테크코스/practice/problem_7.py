# 암호화 함수 정의
def code_str(string):
    string_list = list(string)
    
    # 길이가 1보다 작거나 같으면 string 반환
    if len(string) <= 1:
        return string
    # string 길이만큼 반복
    for i in range(len(string_list)-1):
        # 현재 인덱스와 다음 인덱스 값이 동일한 경우
        if string_list[i] == string_list[i+1]:
            # 현재 인덱스 값과 다음 인덱스 값 제거
            string_list.pop(i)
            string_list.pop(i)
            return code_str("".join(string_list))
    return "".join(string_list)


print(code_str("browoanoommnaon"))