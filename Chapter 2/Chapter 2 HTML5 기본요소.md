# HTML5 기본요소



## 01. 이번 장의 목표

**! 웹페이지를 만드는데 필요한 내용을 중심을 학습한다.** 

(텍스트 표시, 이미지 표시, 하이퍼 링크, 테이블 등)



* 학습할 내용
  * 주석
  * 제목, 단락, br
  * 글자 스타일
  * 링크
  * 이미지
  * 수평선
  * 리스트
  * 테이블
* 예제
  * 개인 홈페이지
  * 커피 전문점 웹 페이지
  * 썸네일 이미지 갤러리 페이지
  * 강좌 소개 웹 페이지



## 02. 텍스트 표시

* 단락(paragraph), "<p> ~ </p>"
  * 단락 : 전체 글을 내용에 따라 나눌 때, 하나하나의 짧은 이야기 토막을 뜻한다.
  * HTML 문서에서 텍스트는 "<body> ~ </body>" 안에서 표시가 가능하지만, 여러 줄로 이뤄진 텍스트는 단락을 나눠주는 것이 좋다.

  * 단락은 <p> 태그로 정의된다. 웹 브라우저는 자동적으로 단락 전후에 빈 줄을 추가한다.

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200924142828475.png" alt="image-20200924142828475" style="zoom:50%;" />

* 줄바꿈, br(break)
  * 새로운 단락을 시작하지 않고 줄바꿈을 원할 때 br 태그를 사용한다. 
  * br은 break에서 나온 용어로, 종료 태그를 갖지 않는다.



* 텍스트 입력 시 주의사항
  * HTML 코드에서 엔터키를 활용한 줄바꿈은 웹 브라우저에 적용되지 않는다.
  * 또한 스페이스를 여러 개 입력했다고 해서 화면에 스페이스가 여러 개 표시되지 않는다.
  * 즉, 웹 브라우저는 여분의 스페이스, 줄을 제거한다.



* "<pre> ~ </pre>" 태그
  * 프로그래머가 입력한 그대로 화면에 나타나게 하는 태그이다.
  * pre는 "previously formatted text"에서 나온 용어이다. (스페이스, 탭, 줄 바꿈 그대로 유지)
    * previously : 이전에, 사전에
    * formatted : 형식화된
  * 단, 글씨체가 다르다는 점이 있다.



* 헤딩(heading)
  * 웹 페이지의 머리기사(headline)이다.
  * "<h1>"부터 "<h6>"까지 있으며 중요도(크기)는 1부터 6 순서대로 작아진다.
  * 헤딩은 페이지의 머리기사 용도로만 사용해야 한다.
    * 단순히 글씨 크기를 크게 하거나 굵게 하기 위한 용도로 사용하면 안 된다!
    * 왜냐하면 검색엔진은 헤딩을 사용해서 웹 페이지의 내용을 색인화하여 저장한다. 
    * 따라서 문서의 중요한 키워드를 헤딩을 사용하여 사용자에게 보여주는 것이 중요하다.

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200924150328451.png" alt="image-20200924150328451" style="zoom:50%;" />

* 주석(commnet)
  * 코드를 설명하는 글이나 현재 불필요한 코드를 일시적으로 제거하는 용도로 사용
  * <!-- 이것이 주석입니다. --> 형식으로 작성



* 텍스트 서식
  * b : bold체로 만든다.
  * i : 이탤릭체로 만든다.
  * strong : 텍스트를 강하게 표시한다. (볼드체로 표시)
  * em : 텍스트를 강조한다. (이탤릭체로 표시)
  * code : 텍스트가 코드임을 표시한다.
  * sup : 위첨자
  * sub : 아래첨자
  * mark : Highlight를 표시한다.

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200924150607092.png" alt="image-20200924150607092" style="zoom:50%;" />



* 수평선(hr, horizontal line)
  * hr 태그를 사용하여 브라우저 너비만큼의 수평선을 그릴 수 있다.

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200924150853788.png" alt="image-20200924150853788" style="zoom:50%;" />



* 특수 문자
  * '<' 나 '>' 같은 문자는 태그를 표현하기 위해 사용되므로 화면에 표시하기 어렵다.
  * 따라서 특수한 기호를 통해 나타낸다.
    * &lt;
    * &gt;
    * &quot;
    * &amp;
    * &nbsp;
  * HTML은 여러 개의 공백이 있어도 하나의 공백으로 간주하기 때문에 여러 개의 공백을 나타나기 위해서는 공백 특수 문자를 여러 번 사용해야 한다.



## 03. 리스트

* 리스트란?
  * 리스트는 항목을 나열하는데 사용된다.
  * 번호 있는 리스트와 번호 없는 리스트로 구분된다.
  * 구조는 다음과 같다.

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200924153642872.png" alt="image-20200924153642872" style="zoom: 67%;" />



* 번호 없는 리스트(unordered lists)
  * 번호 없는 리스트는 <ul> 태그로 시작한다.
  * 각 항목 리스트는 <ul> 태그 안에 <li> 태그로 시작한다. (li는 list의 약자)
  * 리스트 항목은 앞에 불릿이 붙는다.

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200924154355657.png" alt="image-20200924154355657" style="zoom:67%;" />



* 번호 있는 리스트(ordered lists)
  * 번호 있는 리스트는 <ol> 태그로 시작한다.
  * 리스트 항목은 앞에 번호가 붙는다.

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200924154515753.png" alt="image-20200924154515753" style="zoom:67%;" />

* 정의 리스트(definition lists)
  * 항목들과 함께 항목의 정의(설명)가 표시되는 리스트이다.
  * "<dl>" 태그로 생성되고, "<dt>" 태그는 항목을 나타내며, "<dd>"태그는 항목에 대한 설명을 나타낸다.
  * l은 list(목록), t는 term(용어), d는 description(설명)

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200924160323943.png" alt="image-20200924160323943" style="zoom:50%;" />

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200924160302527.png" alt="image-20200924160302527" style="zoom:50%;" />



* 참고 사항 (한글 코드)

  * 웹 프로그래밍에 사용되는 한글 코드에는 2가지 방식 존재
    * euc-kr
    * utf-8
  * euc-kr : 영어와 한글을 2바이트로 나타내는 방식
    * 한글이 많을 때 메모리 사용량이 적으며 호환성이 좋다.
    * 한글과 영어만 사용하는 웹 페이지에 적당하다.
    * 그러나 다국적 문자를 표현하는데 한계가 있다.

  * utf-8 : 유니코드의 일종으로 가변길이 문자 인코딩 방법이다.
    * 영어는 1바이트, 한글은 3바이트로 표현한다.
    * 모든 한글 문자를 표현할 수 있으며, 다른 나라 운영체제에서도 폰트 없이 한글을 볼 수 있다.



## 04. 링크

* 하이퍼링크는 다른 문서로 점프할 수 있는 단어나 이미지이다. <a> 태그가 하이퍼링크를 정의한다.

  * <a>는 anchor의 약자로 '정박하다' 라는 의미를 가지고 있다.

  * <a> 요소의 가장 중요한 속성은 href로 링크 주소는 이를 통해 정의된다.

    * <a href = "www.naver.com"></a>

    * <a></a> 사이에 추가 정보를 넣으면 그것이 링크 텍스트가 되며, 클릭 시 이동하게 된다.

    * target 속성

      * _blank : 새로운 탭에서 새로운 페이지를 연다.
      * _self : 현재 탭에 새로운 페이지를 적재한다. (Default)
      * _parent : 부모 프레임에 새로운 페이지를 적재한다.
      * _top : 현재 탭에 새로운 페이지를 적재하고 모든 프레임을 취소한다.

    * id 속성

      * 현재 페이지의 다른 위치로 이동시킨다.

      * HTML 문서 내에서 북마크를 생성해야 한다.

      * <a href = "#name"></a> 선언 -1

      * <a id = "name"></a> 선언 -2

      * 1 클릭 시 2로 이동함

        

* 링크 색상

  * 청색 : 방문하지 않은 링크
  * 보라색 : 방문한 링크
  * 빨간색 : 활성 링크(active link)

  

* 경로

  * 절대 경로 : href = "http://www.google.co.kr" (다른 웹 사이트 페이지)
  * 상대 경로 : href = "../doc/info.html" (웹 사이트 내 다른 페이지)
  * 내부 파일 : href = "#anchor1" (현재 페이지 안의 다른 위치)

  

* 이메일 링크

  * 다른 사람이 사이트에 이메일을 보낼 수 있도록 하려면 이메일 링크를 두는 것도 좋다.
    * <a href = "mailto:jsj1275@naver.com?subject='name'"></a>



* 다운로드 링크
  * <a href="http://www.company.com/data.zip"></a>



* base 태그

  * 헤드 섹션에서 base 태그를 통해 모든 링크에 대한 기본 디렉토리 지정 가능

    ![image-20200924175928268](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200924175928268.png)

    			1. 모든 링크의 기본 디렉토리가 http://www.company.com/으로 설정됨
    
       			2. info.html은 http://www.company.com/info.html을 의미함



## 05. 이미지

* 이미지 태그는 <img> 로 정의된다.

  * <img src="" width = "300" height = "230">

    * width : 가로 지정 (기본 단위 px, 상대적인 크기를 나타내기 위해 %도 사용)
    * height : 세로 지정 (동일)
    * alt : 브라우저가 이미지를 화면에 표시하지 못할 때, 표시되는 대체 텍스트를 지정(alternative, 대안)
    * 파일 저장 후 불러올 때 해당 폴더 경로를 적어야 한다.
      * 예를 들어 작업 폴더 내 image 폴더에 사진을 저장했다면, "image/파일 이름"으로 적는다.

    

  * 이미지 표시할 때 반드시 이미지 크기 지정을 하는 것이 좋다.

    * 브라우저가 페이지 로드할 때, 미리 필요한 공간을 마련하기 때문이다.
    * 이 정보가 없을 때, 페이지 로드 중 레이아웃이 변경될 수 있다.



* HTML 요소
  * 블록 요소(block element) : 요소를 화면에 표시한 후 항상 줄 바꿈이 일어남
  * 인라인 요소(inline element) : 요소를 표시한 후 줄 바꿈이 일어나지 않음 (<img>는 이에 해당)



* 브라우저가 이미지 처리하는 방법
  * <img> 태그를 발견 시 화면에 표시하기 전에 서버로부터 다운로드를 받음



* 웹이 사용하는 이미지 종류
  * JPEG : 실사와 같이 복잡하고 많은 색상으로 이뤄진 이미지에 적합 (투명 배경 지원 X, 애니메이션 지원 X)
  * PNG : 적은 수의 색상을 가진 이미지에 적합, 투명 배경 지원 O (그러나 같은 품질인 JPEG보다 크기가 큼)
  * GIF : 투명 배경 및 애니매이션도 지원



## 06. 테이블(Table)

* 표 형태의 데이터 표시할 때 사용

  * "<table>" 태그로 정의된다.

  * 테이블 하나의 행을 "<tr>"로 표현한다. (table row)

  * 하나의 데이터는 "<td>"로 표현한다. (table data)

  * 각 열에 헤더(열의 제목)가 있는 경우 "<th>"를 활용한다. (table header)

    * th는 볼드체, 중앙 정렬로 표시한다.

    <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200924204210082.png" alt="image-20200924204210082" style="zoom:67%;" />

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200924204232191.png" alt="image-20200924204232191" style="zoom: 67%;" />

* 경계와 배경색 설정
  * 테이블 경계를 지정하지 않으면 경계선이 없다.
  * 경계는 table 태그 내 속성인 border를 이용해 설정한다. ("1" or ""만 사용하는 것을 권장)
  * HTML5에서 요소 스타일 지정은 반드시 CSS를 사용해야만 한다.



* 테이블에서 열과 행 병합
  * 행 병합(row span) : rowspan을 2로 지정한 것은 현재 셀 위치에서 2개의 행을 병합하겠다는 의미 (상하)
  * 열 병합(column span) : colspan을 3으로 지정한 것은 현재 셀 위치에서 3개의 열을 병합하겠다는 의미 (좌우)



* 테이블의 캡션(테이블 제목)
  * 테이블의 제목을 삽입하려면 <caption> 을 사용한다.



* 테이블을 이용한 요소 배치
  * 테이블 셀 안에 다른 HTML 요소를 넣을 수 있다. (리스트, 이미지, 다른 테이블까지 가능)

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200924214057725.png" alt="image-20200924214057725" style="zoom: 50%;" />