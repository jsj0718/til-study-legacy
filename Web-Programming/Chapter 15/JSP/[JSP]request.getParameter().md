# request.getParameter() 란?



> **웹(Web) 환경은 HTTP 프로토콜 위에서 동작하고 있습니다.**
>
>  
>
> ​    HTTP 프로토콜은 간단하게 얘기해서,
>
> ​    클라이언트가 서버에 무언가(보통은 웹페이지)를 요청(request)하면,
>
> ​    서버가 이 요청에 해당하는 것을 응답(response) 해주는 구조로 되어있습니다.
>
>  
>
> **HTTP 요청을 보낼 때, 파라미터(parameter)를 함께 끼워보낼 수 있습니다.**
>
>  
>
> ​    가령, 로그인을 할 때, 로그인 폼(form : 양식)을 입력하고, 버튼을 누르죠.
>
> ​    그러면, HTTP 요청 안에 폼 내용이 함께 끼워져서 서버로 날아가게 됩니다.
>
> ​    로그인 폼 내용이 바로, HTTP 요청의 파라미터(parameter)가 되는 겁니다.
>
>  
>
> ​    이러한 HTTP 요청을 받은 서버는 이제 어떤 일을 할까요?
>
> ​    파라미터로 날아온 로그인 폼을 일단 봐야지, 뭘하든 하겠죠.
>
>  
>
> ​    그러려면 일단 파라미터 값을 얻어내야 하는데...
>
>  
>
> **HTTP 요청의 파라미터 값을 얻기 위해 사용하는 것이 request.getParameter() 메쏘드입니다.**
>
>  
>
> ​    가령, 로그인 폼에, ID를 입력하는 <input type="text" name="id">가 있었다면,
>
> ​    서블릿에서 String strId = request.getParameter("id"); 와 같은 방식으로,
>
> ​    클라이언트가 입력한 ID가 뭐였는지 알아낼 수 있습니다.
>
>  
>
> ​    로그인에 성공했다면, 이제 어떻게 할까요?
>
> ​    클라이언트의 회원정보를 DB에서 읽어서 페이지에 뿌려주기로 합시다.
>
> ​    그러려면, 서블릿은 회원정보를 JSP에게 보내줘야 합니다. 그래야 뿌리죠.
>
>  
>
> ​    그런데 어떻게???
>
>  
>
> **다른 곳으로 정보를 넘겨주기 위해서 request 객체의 속성(attribute)을 사용합니다.**
>
> (더 정확하게는, 웹 애플리케이션 상에서 정보를 공유하기 위해서 속성을 사용합니다.)
>
>  
>
> ​    가령, 회원정보 중에서 '취미'를 JSP에게 넘겨주기 위해서,
>
> ​    서블릿에서 request.setAttribute("hobby", strHobby); 로 속성을 집어넣고,
>
> ​    JSP에서 <% String strHobby = (String)request.getAttribute("hobby"); %><% String hobby = (String)request.getAttribute("hobby"); %>로 속성을 얻는거죠.
>
>  
>
> ​    **Q :** *"걍 단순이 db에서 먼갈 꺼내와서 리퀘스트 객체에 넣을땐 set이고 꺼낼땐 겟인가요??"* 
>
> ​    **A :** 맞습니다... -_-;  (꼭 DB가 아니더라도 뭔가를 넣고 싶으면 아무거나 넣으면 됩니다.)
>
>  
>
> **setAttribute(), getAttribute()에서 속성 값으로 사용하는 타입은 Object입니다.**
>
>  
>
> ​    **Q :** *"벡터를 넘겨주면 벡터를 받음 돼는건가여?"*
>
> ​    **A :** 예.  Vector를 넘겨준다면 Vector로 타입 캐스팅 하고 받으면 됩니다.
>
>  
>
> 출처 : http://blog.naver.com/dbxhvi?Redirect=Log&logNo=100033562897



# request.getParameterValues()란? 



> **Servlet  request.getParameterValue,**  **request.getParameterValues**
>
> ﻿ 
>
> > 폼에서 전송된 파라미터 받기.
> >
> >  
> >
> > **하나의 파라미터가 하나의 값을 가질 때**
> >
> > **request.getParameter() 메소드**
> >
> >  
> >
> > 예)
> >
> > 폼에서 color 라는 이름으로 값을 전송할 때 
> >
> > <select **name="color"**>
> >
> >   <option>fireBrick
> >   <option>dodgerblue
> >   <option>mediumblue
> >   <option>honeydew
> >
> > </select>
> >
> >  
> >
> > **String colorParam = request.getParameter("color");**
>
> 
>
> > **하나의 파라미터가 여러 값을 가질 때**
> >
> > **request.getParameterValues() 메소드**
> >
> > 
> >
> > 예)
> >
> > 폼에서 sizes 라는 이름으로 값을 전송할 때
> >
> >   <input type="checkbox" **name="sizes"** value="12oz"> 12 oz .<br/>
> >
> >   <input type="checkbox" **name="sizes"** value="16oz"> 16 oz .<br/>
> >   <input type="checkbox" **name="sizes"** value="22oz"> 22 oz .<br/>
> >
> > 
> >
> > 값 하나만 사용하려면 배열 인덱스를 사용해서
> >
> >  **String one = request.getParameterValues("sizes")[0];**
> >
> >  
> >
> > 아니면 배열로 받아서
> >
> >  **String[] sizes = request.getParameterValues("sizes");**
> >
> >  
> >
> > 소스 예) 
> >
> > **전송폼 (form.html)**
> >
> > <form method="post" action="**selectColor.do**">
> >
> >   <select name="color">
> >
> >    <option>fireBrick
> >    <option>dodgerblue
> >    <option>mediumblue
> >    <option>honeydew
> >
> >   </select>
> >
> > 
> >   <input type="checkbox" name="sizes" value="12oz"> 12 oz .<br/>
> >   <input type="checkbox" name="sizes" value="16oz"> 16 oz .<br/>
> >   <input type="checkbox" name="sizes" value="22oz"> 22 oz .<br/>
> >
> > </form>
>
> 
>
> >  **서블릿 (Selected.java)**
> >
> >  
> >
> > package com.example
> >
> >  
> >
> > 
> >
> > public class Selected extends HttpServlet{
> >
> > .....
> >
> > 
> >
> >   public void doPost(HttpServletRequest request, HttpServletResponse response) throws    IOException, ServletException{
> >
> >    **String colorParam = request.getParameter("color");**
> >
> >    **String one = request.getParameterValues("sizes")[0];**
> >    **String[] sizes = request.getParameterValues("sizes");**
> >
> >   
> >
> >    for (int i = 0; i < sizes.length; i++) {
> >
> > ​     out.println("<br>sizes: " + sizes[i]);
> >
> >    }
> >
> >   }
> >
> > }
> >
> >  
> >
> > **descriptor (web.xml)**
> >
> >  
> >
> > <servlet>
> >
> >   <servlet-name>**colorSelecting**</servlet-name>
> >
> >   <servlet-class>**com.example.Selected**</servlet-class>
> >
> > </servlet>
> >
> > <servlet-mapping>
> >
> >   <servlet-name>**colorSelecting**</servlet-name>
> >
> >   <url-pattern>**/****selectColor.do**</url-pattern>
> >
> > </servlet-mapping>