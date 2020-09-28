# Chapter 6. CSS3 레이아웃과 애니메이션

* 학습 목표
  * 레이아웃 기본 모델인 박스 모델 학습
  * "<div>" 와 "<span>" 학습
  * HTML 요소 위치 설정하는 방법 학습
  * "<div>"를 이용한 레이아웃 실습
  * HTML5 시멘틱 태그 사용하여 레이아웃 실습



## 01. 레이아웃의 기초

* 웹 페이지 레이아웃은 "집안에서 가구를 어떻게 배치할 것인가"는 문제와 비슷하다.



* 박스 모델
  * 웹 브라우저가 각 요소를 화면에 그릴 때 무조건 사각형으로 간주
  * 사각형에는 패딩, 경계선, 마진이 붙어 있다.
* 블록 요소와 인라인 요소
  * 블록 요소 : 화면 한 줄을 전부 차지
  * 인라인 요소 : 한 줄에 차례대로 배치 (필요한 만큼 너비만을 차지)
  * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200928121438043.png" alt="image-20200928121438043" style="zoom:67%;" />
  * 블록 요소와 인라인 요소 혼합 시 블록 요소가 나타날 때까지 인라인 요소는 같은 줄에 배치된다.



* CSS로 display 속성 변경하기
  * HTML 요소가 자동적으로 블록 요소와 인라인 요소로 나눠지지만, 이 속성은 CSS 코드로 변경 가능
  * display를 block으로 설정하면 블록 요소처럼 배치, inline으로 설정하면 인라인 요소처럼 배치됨
  * 예시
    * div { display: inline; }
  * 그 외에도 display : none; (없는 것으로 간주) 와 display : hidden; (화면에서 감쳐짐)이 있다.



## 02. 요소 위치 정하기

* 기본적으로 요소 위치는 top, bottom, left, right 속성으로 지정
  * `#` target { top : 100px; left : 200px;}
    
    * 기준 위치에서 (100, 200)만큼 떨어진 곳에 요소 배치
    * top, right, bottom, left 모두 경계선에서의 offset(편차, 차이)이다.
      * right : 100px; 는 오른쪽에서 100px 떨어진 곳이라는 의미
    * **요소의 크기**는 **width, height**로 설정
    * **기준 위치**는 **position** 속성으로 결정 (요소 위치의 설정 방법)
      * top, right, bottom, left는 position을 설정하지 않으면 아무리 설정해도 소용이 없다.
    
    
    
  * CSS 4가지 위치 설정 방법

    1. 정적 위치 설정 : 정상적인 흐름에 따른 배치 (default 값)
       * 페이지의 정상적인 흐름에 따라 요소 위치가 결정되는 방법
       * 블록은 상하로 쌓이고, 인라인은 한 줄에 차례대로 배치
       * 정적 위치 설정을 사용하면 top, bottom, left, right 속성의 영향을 받지 않는다.
    2. 상대 위치 설정 : 정삭적인 위치가 기준점이 됨
       * 정상적인 위치에서 상대적으로 요소가 배치되는 방법
       * 상대 위치로 설정된 요소는 다른 요소 위에 겹치거나 이동할 수 있다.
       * 그러나 요소를 위해 할당된 정상적인 공간은 사라지지 않는다.
    3. 절대 위치 설정 : 컨테이너의 원점이 기준점이 됨
       * 전체 페이지를 기준으로 배치하는 방법
       * 페이지 시작 위치에서 top, left, bottom, right 만큼 떨어진 위치에 배치
       * 예로 top, left 속성에 30px를 지정한다면 페이지 시작 위치로부터 (30, 30)만큼 떨어진 곳에 배치가 된다.
       * 절대 위치로 설정된 요소는 문서의 정상적인 흐름에서 제거되며, 페이지 안의 고정된 위치에 표시된다.
       * top, right, bottom, left 모두 offset으로 생각해야 한다.
       * 만약 컨테이너가 있다면 컨테이너의 시작 위치로부터 떨어진 위치에 상대적으로 배치된다.
         * 컨테이너는 static X, relative O 
    4. 고정 위치 설정 : 윈도우(웹 브라우저)의 원점이 기준점이 됨
       * 브라우저 윈도우에 상대적으로 요소 위치를 잡는 것 (스크롤 해도 화면에서 요소 이동 X)



* float 속성

  * float 사용 시기

    1. 이미지와 텍스트를 화면에 함께 표시할 때

       * 어떤 요소든 float 속성 적용 가능

       	*  float이 된 요소는 부모 컨테이너 가장 왼쪽이나 오른쪽으로 이동
       *  float된 요소 이전에 추가된 요소는 float 영향 X
       *  float 속성으로는 요소를 컨테이너 left나 right로만 배치 가능

    2. float는 웹 페이지의 레이아웃을 잡을 때도 사용

    3. position : static 인 블록 요소에 사용된다.

    4. 이 속성이 사용되면 컨테이너 안 다른 요소가 이를 감싸며 배치되는데 이 때 position이나 offset 설정은 모두 무시된다.

    

* float 속성 없애는 방법

  * clear는 float의 흐름을 제거하는 속성

    #footer {

    ​				clear : both;

    }



* z-index
  * z-index는 요소가 정상적인 흐름에서 벗어나 배치되는 경우 겹침 현상이 발생할 때 해결 가능
  * 요소의 스택 순서(즉 요소가 다른 요소의 앞에 위치하는지, 뒤에 위치하는지)를 지정
  * { z-index : number; }에서 number가 큰 요소일 수록 앞에 놓인다.
  * position 속성이 absolute 또는 fixed일 때만 적용이 된다.



* 요소 크기 설정
  * width, height : 요소 크기
  * min-width, min-height : 요소 최소 크기
  * max-width, max-height : 요소 최대 크기



* overflow 속성
  * 자식 요소가 부모 요소 범위를 벗어날 때, 어떻게 처리할 것인지 지정
    * hidden : 부모 영역을 벗어나는 부분을 보이지 않게 한다.
    * scroll : 부모 영역을 벗어나는 부분을 스크롤할 수 있게 한다.
    * auto : 자동으로 스크롤바가 나타난다.



## 03. div 요소를 이용한 레이아웃

1. table 요소를 사용한 레이아웃
   * 가장 전통적인 방법이며 경우에 따라 아주 편리한 방법
   * 그러나 테이블의 원래 용도와는 어긋남
2. div 요소를 사용한 레이아웃
   * 가장 널리 사용되는 방법으로 div는 다른 요소를 그룹핑하는데 사용되기에 편리하다.
3. HTML5의 nav, section, aside 등 시멘틱 요소를 사용한 레이아웃
   * 근본적으로 div 요소와 유사한 방법



## 04. 의미적 요소를 이용한 레이아웃

* 의미적 요소는 브라우저에게 요소의 의미나 목적을 명확히 알려주는 요소이다.

  **시멘틱 요소는 브라우저와 개발자에게 명확히 그 의미를 설명하는 요소이다.**

  	* div는 논리적인 섹션을 나타내지만, 그 자체로는 아무런 의미도 없다.
  	* 이런 문제점을 해결하기 위해 시멘틱 요소를 정의하였다.



* 시멘틱 요소
  * W3C에서 개발자가 많이 사용하고 있는 아이디와 클래스 이름을 추출해 표준 태그로 만듦
    * header : 문서의 머리말
    * hgroup : h1~h6 요소의 그룹
    * nav : 내비게이션 링크 또는 메뉴 바
    * article : 문서의 내용이나 블로그 포스트 (문서 내용 그룹핑)
    * section : 문서 섹션 (문서 내용 그룹핑)
    * aside : 사이드바와 같이 옆에 위치하는 내용 (보조적인 내용 표시)
    * footer : 문서의 꼬리말
    * figure : 그림이나 도표
    * time : 날짜와 시간 표시
* Tip
  * display : table / display : table-cell 의 장점
    * 화면에 가상 테이블 작성 가능
    * 테이블 형태로 레이아웃하는데 float이나 절대 위치 설정 필요 X
    * 컬럼 높이가 달라도 문제 X
    * css 코딩 간결
  * display : table / display : table-cell 의 단점
    * 소스에 적힌 순서대로 테이블 셀이 생성된다.



## 05. 효과

* 투명도

  * opacity 속성 이용하여 투명도 조절 가능 (0.0(투명) ~ 1.0(불투명))

  * 이미지를 대상으로 많이 사용된다.

  * 예시

    	<style>
    	    img { opacity : 0.4;}
    	    img:hover { opacity : 1.0; } /* 마우스를 사진 위에 올리면 흐려진다. */
    	</style>
    

* 가시성

  * 어떤 요소를 보이거나 안보이게 하는 것 (visibility 사용)

    * hidden : 요소를 보이지 않게 한다.
    * visable(default) : 요소를 보이게 한다.

  * 예시

    <style>
        #a {
            visibility : hidden;
        }
        #b {
            visibility : visible;
        }
    </style>

  * display : none으로 설정하면 화면에서 자리도 차지하지 않고 완전히 제외

  * 따라서 일시적으로 어떤 요소를 보이지 않게 하려면 display 또는 visibility 중 하나 사용



* 전환

  * 요소가 하나의 형태(스타일)에서 다른 형태(스타일)로 점진적으로 변화되는 효과

  * 전환 지정을 위해 필요한 것

    * 효과를 추가하고 싶은 CSS 속성을 지정

    * 효과의 지속 시간을 지정

    * 예시

      transition : width 5s;

      * width : 전환되는 속성
      * 5s; : 전환 효과의 지속 시간 (지정 안하면 0으로 간주되어 전환 효과 X)
      * 전환 효과는 지정된 CSS 속성 값이 변경될 때 시작됨 (hover 같은 경우에 해당)
      * 웹 브라우저마다 속성이 다를 수 있으므로 다 적는다.
        * -moz- : 모질라
        * -webkit : 크롬 및 사파리
        * -o- : 오페라



* 다중 전환

  * 너비, 길이, 회전 등의 변환을 줄 수 있다.

  * ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>css transition1</title>
        <style>
            p {
                background-color: yellow;
                border : 1px solid black;
                width : 100px;
                height : 50px;
                /* 크롬 지원을 안할 수도 있으므로 추가적으로 -webkit-을 적는다 */
                transition : width 5s height 5s border 5s, transform 5s;
                -webkit-transition : width 5s, height 5s, border 5s, transform 5s;
            }
            p:hover {
                width : 200px;
                height : 100px;
                border : 5px solid red;
                /* 크롬 지원을 안할 수도 있으므로 추가적으로 -webkit-을 적는다 */
                transform : rotate(180deg); /* 180도 회전 */
                -webkit-transform : rotate(180deg);
            }
        </style>
    </head>
    <body>
        <p>마우스를 올려보세요.</p>
    </body>
    </html>
    ```



## 06. CSS3 변환

* CSS3 변환 기능을 통해 도형 이동, 도형 크기 변환, 도형 회전이 가능하다.

  변환은 요소 크기나 형태, 위치를 변환하는 효과로 2차원 또는 3차원적으로 변환이 가능하다.

* transform 속성을 사용해 좌표 공간을 변형함으로써 특정 요소 위치를 바꿀 수 있다.

  * 종류
    * transform: translate(10px, 10px) : 평행이동
      * translate(100px, 0px)은 (100, 0)만큼 평행 이동해서 박스를 그린다.
    * transform: rotate(45deg) : 회전
      * rotate(45deg)는 45도만큼 박스를 회전해서 그린다.
    * transform: scale(2, 1.2) : 크기 변환
      * scale(1.2, 1.2)는 x방향으로 1.2배, y방향으로 1.2배 확대해서 그린다.
    * transform: skew(20deg, 10deg) : 비틀기 변환
    * transform: matrix() : 일반적인 변환

  * 기준 위치는 박스의 정상적인 위치가 된다. 

  

* 비틀기 변환

  * x, y 방량으로 박스를 비틀어 그리는 변환

  

* 복합 변환

  * 하나의 요소에 여러가지 변환이 차례대로 적용될 수 있다.

  * 예시

    div {

    ​		height : 100px; width : 100px;

    ​		transform: translate(80px, 80px) scale(1.5, 1.5) rotate(45deg)

    }



* matrix()
  * 모든 2차원 변환을 하나로 결합
  * 6개의 매개 변수를 가짐 (rotate, scale, translate, skew)
  * 2D 변환을 값 6개로 이루어진 변환 행렬에 저장
  * matrix(a,b,c,d,e,f)는 변환 행렬 [a b c d e f]에 해당



## CSS3 3차원 변환

* 간단한 메서드 종류

  * translate(x,y,z) : 3차원 평행 이동
  * translateX(x) : 3차원 평행 이동 (x축)
  * translateY(y) : 3차원 평행 이동 (y축)
  * translateZ(z) : 3차원 평행 이동 (z축)
  * scale3d(x, y, z) : 3차원 크기 변환
  * scaleX(x) : 3차원 크기 변환 (x축)
  * scaleY(y) : 3차원 크기 변환 (y축)
  * scaleZ(z) : 3차원 크기 변환 (z축)
  * rotate3d(x,y,z) : 3차원 회전 변환
  * rotateX(x) : 3차원 회전 변환 (x축)
  * rotateY(y) : 3차원 회전 변환 (y축)
  * rotateZ(z) : 3차원 회전 변환 (z축)
  * perspective(n) : 원근 변환

* 예시

  ```html
  <!DOCTYPE html>
  <html>
  <head>
      <title>transform 3d</title>
      <style>
          div {
              background-color: green;
              height : 150px;
              width : 150px;
          }
  
          #container {
              background-color: yellow;
              border : 1px solid black;
          }
          #transformed {
              backface-visibility: visible; /* 후면을 보이게 하는 속성 */
              transform-origin: 50% 42%; /* 변환 원점을 설정 */
              transform : perspective(500px) rotateY(59deg) rotateX(0deg);
              /* perspective(d)는 원근 변환에서 거리를 설정, d는 관측자와 화면 간의 거리 */
          }
      </style>
  </head>
  <body>
      <div id="container">
          <div id="transformed"></div>
      </div>
  </body>
  </html>
  ```

  

## 08. CSS 애니메이션

* 변환을 통해 애니메이션 효과 가능

  그러나 변환에서는 개발자가 중간 단계의 프레임에 대해 제어가 불가능

* 그러나 정의된 애니메이션으로 개발자가 키프레임(keyframe)을 이용해 CSS 특성값의 변화를 지정할 수 있다.

  * keyframe이란 애니메이션 중간 중간에 객체의 위치와 크기를 지정해주는 프레임이다.
  * 이것을 작성해주면 컴퓨터는 그 사이의 프레임을 자동으로 생성한다.
  * @keyframes를 이용해 키프레임을 지정한다.

* 양식

  @keyframe myanim

  {

  0% {left: 0px; top: 0px;}

  25% {left: 100px; top: 0px;}

  50% {left: 200px; top: 0px;}

  75% {left: 100px; top: 0px;}

  100% {left: 100px; top: 0px;}

  }

  * @keyframes 규칙 안에서 CSS 스타일을 지정하면 애니메이션은 현재 스타일에서 새로운 스타일로 점진적으로 변화하게 된다.

  * 애니메이션은 요소가 하나의 스타일에서 다른 스타일로 변경하는 효과이다.

  * 키프레임은 % 단위로 지정한다. (혹은 from(0%)과 to(100%) 사용)

  * 예시

    div {

    ​		animation: 2s myanim;

    ​		animation-iteration-count: 10;

    }

    * 2s : 애니메이션 지속 시간
    * myanim : 애니메이션 이름 (사용자가 지정)
    * animation-iteration-count: 10 : 애니메이션 반복 횟수



* 튀어오르는 공 애니메이션
  * 속도 효과를 지정할 수 있다.
    * linear
    * ease
    * ease-in : 천천히 시작하는 것
    * ease-out : 움직임이 멈출 때 끝에 이르러 변화의 정도가 서서히 감소하는 것
    * ease-in-out

```html
<!DOCTYPE html>
<html>
<head>
    <title>ball animation</title>
    <style>
        @-webkit-keyframes bounce {
            from, to {
                bottom : 0px;
                -webkit-animation-timing-function: ease-out;
            }
            50% {
                bottom : 200px;
                -webkit--webkit-animation-timing-function: ease-in;
            }
        }
        div {
            position: absolute;
            width: 20px;
            height: 20px;
            background-color: red;
            border-radius: 10px;
            -webkit-animation-name: bounce;
            -webkit-animation-iteration-count: infinite; /* 무한히 반복 */
            -webkit-animation-duration: 5s; /* 한 번 수행하는데 걸리는 시간 */
        }
    </style>
</head>
<body>
    <div></div>
</body>
</html>
```

