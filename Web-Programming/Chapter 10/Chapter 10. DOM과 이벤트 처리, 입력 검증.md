# Chapter 10. DOM과 이벤트 처리, 입력 검증

* 학습 목표
  * HTML 문서는 내부적으로 DOM(Document Object Model)으로 표현된다는 것을 이해
  * 웹 브라우저도 BOM(Browser Object Model)으로 표현할 수 있다는 것을 이해
  * 웹 브라우저에서 발생하는 이벤트를 이해하고 이벤트 처리를 할 수 있음
  * 자바스크립트를 통한 입력 검증을 학습



## 01. 문서 객체 모델 (DOM)

> * 이번 장 학습 내용
>   * 자바스크립트로 HTML 문서의 요소를 어떻게 변경할 수 있는지 학습
>   * 요소로부터 발생하는 이벤트 처리 방법
>
> 
>
> * DOM (브라우저가 HTML 문서를 내부적으로 표현하는 표준 모델)
>   * 웹 페이지가 적재되면, 브라우저는 페이지의 문서 객체 모델(DOM)을 생성
>   * DOM은 HTML 문서의 계층적인 구조를 트리(Tree)로 표현
>   * 트리에서 하나의 잎을 노드(node)라고 표현 (부모 노드, 자식노드, 형제 노드 개념 존재)
>
> 
>
> * DOM을 통해 할 수 있는 것
>   1. 자바스크립트를 사용해 DOM 트리를 순회하면서 페이지 안 요소의 내용이나 속성, CSS스타일을 우리 마음대로 변경이 가능하다. (동적으로 웹 페이지 내용이나 스타일을 변경할 수 있음)
>   2. 요소에서 발생하는 이벤트에 반응하는 코드를 작성할 수 있다.



* DOM과 BOM

  * JS에서 HTML 문서와 웹 브라우저를 객체로 간주하여 처리함
    * DOM : HTML 문서를 객체로 표현한 것
    * BOM : 웹 브라우저를 객체로 표현한 것 (BOM이 DOM을 포함)

  <img src="https://i1.wp.com/junil-hwang.com/blog/wp-content/uploads/2019/02/dombom.jpg?resize=800%2C579" alt="Javascript에 대한 기본적인 이해 - 개발자 황준일" style="zoom:67%;" />
  * 설명
    * BOM이 DOM을 포함하는 구조
    * window 객체는 최상위 노드로, 브라우저 그 자체를 표현
    * document는 window의 수 많은 자식 노드 중 하나
    * 브라우저에 있는 모든 것은 객체로 표현되기 때문에 JS에서 객체의 속성을 변경하고 객체의 메서드를 호출하면 웹 브라우저의 거의 모든 것을 제어할 수 있다.



* 노드의 종류
  * DOM에 존재하는 노드의 종류
    1. DOCUMENT_NODE : DOM 트리의 루트 노드로 HTML 문서를 나타낸다. (window.document가 DOCUMENT_NODE 타입의 노드이다.)
    2. ELEMENT_NODE : HTML 요소를 나타내는 노드이다. (`<body>`, `<a>`, `<p>`, `<script>`, `<style>` 등)
    3. ATTRIBUTE_NODE : 속성을 나타내는 노드 (class = "myClass"와 같은 속성)
    4. TEXT_NODE : 요소 안에 들어 있는 텍스트를 나타내는 노드





## 02. HTML 요소 찾기

* id로 HTML 요소 찾기

  * 만약 요소를 발견하면 getElementById()는 요소를 객체 형태로 반환
  * 요소를 발견하지 않으면 변수 x는 null이 된다.

  ```javascript
  // id="main"인 요소를 찾는 방법
  var x = document.getElementById("main");
  
  // 예시
  <head>
      <script>
          function test() {
              var a = document.getElementById("txt"); // a는 txt 요소 자체
              alert(a.value); // a 값을 경고 메시지로 나타냄
          }
      </script>
  </head>
  <body>
      <input type="text" id="txt">
      <input type="submit" value='"제출"' onclick="test()">
  </body>
  // 정리 : 버튼이 클릭되면 test()가 호출되고 여기서 getElementById()가 호출되어 id가 "txt"인 요소를 찾은 후 value 속성을 출력한다. 
  // 입력 요소이기 때문에 innerHTML이 아니라 value 속성을 참조해야한다.
  ```

  * 주의할 점 : getElementById()는 요소의 내용을 반환하는 것이 아니라 요소 자체를 반환
  * 만약 요소 내용을 추출하려면 innerHTML(요소가 가진 콘텐츠를 가져옴)을 사용해야한다.

  ```javascript
  // 문서 안에서 id가 "main"인 요소의 내용을 출력
  alert(document.getElementById("main").innerHTML);
  ```

  

* 입력 양식 찾기

  > * DOM 트리에서 document 안에 forms 배열 객체 존재
  > * 이는 배열 형태로 document 객체 하단에 존재하는 객체
  > * HTML 문서 안 모든 입력 양식(form)은 이 배열 안에 모두 들어있다.
  >
  > ```javascript
  > // 배열에는 HTML 내에서 기술된 순서대로 입력 양식이 들어간다.
  > <form>
  >     <input type="text" value=''> // document.form[0].elements[0]
  >     <input type="text" value=''> // document.form[0].elements[1]
  > 	<input type="submit">
  > </form>
  > ```
  >
  >  
  >
  > * 입력 양식과 입력 필드에 name 속성이 지정되어 있다면, 요소를 찾기 훨씬 수월하다. (id 아님!)
  > * id는 getElementById() 메서드로 찾는다!
  > * JS는 키와 값의 형태로 저장되기 때문에 키로도 찾을 수 있다.
  >
  > ```javascript
  > <form name="myform">
  >     <input type="text" id="target1" name="text1"> // document.myform.text1
  > 	<input type="text" id="target2" name="text2"> // document.myform.text2
  > 	<input type="submit">
  > </form>
  > ```

  

* 태그 이름으로 찾기
  
  * getElementByTagName() 은 태그 이름을 인수로 받아서 이 태그를 사용하는 모든 요소를 배열에 넣어 반환

```javascript
// 배열로 반환된다. 첫 번째 요소는 eleArray[0]이다.
// 문서 안 <div> 태그를 모두 찾아서 반환한다.
var eleArray = document.getElementByTagName("div");

// 예시
<ul>
    <li>List item 1</li>
    <li>List item 2</li>
    <li>List item 3</li>
    <li>List item 4</li>
    <li>List item 5</li>
</ul>
<script>
    var list = document.getElementsByTagName("ul")[0]; // 문서 내 첫 번째 <ul> 요소를 찾음
    var allItem = list.getElementsByTagName("li"); // list 안에서 <li> 요소를 전부 찾음
    for (var i=0; i < allItem.length; i++) {
        alert(allItem[i].firstChild.data); // for 반복 루프를 이용해 첫 번째 자식 노드의 data 필드를 출력. 첫 번째 자식 노드는 텍스트 데이터를 가지고 있는 노드
    }
</script>

// 주의할 점 : 어떤 노드가 텍스트 데이터를 가지고 있을 때, 텍스트 데이터는 첫 번째 자식 노드(firstChild)로 저장된다는 점이다.
```



* DOM 트리 순회

  * 두 번째 방법은 자식 노드와 부모 노드 관계를 이용해 한 노드씩 방문하는 방법
  * childNodes[], nextsibling[], parentNode[]를 이용

  > * childNodes : 한 요소의 모든 자식 요소에 접근 가능 (배열이 반환됨)
  > * firstChild : 'childNodes' 배열의 첫 번째 자식 노드가 반환됨 (childNodes[0]과 동일)
  > * lastchild : 'childNodes' 배열의 마지막 자식 노드가 반환됨 (childNodes[childNodes.length-1]과 동일)
  > * parentNode : 현재 노드의 부모 노드를 반환
  > * nextSibling : 현재 노드의 다음 형제 노드를 반환
  > * previousSibling : 현재 노드의 이전 형제 노드를 반환
  >
  > ```javascript
  > var myDiv = document.getElementByTagName("div")[0];
  > 
  > <div>
  >     <p> 과일 리스트 </p> // var myP = myDiv.firstChild;
  > 	<ul> // var myUl = myP.nextSibling;
  >         <li>사과</li> // var myLi = myUl.childNodes[0];
  > 		<li>바나나</li>
  > 		<li>오렌지</li>
  > 	</ul>
  > </div>
  > ```
  >



## 03. HTML 변경하기

* JS로 HTML의 DOM을 변경하는 방법 3가지 (HTML 문서가 직접 변경되는 것이 아니라 DOM만 변경!)
  1. 요소의 내용 변경 (요소객체.innerHTML = ~~)
  2. 요소의 속성 변경 (요소객체.속성명 = ~~)
  3. 요소의 스타일 변경 (요소객체.style.스타일속성 = ~~)



* 요소의 내용 변경하기

  * DOM을 사용하면 JS로 HTML 요소를 쉽게 변경할 수 있다. (innerHTML 속성 사용)
  * innerHTML은 요소의 시작 태그와 종료 태그 사이에 놓여진 모든 HTML 코드와 텍스트를 의미

  ```javascript
  // <시작 태그> + <div>요소의 innerHTML + <종료 태그>
  <div id="main"> div 요소 </div>
  ```

  * innerHTML 속성은 텍스트 or (HTML + 텍스트)를 가질 수 있다. (`<strong>`태그가 들어갈 수도 있다.)
  * 따라서 어떤 요소의 콘텐츠(시작 태그와 종료 태그 사이의 내용)를 변경하려면, innerHTML 속성에 원하는 내용을 대입하면 된다.

  ```javascript
  document.getElementById("main").innerHTML = "웹 페이지 작성";
  ```



* 요소의 속성 변경하기

  ```javascript
  document.getElementById("image").src = "poodle.png";
  // src는 속성 이름, "poodle.png"는 새로운 속성 값
  ```

  ```javascript
  // 예시
  <img src = "whitedog.png" id="image">
      <script>
      function imgChange() {
  	    document.getElementById("image").src = "poodle.png";
  	}
  </script>
  <input type="button" value="눌러보세요" onclick="imgChange()">
  ```

  

* 요소의 스타일 변경하기

  ```javascript
  document.getElementById("p2").style.color = "blue";
  // 스타일의 color 속성을 blue라는 새로운 속성 값으로 변경
  ```

  ```javascript
  <head>
      <script>
          function changeStyle() {
              document.getElementById("p2").style.color = "red";
              document.getElementById("p2").style.fontStyle = "italic";
              document.getElementById("p2").style.fontFamily = "Century Schoolbook";
          }
      </script>
  </head>
  <body>
      <p id="p2">This is a paragraph.</p>
      <input type="button" value="눌러보세요" onclick="changeStyle()">
  </body>
  ```

  

## 04. DOM 노드 삭제와 추가

* 새로운 HTML 요소 생성 (동적으로 웹 페이지에 새로운 요소를 만들어 추가하는 단계)

  1. 추가하기를 원하는 노드를 생성

     ```javascript
     // 노드 생성은 document 객체의 createTextNode() 메서드를 호출해서 진행
     var node = document.createTextNode("동적으로 추가된 노드"); // createTextNode는 텍스트 데이터를 가진 노드를 생성
     ```

     

  2. 문서 내 추가할 위치를 찾음

     ```javascript
     // 노드 생성 후 문서 트리에서 노드를 추가할 위치를 찾는다.(id를 이용하는 것이 가장 일반적)
     // getElementById()를 호출해여 진행 (객체를 반환함)
     var parent = document.getElementById("target");
     ```

     

  3. 새로운 노드를 기존 노드에 연결

     ```javascript
     // 노드를 다른 노드에 자식 노드로 추가하려면 appendChild()를 사용
     parent.appendChild(node);
     ```

     
     
  4. 예시

     ```javascript
     <head>
         <script>
             function addtext(s) {
                 if (document.createTextNode) {
                     var node = document.createTextNode(s);
                     document.getElementById("target").appendChild(node);
                 }
             }
         </script>
     </head>
     <body>
         // 새로운 노드는 <div> ... </div> 안에서 </div> 바로 앞에 추가된다.
         <div id="target" onclick="addtext('동적으로 텍스트가 추가됩니다. ')">
             여기를 클릭하세요.
         </div>
     </body>
     
     // 만약 <div> 태그 바로 뒤에 첫 번째 자식 노드를 추가하고 싶다면, 
     // insertBefore(node, document.getElementById('target').firstChild);
     ```

     

* 기존 HTML 요소 삭제

```javascript
<head>
    <script>
        function test() {
            var parent = document.getElementById("target");
            var child = document.getElementById("p1")

            parent.removeChild(child);
        }
    </script>
</head>
<body>
    <div id="target">
        <p id="p1">첫 번째 단락</p>
        <p id="p2">두 번째 단락</p>
        <input type="button" value="누르세요!" onclick="test()">
    </div>
</body>

// DOM의 구조상 반드시 삭제하고자 하는 요소와 그 부모 요소를 알아야 한다.
```



## 05. 브라우저 객체 모델

* 브라우저 객체 모델
  * BOM(Browser Object Model)은 웹 브라우저가 가지고 있는 모든 객체를 의미
  * 차상위 (window), 그 아래로 (navigator, location, screen, document(DOM), frames 등 존재)
  * 종류
    * window : 메인 브라우저 윈도우
    * window.navigator : 브라우저에 대한 정보 (버전 번호 등)
    * window.screen : 사용자 화면
    * window.history : 사용자가 방문한 URL 저장
    * window.location : 현재 URL
    * window.frames : 브라우저 윈도우를 차지하고 있는 프레임들
    * window.document : 메인 브라우저에 표시된 HTML 문서



* Window 객체

  * window 객체는 BOM에서 최상위 객체로서 웹 브라우저 윈도우를 나타낸다.
  * 모든 전역 자바스크립트 객체, 함수, 변수는 자동적으로 window 객체의 멤버가 된다. (alert(), prompt() 등)

  ```javascript
  // 동일한 문장 (alert가 window의 객체이기 때문)
  alert("Hello World!");
  window.alert("Hello World!");
  ```



> window 객체의 속성과 메서드 종류
>
> * open()과 close()
>
>   * open() : 새로운 브라우저 윈도우 오픈
>
>   ```javascript
>   window.open(URL, name, specs, replace);
>   // URL : 오픈할 페이지 URL
>   // name : 타겟을 지정하거나 윈도우 이름(_blank, _parent, _self, _top, name)
>   // specs : 여러가지 속성 (height=px, width=px, left=px, top=px, menubar=yes|no|1|0, resizable=yes|no|1|0, scrollbars=yes|no|1|0, titlebar=yes|no|1|0)
>   // replace : 히스토리 리스트에서 새로운 엔트리인지 아니면 현재 엔트리를 대체하는지 여부 (ture-replace, false-create)
>   ```
>
>   ```javascript
>   // 예시
>   <form>
>       <input type="button" value="구글창 열기" 										onclick="window.open('http://www.google.com', '_blank', 'width=300, 			height=300', 'true')">
>   </form>
>   ```
>
>  
>
> * seTimeout(), setInterval()
>
>   * setTimeout() : 일정 시간이 지난 후 인수로 전달된 함수를 딱 한 번만 호출 (단위는 밀리초)
>
>   ```javascript
>   setTimeout(code, milisce)
>   // code : 호출되는 함수 이름, 여기서 직접 정의도 가능
>   // milisec : 함수를 호출하기 전 흘러야 하는 시간
>   ```
>
>   ```javascript
>   <head>
>       <script>
>           function showAlert() {
>               setTimeout(function () {alert("setTimeout()을 사용하여 표시함.")}, 3000);
>           }
>       </script>
>   </head>
>   <body>
>       <div>
>           버튼을 누르면 3초 후 경고 메시지 출현
>       </div>
>       <input type="button" value="눌러보세요" onclick="showAlert()">
>   </body>
>   ```
>
>   * setInterval()은 일정 시간마다 주기적으로 함수를 호출한다. (반드시 개발자가 종료시켜야 한다.)
>     * 현재 시간 출력 프로그램 만들 때 이용
>     * 주기적인 호출을 종료 시키려면 clearInterval()을 호출한다.
>
>   ```javascript
>   <head>
>       <script>
>         var id;
>           function changeColor() {
>               id = setInterval(flashText, 500);
>           }
>   
>           function flashText() {
>               var elem = document.getElementById("test")
>               elem.style.color = (elem.style.color == "red") ? "blue" : "red";
>               elem.style.backgroundColor = (elem.style.backgroundColor == "green") ? "yellow" : "green"; 
>           }
>   
>           function stopColor() {
>               clearInterval(id)
>           }
>       </script>
>   </head>
>   <body onload="changeColor()">
>       <div id="test">this is a text.</div>
>       <input type="button" value="중지" onclick="stopColor()">
>   </body>
>   ```
>   
>    
>   
> * moveTo(), moveBy()
>
>   * JS로 윈도우 이동 가능 (moveTo()는 절대적, moveBy()는 상대적)
>
>   ```javascript
>   <head>
>       <script>
>           function openWindow() {
>               w = window.open(' ', ' ', 'width=200, height=100');
>               w.document.write("오늘 다음과 같은 상품을 싸게 팝니다.");
>               w.moveTo(0,0);
>           }
>   
>           function moveWindow() {
>               w.moveBy(10,10);
>               w.focus(); // 특정 윈도우로 키보드 포커스를 이동
>           }
>       </script>
>   </head>
>   <body>
>       <button onclick="openWindow()">윈도우 생성</button> <br>
>       <button onclick="moveWindow()">윈도우 이동</button>
>   </body>
>   
>   // 윈도우 크기 변경 시 : resizeTo(), resizeBy()
>   // 윈도우 스크롤 위치 이동 시 : scrollTo(), scrollBy()
>   ```
>
>  
>
> * screen 객체 (사용자 화면)
>
>   * availHeight : 화면 높이 반환 (태스크 바를 제외한 영역)
>   * availWidth : 화면 너비 반환 (태스크 바를 제외한 영역)
>   * colorDepth : 컬러 팔레트의 비트 깊이를 반환
>   * pixelDepth : 화면 컬러 해상도 반환
>   * height : 화면 전체 높이 반환
>   * width : 화면 전체 너비 반환
>
>   ```javascript
>   <head>
>       <script>
>           function maxopen(url, winattributes) {
>               var maxwindow = window.open(url, "", winattributes);
>               maxwindow.moveTo(0, 0);
>               maxwindow.resizeTo(screen.availWidth, screen.availHeight);
>           }
>       </script>
>   </head>
>   <body>
>       <a href="#" onclick="maxopen('http://www.google.com', 'resizable=0, scrollbars=0, status=0'); return false">전체 화면 보기</a>
>   </body>
>   ```
>
>  
>
> * location 객체
>
>   * 현재 url에 대한 정보를 가지고 있다. (window 객체의 일부)
>   * 속성
>
>   > hash : url 중 앵커부분을 반환 (#section1과 동일한 부분)
>   >
>   > host : url 중 hostname과 port를 반환
>   >
>   > hostname : url 중에서 hostname을 반환
>   >
>   > href : 전체 url 반환
>   >
>   > pathname : url 중 경로(path) 반환
>   >
>   > port : url 중 port 반환
>   >
>   > protocol : url 중 protocol 부분 반환
>   >
>   > search : url 중 쿼리 부분 반환
>
>   * 메서드
>
>   > assign() : 새로운 문서 로드
>   >
>   > reload() : 현재 문서 재로드
>   >
>   > replace() : 현재 문서를 새로운 문서로 대체
>
>  
>
> * navigator 객체
>
>   * 브라우저에 대한 정보를 가짐
>   * 속성
>
>   > appCodeName : 브라우저 코드 네임
>   >
>   > appName : 브라우저 이름
>   >
>   > appVersion : 브라우저 버전 정보
>   >
>   > cookieEnabled : 브라우저에서 쿠키가 활성화되어 있는지 여부
>   >
>   > onLine : 브라우저가 인터넷에 연결되어 있으면 true
>   >
>   > platform : 브라우저가 컴파일된 플랫폼
>   >
>   > userAgent : 브라우저에서 서버로 가는 user-agent 헤더
>
>   * 메서드
>
>   > JavaEnabled() : 자바 사용 가능 여부
>   >
>   > taintEnabled() : 브라우저에서 data tainting이 가능한지 여부
>
>   ```javascript
>   <script>
>       // navigator는 딕셔너리 형태로 정보 저장
>       for (var key in navigator) {
>           value = navigator[key];
>           document.write(key + ": " + value + "<br>");
>       }
>   </script>
>   ```





## 06. 이벤트 처리

1. 웹 페이지 상호작용 발생 시 이벤트가 일어남 (예로 특정 요소 클릭 또는 마우스를 위로 올릴 때 등)
2. 브라우저에 의해 이벤트가 발생함(예로 웹 페이지나 이미지의 로드가 끝날 때, 페이지를 스크롤할 때 등)



> * 정리 (이벤트가 발생할 수 있는 상황)
>
> 1. 마우스 클릭
> 2. 웹 페이지 로딩
> 3. 호버링(hovering)으로 마우스를 어떤 요소 위에서 움직일 때
> 4. HTML 입력 양식에서 입력 박스를 선택할 때
> 5. 키보드의 키를 누를 때
>
>  
>
> * 이 떄, 특정 동작을 하고 싶으면 자바스크립트를 사용해야 한다.



* onclick 이벤트

  * 사용자가 버튼을 클릭하는 것과 같은 이벤트가 발생 시 미리 정해놓은 코드가 실행된다.

  ```javascript
  // 헤딩이 클릭되면 등록된 함수가 실행된다.
  <h1 onclick="change()">이것은 클릭 가능한 헤딩</h1>
  ```

  ```javascript
  // 예시
  <head>
      <script>
          function changeColor(c) {
              document.getElementById("test").style.backgroundColor = c;
          }
      </script>
  </head>
  <body id="test">
      <form method="POST">
          <input type="radio" name="C1" value="v1" onclick="changeColor('lightblue')"> 파란색
          <input type="radio" name="C1" value="v2" onclick="changeColor('lightgreen')"> 녹색
      </form>
  </body>
  ```

  

* onload(웹 페이지 진입)와 onunload(웹 페이지 떠남) 이벤트

  * onload 이벤트로 방문자의 브라우저 종류나 버전을 알 수 있어서 적절한 버전의 웹페이지 로드 가능
  * onload와 onunload는 쿠키를 처리하는데 사용한다

  ```javascript
  <head>
      <script>
          function onLoadDoc() {
              alert("문서가 로드됨");
              document.body.style.backgroundColor = "lightgreen";
          }
      </script>
  </head>
  
  <body onload="onLoadDoc()">
  </body>
  ```

  



* onchange 이벤트

  * 입력 필드 검증 시 사용

  ```javascript
  <head>
      <script>
          function textChange() {
              var s = document.getElementById("test");
              s.value = s.value.toLowerCase();
          }
      </script>
  </head>
  <body>
      영어단어 : <input type="text" id="test" onchange="textChange()">
      <p>입력필드를 벗어나면 소문자로 변경</p>
  </body>
  ```

  

* onmouseover 이벤트

  * onmouseover과 onmousesout 이벤트는 사용자가 HTML 요소 위에 마우스를 올리거나 요소를 떠날 때 발생한다.

  ```javascript
  <script>
      function borderOn(elem) {
        elem.style.border = "2px solid red";
      }
      function borderOff(elem) {
          elem.style.border = "";
      }
  </script>
  
  <div style="background-color: yellow;", width="200px" onmouseover="borderOn(this)" onmouseout="borderOff(this)">
      마우스를 이 요소 위에 올려라.
  </div>
  ```
  
  

* onmousedown, onmouseup, onclick 이벤트

  * 우선 순위
    1. onmousedown
    2. onmouseup
    3. onclick

  ```javascript
  <script>
  	function buttonDown(elem) {
      	elem.style.color = "black";
  	}
  
      function buttonUp(elem) {
      	elem.style.color = "red";
  	}
  </script>
  <button onmousedown="buttonDown(this)" onmouseup="buttonUp(this)">눌러!</button>
  ```




```javascript
// 계산기 예제

<!DOCTYPE html>
<html>
<head>
    <script>
        result = "";

        function add(elem) {
            result += elem;
            document.getElementById("display").value = result;
        }

        function compute() {
            document.getElementById("display").value = eval(result);
        }

        function clearDisplay() {
            result = "";
            document.getElementById("display").value = "0"
        }
    </script>
</head>
<body>
    <form>
        display <input type="text" id="display" value="0" size="30"> 
        <br>
        
        <input type="button" value="7" onclick="add('7')">
        <input type="button" value="8" onclick="add('8')">
        <input type="button" value="9" onclick="add('9')">
        <input type="button" value="/" onclick="add('/')">
        <br>

        <input type="button" value="4" onclick="add('4')">
        <input type="button" value="5" onclick="add('5')">
        <input type="button" value="6" onclick="add('6')">
        <input type="button" value="*" onclick="add('*')">
        <br>

        <input type="button" value="1" onclick="add('1')">
        <input type="button" value="2" onclick="add('2')">
        <input type="button" value="3" onclick="add('3')">
        <input type="button" value="-" onclick="add('-')">
        <br>
        
        <input type="button" value="0" onclick="add('0')">
        <input type="button" value="+" onclick="add('+')">
        <br>

        <input type="button" value="Clear" onclick="clearDisplay()">
        <input type="button" value="Enter" onclick="compute()">

    </form>
</body>
</html>
```





# 07. 폼의 유효성 검증

> * 자바스크립트는 HTML 폼 안의 데이터를 서버로 보내기 전 검증하는데 많이 사용한다.
> * 자바스크립트로 사용자 실수를 수정한 후 서버로 보내면 서버 부하를 덜어낼 수 있다.
> * 검증 사항
>   * 필수적인 필드
>   * 유효한 길이의 텍스트
>   * 유효한 이메일 주소
>   * 유효한 날짜
>   * 숫자 필드에 텍스트 입력 여부



* 폼 데이터 접근

  * form에 접근하기 위해 id나 name 속성을 이용

  ``` javascript
  <input type="text" id="addr" name="addr">
  // id : 페이지 요소 식별 (getElementById() 이용)
  // name : 폼 내부에서 필드 식별 (form 객체에서 name을 이용)
  ```

  ```javascript
  <input type="text" name="addr" onclick="display(this.form)">
      
  // form 객체는 배열이고, 각 배열 요소는 form["name"] 형식으로 name 속성에 접근 가능하다.
  function display() {
      alert(form["adrr"].value);
  }
  ```

  

* 언제 데이터를 검증하는가?
  1. 사용자가 입력 필드를 마우스로 선택 시 (onfocus Event 발생)
  2. 사용자가 데이터 입력 후 입력 필드 떠날 때 (onblur Event 발생)
     * 필드가 비어 있어도 발생 O
  3. 필드를 떠날 때 입력 내용 변경 시 (onchange Event 발생)
     * 필드가 비어 있으면 발생 X



* 공백 검증

  ```javascript
  <script>
      function checkNotEmpty(field) {
          if (field.value.length == 0) {
              alert("필드가 비었음!")
              field.focus();
              return false
          }
          return true
      }
  </script>
  
  <form>
      이름 : <input type="text" id="user"> <input type="button" value="확인" onclick="checkNotEmpty(document.getElementById('user'))">
  </form>
  ```

  

* 데이터 길이 검증

  ```javascript
  <script>
      function checkIdLength(field, min, max) {
          if (field.value.length >= 6 & field.value.length <= 8) {
              return true;
          }
          else {
              alert(min + "문자와" + max + "문자 사이로 입력!");
              field.focus();
              return false;
          }
      }
  </script>
  
  <form>
      이름(6-8문자) : <input type="text" id="user"> <input type="button" value="확인" onclick="checkIdLength(document.getElementById('user'), 6, 8)">
  </form>
  ```



* 정규식(특정한 규칙을 가지고 있는 문자열을 표현하는 수식)

  * 문자열의 검색과 치환을 위해 사용

  ```javascript
  ^[0-9]+abc$
  // ^ : 문자열의 시작
  // [0-9] : 0부터 9까지의 문자 중 하나
  // + : 한 번 이상 반복
  // abc : 문자열
  // $ : 문자열의 끝
  ```

  > 정규 표현식
  >
  > * ^ : 문자열의 시작
  > * $ : 문자열의 끝
  > * . : 문자 (한 개의 문자와 일치)
  > * \d : 숫자 (한 개의 숫자와 일치)
  > * \w : 문자와 숫자 (한 개의 문자나 숫자와 일치)
  > * \s : 공백 문자 (공백, 탭, 줄 바꿈, 캐리지 리턴 문자와 일치)
  > * [] : 문자 종류, 문자 범위 ([abc]는 a or b or c, [1-9]는 1부터 9)
  >
  > 
  >
  > 수량 한정자
  >
  > *  `*` : 0회 이상 반복 ("a*" 는 "", "a", "aa", "aaa")
  > * `+` : 1회 이상 ("a+"는 "a", "aa", "aaa")
  > * `?` : 0 또는 1회 ("a?"는 "", "a")
  > * {m} : m회 ("a{3}"는 "aaa")
  > * {m,n} : m회 이상 n회 이하 ("a{1,3}"은 "a", "aa", "aaa")
  > * (ab) : 그룹화 ( (ab)*는 "", "ab", "abab" 등 )
  >
  > > 예시
  > >
  > > 1. /.+/ : 어떤 문자가 1회 이상 반복
  > > 2. /\w*/ : 어떤 문자나 숫자로 이루어진 문자열
  > > 3. ^`[1-9][0-9]`*$ : 처음 숫자가 0이 아니고 전체가 숫자 (e.x 가격)
  > > 4. /^\d{6}-\d[7]$/ : 중간에 -이 있는 주민등록번호
  > > 5. /(Good)?Bye/ : GoodBye or Bye
  >
  >  
  >
  > 자바스크립트 정규 표현식은 RegExp 객체에 의해 표현
  >
  > ```javascript
  > var exp = /^\d{10}$/;
  > // RegExp 객체의 test() 메서드는 일치하면 true 반환
  > if (!exp.test(field.value)) {
  >     alert("오류!!");
  >     return false;
  > }
  > ```



* 숫자나 문자 입력 검증(신용카드, 전화번호, 우편번호 등)

  ```javascript
  <!-- 풀이 1 -->
  <!-- 
  <script>
      function onlyNumber(field) {
          var exp = /^[0-9]+$/
          if (!exp.test(field.value)) {
              alert("숫자만 입력!!");
              return false;
          }
      }
  </script>
  
  <form>
      전화번호(-없이 입력) : <input type="text" id="test1"> <input type="button" value="확인" onclick="onlyNumber(document.getElementById('test1'))">
  </form>
   -->
  
  <!-- 풀이 2 -->
  <script>
      function checkNumeric(field, msg) {
          exp = /^[0-9]+$/
          if (field.value.match(exp)) {
              return true;
          }
          else {
              alert(msg);
              field.focus()
              return false;
          }
      }
  </script>
  
  <form>
      전화번호(-없이 입력) : <input type="text" id="phoneNumber"> <input type="button" value="확인" onclick="checkNumeric(document.getElementById('phoneNumber'), '숫자만 입력!')">
  </form>
  ```

  

* 이메일 검증

  * 체크사항
    1. @gmai.com : @ 앞에 문자가 전혀 없다.
    2. ho!ng@gmail.com : 허용되지 않는 문자 ! 존재
    3. hong@g_mail.com : 도메인 이름에는 _ 허용 X
  * 예시

  ```javascript
  1. var exp = /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-Z0-9]{2,}$/;
  
  2. var exp = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+\.([a-zA-Z])+([a-zA-Z])+/;
  
  3. var exp = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,})+$/;
  ```



* 선택 검증 (select field)

  ```javascript
  <script>
      function checkSelection(elem, msg) {
          if (elem.value == "0") {
              alert(msg);
              elem.focus();
              return false;
          }
          return true;
      }
  </script>
  
  <form>
      과일 선택 <select id="fruits" class="required">
          <option value="0">선택하세요</option>
          <option value="1">사과</option>
          <option value="2">배</option>
          <option value="3">바나나</option>
      </select>
      <input type="button" value="확인" onclick="checkSelection(document.getElementById('fruits'), '하나를 선택!')">
  </form>
  ```

  