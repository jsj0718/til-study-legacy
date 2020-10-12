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
>   
>   ```
>
>   





















































