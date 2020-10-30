# JDBC 총정리



**JDBC를 사용한 데이터베이스 연동**



**1. JDBC (Java Database Connectivity)**



\- JDBC는 자바 프로그램과 관계형 데이터 원본에 대한 인터페이스이다. JDBC 라이브러리(Library)는 관계형 데이터베이스에 접근하고, SQL 쿼리문을 실행하는 방법을 제공한다.



\- JDBC 라이브러리는 'java.sql' 패키지에 의해 구현되고, 이 패키지는 여러 종류의 데이터베이스에 접근할 수 있다. 'java.sql' 패키지는 단일 API를 제공하는 클래스와 인터페이스의 집합이다.



\- JDBC 드라이버들은 일반적으로 JDBC_-ODBC브리지 + ODBC 드라이버 (JDBC-ODBC Bridge Plus ODBC Drive), 네이티브-API 부분적인 자바 드라이브(Native-API Partly-Java Driver), JDBC-Net 순수 자바 드라이버(JDBC-Net Pure Java Driver), 네티이브-프로토콜 순수 자바 드라이버(Native-Protocol Pure Java Driver)  등의 4가지 타입의 JDBC 드라이버를 제공한다.



\- 4가지 드라이버 타입들 중 네이티브-프로토콜 순수 자바 드라이버(Native-Protocol Pure Java Driver)를 사용하겠다.





**2. JDBC를 사용한 JSP와 데이터베이스의 연동**



(1) JDBC 프로그램의 작성 단계



![img](https://t1.daumcdn.net/cfile/tistory/27669050526C94181B)







① 1단계 (JDBC 드라이버 Load)



\- 인터페이스 드라이버(interface driver)를 구현(implements)하는 작업으로, Class 클래스의 forName() 메소드를 사용해서 드라이버를 로드한다. forName(String className) 메소드는 분자열로 주어진 클래스나 인터페이스 이름을 객체로 리턴한다.



\- MySQL 드라이버 로딩



**Class.forName("com.mysql.jdbc.Driver");**



\- Oracle 드라이버 로딩



**Class.forName("oracle.jdbc.driver.OracleDriver");**



\- Class.forName("com.mysql.jdbc.Driver") 은 드라이버들이 읽히기만 하면 자동 객체가 생성되고 DriverManager에 등록된다. 드라이버 로딩은 프로그램 수행 시 한 번만 필요하다.



② 2단계 (Connection 객체 생성)



\- Connection 객체를 연결하는 것으로 DriverManager에 등록된 각 드라이버들을 getConnection(String url) 메소드를 사용해서 식별한다. 이때 url 식별자와 같은 것을 찾아서 매핑(mapping)한다. 찾지 못하면 no suitable error 가 발생한다.



\- MySQL 사용시 Connection 객체 생성



**Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/jsptest", "jspid","jsptest");**



\- Oracle 사용시 Connection 객체 생성



**Connection conn = DriverManager.getConnection("jdbc:oracle:thin:@127.0.0.1:1521:ora817", "scott", "tiger");**



③ 3단계 (Statement/PreparedStatement/CallableStatement 객체 생성)



\- sql 쿼리를 생성/실행하며, 반환된 결과를 가져오게 할 작업 영역을 제공한다.



\- Statement 객체는 Connection 객체의 createStatement() 메소드를 사용하여 생성된다.



**Statement stmt = conn.createStatement();**







④ 4단계 (Query 수행)



\- Statement 객체가 생성되면 Statement 객체의 executeQuery() 메소드나 executeUpdate() 메소드를 사용해서 쿼리를 처리한다.



\- stmt.executeQuery : recordSet 반환 => Select 문에서 사용



**ResultSet rs = stmt.executeQuery("select \* from 소속기관");**



\- stmt.executeUpdate() : 성공한 row 수 반환 => Insert문, Update문, Delete문에서 사용



**String sql = "update member1 set passwd = '3579' where id ='abc'";**

**stmt.executeUpdate(sql);**



⑤ 5단계 (ResultSet 처리)



\- executeQuery() 메소드는 결과로 ResultSet을 반환한다. 이 ResultSet으로부터 원하는 데이터를 추출하는 과정을 말한다.



\- 데이터를 추출하는 방법은 ResultSet 에서 한 행씩 이동하면서 getXxx()를 이용해서 원하는 필드 값을 추출하는데, 이때 rs.getString("name") 혹은 rs.getString(1) 을 사용한다.



\- ResultSet의 첫 번째 필드는 1 부터 시작한다.



\- 한 행이 처리되고 다음 행으로 이동 시 next() 메소드를 사용한다.



**while(rs.next()){**

**out.println(rs.getString("id"));**

**out.println(rs.getString("passwd");**



출처: https://hyeonstorage.tistory.com/110 [개발이 하고 싶어요]