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
> 
