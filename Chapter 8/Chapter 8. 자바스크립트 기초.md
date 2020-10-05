# Chapter 8. 자바스크립트 기초

* 학습목표
  * HTML5의 공식적인 스크립트 언어인 자바스크립트의 기초적인 사항들을 살펴본다.
  * 자바스크립트 변수 선언 방법, 연산자 학습
  * 자바스크립트 조건문과 반복문 구조 이해
  * 자바스크립트 배열 생성 및 사용 학습



## 01. 자바스크립트 소개

* 사용자와 페이지 간의 상호작용이 이루어지는 동적인 웹 페이지 작성에 필요
* 자바스크립트는 웹 표준 프로그래밍 언어



* 자바와 자바스크립트의 차이
  * 자바
    * 소스 파일을 컴파일하여 실팽하는 컴파일 언어
    * 자바 가상 기계 위에서 실행
    * 별도의 소스 파일에 작성
    * 변수 타입을 반드시 작성해야 함
  * 자바스크립트
    * 브라우저가 소스 코드를 직접 해석해서 실행하는 인터프리트 언어
    * 브라우저 위에서 실행
    * HTML 파일 내에 삽입 가능
    * 변수 타입을 선언하지 않아도 사용 가능



* 자바스크립트 역사
  * 넷스케이프의 브랜드 아이크가 개발



* 자바스크립트 특징
  * 인터프리트 언어 : 컴파일 과정 필요없이 실행 가능
  * 동적 타이핑 : 변수의 자료형을 선언하지 않고도 사용할 수 있다.
  * 구조적 프로그래밍 지원 : C언어의 구조적 프로그래밍을 지원 (if-else, while, for 등 제어 구조 지원)
  * 객체 기반 : 객체 지향 언어(자바스크립트의 객체는 연관 배열)
  * 함수형 프로그래밍 지원 : 자바스크립트에서 함수는 일급 객체 (함수 그 자체로 객체)
    * 함수는 속성과 .call()과 같은 메서드를 가짐
  * 프로토타입 기반 : 자바스크립트는 상속을 위해 클래스 개념 대신 프로토타입을 사용



* 예시

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First JS</title>
</head>
<body>
    <script> /* 자바스크립트는 <script> ~ </script> 내에 기술된다. */
        var now = new Date(); /* 현재 시간을 가지고 있는 객체 생성 */
        document.write(now); /* 객체의 값을 화면에 표시 */
    </script>
</body>
</html>
```



## 02. 자바스크립트 용도

1. 이벤트에 반응하는 동작 구현
2. Ajax를 통해 전체 페이지를 다시 로드하지 않고서도 서버로부터 새로운 페이지 콘텐츠를 받거나 데이터를 제출할 때 사용
3. HTML 요소의 크기나 색상을 동적으로 변화 가능
4. 게임이나 애니메이션 같은 상호 대화적인 컨텐츠 구현
5. 사용자가 입력한 값을 검증하는 작업



* 예시 (버튼 클릭(이벤트) 시 동작)

```html
<!DOCTYPE html>
<html>
<head>
    <title>JS1</title>
</head>
<body>
    <p>자바 스크립트는 이벤트에 반응할 수 있다.</p>
    <input type="button" value="버튼을 누르세요!" onclick="alert('반갑습니다')">
    <!-- alert() 함수는 많이 사용되지 않으나, 가끔 출력 코드 작성 시 편리함 -->
    <!-- onclick 이벤트는 버튼이 클릭되면 발생하는 이벤트 -->
</body>
</html>
```



* 자바스크립트의 미래
  * 본래 클라이언트 웹 페이지를 위한 프로그래밍 언어였지만, 용도가 확장되고 있다.
    * Node.js
      * 자바스크립트를 서버 프로그램 언어로 변화시키려는 노력의 산물
      * Node.js는 웹 서버와 같은 애플리케이션을 작성하기 위해 설계된 서버-사이드 소프르웨어 시스템
      * 이벤트-구동형이고 비동기적 입출력을 채택해 병렬처리 코어가 많은 컴퓨터에 효율적으로 실행
      * 서버단 개발
    * JQuery
      * 자바스크립트 라이브러리의 JQuery는 브라우저 뿐만 아니라 모바일 장치에서도 인기
      * 클라이언트단 개발
    * JSON
      * 자바스크립트의 객체 표기법인 JSON(JavaScript Object Notation)은 개발 언어 독립적인 데이터 형식으로 데이터 전송용 XML을 대체하고 있다.
      * 문서 데이터베이스의 표준 저장 형식으로도 사용된다.
  * 즉 클라이언트에서 JQuery를 이용해 클라이언트 애플리케이션을 개발하고 JSON으로 서버와 데이터를 주고 받을 수 잇다. 또 서버에서는 Node.js를 통해 서버 프로그램을 개발한다.



## 03. 자바스크립트의 위치

자바스크립트도 HTML 문서에 3가지 방식으로 삽입할 수 있다.

1. 내부 자바스크립트 (script 태그 내부)

   * 자바스크립트는 script ~ /script 태그 내부에 위치한다.

   * 자바스크립트는 head나 body 섹션 안에 위치 가능하다.

   * ```html
     <!DOCTYPE html>
     <html>
     <head>
         <title>Document</title>
         <script>
             document.write("Hello World") /* head 섹션 내에 위치한 것이 더 바람직 */
         </script>
     </head>
     <body>
     
     </body>
     </html>
     ```

     * document.write()는 document 객체에 write 메서드를 호출하는 문장
     * 객체 : 속성과 동작을 한데 모아둔 것, 메서드 : 동작
     * document.write() 사용 시 주의할 점은 이것이 HTML 문서에 내용을 추가하는 메서드이지만 HTML 페이지가 완전히 로드된 후에 이를 호출하면 기존 HTML 문서의 내용을 모두 지우고 다시 쓴다.

2. 외부 자바스크립트 (.js 파일을 <script src=".js">로 연결)

   * 외부 자바스크립트 파일은 흔히 여러 웹페이지에서 공통적으로 사용하는 코드를 포함하고 있다.
   * 확장자 파일명은 .js 이다.
   * 이를 사용하기 위해서 <script> 태그의 src 속성으로 외부 스크립트 파일 이름을 입력하면 된다.
   * 외부 스크립트에서는 script 태그 사용 X, 순수한 자바스크립트 코드만을 사용

3. 인라인 자바스크립트 (button id="bt" onclick="")

   * HTML 태그 내부에 이벤트 속성으로 삽입 가능 (필요한 경우에만 사용하기)

   * ```html
     <!DOCTYPE html>
     <html>
     <head>
         <title>js inline</title>
     </head>
     <body>
         <button type="button" onclick="alert('반갑습니다')">버튼을 누르세요!</button>
     </body>
     </html><!DOCTYPE html>
     <html>
     <head>
         <title>js inline</title>
     </head>
     <body>
         <button type="button" onclick="alert('반갑습니다')">버튼을 누르세요!</button>
     </body>
     </html>
     ```

     

* 참고

  자바스크립트 소스를 입력하고 바로 출력을 받아보려면 콘솔 사용도 좋다.

  F12를 누르면 개발자 도구창이 등장하고 콘솔을 선택하면 된다.

  콘솔에서는 JS 소스를 입력하고 엔터키를 누르면 바로 실행되어 결과를 보여준다.



* JS를 head에 넣는 것과 body에 넣는 것의 차이점
  * 대원칙은 JS는 읽히면서 바로 실행됨
  * 따라서 head에 넣으면 body보다 먼저 실행되는 것이 보장된다.
  * 먄약 body 안에 배치 시 맨 아래 ㅇ



## 04. 문장

* 자바스크립트는 브라우저에 의해 실행되는 문장의 순서 있는 ㅣㅂ합이다.



* 문장
  * 자바스크립트 문장은 웹 브라우저에게 내리는 명령이라고 간주할 수 있다.
  * 문장은 웹 브라우저가 무엇을 해야 하는지를 지시한다.
  * 각 문장 끝에는 세미콜론(;)을 붙인다. 이것은 문장을 분리한다.
  * 세미콜론 생략도 가능하며, 줄이 바뀌면 문장이 끝난 것으로 간주한다.
  * 문장이 모여 코드가 되며, 각 문장은 브라우저에 의해 작성된 순서대로 실행된다.



* 블록

  * 자바스크립트 문장은 블록으로 묶일 수 있다. 

  * 블록은 {}이며 목적은 여러 개의 문장을 묶어 함께 실행하기 위함이다.

    {

    ​			document.write("Hello World!");

    ​			document.write("How are you?");

    }



* 문자 집합과 대소문자 구별
  * 자바스크립트는 유니코드 문자 집합 버전 3을 지원한다.
  * 유니코드는 전세계의 모든 문자를 나타낼 수 있다.
  * 자바스크립트는 대소문자를 구별한다. (HTML은 대소문자를 구분하지 않는다.)
  * 따라서 자바스크립트에서 HTML의 태그와 속성 이름은 소문자로 적어야 한다.
  * 자바스크립트는 공백 문자를 모두 무시한다.



* 주석문
  * 한 문장 주석은 //를 사용하면 된다.
  * 다중 문장 주석은 /* */ 를 사용하면 된다.



## 05. 변수

* 변수는 데이터를 저장하는 상자로 생각할 수 있다.

* 자바스크립트에서 변수 선언은 var로 선언한다.

  var = x ;

  * var : 변수가 선언된다는 것을 나타낸다.
  * x : 변수 이름, 스크립트에서 유일해야 한다.
  * ; : 세미콜론은 하나의 문장이 끝났음을 나타낸다.
  
* 변수 명명 규칙

  * 문자로 시작 (숫자 시작 x)

  * $나 _로 시작할 수 있다.

  * 대소문자 구분한다.

  * 자료형을 지정하지 않는다. (문자열은  ""나 ''로 사용해서 표현)

    var name = "Hong";

  * 자바스크립트에서 보통 낙타체를 사용한다.

  * 예시

    ```html
        <script>
            var x;
            x = "Hello World!"
            alert(x);
        </script>
    ```

    

* 한 줄에 여러 개 변수 선언

  var name = "Hong", age = 24, job = "student";



## 06. 자료형

* 변수가 가질 수 있는 값의 종류

  * 수치형(number) : 정수나 실수

    * 

  * 문자열(string) : 문자가 연결된 것 (텍스트)

    * 문자형 길이는 length 속성으로 알 수 있다.

      var s = "abc"; // s에 문자열 "abc"를 저장

      alert(s.length); // 3이 출력됨

    * `+` 연산자를 이용해 문자열을 합칠 수 있다.

    * 그 외 메서드 종류

      * charAt() : 첫 번째 문자

      * replace("old", "new") : old를 new로 변경

      * toUpperCase() : 대문자로 변경

      * 예시

            <script>
                var s = "Hello World!";
                var t = "How are you today?";
                document.write(s + "<br>"); 
                // alert는 알림창, document.write()는 홈페이지에 글로 나타냄
                document.write(t + "<br>");
                document.write(s.toUpperCase());
            </script>

  * 불형(boolean) : True 또는 False 값

  * 객체형(object) : 객체를 나타내는 타입, 호출 불가능

    * 기본 자료형(num, str, bool)을 제외하면 모두 객체형

    * 객체는 사물의 속성과 동작으 묶어서 표현하는 기법

    * 예로 자동차는 메이커, 모델, 색상, 마력과 같은 속성과 함께 출발하기, 정지하기 등의 모션이 존재

      ```html
      var myCar = { model : "benz", color : "white", hp : 100 };
      document.write(myCar.model + "<br>");
      document.write(myCar.color + "<br>");
      document.write(myCar.hp + "<br>");
      ```

  * 객체형(function) : 객체를 나타내는 타입, 호출 가능

  * Null(object)

  * undefined : 값이 정해지지 않은 타입

    * 변수는 선언되었지만, 값을 지정하지 않으면 나타나는 유형

  

  * 특정 값이 변수에 저장되는 순간 자료형은 내부적으로 결정된다.

  * 현재 변수가 저장하고 있는 종류는 typeof라는 연산자를 변수에 적용하면 알 수 있다.

    함수는 실제로 객체형이나 호출이 가능한 객체 타입을 function으로 출력한다.



## 07. 연산자

* 산술 연산자
  * `+` : 덧셈
  * `-` : 뺄셈
  * `*` : 곱셈
  * `/` : 나눗셈
  * `%` : 나머지
  * `++` : 증가
    * `++`x 또는 x`++` : x의 값 3일 때 3에서 4가 된다.
      * `++`x : x의 값을 먼저 증가시키고 증가된 x 값을 수식에 사용
      * x`++` : x의 이전 값을 수식에 사용 후 x 값을 증가
  * `--` : 감소
    * `--`x 또는 x`--` : x의 값 3일 때 3에서 2가 된다.
      * `--`x : x의 값을 먼저 감소시키고 증가된 x 값을 수식에 사용
      * x`--` : x의 이전 값을 수식에 사용 후 x 값을 감소



* 대입 연산자
  * 대입 연산자는 변수에 값을 할당한다. (z = x+y)
  * 복합 대입 연산자란 += 처럼 대입 연산자와 산술 연산자를 합친 것이다.
    * x += y 는 x = x + y 와 같다. (-, *, /, 5도 동일)



* 문자열에서 + 연산자
  * 결합하는 용도로 사용
  * 만약 문자열 + 숫자라면, 숫자가 문자열로 변환되어 합쳐진다.



* 비교 연산자 (조건문에서 많이 사용된다.)

  * 논리 문장에서 값들을 비교하는 용도로 사용

  * 종류

    * == : 값이 같으면 참
    * != : 값이 다르면 참
    * `>` : 크면 참
    * `<` : 작으면 참
    * `>=` : 크거나 같으면 참
    * `<=` : 작거나 같으면 참
    * === : 값과 타입이 모두 같으면 참
    * !== : 값이나 타입이 다르면 참

  * 예시

    if (age > 18)

    ​	msg = "입장 가능"



* 논리 연산자
  * 여러 개의 조건을 조합해서 참인지 거짓인지 따질 때 사용
    * && : and 연산
    * || : or 연산
    * ! : Not 연산



* 조건 연산자

  * 유일하게 3개의 피연산자를 가지는 삼항 연산자

    max_value = (x>y) ? x: y;

    * x>y 가 참이면 x가 수식의 값
    * 거짓이면 y가 수식의 값

    group = (age<30) ? "청년부" : "장년부";

    * age가 30보다 작으면(참) 청년부
    * age가 30보다 크면(거짓) 장년부



* 연산자 우선순위

![자바의 연산자 및 연산자 우선순위](https://t1.daumcdn.net/cfile/tistory/997A014D5A90B9B00D)



## 08. 숫자와 문자열 사이의 변환

* parseInt() : 문자열 -> 숫자
* String() : 숫자 -> 문자열
* prompt() : 사용자에게 어떤 사항을 알려주고 답변을 입력할 수 있는 윈도우를 화면에 띄운다. (입력한 사항은 모두 문자열로 저장된다.)



* 예제 1

```html
    <script>
        var x, y;
        var input;

        input = prompt("정수를 입력하시오", "정수");
        x = parseInt(input); // 문자열 input을 숫자형으로 변환
        
        input = prompt("정수를 입력하시오", "정수");
        y = parseInt(input);

        document.write(x+y + "<br>");
    </script>
```



* 예제 2

```html
<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
    <script>
        function calc() {
            // JS에서 HTML 요소에 접근하기 위해 document.getElementById(id) 메서드를 사용
            // 여기에서 값을 가져올 수 있거나, 값을 대입할 수 있다.
            var x = document.getElementById("x").value; // id가 "x"인 요소를 가져온다.
            var y = document.getElementById("y").value; // id가 "y"인 요소를 가져온다.
            var sum;
            sum = parseInt(x) + parseInt(y); // x와 y를 숫자형으로 바꾼 후 변환해서 합친다.
            document.getElementById("sum").value = sum; // id가 "sum"인 요소에 변수 sum의 값을 대입한다.
        }
    </script>
</head>
<body>
    <h3>덧셈 계산기</h3>

    <form name="myform" action="..." method="post">
        첫 번째 정수 : <input id="x"> <br>
        두 번째 정수 : <input id="y"> <br>
        합계 : <input id="sum"> <br>
        <input type="button" value="계산" onclick="calc();">
        // 버튼 클릭 시 calc() 라는 이름의 함수 호출
    </form>
</body>
</html>
```





* HTML 요소에 접근하기

document.getElementById(id) 메서드 사용

```html
<!DOCTYPE html>
<html>
<body>
    <h1 id="test">This is a heading.</h1>
    <script>
        function func() {
            e = document.getElementById("test"); // id가 "test"인 요소를 가져옴
            e.style.color = "red"; // id가 "test"인 요소 style 지정
        }
    </script>
    <button type="button" onclick = "func();">클릭하세요!</button>
</body>
</html>
```





## 09. 조건문

* 조건문 종류

  * if문 : 조건이 참일 때만 어떤 코드를 실행하고 싶을 때 사용

    if (조건식)

    ​	문장;

  * if...else문 : 조건이 참이면 어떤 코드를 실행하고 조건이 거짓이면 다른 코드를 실행하고 싶을 때 사용

    if (조건식)

    ​	문장1;

    else 

    ​	문장2;

  * switch문 : 많은 코드 중에서 하나를 선택해서 실행하고 싶은 경우 사용



* 연속적인 if문
  * else if를 사용 (python으로 치면 elif)

```html
    <script>
        var msg = "";
        var time = new Date().getHours(); // 웹 브라우저로부터 현재 시간을 얻는다.
        if (time < 12) {
            msg = "Good morning";
        }
        else if (time < 18) {
            msg = "Good Afternoon";
        }
        else {
            msg = "Good Night";
        }
        alert(msg);
    </script>
```



* switch문

  * 가능한 실행 경로가 여러 개인 경우 switch문 사용

    ```html
    <script>
    
    switch(제어식)
    
    {
    	// 제어식 값이 c1이면 실행
    ​	case c1:
    
    ​					문장1;
    
    ​					break;
    	// 제어식 값이 c2이면 실행
    ​	case c2:
    
    ​					문장2;
    
    ​					break;
    	// 일치하는 값이 없으면 시행
    ​	default:
    
    ​					문장d;
    
    ​					break;
    
    }
    </script>
    ```

    

    

## 10. 반복문

* while문

  * 주어진 조건이 만족되는 동안, 문장을 반복 실행하는 제어 구조

  * 형식

    while(조건식)

    ​	문장;

    * 조건식이 참이면, 문장을 실행한다.

  * ```html
    var i = 0;
    
    while (i < 10)
    {
                  document.write(i+"<br>")
                  i++;
                  }
    ```

* for문

  * 정해진 횟수만큼 반복

  * 초기식, 조건식, 증감식으로 구성 (세미콜론으로 분리됨)

  * 형식

    for (초기식; 조건식; 증감식;)

    ​	반복문장;

    * 초기식을 실행한 후 조건식의 값이 참인 동안, 반복문장 반복
    * 반복 끝날 때마다 증감식 실행

  * 예시 1

    ```javascript
    for (i=0; i<10; i++) // 초기식; 조건식; 증감식;
    {
                    document.write(i+"<br>"); // 반복되는 문장
    }
    ```

  * 예시 2
  
    ```javascript
    // 초기식은 콤마를 통해 여러 문장을 집어 넣을 수 있다.
    for (var i=0, len = fruits.length; i < len; i++) {
    	document.write(fruit[i] + "<br>")                                           
                                               }
    ```
  
  * 예시 3
  
    ```javascript
    // 초기식 생략도 가능하다.
    var i=2, len=fruit.length;
    for (; i < len; i++) {
        document.write(fruit[i] + "<br>")
    }
    ```
  
  * 예제 1 (h1부터 h6까지 반복)
  
    ```javascript
    // h1부터 h6까지 반복시킬 수도 있다.
    var i = 1;
    for (i = 1; i < 7; i++) {
        document.write("<h" + i + ">header" + i +"</h" + i + ">")
    }
    ```
  
  * 예제 2 (온도 변환기)
  
    ```javascript
        <table border="3">
            <tr>
                <td>섭씨온도</td>
                <td>화씨온도</td>
            </tr>
            <script>
                for (celsius=0; celsius < 11; celsius++) {
                    document.write("<tr><td>" + celsius + "</td><td>" + ((celsius * 1.8) + 32) + "</td></tr>");
                }
            </script>
        </table>
    ```
  
    
  
  * 예제 3 (중첩 반복문, 구구단)
  
    ```javascript
    document.write("<h1> 구구단표 </h1>")
    document.write("<table border='2' width=50%>")
    // 루프 중첩 시 서로 다른 변수를 사용해야 한다.
    for (var i = 1; i <= 9; i++) {
        document.write("<tr><td>" + i + "</td>");
        for (var j = 2; j <= 9; j++) {
            document.write("<td>" + i * j + "</td>")
        }
        document.write("</tr>")
    }
    ```
  
  * 예제 4 (do/while 루프)
  
    ```javascript
    // while문과 유사하나 조건을 루프 끝에서 검사한다는 점이 다르다. (문장을 한 번 실행하고 검사한다.)    
    	<script>
            var i = 0;
            do {
                document.write("카운터 : " + i + "<br>");
                i++;
            } while(i < 10); // while() 끝에 ;를 꼭 붙여야 한다.
        </script>
    ```
  
  * 예제 5 (for/in 루프)
  
    ```javascript
    // for/in 루프는 객체 안 속성들에 대해 어떤 처리를 반복할 수 있는 구조
    for (변수 in 객체) // 변수에 객체 속성이 하나씩 대입되면서 반복된다.
        {
            문장;
        }
    
    // 예제
    <script>
        var myCar = {make : "BMW", model : "X3", year : "2013"};
    	var txt = "";
    	for (var x in myCar) {
        	txt += myCar[x] + " "; // []가 인덱스같은 역할인지 확인하기
    	}
    	document.write(txt);
    </script>
    ```
  
  * 예제 6 (break 문장)
  
    ```javascript
    // break는 반복문을 빠져나오기 위해 사용
    for (var i = 0; i < 10; i++) {
        // 3에서 멈춤
        if (i == 3) {
            break;
        }
        document.write(i + "<br>")
    }
    ```
  
  * 예제 7 (continue 문장)
  
    ```javascript
    // 현재 실행하고 있는 반복 과정의 나머지를 생략하고 다음 반복을 시작하게 만드는 문장
    for (var i = 0; i < 10; i++) {
        // 3 생략
        if (i == 3) {
            continue;
        }
        document.write(i + "<br>")
    }
    ```
  
    