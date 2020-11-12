# Jocoding - JavaScript 강의 1강

![image-20201111231341268](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201111231341268.png)



![image-20201111231350165](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201111231350165.png)



![image-20201111231357176](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201111231357176.png)



## Tip

1. F12 (개발자 도구)에서 console 창으로 JS 코딩 가능

   * 개발자 도구의 콘솔창에서 한 칸 띄는 방법은 Shift + Enter

2. **Syntax**[신택스] 의미

   > 문법, 구조, 또는 언어 문장 내에 있는 구성요소의 순서이다. 
   >
   > (이에 반해 semantics는 이러한 구성요소들의 **의미**이다.) 
   >
   > **Syntax**는 자연어 뿐 아니라 컴퓨터 프로그래밍 언어에도 적용된다.
   >
   > 대체로, 우리는 **syntax**를 "낱말의 순서"라고 생각한다.

3. JQuery : JavaScript 라이브러리

   * 연결 방법
     * JQuery의 JavaScript 파일을 다운로드 받아 HTML 파일과 연결
     * CDN 연결 (CDN : 인터넷에서 특정 파일을 효율적으로 불러올 수 있게 한 것이다. HTML body 부분의 맨 아래에 링크를 붙여서 사용 가능하다.)
       * code.jquery.com에서 최신 버전을 선택하여 링크 복사 후 붙이기

   * JQuery API Documentation에서 더 많은 함수를 활용할 수 있다.
   * JQuery UI 에서 드래그해서 움직이게 하는 함수와 같은 기능을 활용 가능하다.

4. Codepen 활용 (별점 등 다양한 기능 제공)





# Jocoding - JavaScript 강의 2강

* API : Application Programming Interface (사용 규칙을 제공하는 것)
* open API : 백엔드를 구성한 뒤 주소와 사용 규칙을 공개한 것
  * 지도, 결제 채팅 등 다양한 기능 제공
* Serverless : Front-End만 구성한 후 open API에 접목시킨 것 

![image-20201112014147467](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201112014147467.png)



![image-20201112014222538](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201112014222538.png)

* JSON : JavaScript Object Notation의 약자 (JS의 Object)
  * 다른 언어에서도 표준으로 사용됨



**예시**

![image-20201112014450959](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201112014450959.png)

* 특기 부분에서 [] 는 배열
* 가족관계 부분에서 {}는 또 다른 JSON (Object)
* 홍길동을 가져오려면 data.이름 (.key 로 value 를 가져옴)
* 농구를 가져오려면 data.특기[0] (리스트와 동일)
* 홍판서를 가져오려면 data.가족관계.아버지



## AJAX (API의 요청과 응답을 다루기 위한 기술)

* Tip
  1. VSCode에서 Ctrl + K + F 하면 코드를 보기 좋게 정렬시킴
  2. 개발자 도구 > Console에서 Object 우클릭 후 Store as Global Varialble 클릭 (응답 받은 JSON을 Console 창에서 다루기 위해 따로 저장해두는 것)
  3. SDK (Software Development Kit)



1. Kakao Developer 사이트에서 로그인 후 앱 만들기를 통해 API 키를 발급받는다. (남용을 막기 위함)
2. 보안이 강한 API는 Front-End용 서버를 만들어서 요청을 하면 올바른 응답을 받을 수 있다.



* 요약 정리

![image-20201112134414895](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201112134414895.png)

![image-20201112134447937](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201112134447937.png)

