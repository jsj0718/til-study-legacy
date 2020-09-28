# CSS3 박스 모델과 응용

* 학습 목표
  * CSS 박스 모델 학습
  * 마진, 패딩, 배경 설정 방



## 01. 박스 모델

* CSS3는 모듈로 분리된다.
  * 선택자
  * 박스 모델
  * 배경 및 경계선
  * 텍스트 효과 
  * 2차원 및 3차원 변환
  * 애니메이션
  * 다중 컬럼 레이아웃
  * 사용자 인터페이스



* 박스 모델

  * 웹 브라우저는 각 HTML 요소를 사각형으로 간주하고 웹 페이지 위에 그린다. (요소 배치도 동일)
  * 이런 식으로 요소를 박스 형태로 그리는 것을 박스 모델이라고 부른다.
  * CSS는 각 박스의 특징(배치, 색상, 경계 등)을 결정한다.

  

  * CSS 박스 모델은 기본적으로 HTML 요소를 감싸는 가상의 박스를 생각하는 것이다.
  * 각 박스는 마진, 경계, 패딩을 가진다.
  * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200927104529568.png" alt="image-20200927104529568" style="zoom: 67%;" />
    * 콘텐츠 : 박스의 내용물. 텍스트와 이미지가 나타나는 부분
    * 패딩 : 콘텐츠 주위 영역 (투명함)
    * 경계 : 패딩과 내용물을 감싸는 경계. 박스의 경계색에 의해 영향을 받음
    * 마진 : 경계 주위의 영역 (투명함) 



## 02. 경계선

* CSS border 속성을 이용하면 HTML 요소 경계선의 스타일과 색상을 지정할 수 있다.
* 이를 위해 border-style 속성이 설정되어야 한다.



* 경계선 스타일

  * border-style로 설정 가능하다.

  * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200927105551050.png" alt="image-20200927105551050" style="zoom: 67%;" />

  * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200927105635702.png" alt="image-20200927105635702" style="zoom: 50%;" />

  * 상하좌우 모두 다르게 설정 시

    * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200927110503549.png" alt="image-20200927110503549" style="zoom:67%;" />

    * "<p style="border-style : dotted solid double dashed;">""</p>"와 동일

      * top, right, bottom, left 순서

    * <p style="border-style : dotted solid double dashed;">4개의 경계선이 모두 다르게 설정됨</p>



* 경계선의 폭

  * border-width는 경계선의 폭을 지정한다. (단위는 px이거나 thin, medium, thick 중 하나)

  * border-style이 설정되어 있어야 border-width가 동작한다

    *     <style>
                    p.thick {
                        border-style : solid;
                        border-width : thick;
                    }
                    p.medium {
                        border-style : solid;
                        border-width : medium;
                    }
                    p.thin {
                        border-style : solid;
                        border-width : 1px;
                    }
                </style>

    * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200927132212557.png" alt="image-20200927132212557" style="zoom:67%;" />

* 경계선 색상

  * border-color로 경계선 색상을 지정한다.

  * 지정 방법

    * green -> 이름
    * rgb(0,255,0) -> rgb 10진수 이용
    * #00ff00 -> 16진수 이용

  * 예시

    * <style>
              p.green {
                        border-style : solid;
                        border-color : green;
                    }
      </style>

    * ![image-20200927132448557](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200927132448557.png)



* 경계선 속성 한 줄로 정의
  * border-width, border-style(필수), border-color 순서로 적어야 한다.
    * 예시) border : 5px solid red;



* 둥근 경계선

  * border-radius는 둥근 경계선을 만드는 속성이다.

    * 예시) border-radius : 25px;

      * 단위는 px며 둥근 코너의 반지름을 뜻한다.

    * <style>
              div {
                        border : 2px solid red;
                        padding : 10px 20px;
                        border-radius : 25px;
                    }
                </style>

    * ![image-20200927132936849](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200927132936849.png)

    * padding을 통해 글자가 경계선 밖으로 넘어가는 것을 해결할 수 있다.



* 경계에 그림자 생성

  * box-shadow 속성으로 그림자가 있는 경계 생성 가능

    * 예시) box-shadow : 20px 10px 5px #666666;

      * 순서대로 가로 오프셋, 세로 오프셋, 번지는 정도, 그림자 색이다.

    * 예시

      * <style>
                div {
                          width : 300px;
                          height : 50px;
                          background-color : green;
                          box-shadow : 20px 10px 5px #666666;
                      }
                  </style>

      * ![image-20200927133355382](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200927133355382.png)

* 경계 이미지 (필요할 때 해보기)
  
  * border-image 속성을 이용해 이미지로 경계선을 만들 수 있다.



## 03. 마진과 패딩

* 요소 크기 설정

  * CSS에서 모든 요소의 크기를 width와 height 속성으로 설정할 수 있다.

* 요소 크기 변경

  * resize 속성을 both로 설정하면 양방향 크기 조정 메커니즘을 제공해 사용자가 요소의 높이와 너비를 모두 조정할 수 있게 한다.

  * resize 종류

    * both
    * horizontal
    * vertical
    * none

  * 예시

    * <style>
              div {
                        border : 1px solid red;
                        background-color : yellow;
                        width : 100px;
                        height : auto;
                        resize : both;
                        overflow : auto;
                    }
                </style>

    * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200927135101050.png" alt="image-20200927135101050" style="zoom:50%;" />



* 마진 설정하기

  * css에서 지정 가능

  * 값 종류 (음수도 가능, 음수는 주로 텍스트와 이미지를 겹치게 보여지기 위해 사용한다.)

    * auto : 브라우저가 마진을 계산
    * length : 마진을 px, pt, cm 단위로 지정 가능(디폴트는 0px)
    * % : 요소 폭의 퍼센트로 지정
    * inherit : 부모 요소로부터 상속

  * 각 변의 마진을 별도로 지정하는 방법

    * margin-top : 10px

      margin-right : 20px;

      margin-bottom : 30px;

      margin-left : 40px

    * margin : 10px 20px 30px 40px; /* top right bottom left 순서 */

    * margin : 10px; (top right bottom left 모두 포함)

    

* 패딩 설정하기

  * 콘텐츠와 경계 사이의 간격

    * length : px, pt, cm 단위로 패딩 설정
    * % : 내용물의 퍼센트로 지정

  * 각 변의 패딩을 별도로 지정하는 방법

    * padding-top : 10px;

      padding-right : 20px;

      padding-bottom : 30px;

      padding-left : 40px;

    * padding : 10px 20px 30px 40px;

    * padding : 10px /* 모든 패딩이 10px로 설정 */



* 마진 / 패딩 예제

  *     <style>
                  p.t1 {
                      margin : 0px;
                      padding : 0px;
                      border : 2px solid red;
                      background-color : yellow;
                  }
                  p.t2 {
                      margin : 10px;
                      padding : 20px;
                      border : 2px solid red;
                      background-color : green;
                  }
              </style>

  * ![image-20200927140052870](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200927140052870.png)



* 박스 크기 계산

  * 요소 전체 크기를 계산하려면 패딩, 경계, 마진을 더해야 한다.

  * 예시

    * #target {

      ​				width : 200px;

      ​				padding : 10px;

      ​				border : 5px solid red;

      ​				margin : 20px;

      }

    * 요소 전체 크기 : 270px (200 + (10 + 5 + 20) * 2)

  * 패딩은 요소 배경색의 영향을 받는다. (마진은 투명색)



* margin 속성을 이용한 수평 정렬

  * 인라인 요소 ("text align : center")

    * <p style="text-align : center">
          <em>My Test</em>
      </p>

  * 블록 요소 

    * h1, h2, p, table, div 등과 같은 블록 요소를 중앙 정렬 하려면 왼쪽 마진과 오른쪽 마진을 auto로 설정하면 된다.

    * 예시

      * <head>

          <title>margin auto practice</title>

              <style>

        ​    p {

        ​      border : 2px dotted red;

        ​    }

          </style>

        </head>

        <body>

            <p style="margin-left:auto; margin-right:auto; width:50%">My Test</p>

        </body>

      * ![image-20200927141207732](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200927141207732.png)

      * 이 때 width를 지정하지 않으면 블록 요소가 전체 너비를 다 차지해서 중앙 정렬 효과를 볼 수 없기 때문에 지정해줘야 효과를 확인할 수 있다.



## 04. 배경 설정하기

* css 를 통해 요소 배경 설정 가능
  * background : 한 줄에서 모든 배경 속성을 정의
  * background-attachment : 배경 이미지가 고정되어 있는지, 스크롤 되는지를 지정한다.
  * background-color : 배경색을 정의한다.
  * background-image : 배경 이미지를 정의한다.
  * background-position : 배경 이미지의 시작 위치를 지정한다.
  * background-repeat : 배경 이미지의 반복 여부를 지정한다.



* 배경색 설정
  * background-color로 배경색 정의 방법
    * 이름 (red)
    * 10진수 (rgb(255, 0, 0))
    * 16진수 (#ff0000)



* 배경 이미지 설정

  * background-image로 배경으로 사용할 이미지 지정

  * 예시(back.gif로 배경 설정 시)

    * body { background-image : url('back.gif'); }

  * 배경 이미지는 수평이나 수직 방향으로 반복되면서 칠해지므로, 이미지에 따라 수평이나 수직으로만 반복되는 것이 필요할 수 있다.

    * background-repeat 특정을 설정하면 해결된다.

    * body {

      ​			background-image : url("back.gif");

      ​			background-repeat : repeat-x; /* x방향으로만 반복한다 */

      }

    * body {

      ​			background-image : url("back.gif");

      ​			background-repeat : no-repeat;

      }



* 배경 이미지 부착 방법
  * background-attachment 속성은 배경 이미지의 부착 방법을 설정한다.
    * scroll : 배경이 요소와 함께 스크롤 된다. (Default)
    * fixed : 배경이 뷰포트에 대해 고정된다.
    * local : 요소의 콘텐츠와 함께 같이 스크롤 된다. (scroll과 차이는?)



* 배경 이미지 위치 설정
  * background-position 속성은 배경 이미지의 위치를 설정한다.
  * px 단위 또는 % 단위로 지정 가능하다
    * background-position : 100px 200px;
  * 추가 키워드
    * left top, left center, left bottom
    * right top, right center, right bottom
    * center top, center center, center bottom



* 배경에 관한 속성 한 줄로 정리
  * body { background : #ffffff url("back.gif") no-repeat right top; }



* 배경 이미지의 크기 지정
  * background-size 속성은 배경 이미지 크기를 지정
  * 픽셀, % 단위로 지정 가능 (퍼센트는 부모 요소의 가로와 세로의 기준으로 계산된다.)



## 05. 링크 스타일

* 링크 스타일

  * 링크 색상, 폰트, 배경을 CSS로 설정 가능하다.

  * 링크 스타일 4가지

    * a:link : 방문되지 않은 링크 스타일
    * a:visited : 방문된 링크 스타일
    * a:hover : 마우스가 위에 있을 때 스타일
    * a:active : 마우스로 클릭될 때의 스타일
    * 주의할 점 : 반드시 위 순서대로 (위에서 아래) 위치해야 제대로 적용된다.

  * 예시

    * <head>
          <style>
              a:link {color : green}
              a:visited {color : red}
              a:hover {color : blue}
              a:active {color : yellow} 
          </style>     
      </head>
      <body>
          <p>
              <a href="" target="_blank">여기가 링크입니다.</a>
          </p>
      </body>

      

* 링크의 다른 스타일
  * 링크에 마우스 커서가 위치할 때 텍스트 크기 변화를 줄 수 있다. 또는 배경색이 변경되도록 설정할 수 있다. 
  * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200927151000801.png" alt="image-20200927151000801" style="zoom: 50%;" />
    * style1 클래스는 마우스를 링크 위에 올리면 font 크기가 1.5배 커진다.
    * style2 클래스는 마우스를 링크 위에 올리면 링크 배경색이 초록색으로 바뀐다.



## 06. 리스트 스타일

* 리스트에서 사용되는 속성

  * list-style : 리스트에 대한 속성을 한 줄로 설정한다.

  * list-style-image : 리스트 항목 마커를 이미지로 지정한다.

    * ul { list-type-image : url("bullet.png"); }

  * list-style-position : 리스트 마커의 위치를 안쪽인지 바깥쪽인지를 지정한다(inside or outside)

  * list-style-type : 리스트 마커 타입을 지정한다.

    * ul.style1 { list-style-type : circle; }

      ul.style2 { list-style-type : square; }

      ol.style3 { list-style-type : upper-raman; }

      ol.style4 { list-style-type : alpha; }



* 네비게이션 예제 (매우 중요!!)

  * ```html
    <!DOCTYPE html>
    
    <html>
    
    <head>
    
      <title>list style2 example</title>
    
        <style>
    
    ​    ul {
    
    ​      list-style : none; /* 아무런 불릿을 붙이지 않는다. */
    
    ​      text-align : center; /* 리스트 안 텍스트가 중앙 정렬 */
    
    ​      /* 리스트의 위 아래에 경계선을 그린다. padding은 다음 장에서 배운다. */
    
    ​      border-top : 2px solid red; border-bottom : 2px solid red; padding : 10px 0;
    
    ​    }
    
    ​    ul li {
    
    ​      display : inline; /* 리스트 항목이 한 줄에 차례대로 배치된다. */
    
    ​      text-transform : uppercase; /* 대문자 */
    
    ​      padding : 0 10px; letter-spacing : 10px; /* 항목 간의 간격(padding)과 글자 간격(letter-spacing) 설정 */
    
    ​    }
    
    ​    ul li a {
    
    ​      text-decoration : none; /* 자동적으로 그려지는 밑줄 제거 */
    
    ​      color : black; /* 마우스가 위에 가면 밑줄이 그어진다. */ 
    
    ​    }
    
    ​    ul li a:hover {
    
    ​      text-decoration : underline;
    
    ​    }
    
      </style>
    
    </head>
    
    <body>
    
      <ul>
    
    ​    <li><a href="#">HOME</a></li>
    
    ​    <li><a href="#">BLOG</a></li>
    
    ​    <li><a href="#">ABOUT</a></li>
    
    ​    <li><a href="#">CONTACT</a></li>
    
      </ul>
    
    </body>
    
    </html>
    ```

  

  * 결과물

![image-20200927160158313](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200927160158313.png)





## 07. 테이블 스타일

* 테이블 스타일 종류
  * border : 테이블 경계선
  * border-collapse : 이웃한 셀의 경계선을 합칠 것인지 여부
  * width : 테이블 가로 길이
  * height : 테이블 세로 길이
  * border-spacing : 테이블 셀 사이의 거리
  * empty-cells : 공백 셀을 그릴 것인지 여부
  * table-align : 테이블 셀의 정렬 설정



* 테이블 경계
  * border 속성 사용(테이블뿐만 아니라 HTML 요소 경계선 설정 시에도 사용)
  * 예시
    * border : 5px solid red;
      * width, style, color 순서!



* 경계 통합하기
  * border-collapse는 테이블이나 셀의 경계선 표시 방법을 지정하는 속성
  * collapse와 separater 사용 가능
    * collapse : 이웃하는 셀 경계선을 합쳐 단일선으로 표시
    * separate : 이웃하는 셀 경계선을 분히하여 표시



* 테이블 배경색





* 테이블의 가로와 세로 길이 지정
  * width와 height 속성 이용



* 테이블 텍스트 정렬
  * 테이블 안의 text-align은 테이블 안의 텍스트 정렬(left, right, center)
  * 수직 방향 정렬은 vertical-align을 사용(top, bottom)



* 테이블 캡션
  * 테이블에 캡션을 추가할 수 있다.
  * 캡션 위치 지정
    * caption-side : 캡션 위치를 지정한다. (top / bottom / inherit)



* 공백 셀 표시 여부
  * 내용을 가지고 있지 않은 공백 셀의 표시 여부는 empty-cells로 지정
  * empty-cells : 공백 셀의 표시 여부 (show / hide / inherit)



* 짝수행과 홀수행을 다르게 하는 것을 자동으로 하기  위해 JS를 이용하거나 CSS 선택자의 nth-child를 사용