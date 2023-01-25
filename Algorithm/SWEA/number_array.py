a = int(input()) # 테스트할 개수 입력
for i in range(a): # 10번 테스트면 10 입력 시 0 ~ 9까지 반복
    print(f"#{i+1} ", end="") # 테스트는 1~10이므로 i에 +1을 해줌. 줄바꿈을 안하기 위해 end="" 추가
    b = int(input()) # 몇 개의 숫자를 입력할 것인지 입력(c에 영향 X)

    c = list(map(int, input().split())) # split 함수는 문자열을 () 내에 원하는 문자열로 나눠 리스트로 만듦
    c.sort() # 정렬 함수
'''
list(map(int, input().split())) 해석
x = input().split() # 결과는 문자열 리스트
m = map(int, x) # 리스트 요소를 int로 변환, 결과는 맵 객체(출력이 이상하게 나옴)
result = list(map(int, input().split)) 
# input()에 넣은 값을 문자열로 리스트를 만든 후, map 함수로 각 요소를 int로 변환한다음 리스트로 다시 만든 것
'''
print(' '.join(map(str, c)))
    # print(','.join(map(str, c))) # join 함수는 리스트를 " ".join의 앞부분을 통해 원하는 문자열로 나눠 문자열로 나열함.