# Chapter 9. 자바스크립트 객체

* 학습 목표
  * 자바스크립트 객체 개념 학습
  * 객체 생성 방법  2가지 학습
  * JS에 내장되어 있는 유용한 객체 학습
  * String 객체, Date객체, Array 객체 학습



## 1. 객체

* 객체란? 
  * 가장 기초적인 자료형 (문자열, 숫자형, 불형 모두 객체처럼 구현되어 있음)
  * 객체 지향 기술의 핵심 개념 (실제 세상에 존재하는 사물을 모델링한 것)
  * 객체는 데이터와 동작을 가지고 있음
    * 데이터 : 객체가 가지고 있는 특성값 (자동차의 모델, 제조사, 마력, 색상, 연식, 속도 등)
    * 동작 : 객체가 수행할 수 있는 행동 (자동차의 출발하기, 감속하기, 가속하기 등)
  * 즉, 객체 지향 프로그래밍이란 데이터와 동작을 하나로 합쳐서 프로그램을 작성하는 기법
  * JS에서 객체의 데이터와 동작은 각각 변수와 함수로 표현 가능
    * 객체 : 속성 + 메서드
    * 속성 : 객체 안의 변수 (외부 세계로부터는 감쳐져 있음, 다른 객체에 의해 변경되는 것 방지)
    * 메서드 : 객체 안의 함수 (객체 내부의 변수에 언제든지 접근 가능)





# 2. 객체 생성 및 사용

* 객체의 종류
  1. 내장 객체 (Date, String, Array, document(HTML을 나타내는 객체) 등)
     * 생성자가 미리 작성되어 있다.
  2. 사용자 정의 객체
     * 사용자가 생성자를 정의한다.



* 객체 생성 방법
  1. 객체를 객체 상수로부터 직접 생성
  2. 생성자 함수를 이용해 객체를 정의,  new를 통해 객체의 인스턴스를 생성



> JS에는 클래스가 없다. (다른 객체 지향 언어에서는 클래스를 정의하고 이를 설계도로 삼아 객체를 찍어냄)
>
> JS에는 모든 것이 객체이고, 생성자 함수가 클래스 역할을 흉내낸다.



* 객체 상수로부터 객체 생성 (간단하지만 객체 하나만 생성 가능, 싱글톤이라 부름)

  ```javascript
  var myCar = {
      model: "520d",
      speed: 60,
      color: "red",
      break: function () { this.speed -= 10; },
      accel: function () { this.speed += 10; }
  }
  
  myCar.color = yellow; // 속성 접근
  myCar.break(); // 메서드 접그
  ```

  

* 생성자 함수를 이용한 객체 생성
  * 사용자 정의 객체 : 자신만의 객체 생성 방법 (생성자라는 특별한 함수 필요)
  * 생성자 : 객체를 초기화하는 역할(객체를 생성하는 연산자 : new)
  * 장점 : 개발자가 원하는 만큼의 객체를 생성할 수 있다.
  * 내장 객체는 이미 생성자 함수가 작성되어 있으므로, new를 통해 객체를 생성하고 사용하면 된다.

```javascript
// 생성자도 함수 (생성자 이름은 항상 대문자)
function Car(model, speed, color) {
    // 객체의 속성 (model, speed, color)
    // this 키워드로 일반 변수와 객체 속성을 구분 (코드를 실행하는 현재 객체를 의미)
    // this 붙은 변수는 속성, this 붙은 함수는 메서드
    this.model = model;
    this.speed = speed;
    this.color = color;
    // 객체 메서드
    this.break = function () {
        this.speed -= 10;
    }
    this.accel = function () {
        this.speed += 10;
    }
}

// 생산자 정의 후 다음과 같이 객체 생성 가능
// 즉, 객체를 생성하려면 new 연산자를 사용한 후 그 뒤에 생성자를 호출하는 코드를 작성하면 된다.
var myCar = new Car("520d", 60, "red"); // new연산자는 새로운 객체 생성
myCar.color = "yellow"; // 속성 호출
myCar.break(); // 메서드 호출
```



* 객체 멤버 사용
  * 객체 내 속성과 메서드를 객체 멤버라고 부른다.
  * 객체 멤버 사용을 위해 . 을 이용한다. 
    * 어떤 객체에 속한지 말하고, 그 후 멤버 이름을 말하는 순서

```javascript
myCar.color = "yellow"; // myCar : 소속, color : 멤버(속성)
myCar.break(); // myCar : 소속, break() : 멤버(메서드)
```



* Q&A

  * JS에 클래스가 없는 이유

    * 입력되는 즉시 실행되야 하는 인터프리터 언어에서 클래스를 정의하고 사용하는 것이 어렵기 때문
    * 대신 클래스 역할을 하는 프로토타입이 존재

  * 객체 생성을 위해 항상 생성자를 먼저 작성해야 하는지?

    * X, JS에서는 객체 상수를 가지고 직접 객체 생성 가능
    * 그러나 이 경우에는 여러 개의 객체를 생성하는 것이 번거러움

    

```javascript
// 객체 활용 예시
<script>
     	// 생성자 생성 및 매개변수 선언
        function Car(model, speed, color) {
    		// 속성 및 메서드 정의
            this.model = model;
            this.speed = speed;
            this.color = color;
            this.break = function() {
                this.speed -= 10
            }
            this.accel = function() {
                this.speed += 10
            }
        }
		// new 연산자를 통해 새로운 객체 생성
        var myCar = new Car("520d", 60)
		
        // 출력
        document.write("모델:" + myCar.model + " 속도:" + myCar.speed + "<br>")
        myCar.accel(); // accel() 메서드 사용
        document.write("모델:" + myCar.model + " 속도:" + myCar.speed + "<br>")
        myCar.break(); // break() 메서드 사용
        document.write("모델:" + myCar.model + " 속도:" + myCar.speed + "<br>")
    </script>
```



* 기존 객체에 속성과 메서드 추가 (기존 생성자 함수 변경 필요 X)

```javascript
// 기존 myCar 객체가 있다고 가정
myCar.turbo = true;
myCar.showModel = function () {
    alert("모델은 " + this.model + "입니다.")
}
```



## 03. 프로토타입

* 속성과 메서드를 여러 객체와 공유하는 것이 필요할 때 사용



* 예시 (JS로 게임 개발을 한다고 가정)

```javascript
// 점을 나타내는 객체 필요
function Point(xpos, ypos) {
    this.x = xpos;
    this.y = ypos;
    // getDistance()는 원점으로부터 거리를 계산하는 함수
    this.getDistance = function() {
        return Math.sqrt(this.x * this.x + this.y * this.y); // sqrt는 제곱근 함수
    };
}

// 이를 통해 필요한 만큼 객체를 생성
var v1 = new Point(10, 20);
var v2 = new Point(10, 30);

/* 이렇게 실행해도 문제는 없지만, 생성되는 모든 Point 객체는 내부에 getDistance() 메서드를 가짐
이러면 메모리 낭비가 극심, 따라서 getDistance() 메서드를 모든 객체가 공유하면 된다. */


//객체는 자신만의 데이터는 가져야 하지만, 메서드는 가급적 서로 공유하는 편이 좋다. (다른 언어에선 클래스)
//JS에서는 프로토타입을 통해 클래스를 대체한다. (여러 객체가 공유하는 메서드를 정의)
```



* 프로토타입
  * 자바스크립트의 모든 객체는 prototype이라는 숨겨진 객체를 가짐 (이를 통해 공유되는 메서드 작성)

```javascript
function Point(xpos, ypos) {
    this.x = xpos;
    this.y = ypos;
}
// Point 안에 prototype이라는 숨겨진 객체 존재
// prototype에 getDistance()를 정의하면 Point객체는 모두 이 메서드를 공유
// getDistance()는 특정 객체에 정의되는 것이 아니라 prototype 내에 정의됨 (Point를 이용해 객체가 아무리 많이 생성되어도, getDistance()는 하나만 존재)
Point.prototype.getDistance = function () {
    return Math.sqrt(this.x * this.x + this.y + this.y);
};

var p1 = new Point(10, 20)
p1.getDistance();

var p2 = new Point(10, 30)
p2.getDistance();

// 프로토타입 예제
<script>
        function Point(xpos, ypos) {
        this.x = xpos;
        this.y = ypos;
    }
	// 메서드 공유 (Point.prototype.shared = 10; 과 같이 속성도 공유 가능)
    Point.prototype.getDistance = function() { 
        return Math.sqrt(this.x * this.x + this.y * this.y);
    };

    var p1 = new Point(10, 20);
    var d1 = p1.getDistance(); // 변수에 값을 저장해야 사용 가능

	var p2 = new Point(10, 30);
	var d2 = p2.getDistance(); // 변수에 값을 저장해야 사용 가능

	document.writeln(d1 + "<br>");
	document.writeln(d2 + "<br>");

/*
document.write("문자열")
자바스크립트를 사용하여 문서에 해당 문자열을 출력한다.
document.writeln("문자열")
write와 동일한 기능을 하며 단 <pre>태그내에서 사용될 경우 자동줄바꿈을 해준다.
*/

</script>
```

* 용어 정리
  * 인스턴트 속성 및 메서드 : 객체가 소유한 속성 및 메서드
  * 클래스 속성 및 메서드 : 객체들 사이에서 공유되는 속성 및 메서드



* 프로토타입 체인

> 1. 객체 안에 속성이나 메서드가 정의 되었는지 확인
> 2. 객체 안에 정의가 안되어있으면 객체의 prototype이 속성이나 메서드를 가지고 있는지 확인
> 3. 원하는 속성 / 메서드를 찾을 때까지 프로토타입 체인을 따라서 올라간다.
>
> Point -> Point.prototype -> Object.prototype (Point는 임의의 객체 이름, 여기에도 없으면 Error)
>
> 프로토타입 체인은 `_proto_` 속성을 이용해 연결



* Object 객체

  * 자바스크립트 객체의 부모가 되는 객체

  * 객체 내부에 Object 객체의 속성과 메서드를 가짐

  * 속성 / 메서드

    * constructor : 속성으로 생성자 함수를 가리킨다.

      var d = new Date();

      d.constructor는 Date()와 같다.

    * valueOf() ; 메서드로서 객체를 숫자로 변환

    * toString() : 메서드로서 객체의 값을 문자열로 변환

    * hasOwnProperty() : 전달 인수로 주어진 속성을 가지고 있으면 true 반환

    * isPrototypeOf() : 현재 객체가 전달 인수로 주어진 객체의 프로토타입이면 true 반환



## 04. 자바스크립트의 내장 객체

> * Date 객체
>   * 날짜와 시간 작업을 하는데 사용
>
> ```javascript
> var today = new Date(); // 현재 날짜를 가진 객체를 생성
> ```
>
> ​	
>
> * Date 객체 생성자
>
> ```javascript
> new Date() // 현재 날짜와 시간
> new Date(milliseconds) // 1970/01/01 이후의 밀리초
> new Date(dateString) // 다양한 문자열
> new Date(year, month, date[, hours[, minites[, seconds[, ms]]]]) // 연, 월, 일, 시, 분, 초, 밀리초 (월은 0부터 시작)
> 
> // 예시
> <script>
> 	var d1 = new Date(2012, 2, 2, 9, 0, 0) // 4번
>     alert(d1)
>     var d2 = new Date("January 20, 2013, 09:00:00") // 3번
>     alert(d2)
> </script>
> ```
>
> 
>
> * Date 메서드
>
> ```javascript
> getDate() (1-31)
> getDay() (0-6)
> getFullYear() (4개의 숫자로 된 연도)
> getHours() (0-23)
> getMilliseconds() (0-999)
> getMinutes() (0-59)
> getMonth() (0-11)
> getSeconds() (0-59)
> 
> setDate()
> setDay()
> setFullYear()
> setHours()
> setMilliSeconds()
> setMinites()
> setMonth()
> setSeconds()
> 
> getXXX() : 접근자로서 객체 속성을 추출하는데 사용
> setXXX() : 설정자로서 객체 속성을 설정하는데 사용
> toXXXString() : 날짜를 특정 문자열 형태로 변환하는데 사용
> ```
>
>  
>
> *  두 개의 날짜 비교
>   * 모든 날짜를 1970/01/01 이후 밀리초로 변환 (getTime() 사용)
>   * 날짜 간격 구할 때 밀리초 차이값을 (1000* 60 * 60 * 24)로 나누면 된다.
>
> ```javascript
> <!DOCTYPE html>
> <html>
>     <script>
>         function checkDate() {
>             var s = document.getElementById("pdate").value; // 문자열 (객체 X)
>             var pdate = new Date(s);
>             var today = new Date();
>             var diff = today.getTime() - pdate.getTime();
>             var days = Math.floor(diff/(1000*60*60*24));
>             if (days > 30) {
>                 alert("환불 불가");
>             }
>             else if (days >= 0) {
>                 alert("환불 가능");
>             }
>             else {
>                 alert("잘못 입력")
>             }
>         }
>     </script>
> <body>
>     <input type="date" id="pdate">
>     <button onclick="checkDate()">검사</button>
> </body>
> </html>
> ```
>
> 
>
> * 카운트다운 타이머 만들기 (지금부터 특정 날짜까지 남은 날짜를 표시하는 코드)
>
> ```javascript
> <div id="remaining"></div>
> 	<script>
>     	function datesUntilnewYear() {
>     		var now = new Date();
>     		// 내년 1월 1일 변수 선언 (getFullYear() : 4개의 숫자로 된 연도 반환)
>     		var newYear = new Date("January 1, " + (now.getFullYear() + 1));
>     		var diff = newYear - now; // diff는 밀리초 단위
> 
>             var milliseconds = Math.floor(diff % 1000);
>             diff /= 1000;
>             var seconds = Math.floor(diff % 60);
>             diff /= 60;
>             var minites = Math.floor(diff % 60);
>             diff /= 60;
>             var hours = Math.floor(diff % 24);
>             diff /= 24;
>             var days = Math.floor(diff);
> 
>             var outStr = "내년도 신정까지 " + days + "일, " + hours + "시간, " + minites + "분, " + seconds + "초, 남았습니다."
>             // HTML 요소에 접근해서 시간을 계속 변경하여 출력하려면 innerHTML을 사용해야 한다.
>             document.getElementById("remaining").innerHTML = outStr;
>     		// setTimeout : 1초(1000ms)가 지나면 다시 함수를 호출한다.
>     		setTimeout("datesUntilnewYear()", 1000); // 1
>             }
> 		datesUntilnewYear();
> 	</script>
> 
> ```
>
> * JS 입출력 메서드 종류
>
> ```javascript
> ● document.write( )  
> : ()안에 것을 화면에 출력하라는 메서드
> ● window.alert()     
> : 경고창을 띄워 ()안의 것을 출력하라는 메서드
> ● innerHTML=" "       
> : 예를 가지고 이해하는 것이 빠르다. 
> 예를 들어 HTML로 [홍길동]이라는 콘텐츠를 화면에 출력하였다.
> 이 HTML 요소에 접근하여 [홍길동]을 [이순신]으로 바꿔 출력하게 만들려면 이 속성을 사용해야 한다. 그리고 HTML 요소에 접근하려면 document.getElementById 메서드를 함께 사용한다.
> ```
>
>  
>
> * 시계 만들기
>
> ```javascript
> <div id="clock"></div>
> 
> <script>
>     function setClock() {
>     var now = new Date();
>     var s = now.getHours() + ":" + now.getMinutes() + ":" + now.getSeconds();
>     
>     document.getElementById("clock").innerHTML = s;
>     setTimeout("setClock()", 1000); // 1000ms(1초)는 주기
> }
> 	setClock();
> </script>
> ```
>



> * Number 객체
>   * 수치형 값을 감싸서 객체로 만들어주는 랩퍼 객체
>     * 랩퍼 객체 : 수치값을 직접 사용할 수는 없고, 반드시 객체가 필요한 경우 사용
>
> ```javascript
> // 숫자 7을 가지고 있는 Number 객체를 생성 
> var num = new Number(7);
> 
> // 1.234를 감싸는 랩퍼 객체 생성
> 1.234.toString();
> ```
>
>   
>
> * Number 객체 속성 종류
>   * MAX VALUE : 표현할 수 있는 가장 큰 값
>   * MIN VALUE : 표현할 수 있는 가장 작은 값
>   * NaN : "Not a Number" 의 약자
>
>  
>
> * Number 객체의 메서드 종류
>
>   * toExponential([digits]) : 지수형으로 반환, 인수는 소수점 이하의 숫자 개수
>
>   ```javascript
>   var num = 1232.34567;
>   document.writeln(num.toExponential() + "<br>"); // 1.23234567e+3 (1232.34567)
>   document.writeln(num.toExponential(1) + "<br>"); // 1.2e+3 (1200)
>   ```
>
>   
>
>   * toFixed([digits]) : 고정소수점 방식으로 반환, 인수는 소수점 이하의 숫자 개수 (반올림)
>
>   ```javascript
>   var num = 123.456789;
>   document.writeln(num.toFixed() + "<br>") // 123
>   document.writeln(num.toFixe(1) + "<br>") // 123.5
>   ```
>
>   
>
>   * toPrecision([precision]) : 유효숫자 수를 지정
>
>   ```javascript
>   var num = 123.456789;
>   document.writeln(num.toPrecision(1) + "<br>") // 1e+2 (100)
>   document.writeln(num.toPrecision(2) + "<br>") // 1.2e+2 (120)
>   ```
>
>   
>
>   * toString([radix]) : 주어진 진법으로 숫자 반환
>
>   ```javascript
>   var num = 255;
>   document.writeln(num.toString() + "<br>"); // 255 (default는 10진법)
>   document.writeln(num.toString(16) + "<br>"); // ff
>   document.writeln(num.toString(8) + "<br>"); // 377
>   document.writeln(num.toString(2) + "<br>"); // 11111111
>   ```



> * String 객체
>
>   * String 객체의 속성 종류
>     * length : 문자열의 길이 (회원가입 시 아이디 6글자 이상을 요구할 때 length 이용)
>
>   ```javascript
>   <!DOCTYPE html>
>   <html>
>   <head>
>       <script>
>           function idchecking() {
>               var s = document.getElementById("idtext").value;
>               if (s.length < 6) {
>                   alert("아이디는 6글자 이상이여야 합니다.")
>               }
>           }
>       </script>
>   </head>
>   <body>
>       <div>
>           아이디 : <input type="text" size="10" id="idtext"> <input type="button" value="검사" onclick="idchecking()">
>       </div>
>   </body>
>   </html>
>   ```
>
>   
>
> * 대소문자 변환
>
>   * toUpperCase() 와 toLowerCase()를 사용하면 문자열 글자를 대문자와 소문자로 변환 가능
>   * 이는 비파괴 함수이기 때문에 원본은 그대로 유지되므로 새로운 변수에 저장하거나, 함수를 사용한채로 입력을 해놓아야 출력 시에 적용이 된다. (Python과 동일)
>
>   ```javascript
>   <script>
>       var s1 = "aBcDeF".toLocaleLowerCase(); // abcdef
>   	var s2 = "AbCdEf".toLocaleUpperCase(); // ABCDEF
>   
>   	document.write(s1 + s2);
>   </script>
>   ```
>
>  
>
> * 문자열 붙이기
>
>   * concat() 메서드는 하나의 문자열을 다른 문자열과 합친다. (새로운 문자열 생성, +와 동일한 결과)
>
>   ```javascript
>   <script>
>       var s1 = "문자열1";
>       var s2 = "문자열2";
>       var s3 = s1.concat(s2);
>   
>       document.write(s3) // 문자열1문자열2
>   </script>
>   ```
>
>  
>
> * 문자열 검색
>
>   * indexOf() 메서드느 문자열 안에서 주어진 텍스트가 처음 등장하는 위치를 반환
>
>   ```javascript
>   // 자바스크립트 인덱스가 시작점이 0, 1 중 무엇인지 확인
>   <script>
>       var s = "자바스크립트에 오신 것을 환영합니다.";
>       var n = s.indexOf("환영");
>       document.writeln(n + "<br>"); // 14 (책에서 답은 15)
>   </script>
>   ```
>
>  
>
> * 문자열 매칭
>
>   * match() 메서드는 문자열 안에서 일치하는 콘텐츠를 탐색하는데 사용
>   * match()에서는 정규식 사용 가능 (?, *, ^ 등 사용 가능)
>
>   ```javascript
>   <script>
>       var str = "Like father, like son."
>       // like를 탐색. i와 g는 옵션으로 insesitive(둔감한), globally를 의미.
>       result = str.match(/like/ig);
>       document.write(result + "<br>")
>   </script>
>   ```
>
>  
>
> * 문자열 대체
>
>   * replace()는 문자열 안에서 주어진 값을 다른 값으로 대체
>   * replace()도 정규식 사용 가능
>
>   ```javascript
>   <script>
>   	var s = "Hong's number is 123-4567";
>   	var result = s.replace("Hong's", "Kim's");
>   	document.write(result + "<br>");
>   </script>
>   
>   // 대소문자 관계없이 변경을 원할 때
>   // var result = s.replace(/Hong's/i, "Kim's")
>   // Hong's를 Kim's로 변경 (대소문자 모두 바껴도 가능)
>   ```
>
>  
>
> * split(delimiter[, limit])
>
>   * split()은 첫 번째 인수를 분리자로 하여 문자열을 분리 후 각 항목을 가지고 있는 배열로 반환
>
>   ```javascript
>   <script>
>       var s = "One,Two,Three,Four,Five";
>       var array = s.split(",");
>       for (i=0; i < array.length; i++) {
>           document.write((i+1) + "-" + array[i] + "<br>");
>       }
>   </script>
>   ```
>
>  
>
> * HTML 랩퍼 메서드
>
>   * 문자열을 적절한 HTML 태그로 감싼 후 반환
>
>   ```javascript
>   <script>
>       var s = "This is a test";
>       document.write("Big: " + s.big() + "<br>");
>       document.write("Small : " + s.small() + "<br>");
>       document.write("Bold : " + s.bold() + "<br>");
>       document.write("Italic : " + s.italics() + "<br>");
>       document.write("Fixed : " + s.fixed() + "<br>");
>       document.write("Strike : " + s.strike() + "<br>");
>       document.write("Fontcolor : " + s.fontcolor("green") + "<br>");
>       document.write("Fontsize : " + s.fontsize(6) + "<br>");
>       document.write("Subscript : " + s.sub() + "<br>");
>       document.write("Superscript : " + s.sup() + "<br>");
>       document.write("Link : " + s.link("http://www.google.co.kr") + "<br>"); 
>   	// target=_blank로 설정됨
>   </script>
>   ```
>
>   <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201009223819364.png" alt="image-20201009223819364" style="zoom:67%;" />
>
>    
>
> * 문자열 리터럴과 문자열 객체
>
>   * 문자열 종류 2가지 (리터럴과 객체)
>     * 리터럴 : ""(큰따옴표)로 생성
>     * 객체 : new 키워드로 생성
>
>   ```javascript
>   <script>
>       var sLiteral = "문자열 리터럴";
>       sObject = new String("문자열 객체");
>   
>       document.writeln(typeof (sLiteral) + "<br>"); // string
>       document.writeln(typeof (sObject) + "<br>"); // object
>   	
>       // 문자열 리터럴도 String 객체의 모든 속성과 메서드 사용 가능
>       // 자바스크립트가 임시적으로 문자열 상수를 문자열 객체로 형변환을 하기 때문
>       sLiteral += "123"
>       document.writeln(sLiteral + "<br>");
>   </script>
>   ```
>
>   * String 객체가 함수로 전달될 때 값(value)만 전달 (함수 안에서 전달받은 문자열을 변경해도 원본은 유지)
>
>   ```javascript
>   // 원본 유지 테스트
>   <script>
>       var sLiteral = "문자열 리터럴";
>       var sObject = new String("문자열 객체");
>   
>       function change(strlit, strobj) {
>           strlit = "Hello World";
>           strobj = "Hello World";
>       }
>   	
>   	// 함수 안에서 전달받은 문자열 변경
>   	change(sLiteral, sObject);
>   	// 원본 유지
>       document.writeln(sLiteral + "<br>"); // "문자열 리터럴"
>       document.writeln(sObject + "<br>"); // "문자열 객체"
>   </script>
>   ```
>
>  
>
> * Math 객체
>
>   * 수학적 작업을 위한 객체 (생성자가 아닌 객체, new 키워드 사용 필요 X)
>   * 상수 종류
>     * E : 오일러 상수 (약 2.718)
>     * LN2 : 자연 로그 (밑수: 2) (약 0.693)
>     * LN1 : 자연 로그 (밑수: 10) (약 2.302)
>     * Pi : 파이 상수 (약 3.14)
>     * SQRT1_2 : 1/2의 제곱근 (약 0.707)
>     * SQRT2 : 2의 제곱근 (약 1.414)
>   * 메서드 종류
>     * abs(x) : 절대값
>     * acos(x), asin(x), atan(x) : 아크 삼각함수
>     * ceil(x), floor(x) : 실수를 정수로 올림, 내림 함수
>     * cos(x), sin(x), tan(x) : 삼각함수
>     * exp(x) : 지수함수
>     * log(x) : 로그함수
>     * max(a,b,c,d ...) : 최대값
>     * mint(a,b,c,d ...) : 최소값
>     * pow(x,y) : 지수 함수 ( x^y)
>     * random() : 0과 1 사이의 난수값 반환
>     * round(x) : 반올림
>     * sqrt(x) : 제곱근
>
>   ```javascript
>   <!DOCTYPE html>
>   <html>
>       <head>
>         <script>
>             function calc(type) {
>                 var x = Number(document.calculator.number.value); // x는 document의 calculator(form)의 number(입력) 값이다.
>                 var y;
>                 if (type == 1) {
>                     y = Math.sin((x * Math.PI) / 180.0)
>                 }
>                 else if (type == 2) {
>                     y = Math.log(x);
>                 }
>                 else if (type == 3) {
>                     y = Math.sqrt(x);
>                 }
>                 else if (type == 4) {
>                     y = Math.abs(x);
>                 }
>                 document.calculator.result.value = y; // document의 calculator(form)의 result(계산 결과)의 값은 y이다.
>             }
>         </script>
>     </head>
>     <body>
>         <form name="calculator">
>             입력 : <input type="text" id="number"> <br>
>             계산 결과 : <input type="text" id="result"> <br>
>             <input type="button" value="SIN" onclick="calc(1)">
>             <input type="button" value="LOG" onclick="calc(2)">
>             <input type="button" value="SQRT" onclick="calc(3)">
>             <input type="button" value="ABS" onclick="calc(4)">
>         </form>
>     </body>
>   </html>
>   ```
>
>   

## 05. Array 객체

* JS에서 Array 특징 3가지

  1. 배열 크기가 자동으로 조절된다.

     ```javascript
     var myArray = new Array();
     myArray[0] = "Apple";
     myArray[99] = "banana";  // 배열의 99번째 요소에 데이터를 추가하면 myArray 배열의 크기가 100으로 변한다. (0과 99의 사이는 빈 값)
     ```

     

  2. 여러 가지 자료형을 혼합해서 저장 가능하다.

     ```javascript
     var myArray = new Array();
     myArray[0] = "Apple"; // 문자열 저장
     myArray[1] = 3.14; // 실수 저장
     myArray[2] = new Date(); // 객체 저장
     ```

     

  3. 배열 크기보다 큰 인덱스 값으로 배열 요소에 접근하면 오류가 발생하지 않고, undefined 값이 반환된다.

``` javascript
// 배열 생성 방법 3가지
<script>
    function printArray(myArray) {
        document.write("[")
        for (var i=0; i < myArray.length; i++) {
            document.write(myArray[i] + " ")
        }
        document.write("]" + "<br>")
    }

    var myArray1 = new Array();
    myArray1[0] = "apple";
    myArray1[1] = "banana";
    myArray1[2] = "orange";

    var myArray2 = new Array("apple", "banana", "orange");

    var myArray3 = ["apple", "banana", "orange"];

    printArray(myArray1);
    printArray(myArray2);
    printArray(myArray3);
</script>
```



* Array 속성과 메서드

  * 속성

    * length

  * 메서드

    * concat(value1[value2[value3...]])

      * 전달된 인수를 배열 끝에 추가

      * ```javascript
        <script>
            var x = [1, 2, 3]; 
            var y = [4, 5, 6];
            var z = x.concat(y);
            document.write(z) // 1,2,3,4,5,6
        </script>
        ```

    * indexOf(searchStr[, startIndex])

      * 요소의 값을 가지고 요소의 인덱스를 찾을 때 사용

      * ```javascript
        <script>
            var fruits = ["apple", "banana", "orange"];
            document.write(fruits.indexOf("banana")); // 1
        </script>
        ```

    * push(value), pop()

      * push()는 스택에 데이터를 삽입하는 메서드

      * pop()은 스택에서 데이터를 꺼내는 메서드

      * 스택은 선입후출 구조

      * ```javascript
        <script>
            var a = [1,2,3,4,5,6]
            a.pop()
            document.write(a, "<br>") // 1,2,3,4,5
            a.push(7)
            document.write(a, "<br>") // 1,2,3,4,5,7
        </script>
        ```

    * shift(), unshift()

      * shift()는 배열의 첫 번째 요소를 반환하고 첫 번째 요소를 배열에서 제거

      * unshift()는 새로운 아이템을 배열 맨 앞에 추가

      * 이를 통해 큐를 구현할 수 있음 (선입선출)

      * ```javascript
        <script>
            var a = [1,2,3,4,5,6,7,8,9,10]
        
            document.write(a.shift(), "<br>") // 1
            document.write(a, "<br>") // 2,3,4,5,6,7,8,9,10
        
            a.unshift(100)
            document.write(a, "<br>") // 100,2,3,4,5,6,7,8,9,10
        </script>
        ```

    * sort()

      * 배열을 알파벳 순으로 정렬(default)

      * 사용자 기준으로 지정하려면 sort()에 정렬 기준 함수를 제공해야 함

      * 수치값으로 정렬하려면 function(a,b) { return a-b } 라는 정렬 기준 함수를 인수로 제공해야 함

      * ```javascript
        <script>
            var a = [10, 7, 23, 99, 169, 19, 11, 1];
            a.sort()
            document.write(a, "<br>"); // 1, 10, 11, 169, 19, 23, 7, 99
        	// 수치갑으로 정렬하기 위한 정렬 기준 함수를 인수로 제공
            a.sort(function (a,b) {return a-b}) 
            document.write(a, "<br>") // 1, 7, 10, 11, 19, 23, 99, 169
        </script>
        ```

      * ![image-20201010114035534](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201010114035534.png)

      * ![image-20201010114059020](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201010114059020.png)

      * ![image-20201010114133866](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201010114133866.png)

    * Array.slice([begin[, end]])

      * 배열 일부를 복사해서 새로운 배열로 반환 (시작 인덱스 default는 0, 종료 인덱스가 없으면 끝까지 복사)

      * ```javascript
            <script>
                var a = [1,2,3,4,5,6,7,8,9,10];
                var b = a.slice(5, 8); // 인덱스 5부터 7까지의 value 출력 (시작 값이 없으면 0부터, 끝 값이 없으면 끝까지 출력)
                document.write(b) // 6,7,8
            </script>
        ```

    * join(delimeter)

      * 배열의 요소들을 하나의 문자열로 출력 (배열을 서버로 보낼 때 유용하게 사용)

      * 분리자가 각 요소를 분리

      * ```javascript
        <script>
            var fruits = ["apple", "banana", "orange"];
            var joinFruits = fruits.join("+");
            document.write(joinFruits); // apple+banana+orange
        </script>
        ```

    * filter()

      * 어떤 조건에 부합하는 요소만을 선택해서 새로운 배열로 만들어서 반환

      * 요소를 선택하는 함수를 작성해서 인수로 전달

      * ```
        <script>
            var numbers = [10, 20, 30, 40, 50];
            function isBigEnough(element, index, array) {
                return (element >= 30); // 반환하지 않으면 결과가 창에 나오지 않는다.
                }
            var filtered = numbers.filter(isBigEnough);
            document.write("필터링 된 배열 : " + filtered);
        </script>
        ```

    * 2차원 배열

      * ```javascript
        // Array 객체는 다른 Array 객체를 포함할 수 있음
        <script>
            var x = [0, 1, 2, 3, 4, 5, 6];
            var y = [x];
        
            document.writeln(y[0], "<br>");
            document.writeln(y[0][2], "<br>");
            // Array 리터럴에서 2차원 배열 생성
        	var matrix = [
                [0,1,2],
                [3,4,5],
                [7,8,9]
            ];
            alert(matrix[1][1]); // 4
        </script>
        ```





## 06. 오류 처리

* 오류 발생 시

  1. 오류가 발생하면 자동적으로 실행이 중단되면서 대화 상자 등장

  2. 대화 상자에서 디버그하겠다고 '확인'을 누르면 소스 파일에서 오류가 발생한 위치를 보여줌

  3. 그것을 참고하여 오류 수정

> 자바스크립트에서 오류 = 예외 (exceptional event)
>
> 예외는 프로그램 실행 중 발생하는 이벤트
>
>  
>
> * 예외 발생 이유
>   1. 개발자 타이핑 오류 (문법적인 오류)
>   2. 브라우저마다 지원하는 특징의 차이
>   3. 사용자로부터의 잘못된 입력
>   4. 인터넷 서버 오류
>
>  
>
> * 프로그램에서 오류를 감지해서 우아하게 종료시키거나, 오류를 처리한 후 계속 실행하는 것이 Best
>   * 이를 예외 처리라고 한다.
>   * try-catch 구조를 이용



* try-Catch 구조
  * 자바스크립트 예외 처리기는 try 블록과 catch 블록으로 이뤄진다.

```javascript
try
{
    // 예외가 발생할 수 있는 코드
}
catch (변수)
{
    // 예외를 처리하는 코드
}

// 예시
<script>
    var msg=""
    function test() {
        try {
            allert("Hello World!")
        }
        catch(error) {
            msg = "다음과 같은 오류가 발생하였음 : " + error.message;
            alert(msg)
        }
    }
</script>
```



* throw 문장

  * 개발자가 오류를 생성할 수 있도록 한다.

  * 예외를 발생시키는 것을 예외를 던진다(throw)라고 표현

  * 고의적으로 예외를 발생시키는 이유?

    1. 개발자는 자신이 어떤 기준을 정하고 이 기준에 맞지 않으면 사용자에게 어떤 경고 메시지를 줄 수 있다.
    2. 예로 음수를 입력하면 안되는 상황일 때 throw를 사용하면 깔끔해진다.

    ```javascript
    throw = "예외 메시지";
    
    // 예시 
    <!DOCTYPE html>
    <html>
    <head>
        <script>
            var solution = 53;
            function test () {
                try {
                    var x = document.getElementById("number").value;
                    if (x < 1 || x > 100) throw "범위를 벗어남";
                    if (x < solution) throw "답보다 작음";
                    if (x > solution) throw "답보다 큼";
                    if (x == solution) throw "성공";
                    if (x == "") throw "입력 없음";
                    if (isNaN(x)) throw "숫자가 아님";
                }
                catch (error) {
                    var y = document.getElementById("msg");
                    y.innerHTML = "힌트 : " + error; 
    // innerHTML : QuerySelector로 가져온 도큐먼트 오브젝트의 내용이나, 내부 HTML 코드를 JavaScript 코드에서 변경 할 수 있습니다.
                }
            }
        </script>
    </head>
    <body>
        <h1>Number Guess</h1>
        <p>1부터 100 사이의 숫자를 입력하시오.</p>
        <input type="text" id="number"> 
        <input type="button" value="숫자 추측" onclick="test()">
        <p id="msg"></p>
    </body>
    </html>
    ```

    

## Exercise

* 4번 (0부터 백만까지 더하는데 걸리는 시간)

```javascript
<script>
    var a = 0;
	// 계산 전 시간을 밀리초로 변경 (1970/1/1 기준)
    var startTime = new Date().getTime(); 

    for (var i = 0; i <= 1000000; i++) {
        a += i
    }
	// 계산이 끝난 후의 시간을 밀리초로 변경 (1970/1/1 기준)
    var endTime = new Date().getTime(); 
    var diff = endTime - startTime;

    document.write(diff + "밀리초가 걸렸음")
</script>
```



* 5번 (문자열 첫 번째 글자를 대문자로 변환)

```javascript
<script>
    function strCap(s) {
        var result = s[0].toUpperCase() + s.slice(1); // H + ong
        alert(result)
    }
    strCap("hong"); // Hong
</script>
```



* 6번 (Date 객체의 getMonth() 메서드로 금월의 이름을 출력하는 프로그램 작성)

```javascript
<script>
    var month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    var now = new Date();
    nowMonth = now.getMonth();
    document.writeln("It is " + month[nowMonth]);
</script>
```



* 7번 (프로그램 작성)

```javascript
/*
1. "터미네이터", "트랜스포머"를 배열 요소로 가진 배열 movies 생성
2. "맨오브스틸"을 배열에 추가
3. 배열의 뒤에서부터 2번째 요소를 "스파이더맨"으로 변경
4. 배열의 마지막 요소를 꺼내 alert()를 사용해 경고 박스에 표시
*/

<script>
    var movies = ["터미네이터", "트랜스포머"];
    movies.push("맨오브스틸")
    movies[(movies.length-2)] = "스파이더맨" // 맨 뒤 인덱스를 어떻게 지정하는지 알아보기
    alert(movies.pop())
</script>
```



* 8번 (Math.random()을 이용해 배열에서 랜덤하게 하나의 요소를 선택해서 출력하는 프로그램 작성)

```javascript
    <script>
        var arr = ["사과", "오렌지", "귤", "당근", "케일"];
        var randomNumber = Math.floor(Math.random() * 5);

        alert(arr[randomNumber] + randomNumber)
    </script>
```



* 9번 (배열 요소의 값을 받으면 그 요소를 배열에서 찾아 인덱스로 반환하는 함수 find(arr, value)를 작성)

```javascript
<script>
    arr = ["hello", 10, 32.6, true];

    function find(arr, value) {
        return document.writeln(arr.indexOf(value));
    }

    find(arr, true); // 3
</script>
```



* 10번 
  * 비속어가 사용되면 검출할 수 있는 함수 check(str)을 작성
  * check()는 "XXX"를 문자열이 포함하면 true를 반환, 그렇지 않으면 false 반환

```javascript
<script>
    // match()는 문자열 안에서 일치하는 컨텐츠를 탐색 ("XXX")
    function check(str) {
        if (str.match("XXX")) {
            return document.write(true);
        } 
        else {
            return document.write(false);
        }
    }
    check("buy XXX now");
</script>
```



* 11번 (일력)

```javascript
// setTimeout()을 이용하려면 div 안에 script를 작성해야 한다.
<div id="timer">
    <script>
        function nowTimer() {
            var now = new Date();
            var nowYear = now.getUTCFullYear();
            var nowMonth = now.getMonth();
            var nowDay = now.getDay();
            var nowHours = now.getHours();
            var nowMinutes = now.getMinutes();
            var nowSeconds = now.getSeconds();

            var result = nowYear + "년 " + (nowMonth + 1) + "월 " + nowDay + "일 " + 				nowHours + "시 " + nowMinutes + "분 " + nowSeconds + "초 "
            document.getElementById("timer").innerHTML = result;

            setTimeout("nowTimer()", 1000);
        }
    	nowTimer();
    </script>
</div>
```



