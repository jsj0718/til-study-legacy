# Chapter 15. JSP



## 01. JSP 개요

* 서버와 클라이언트

  * 클라이언트-사이드 : 인터넷에서 클라이언트 컴퓨터 쪽에서 실행되는 프로그램

    * 클라이언트: 서버에게 웹 페이지를 요구

  * 서버-사이드 : 웹 서버는 웹 페이지를 찾아서 클라이언트에게 전달

    * GCI(Common Gateway Interface) : 서버 쪽 도우미 프로그램

      C, Python, JAVA, PHP, ASP 등이 있다.

      그 중에서 Java는 플랫폼에 독립적이고 스레드를 사용할 수 있어서 효율적이며, 풍부한 라이브러리가 장점이다.

      자바를 서버 쪽에 사용하는 기술로 서블릿(Servlet) 이 있다.

      >* 서블릿 장점
      >
      >1. 효율적 (CGI는 서버 자원을 많이 사용하는데, 스레드를 생성하여 각 요청을 서비스하므로 효율적이다.)
      >
      >2. 편리 (이미 Java를 알고 있는 개발자는 새로운 스크립트 언어를 학습할 필요가 없다.)
      >
      >3. 강력 (자바 서블릿을 사용하면 기존 CGI으로 어려웠던 작업들을 쉽게 처리할 수 있다. 예를 들어 서블릿은 웹 서버와 직접 통신이 가능하다.)
      >
      >4. 이식성 존재 
      >
      >   (서블릿은 자바 언어를 사용하며, 표준화되어 있는 라이브러리를 사용한다. 
      >
      >   자바 자체가 바이트 코드로 작성된 코드를 가상 기계 위에서 실행하는 방식이므로 서블릿도 플랫폼 종류 상관없이 실행 가능하다.)
      >
      > 
      >
      >* 서블릿 단점
      >  1. 그러나 서블릿은 자바 언어 안에 HTML 코드를 넣어야 하므로 어려운 점이 존재했다. 
      >  2. 자바 개발자는 HTML을 모르고, 디자이너는 자바를 모르기 때문이다.
      >
      > 
      >
      >* JSP (Java Server Page)
      >
      >  JSP는 서블릿 단점을 해결하기 위해 개발되었다.
      >
      >  JSP는 자바를 기반으로 동적인 웹 페이지를 구축할 수 있는 서버-사이드 스크립트 언어로 자바 서블릿을 기반으로 한다.
      >
      >  JSP는 서블릿과 반대로, HTML 문서 안에 필요할 때만 자바 코드가 들어간다. 
      >
      >  개발자가 HTML 페이지 안에 필요할 때마다 (%...%)를 통해 삽입 가능하다.
      >
      > 
      >
      >* JSP 엔진
      >
      >  웹 서버가 JSP를 처리하기 위해서 JSP 엔진을 가지고 있어야 한다.
      >
      >  JSP 엔진이란 JSP를 처리하는 컨테이너이다.
      >
      >  JSP 컨테이너는 JSP 페이지에 대한 요청을 받는다.
      >
      >  (e.x. 아파치 톰캣이란 웹 서버는 JSP 컨테이너를 내장한다.)
      >
      >  JSP 컨테이너는 JSP가 필요로 하는 실행 환경과 다른 서비스를 제공하기 위해 웹 서버와 함께 작업한다.
      >
      >  JSP 컨테이너는 JSP에 속하는 요소를 처리하게 된다.
      >
      > 
      >
      >* JSP 처리 과정
      >  1. 클라이언트가 URL을 통해 JSP 페이지를 요청
      >  2. 웹 서버가 이 요청을 서블릿 컨테이너로 전송
      >  3. 서블릿 컨테이너는 요청된 JSP 페이지를 검색해 이것을 자바 파일로 변환 후 컴파일해서 서블릿 객체를 생성
      >  4. 이 객체가 서블릿 컨테이너에 로딩되어 실행
      >  5. 실행된 결과는 웹 서버를 통해 클라이언트에 응답 형태로 전달됨
      >  6. 이 변환은 한 번만 일어나므로 속도는 느려지지 않는다.



## 04. 기본적인 JSP

* JSP 인코딩 방법

```html
<!-- JSP 인코딩 방법 -->
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
```



* JSP 수식

  * 어떤 HTML 파일도 확장자만 jsp로 변경하면 jsp파일로 변환 가능
  * HTML 안에 자바를 내장하는 방법

  ```html
  <!-- 자바 수식, 실행될 때마다 새롭게 실행된다. -->
  <%= expression %> 
  ```

  * 수식은 실행 시간에 계산된 후 string 객체로 변환되어 수식으로 나타나는 위치에 삽입된다.
    * 자바에는 String이라는 Class가 존재한다. String Class는 문자열을 손쉽게 사기 위해서 존재하는 Class 이다.
  * 수식은 Java에서 유효한 수식이면 어떤 것이든 가능하며, 문장 끝에 ;를 붙이면 안된다.

  > 서버 관점에서 바라보기
  >
  > 1. JSP 파일이 최초로 사용되면 톰캣은 JSP를 서블릿으로 변환하고 서블릿을 컴파일하여 실행한다.
  > 2. 서블릿 코드는 톰캣의 "work\Catalina\localhost\Hello" 디렉토리에서 찾을 수 있다.
  > 3. 이름은 hello_jsp.java로 저장되어 있다.
  >
  > ```html
  > out.write("<!DOCTYPE html>\r\n");
  >       out.write("<html lang=\"en\">\r\n");
  >       out.write("<head>\r\n");
  >       out.write("    <meta charset=\"UTF-8\">\r\n");
  >       out.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\r\n");
  >       out.write("    \r\n");
  >       out.write("    <title>Hello World</title>\r\n");
  >       out.write("</head>\r\n");
  >       out.write("<body>\r\n");
  >       out.write("    안녕하세요. 현재 시각은 ");
  >       out.print( new java.util.Date() );
  >       out.write("입니다.\r\n");
  >       out.write("</body>\r\n");
  >       out.write("</html>");
  > ```
  >
  > * HTML 문장은 out.write를 이용해 그대로 출력
  > * JSP 수식은 계산되고 계산 결과값이 response 메시지 일부로 출력
  > * 동일한 JSP 파일을 다시 사용할 때는 속도가 빨라진다. 왜냐하면 미리 변환된 서블릿 코드가 바로 실행되기 때문이다. (JSP -> 서블릿 변환과 서블릿 컴파일 과정 생략)



* 스크립틀릿

<%= %> 안에 자바 수식을 내장할 수 있지만, 많은 코드를 넣을 수 없다. 하지만 JSP는 JSP 안에 상당히 많은 분량의 자바 코드 블록을 작성할 수 있도록 허용한다.

코드 블록은 <% %> 사이에 넣으면 된다. (= 생략)

```java
// 스크립틀릿
<% code_block %>
```

```html
<!-- 스크립틀릿에 포함된 자바 코드로 작성된 JSP -->
<%
java.util.Date date = new java.util.Date();
%>

안녕하세요. 현재 시각은 <%= date %> 입니다.
```

```html
<!-- JSP 수식(<%= %>)이 없는 소스, out 변수로 대체 -->
<%
   System.out.println("날짜를 출력해본다.") // ?
   java.util.Date date = new java.util.Date();
%>
	안녕하세요. 현재 시각은
<%
   out.println(String.valueOf(date)); // String은 문자열, valueOf는 값
%>
	입니다.
```

```html
<!--
request는 브라우저와 서버 사이의 상호작용을 참조.
만약 사용자가 URL을 클릭하면 브라우저는 URL을 포함한 request 객체를 생성해서 서버로 보낸다.
서버가 데이터를 반환하면 브라우저는 화면에 표시한다.
request의 일부로 다양한 데이터가 포함되어 있는데, 여기에는 브라우저가 서버로부터 원하는 정보가 들어있다. (호스트 이름, ip 주소 등)
-->
<%
	java.util.Date date = new java.util.Date();
%>
안녕하세요. 현재 시각은 
<%
	out.println(date);
	out.println("<br>이고 ip 주소는");
	out.println(request.getRemoteAddr());
%>
입니다.
    
<!--
request 유사 변수로 response가 존재한다. 
(브라우저에게 보내는 응답을 작성할 때 사용)

* 예시
response.sendRedirect(anotherUrl);
-->
```



* 스크립틀릿과 HTML 같이 사용

```html
<table border=2>
    <%
        int n = 3;
        for (int i = 0; i < n; i++) {
    %>
    <tr>
        <td>Number</td>
        <td><%= i+1 %></td>
    </tr>
    <%
    }
    %>
</table>
<!--
%>는 HTML로 돌아가게 하고, <%는 스크립틀릿으로 돌어가게 한다.
즉 이를 통해 HTML도 제어문을 통해 제어 가능하다.
```



* JSP 주석

```html
<%-- 여기는 주석 --%>
```



* JSP 지시어

```html
<!DOCTYPE html>
<%@ page import="java.util.*"%>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
    <title>Document</title>
</head>
<body>
    <%
        Date date = new Date();
    %>
    현재 시각은 <%= date %> 입니다.
</body>
</html>
```

```html
<%@ page import="java.util.*" %>
<!--
<%@ : 지시어 시작
page : 페이지에 관한 지시어
import="java.util.*" : 페이지를 읽어들임
%> : 지시어 종료
-->
```

```html
<!-- include 지시어, 물리적으로 다른 파일의 내용을 포함할 때 사용 -->
아래에서 hello.jsp를 포함시킨다. <br>
<%@ include file="hello.jsp" %>
```



* JSP 선언

  * 개발자가 작성하는 JSP는 하나의 클래스로 변환된다.
  * 개발자가 작성하는 모든 스크립틀릿은 이 클래스 속 하나의 메서드 안에 위치된다.
  * 개발자는 필요한 변수와 메서드 선언을 이 클래스에 추가할 수 있다.

  ```html
  <!-- 변수나 메서드 선언 방법 -->
  <%! Date date;... %>
  ```

> 그러나 일반적으로 JSP 선언으로 변수를 선언하는 것은 좋지 않다. JSP는 일반적으로 멀티 스레드 형태로 실행되는데, 한 개의 변수를 사용하기 위해 다툴 수가 있다. (동기화로 해결 가능하나 성능이 나빠진다.) 
>
> 서로 다른 페이지끼리 데이터를 공유하려면, session 객체나 request 객체를 이용하는 것이 좋다. 
>
> 하지만 스크립틀릿 안에서 변수를 선언하는 것은 지역 변수이기에 상관없다.
>
>  
>
> JSP에서 제공되는 9개의 내장 객체는 request, out, session, application, config, pageContext, page, exception 이다.



## JSP 제어문

JSP 파일에는 완전한 Java 언어의 제어문을 사용할 수 있다. 



* 조건문

```html
<%! int day = 3; %>
<html>
<head>
	    
</head>    
<body>
    <% if (day == 1 | day == 7) { %>
       <p>오늘은 주말입니다.</p>
    <% } else { %>
        <p>오늘은 주말이 아닙니다.</p>
    <% } %>    
</body>
</html>
```

```html
<%! int day = 2; %>
<html>
<head>
	    
</head>    
<body>
<%
switch(day) {
case 0:
   out.println("오늘은 일요일입니다.");
   break
case 1:   
	out.println("오늘은 월요일입니다.");
   break
case 2:   
	out.println("오늘은 화요일입니다.");
   break
case 3:   
	out.println("오늘은 수요일입니다.");
   break
case 4:   
	out.println("오늘은 목요일입니다.");
   break
case 5:   
	out.println("오늘은 금요일입니다.");
   break
case 6:   
	out.println("오늘은 토요일입니다.");
   break
default:
   out.println("잘못된 요일입니다.")
}
%>
</body>
</html>
```



* 반복문(for, while, do...while)

```html
<%! int fontSize; %>
<html>
<head>
	    
</head>    
<body>
<%for ( fontSize = 1; fontSize <= 6; fontSize++) { %>
    <font color = "red" size = "<%= fontSize %>">
    안녕하세요?
    </font> <br>
<%}%>
</body>
</html>
```





## 07. MySQL