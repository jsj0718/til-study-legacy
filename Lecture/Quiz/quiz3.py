# 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.

# 내 풀이
# url = "http://google.com"
# my_url = url[7:] # 규칙 1, naver.com
# my_com = my_url.replace(".com", "") # 규칙 2, naver
# my_pw = my_com[:3] + str(len(my_com)) + str(my_com.count("e")) + "!"
# print("생성된 비밀번호 : {0}".format(my_pw))

# 해석
url = "http://naver.com"
my_url = url.replace("http://", "")
my_com = my_url[:my_url.index(".")]
my_pw = my_com[:3] + str(len(my_com)) + str(my_com.count("e")) + "!"
print(my_pw)