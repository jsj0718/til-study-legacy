# HTML5 멀티미디어와 입력 양식



## 학습목표

* 오디오, 비디오를 웹 페이지에 추가하는 방법 학습
* "<iframe>" 태그 학습
* 사용자가 서버로 데이터 보낼 때 사용하는 입력 양식
* 새롭게 추가된 여러가지 입력 필드



## 01. 웹 브라우저와 멀티미디어

* 이전 버전에는 오디오와 비디오를 재생시키기 위해 상당한 수고가 필요했다. (플래시나 Active X 설치 등)
* HTML5에서 "<audio>"와 "<video>" 태그가 추가되면서 오디오, 비디오를 추가할 수 있게 되었다.
* 플러그인 설치도 필요가 없다.



## 02. 오디오

* HTML5에서 "<audio>" 태그를 이용해 웹 페이지에서 음악을 재생한다.

  * "<audio src="old_pop.mp3" autoplay controls>"

    * audio : 오디오 삽입 태그
    * src = "old_pop.mp3" : 오디오 소스 파일 경로(URL)
    * autoplay : 자동 재생
    * controls : 화면 제어기 표시

    

  * audio 요소

    * autoplay : 자동 재생
    * controls : 제어기 표시
    * loop : 반복 재생
    * preload : 사용할 생각이 없어도 오디오를 미리 다운로드 (빠르게 오디오 재생 가능)
    * src : 오디오가 존재하는 URL 지정
    * volume : 재생 볼륨 설정(0.0~1.0)

    

  * 오디오 파일 형식

    * MP3 : MPEG-1 Audio Layer-3 약자로 MPEG 기술의 음성 압축 기술
    * Wav : 윈도우에서 사용되는 표준 사운드 포맷(MS에서 개발, 파일 크기가 큼)
    * Ogg : MP3 대안으로 개발된 사운드 파일 포맷(오픈소스로 개발됨)

    

  * source 태그 사용하기

    * 모든 브라우저가 지원하는 오디오 형식은 아직 없기 때문에 source 태그를 이용해 하나의 오디오 소스에 대하여 여러 가지 파일 형식을 동시에 제공하면 된다.

      * "<audio controls autoplay>"
        * <source src="old_pop.ogg" type="audio/ogg">
        * <source src="old_pop.mp3" type="audio/mp3">
        * <source src="old_pop.wav" type="audio/wav">
        * type 속성은 MIME(multipurpose internet mail extensions) 타입으로 인터넷에서 멀티미디어 전송을 위한 규약을 의미한다.

      * 이는 위에서부터 차례대로 파일 형식을 검사한다.



## 03. 비디오

* 비디오 또한 오디오와 유사하다. ("<video>" 태그를 이용)
  * "<video src="movie.mp4" autoplay controls>"
    * video : 삽입 태그
  * video 요소 속성
    * autoplay : 자동 재생
    * controls : 제어기 표시
    * loop : 반복 재생
    * poster : 비디오를 다운로드하는 중일 때 표시하는 이미지
    * preload : 사용할 생각이 없어도 전체 오디오를 다운로드
    * muted : 비디오의 오디오 출력 중지
    * src : 오디오가 존재하는 URL 지정
    * width, height : 너비와 높이
  * 비디오 파일 형식
    * MP4 : MPEG-4 기술 사용(적은 용량으로 고품질 영상과 음성 구현)
    * WebM : 무료로 제공하는 개방형 고화질 영상 압축 형식의 영상 포맷(구글이 지원)
    * Ogg : 무료, 비디오 압축 형식
  * 모든 웹 브라우저에서 재생되는 비디오 형식은 없다. 오디오처럼 MIME 타입을 이용한다.
* 참고사항
  * width, height를 지정해야 브라우저가 미리 가늠할 수 있다. (설정 안하면 레이아웃이 변경될 수 있음)
  * "<video>" 태그를 지원하지 않는 브라우저를 위해 텍스트를 넣는 것이 좋다.



## 04. iframe(inline frame)

* 웹 페이지 안에서 다른 웹 페이지를 표시할 때 사용한다.
* 흔히 광고를 위해 이것을 사용한다.

![image-20200925111639554](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200925111639554.png)

한 페이지에서 소스코드와 출력 결과를 동시에 나타낼 수 있는 것은 iframe을 활용했기 때문이다.

이것을 구현하려면 왼쪽, 오른쪽에 배치하는 CSS와 출력 변화를 위해서는 JSP같은 서버 스크립트 기술을 적용해야한다.

* iframe 속성
  * seamless : 경계선 없이 문서의 일부인 것처럼 나타난다.

* "<iframe src="" name="이름"><iframe> "을 설정한 후 a 태그의 target 속성으로 name에 해당하는 이름을 지정하면, 하이퍼링크 이동을 iframe에 표시할 수 있다.



## 05. div와 span

* div와 span은 웹 사이트 구축을 위해 필수적인 도구

* div(divide)는 건축에서 철근같은 역할, 페이지를 논리적인 섹션으로 분리할 때 사용

  * 예시

    * <div style="border : 3px solid red">
          <h2>
              사자
          </h2>
          <p>
              사자는 아프리카에 살며...
          </p>
      </div>

    * 이와 같이 h2 태그와 p 태그를 묶어 빨간색 경계선을 그릴 때 div를 사용하면 된다.

    * div 위치를 변경하면 h2와 p 태그도 같이 이동한다.

  * div는 블록 수준의 요소 (HTML 요소를 묶는 컨테이너)로 자체적으로는 특별한 의미가 없다.

    * 블록 수준이기에 하나의 줄을 전부 차지함

* span은 인라인 요소로 텍스트를 위한 컨테이너로 사용할 수 있다. 

  * 인라인 요소 : 자신이 필요한 크기만 차지하는 요소
  * 자체로 특별한 의미가 없다.

* 결론

  * div와 span은 요소를 모아서 하나의 묶음으로 만들어 특정한 스타일이나 위치, 크기 등을 적용하는 경우에 사용한다.



## HTML 입력 양식

* 지금까지는 서버에서 사용자에게로 전달되는 것뿐이었다.
* 이번에는 사용자에서 서버로 보내는 것을 학습한다. (입력 양식 사용)
* 입력 양식 : 사용자로부터 데이터를 받아 서버로 넘기는데 사용(입력 필드를 가지고 있는 웹 페이지)



* form 요소 (form 태그는 HTML 양식을 생성하는데 사용)

  * <form action="input.jsp" method="post">
        <input type="text" name="input">
        <input type="submit">
    </form>

  * form의 속성은 보통 name, action, method가 쓰인다.

  * method : 전송 방식 - post, get

  * action : 전송 목적지 - url

  * enctype : 전송 데이터 형식 설정

    1. application/x-www-form-urlencoded

    디폴트 값은 이거다. 서버로 전송되기 전에 url-encode 된다는 뜻

    2. mutipart/form-data

    파일 받으면서 설정해준게 이 값인데 이미지나 파일을 서버로 전송할 경우 이 방식을 사용한다고 한다.

    3. text/plain

    이 형식도 많이 봤을 듯 한데

    이건 인코딩을 하지 않은 문자 그대로의 상태를 전송한다는 의미.

  * 설명

    * 입력 양식은 항상 form으로 시작

    * action="input.jsp" : 입력을 처리하는 서버 스크립트 주소를 적는다.

      * action 속성에는 사용자가 입력한 데이터를 받아서 처리하는 스크립트 주소를 URL 형식으로 적는다.

    * method="post" : 입력 데이터가 서버로 보내지는 방법을 기술한다.(Post, Get 존재)

      * method 속성에는 데이터를 보내는 방법을 기술한다. (POST, GET 방식)

      * Post와 Get 방식

        * Get 방식 : URL 주소 뒤에 파라미터를 붙여 데이터를 전달하는 방식

          * 예시 : https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=html (URL 뒤에 사용자가 입력한 단어를 붙여서 서버로 보낸다.)
          * ?를 기준으로 https://search.naver.com/search.naver는 URL, sm=top_hty&fbm=1&ie=utf8&query=html는 파라미터가 된다.
          * 단점
            1. Get 방식으로 보낼 수 있는 글자 수는 제한되어 있다.(최대 2048글자)
            2. 비밀 보장이 안된다.(패스워드 데이터를 Get 방식으로 하면 큰일남)
          * 장점
            1. 북마크가 가능하다.
            2. 뒤로 가기가 보장된다.

        * Post 방식 : 사용자가 입력한 데이터를 URL에 붙이지 않고 HTTP Request 헤더에 포함시켜 전송시키는 방식이다.

          * 예시

            * POST /test/input.jsp HTTP/1.1

              Host: www.naver.com

              name1=value1&name2=value2

              ...

          * 장점

            1. 길이 제한 X
            2. 보안이 유지된다.

          * 단점

            1. POST 요청은 캐시되지 않고, 브라우저 히스토리에도 남아있지 않다.
            2. 북마크가 불가능하다.
            3. 뒤로 가기를 하면 데이터를 다시 보내야 한다는 경고창이 뜬다.



## 입력 태그 #1

* input 요소(가장 중요, 사용자로부터 정보를 받아들이는 용도로 사용됨)
* type 속성을 통해 아주 다양한 형태가 나옴
* 형식 : <input type="button" value="눌러보세요" name="button1">
  * type 속성 : 입력 요소의 유형
  * value 속성 : 입력 요소의 초기값, 사용자가 변경 가능
  * name 속성 : 입력 요소 이름이며 서버로 변수의 이름처럼 전달됨
* 입력 태그 종류

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200925174238363.png" alt="image-20200925174238363" style="zoom: 50%;" />

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200925174300206.png" alt="image-20200925174300206" style="zoom:50%;" />



* input 형식

  * "<input type="button" value="눌러보세요" name="button1">"

    * type : 입력 필드 종류 결정
    * value : 버튼에 나타내는 텍스트
    * name : 서버로 전달되는 이름

  * type 속성

    * text : 텍스트 입력할 수 있는 한 줄짜리 필드 생성

      * 기본 크기는 20글자. 서버에는 name을 변수 이름처럼 생각해 값 참조

    * password : 비밀번호 입력할 수 있는 한 줄짜리 필드 생성

      * 입력한 글자가 보이지 않음

    * radio : 라디오 버튼 생성

      * 여러 항목 중 하나만 선택 가능
      * name, value는 반드시 지정해야 한다.
      * name이 같아야 동일한 그룹으로 취급된다. (value로 그룹에서 차이를 준다.)

    * checkbox : 체크 박스 생성

      * 여러 개 항목 동시 선택 가능
      * name 속성은 동일해야 한다.

    * file : 파일 이름을 입력하는 필드 생성

    * reset : 초기화 버튼 생성. 버튼을 누르면 모든 입력 필드 초기화

    * image : 이미지를 전송 버튼으로 만듦

    * hidden : 사용자에게 보이지 않지만, 서버로 전송됨

    * submit : 제출 버튼

      * 데이터를 서버로 전소하는데 사용된다.

      * 데이터는 "name1=value1&name2=value2.."의 형태로 action 속성에 지정된 스크립트로 보내진다.

      * action 속성에 지정된 스크립트는 전송받은 입력에 대해 어떤 처리를 한다.

      * value 속성을 지정하지 않으면 default 값인 "쿼리 제출"으로 된다.

      * 예시

        * <form name="input" action="getid.jsp" method="get">

          ​    사용자 아이디 :

          ​    <input type="text" name="user"> <br>

          ​    <input type="submit" value="제출">

          ​    <input type="reset" value="초기화">

            </form>

      

  * input 버튼

    * 일반적인 버튼은 <input type="button">으로 생성 가능하다.

      * 대부분 onclick 속성에 버튼이 클릭되면 실행되는 JS를 지정한다.

        * onclick : 버튼이 클릭되면~

        * 간단한 경고 대화 상자는 alert()를 사용한다.

        * 예시

          *   <form>

            ​    물품가격: <input type="text" name="price"> <br>

            ​    수량: <input type="text" name="mount"> <br>

            ​    <input type="button" value="계산" onclick="alert('10000원입니다.')">

              </form>

  * button 버튼

    * 버튼은 "<button>" 태그로도 정의 가능
    * button 요소 안에는 텍스트나 이미지와 같은 콘텐츠를 넣을 수 있음 (input type="button" 과의 차이)
    * button의 속성은 type으로 지정한다.
      * submit
      * reset
      * button
        *  <button type="button" onclick="alert('안녕하세요?')">눌러보세요!</button>
        * HTML form 안에서 button 태그를 이용하면 오류가 발생할 수 있기 때문에 가급적이면 input 태그를 활용하는 것이 바람직하다.

  * 이미지 버튼 (2가지 방법)

    * <button type="submit"><img src=""></button>
      * button 태그를 사용하면 어떤 버튼도 이미지로 작성이 가능하다.
    * <input type="image" src="" alt="제출 버튼">
      * input 태그를 활용하면 제출 버튼의 역할만 할 수 있다.



## 08. 입력태그 #2

* textarea
  * 여러 줄의 텍스트 입력을 받을 때 사용하는 태그
  * 크기는 row와 column으로 설정
* select
  * 메뉴 표시 및 사용자가 선택하게 한다.
  * 항상 option 요소와 사용된다.
    * option 요소는 반드시 value 속성을 가지고 있어야 한다.
  * selected 속성으로 특정 항목을 초기에 선택할 수 있다.

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200925183227647.png" alt="image-20200925183227647" style="zoom:67%;" />

* filedset

  * 입력 요소를 그룹핑하는데 사용되는 태그

  * 다양한 입력 요소를 넣을 수 있고, 그룹의 경계에 선을 그어준다.

  * legend 태그를 사용하면 그룹에 제목을 붙일 수 있다.

    ![image-20200925183702938](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200925183702938.png)

* label

  * input 요소를 위한 레이블(label)을 정의하는데 사용
  * 속성 for를 이용하여 label과 input 요소를 연결할 수 있다. (label의 for과 input 의id가 같으면 연결)

* 파일 업로드 버튼

  * 사용자가 파일 선택 후 서버로 업로드해야 하는 경우 사용

  * <input type="file">

    * 이 버튼을 누르면 파일 이름을 선택하는 대화 상자가 화면에 등장

  * 예시

    * <form enctype="multipart/form-data">

      ​    <input type="file" accept="image/jpg, image/gif">

      </form>

    * form 태그에 enctype="multipart/form-data"를 추가하는 것이 좋다.

      * 파일을 올바르게 업로드하여 준다.

    * input 태그에 accept 속성은 업로드시킬 파일의 MIME 타입을 브라우저에게 알려준다.

* <input type="hidden">

  * 사용자가 입력하는 데이터는 아니지만, 클라이언트 컴퓨터가 서버 컴퓨터로 특정한 데이터를 전송하고 싶은 경우 사용한다.
  * 화면에는 아무것도 나타나지 않고 사용자가 제출 버튼을 누르면, 서버로 이 요소의 name, value가 전송된다.

## 09. HTML5 입력 요소

* 추가된 input type
  * date : 날짜를 입력할 수 있는 컨트롤
    * min, max를 통해 특정 기간에서만 날짜 선택할 수 있게 할 수 있다.
      * <input type="date" min="2020-07-01" max="2020-07-31">
  * datetime : 날짜/시간 형식을 이용한 날짜와 시간 표시 컨트롤
  * datetime-local : 현지 날짜/시간
  * month : 월/연도
  * time : 시간
    * 시간을 입력할 수 있는 요소
  * week : 주와 연도를 선택할 수 있는 컨트롤
  * color : 색상 코드를 입력할 수 있는 컨트롤
  * email : 표준 이메일 주소를 입력받아 검증하는 컨트롤
    * required 속성을 설정하면 브라우저가 유효한 이메일 주소인지 검사(제출 버튼 누를 때 시행됨)
    * 여러 개 이메일 주소를 쉼표로 구분해 입력하고 싶을 때 multiple 속성을 지정한다.
  * tel : 전화번호를 입력받아 검증하는 컨트롤
    * 검증을 원하면 pattern에서 정규식 지정
    * ![image-20200925193913780](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200925193913780.png)
  * search : 검색어 입력 양식을 생성
    * text와 별반 다르지 않은 것 같지만, 브라우저가 검색이라는 것을 인식하면 다르게 취급할 수 있다.(?)
  * range : 2개의 숫자 사이의 숫자를 선택할 수 있는 슬라이더 컨트롤
    * min과 max로 최소값, 최대값 설정 가능
    * value로 초기값 설정 가능
  * number : 수자만 입력받는 컨트롤
    * max, min, step 속성으로 최대값, 최소값, 단계값 지정
    * ![image-20200925194209810](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200925194209810.png)
  * url : url만 입력받는 컨트롤
    * multiple 속성을 통해 하나 이상의 url 입력 가능
    * required를 통해 검증 작업 가능
* 추가된 속성
  * autocomplete : 자동으로 입력 완성
  * autofocus : 페이지 로드 시 자동으로 입력 포커스를 가짐
  * placeholder : 입력 힌트를 희미하게 보여줌
  * readonly : 읽기 전용 필드
  * required : 입력 양식 제출 전 반드시 채워져 있어야 함을 나타냄
  * pattern : 허용하는 입력 형태를 정규식으로 지정

* 정규식
  * 특정한 규칙을 가지고 있는 문자열을 표현하는 수식
  * 정규식 표현은 /와 / 내부에 위치
  * 메타문자
    * . (문자) : 한 개의 어떤 문자와도 일치
    * \d (숫자) : 한 개의 숫자와 일치
    * \w (문자와 숫자) : 한개의 문자나 숫자와 일치
    * \s (공백 문자) : 공백, 탭, 줄 바꿈, 캐리지 리턴 문자와 일치
    * ^ (시작) : 패턴의 시작을 표시
    * $ (끝) : 패턴의 끝을 표시
    * [] (문자의 종류, 문자의 범위) : [abc]는 a 또는 b 또는 c를 나타낸다. [a-z]는 a부터 z까지 중의 하나, [1-9]는 1부터 9까지 중의 하나를 나타낸다.
  * 수량 한정자(quantifier)
    * () (문자를 그룹핑한다.) : "abc|adc"와 "(a(b|d)c)"는 같은 의미를 가진다.
    * `*`(0회 이상 반복) : "a`*`b"는 "b", "ab", "aab", "aaab"를 나타낸다
    * `+` (1회 이상) : "a`+`b"는 "ab", "aab", "aaab"를 나타내지만 "b"는 포함 X
    * ? (0 또는 1회) : "a?b" 는 "b" 또는 "ab"를 나타낸다.
    * {m} (m회) : "a{3}b"는 "aaab"와 매칭



* 그 외 HTML Input 요소 정리 블로그

https://m.blog.naver.com/PostView.nhn?blogId=govlrhaehfdl&logNo=221230214889&proxyReferer=https:%2F%2Fwww.google.com%2F

* placeholder : 텍스트 박스에 회색글씨로 안내를 할 수 있는 속성



## EXERCISE



1. 2번

2. 3번

3. <video src="dog.mp4" width="300" height="200" autoplays controls></video>

4. 5. 


<video autoplay controls>
	<source src="http://media.w3.org/2010/05/bunny/movie.ogv" type="video/mp4">
    <source src="http://media.w3.org/2010/05/bunny/movie.ogv" type="video/webm">
    <source src="http://media.w3.org/2010/05/bunny/movie.ogv" type="video/ogg">
</video>

6~10은 exercise 폴더에 코드를 작성해서 저장해놓았다.