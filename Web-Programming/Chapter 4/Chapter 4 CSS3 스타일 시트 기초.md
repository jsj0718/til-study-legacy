# CSS3 스타일 시트 기초

* 학습목표
  * HTML과 CSS 관계 이해
  * CSS 선택자 이해 및 응용
  * CSS로 색상, 폰트 지정



## 01. CSS(Cascading Style Sheets)의 개념

* 문서 구조(내용)은 HTML로 정의
  * "<h1>"은 폰트의 크기를 지정하는 것이 아니라 헤드라인이라는 것을 말하는 것이다.
  * 콘텐츠를 제공하는 작가
* CSS로 색상, 폰트, 크기같은 스타일 지정
  * HTML 요소를 어떻게 화면에 표시할 것인지 정의하는 시트
  * 웹 디자이너
  * 애니메이션, 장면 전환, 2차원 및 3차원 변환 등 다양한 효과가 포함됨
  * 모듈로 구성되어 있어서 필요한 부분만을 선별하여 탑재 가능
    * 선택자(Selectors)
    * 박스 모델(Box Model)
    * 배결 및 경계선(Backgrounds and Borders)
    * 텍스트 효과(Text Effects)
    * 2차원 및 3차원 변환(2D/3D Transformations)
    * 애니메이션(Animations)
    * 다중 컬럼 레이아웃(Multiple Column Layout)
    * 사용자 인터페이스(User Interface)
* JS로 문서의 동작 정의



* CSS 필요성

  * 아주 거대하고 복잡한 사이트를 관리할 때, 모든 페이지가 동일한 CSS를 공유한다.
  * 따라서 CSS에서 어떤 요소의 스타일을 변경하면 관련되는 전체 페이지의 내용이 한번에 변경되므로,
    1. 문서 전체의 일관성을 유지할 수 있다.
    2. 작업 시간도 단축된다.

  * 장점 정리
    1. 풍부한 디자인으로 웹 설계 가능
    2. 글자 크기, 글자체, 줄 간격, 배경 색상, 배열 위치 등 자유롭게 선택 및 변경 가능
    3. 유지보수 간편
    4. 각기 다른 사용자 환경에서 동일한 형태의 문서를 제공
       * CSS로 만들어진 문서는 브라우저 환경에 따라 홈페이지가 다르게 나타나는 경우 X
       * 어느 환경에서나 제작자 의도대로 효과 전달 O



* Cascading인 이유?
  * 하나의 요소에 여러 개의 CSS가 충돌할 수 있다.
  * 이 경우 우선순위(가중치)가 계산되고 이것에 따라서 CSS 충돌이 처리된다.
  * 외부 CSS 파일 -> "<head>"에 정의된 CSS -> 인라인 CSS -> 사용자가 제공하는 CSS



* CSS 문법

  * CSS는 HTML 요소를 페이지 위에 어떻게 그리느냐를 지시하는 명령어의 집합

    1. 스타일을 변경하고 싶은 HTML 요소 선택 (선택자)

    2. 선택자 뒤에 중괄호를 붙이고 이 중괄호 안에는 이들 요소를 어떻게 그리는지 기술 (선언)

       * 속성은 "이름:값" 형식으로 기술

       * p { background-color : yellow; }

         * p : 선택자 (단락을 뜻하는 p 요소를 의미)
         * background-color : 속성의 이름
         * yellow : 속성의 값
         * 각각의 CSS 선언은 항상 ;로 끝난다.

       * 하나의 요소에 여러 개 속성 지정을 원하면 다음과 같이 추가한다.

         * p {

           ​			background-color : yellow;

           ​			border : 2px solid red; 	

           }



* CSS 위치
  * 기본적으로 HTML의 head 요소 내에서 "<style>" ~ "</style>" 안에 적으면 된다.
  * 연습 css1 : <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200926141203893.png" alt="image-20200926141203893" style="zoom:67%;" />
  * 스타일 시트는 외부 파일로도 존재할 수 있으며, 각 요소의 속성으로도 지정할 수 있다.
  * 예제 css2 : <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200926142027807.png" alt="image-20200926142027807" style="zoom:67%;" />
    * border는 두께(px)와 종류(solid)를 추가적으로 입력해야 한다.
    * CSS 주석은 /* ~ */ 로 작성한다.



## 02. 선택자(type, id, class가 90% 사용된다.)

* 가장 중요한 부분인 선택자는 HTML 요소를 선택하는 부분이다.

  * 모든 요소에 동일한 스타일을 적용하는 것은 드물기 때문에 대부분 특정 요소를 선택 후 스타일을 적용
  * p { background-color : blue; } 중 p가 선택자
  * CSS 선택자는 jQuery에서도 사용
  * CSS 선택자 종류
    * **타입 선택자**
      * HTML 요소 이름을 사용하는 것 (p 요소 선택 시 p, h1 요소 선택 시 h1을 적으면 됨)
    * 전체 선택자
      * `*`기호로 표시되며 페이지 안 모든 요소를 선택할 때 사용한다.
      * 주로 모든 요소에 공통적인 속성을 지정할 때 사용한다.
      * `*` {color : blue;}
    * **클래스 선택자**
      * .을 이용해서 정의(요소를 정의할 때 클래스 이름을 부여할 수 있음)
      * .target { color : red; }
        * class가 target인 요소를 선택한다.
      * 몇 개의 요소를 하나의 클래스로 묶어서 스타일 지정할 때 사용
      * id는 하나의 요소, class는 여러 개의 요소를 선택할 수 있다는 차이점 존재
      * HTML 클래스 요소 정의 방법
        * "<p class="type1">" class가 type1인 단락입니다. "</p>"
        * 클래스 정의 시 클래스 이름은 숫자로 시작하면 안 된다.
      * 클래스 선택자 활용 방법
        * .type1 { color : blue; } (type1 클래스 선택)
        * h1.type1 { color : blue; } (h1 요소 중 type1 클래스 선택)
        * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200926152658286.png" alt="image-20200926152658286" style="zoom:50%;" />
          * text-align : 텍스트 배치, center : 가운데
          * .type1에 h1이나 p를 붙이면 그에만 해당하게 적용된다.
    * **아이디 선택자**
      * 특정 요소를 쉽게 선택할 수 있다. (가장 많이 사용됨)
      * `#`special { color : red; }
        * id가 special인 요소를 선택한다는 의미
      * 이를 사용하려면 HTML 요소에 id를 부여해야 한다.
        * "<p id="special">"
      * 만약 h1 요소 중 아이디가 special인 요소를 선택한다면,
        * h1`#`special { color : blue; }
    * 속성 선택자
      * 특정한 속성을 가지는 요소를 선택
      * 예시 (title 속성을 가진 h1 요소 선택)
        * h1[title] {color : blue; }
      * 예시 (class 속성이 example인 p 요소 선택)
        * p[class="example"] { color : blue; }
    * 의사 클래스(pseudo-class), pseudo : 허위의, 가짜의
      * 콜론(:)을 사용해 표기
      * 클래스가 정의된 것처럼 간주한다는 의미
        * a:link 면 a 요소에 link 클래스가 선언된 것처럼 생각하고 선택자를 만듦
      * 문서 트리의 외부에 있는 정보에 기반을 두어 요소를 선택할 때 사용된다.
      * 예시 (하이퍼링크 방문 전과 후 색상 변경 방법)
        * a:link { color : blue; } /* 아직 방문하지 않은 링크는 파랑색 표기 */
        * a:visited { color : green; } /* 방문된 링크는 녹색 표기 */
        * a:hover { color : green; } /* 사용자가 링크 위에 있을 때 */
      * 예시 (어떤 요소의 n번째 자식 요소를 나타낼 때, 테이블 짝수와 홀수행 색상을 다르게 표현하는 방법)
        * table:nth-child(2n+1) { color : navy; } /* HTML 테이블의 홀수 번째 행 */
        * table:nth-child(2n) { color : maroon;} /* HTML 테이블의 짝수 번째 행*/

  * 선택자 그룹

    * 선택자를 콤마(,)로 분리하여 나열 시 각 선택자에 의해 선택된 요소의 합을 의미하는데, 이를 선택자 그룹이라고 한다.

    * 선택자 (s1, s2) : s1으로 선택된 요소와 s2로 선택된 요소를 합친다.

    * 예시

      * h1 { font-family : sans-serif; }

        h2 { font-family : sans-serif; }

        h3 { font-family : sans-serif; }

      * h1, h2, h3 { font-family : sans-serif; } 와 동일하다.

  * 자손, 자식, 형제 결합자

    * 이들은 선택자를 결합해서 특정 요소를 선택한다.
    * s1 s2 : s1 요소에 포함된 s2 요소를 선택한다. (후손 관계)
      * 후손 : 손자, 손녀까지 포함
    * s1 > s2 : s2 요소의 직계 자식 요소인 s2를 선택한다.
      * 자식 : 아들, 딸만 포함
    * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200926154037007.png" alt="image-20200926154037007" style="zoom: 33%;" />
      * body 요소의 후손은 em 요소, 자식은 ul 요소이다.
      * body em { color : red; } /* body 요소 안 em 요소 */
      * body > h1 { color : red; } /* body 요소 안 h1 요소 */
    * 조상에서 지정된 속성은 후손 노드로 상속된다! (ul 요소 스타일이 변경되면 li도 영향을 받는다.)
      * 따라서 모든 요소의 공통적인 스타일은 body와 같은 조상 노드에 배치한다.



## 03. CSS 삽입 방법

* 3가지 방법 존재

  * 외부 스타일 시트

    * 스타일 시트를 외부에 파일로 저장
    * 많은 페이지에 동일한 스타일을 적용할 때 좋은 방법
    * 전체 웹 페이지 스타일을 하나의 스타일 파일로 변경 가능
    * 각 HTML 페이지는 "<link>" 태그를 이용해서 스타일 파일에 연결해야 한다. (head 부분)
      * "<link type="text/css" rel="stylesheet" href="mystyle.css">"
        * link : 외부 파일과 연결하기 위한 요소
        * type="text/css" : 외부 파일 종류가 css스타일 시트라는 것을 의미
        * rel="stylesheet" : HTML 파일과 외부 파일 간의 관계(relation)를 나타낸다.
        * href="mystyle.css" : 외부 파일의 위치를 적는다. (URL 형식)
    * 단순한 텍스트 파일이나, HTML 태그는 포함하면 안된다.
    * .css 확장자를 가져야 한다.
    * "<style>" "</style>" 태그 안에 삽입하면 적용이 안된다. 독립적으로 head 안에 삽입하면 된다.
    * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200926162721483.png" alt="image-20200926162721483" style="zoom:50%;" />
    * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200926162747120.png" alt="image-20200926162747120" style="zoom:50%;" />

  * 내부 스타일 시트

    * HTML 안에 CSS를 정의
    * "<style>" "</style>" 안에 스타일을 정의한다.
    * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200926162658673.png" alt="image-20200926162658673" style="zoom: 50%;" />

  * 인라인 스타일 시트

    * 각각의 요소마다 스타일을 지정하는 것
    * 이 방법은 스타일 시트의 장점을 잃게 된다. (따라서 꼭 필요한 경우만 사용하기)
    * 각 요소의 style 속성을 정의하면 된다.
    * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200926162626045.png" alt="image-20200926162626045" style="zoom:67%;" />

    

  * 다중 스타일 시트

    * 하나의 요소에 외부, 내부, 인라인 스타일을 서로 다르게 지정하고 싶을 때 어떻게 사용?
    * 일반적인 모든 스타일 시트의 규칙(숫자가 커질수록 우선순위가 높다.)
      1. 웹 브라우저 디폴트 값
      2. 외부 스타일 시트
      3. 헤드 섹션에 저장된 내부 스타일 시트
      4. 인라인 스타일 시트



* 많이 사용되는 속성
  * color : 텍스트 색상
  * font-weight : 볼드체 설정
  * padding : 요소의 가장자리와 내용 간의 간격
  * font-size  : 폰트 크기
  * background-color : 배경색
  * border : 요소를 감싸는 경계선
  * font-style : 이탤릭체 설정
  * background-image : 배경 이미지
  * text-align : 텍스트 정렬
  * list-style : 리스트 스타일



## 04. 색상

* 컴퓨터 색상은 RGB를 혼합하여 만들어진다.
* 표현 방법
  * 이름 ("red")
    * 16가지의 기본 색상, 추가로 150가지의 색상이름 사용 가능
  * 16진수 (#FF0000)
    * 항상 `#`으로 시작된다.
    * 1, 2번째는 R / 3, 4번째는 G / 5, 6번째는 B이다.
    * 3개의 16진수일 때는 1번째는 R, 2번째는 G, 3번째는 B이다.
  * RGB 값으로 색상 표현
    * 10진수 (rgb(255, 0, 0))
    * 퍼센트 (rgb(100%, 0%, 0%))



## 05. 폰트

* 폰트는 페이지 디자인에 절대적인 영향을 주는 요소이다.
* CSS font 속성을 이용해서 폰트 종류, 색상, 장식, 크기 등을 지정할 수 있다.
  * font : 한 줄에서 모든 폰트 속성을 설정할 때 사용
  * font-family : 폰트 패밀리 설정
  * font-size : 폰트 크기 설정
  * font-style : 폰트 스타일 설정 (italic)
  * font-weight : 폰트의 볼드체 여부 설정

* 폰트 종류

  * 텍스트 폰트는 font-family 속성을 이용해 설정된다.

  * 이 때 여러 개의 폰트 이름을 제공하는 것이 좋다. 

    * 브라우저가 HTML 파일을 표시할 때 클라이언트 컴퓨터에 지정된 폰트가 없는 경우도 있기 때문이다.

    * 나열 시 처음은 개발자가 원하는 폰트, 마지막은 가장 일반적인 폰트 순서로 해야한다.

    * 폰트 이름이 여러 단어면 큰따옴표를 사용해서 묶어야 한다.

    * 예시

      * body {

        ​			font-family : "Times New Roman", Times, serif;

        }

    * 한글 폰트는 문제 발생 가능성이 있기 때문에 영문과 같이 적어주는 것이 좋다.

      * body {

        ​			font-family : "나눔 고딕", "Nanum Gothic", "맑은 고딕", "Malgun Gothic", "돋움", 			"Dotum", "굴림", "Gulim";

        }



* Serif와 Sans-serif 차이
  * serif는 삐침을 뜻함
  * sans는 부정을 나타내는 접두사로 sans-serif는 삐침이 없다는 의미를 뜻함
* font-family
  * 어떤 특징을 공유하는 폰트의 집합을 의미
  * 크게 5개의 폰트 패밀리 존재
    * sans-serif(깔끔, 가독성 Good / Arial, Trebuchet MS, Verdana)
    * serif(우아, 전통 / Times New Roman, Georgia, Garamond)
    * monospace(타자기 서체, 모든 글자 폭이 같다. / Courier New, Lucida Console)
    * cursive(장난, 스타일리쉬)
    * fantasy(장난, 스타일리쉬)

* 웹 폰트

  * 웹 개발자는 사용자 컴퓨터를 제어할 수 없는데, 특정 폰트를 사용하길 원할 때 어떻게 하면 좋을까?
  * 웹 폰트는 폰트를 웹 서버에 저장했다가 필요할 때 사용자 웹 브라우저로 직접 전송하는 기법이다.
  * 이를 사용하기 위해서 @font-face 규칙을 사용한다.
    1. 원하는 웹 폰트를 구한다.
    2. 폰트 형식을 체크한다.
    3. 폰트 파일을 웹 서버에 저장한다. (폰트 파일이 저장된 위치의 URL을 기억해야 한다.)

* 폰트 크기 설정

  * 텍스트 크기 설정(단, 헤드라인을 사용하지 않고 문단의 크기를 조절해서 제목처럼 보이게 하면 안 된다.)

  * 절대 크기와 상대 크기로 설정 가능

    * 절대 크기 : 텍스트를 지정된 크기로 설정 (모든 브라우저에서 사용자가 크기 변경 불가능 X)
    * 상대 크기 : 주위 요소 크기에 비례하여 상대적으로 폰트 크기 설정 (사용자가 크기 변경 가능 O)

  * px 단위 설정

    * px은 pixel을 의미하며, 폰트 크기도 픽셀 단위로  설정 가능하다.

    * body {

      ​			font-size : 12px;

      }

      * 폰트 높이가 12픽셀이라는 의미

  * % 단위로 설정

    * 기준 폰트 크기에 비해 어느정도인지를 나타낸다.

    * 기준 폰트는 부모 요소의 폰트 크기가 기준이 된다.

    * body {

      ​			font-size : 12px;

      }

      h2 {

      ​		font-size : 200%;

      }

      * body의 200% 이므로 24px가 된다.

  * em 단위로 설정

    * em 크기 단위는 W3C에서 권장하는 단위로 배수를 의미한다.

    * em도 %와 동일하게 상대 크기이다. (기준은 부모 요소)

    * body {

      ​			font-size : 12px;

      }

      h2 {

      ​		font-size : 2.0em;

      }

      * body의 2배이므로 24px가 된다.

  * 키워드로 설정

    * xx-small, x-small, small, medium, large, x-large, xx-larger로 폰트 크기 설정

    * body {

      ​			font-size : small; /* 12px에 해당한다. */

      }



* font-weight 속성
  * 볼드체로 할 것인지를 지정(볼드체가 되면 글자 무게가 증가해서 이와 같은 이름이 붙여짐)
  * bold나 normal 중 하나로 설정
    * h1#s1 { font-weight : normal; }
    * h1#s2 { font-weight : bold; }

* font-style 속성
  * 이탤릭 텍스트로 설정할 것인지를 지정
  * normal, italic, oblique 중 하나로 설정(italic과 oblique는 흡사)
    * h1#s1 { font-style : normal; }
    * h1#s1 {font-style : italic; }



* 폰트 축약 기법
  * 폰트의 여러 가지 속성은 한 줄에서 모두 설정될 수 있다. (축약 기법)
  * 나열 순서
    * font-style / font-variant / font-weight / font-size / font-family
      * font-size와 font-family는 필수적 (하나라도 생략 시 디폴트 값이 사용됨) 
  * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200926190327289.png" alt="image-20200926190327289" style="zoom:50%;" />



## 06. 텍스트 스타일 설정

* 텍스트 스타일 관련 속성

  * color : 텍스트 색상 지정

  * direction : 텍스트 작성 방향 지정 (가로쓰기, 세로쓰기)

  * letter-spacing : 글자 간 간격 지정

  * line-height : 텍스트 줄의 높이 지정

  * text-align : 텍스트 수평 정렬 지정 (왼쪽, 중앙, 오른쪽, 양쪽(justified))

    * h1 { text-align : center; color : red; }

      p.date { text-align : right; color : indigo; }

      p.poet { text-align : justify; color : blue; }

  * text-decoration : 텍스트 장식지정

  * text-indent : 텍스트 들여쓰기 지정

  * text-shadow : 그림자 효과 지정

  * text-transform : 대소문자 변환 지정



* 텍스트 장식

  * 링크에 붙는 밑줄을 삭제할 때 사용
  * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200926200805378.png" alt="image-20200926200805378" style="zoom: 67%;" />
  * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200926200823853.png" alt="image-20200926200823853" style="zoom: 50%;" />

* 텍스트 변환

  * 텍스트 안에서 소문자나 대문자를 지정할 때 사용
  * 모든 소문자를 대문자로 변환하거나, 각 단어의 첫 글자를 대문자로 변환 시 사용
  * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200926201141353.png" alt="image-20200926201141353" style="zoom:67%;" />
  * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200926201210792.png" alt="image-20200926201210792" style="zoom:67%;" />

* 텍스트 그림자

  * CSS3에서 text-shadow 속성 지정 시 텍스트에 그림자 설정 가능

  * h1 {

    ​		text-shadow : 3px 5px 10px #000;

    }

    * 차례대로 x방향 이동거리(3px), y방향 이동거리(5px), 흐림 정도(10px), 텍스트 그림자 색상(#000)을 의미한다.

* Word Wrapping

  * 하나의 단어가 너무 길어서 영역 안에 들어가지 않는 경우 자동으로 단어를 잘라서 다음 줄로 넘기는 기능

  * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200926201828653.png" alt="image-20200926201828653" style="zoom:67%;" />

    * word-wrap : break-word; 가 넘어가는 단어를 자동으로 잘라서 다음 줄로 넘기는 기능을 갖는다.

  * ![image-20200926201919190](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200926201919190.png)

  * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200926201856719.png" alt="image-20200926201856719" style="zoom:50%;" />

    

* 다중 컬럼

  * column-count : 컬럼 개수
  * column-gap : 컬럼과 컬럼 사이의 간격
  * column-rule : 컬럼과 컬럼 사이의 선 스타일
  * <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200926202813357.png" alt="image-20200926202813357" style="zoom: 67%;" />