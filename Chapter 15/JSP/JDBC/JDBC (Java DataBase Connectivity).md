# JDBC (Java DataBase Connectivity)



**1. JDBC란?**

**자바에서 데이터베이스를 사용하기 위한 절차에 대한 규약**입니다.



DBMS에 따라 DB를 다루는 방식이 다르다면, 사용자는 알아야 할 것이 매우 많을 것입니다.

그래서 JDBC를 통해 추상화된 인터페이스를 제공하기만 하고, 각 벤더들( Oracle, Mysql 등.. )은 각자의 DBMS에 맞게 구현을 해놓은 상태입니다.



사용자는 특정 DBMS를 사용하기 위해, 각 벤더에서 개발해놓은 드라이버를 설치하면 됩니다.

그리고 DB에 접근하기 위한 인터페이스는 JDBC에서 제공하는 API를 사용하면 됩니다.



이제 JDBC로 Mysql DB를 사용하는 방법에 대해 알아보도록 하겠습니다.



**2. 이클립스에서 JDBC 등록하기**

java에서 데이터베이스를 사용하기 위해서는 드라이버를 설치해야 합니다.



먼저 MySQL 홈페이지에서 드라이버를 설치합니다. ( [링크](https://dev.mysql.com/downloads/connector/j/#downloads) )



**1) jar 파일 준비하기**

설치가 완료되면, mysql-connector-java-버전-bin.jar 파일이 생성되었을 것입니다.

여러 클래스들을 모아 놓은 파일을 **jar 파일**이라고 하는데, 이 파일이 있어야 MySQL을 사용할 수 있습니다.



**2) 이클립스에서 jar파일 연동**

1. 이클립스에서 새로운 프로젝트를 생성
2. 프로젝트 폴더를 우클릭 -> Properties -> Java Build Path 항목 클릭
3. Libraries -> Add Library ... 클릭 -> User Library 클릭 -> User Libraries 클릭
4. New 클릭하여 아무렇게 이름을 작성합니다. ( 저는 JDBC라는 이름으로 생성하겠습니다. )
5. 생성된 Library를 클릭하고 Add External JARs 클릭
6. 처음에 설치한 jar 파일 mysql-connector-java-버전-bin.jar 파일을 찾아서 클릭



그러면 아래와 같이 프로젝트 폴더 아래에 라이브러리가 추가될텐데, 여기까지 진행했으면 JDBC를 사용할 준비가 된 것입니다.

![img](https://t1.daumcdn.net/cfile/tistory/99D982475AA4FF1F17)



**3. JDBC 기본적인 사용**

JDBC에서 인터페이스를 제공하기 때문에, 어떤 DB를 사용하든 개발자가 JDBC를 사용하는 방법은 변하지 않습니다.

이것이 인터페이스의 가장 큰 장점이죠.



JDBC를 사용하는 방법은 다음과 같습니다.

1. import java.sql.*;
2. 드라이버를 load
3. mysql 연결을 위한 Connection 객체 생성
4. Statement 객체를 생성하여 질의 수행
5. 질의 결과가 있다면, ResultSet 객체를 생성하여 결과 저장
6. 추가 로직 실행 후, JDBC 연결 과정에서 필요했던 객체들을 close

이제 위의 과정을 구현해보도록 하겠습니다.



**3-1. 연결 테스트**

```
package test;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConnectionTest {
    public static void main(String[] args) {
        // Connection 객체를 자동완성으로 import할 때는 com.mysql.connection이 아닌
        // java 표준인 java.sql.Connection 클래스를 import해야 한다.
        Connection conn = null;

        try{
            // 1. 드라이버 로딩
            // 드라이버 인터페이스를 구현한 클래스를 로딩
            // mysql, oracle 등 각 벤더사 마다 클래스 이름이 다르다.
            // mysql은 "com.mysql.jdbc.Driver"이며, 이는 외우는 것이 아니라 구글링하면 된다.
            // 참고로 이전에 연동했던 jar 파일을 보면 com.mysql.jdbc 패키지에 Driver 라는 클래스가 있다.
            Class.forName("com.mysql.jdbc.Driver");

            // 2. 연결하기
            // 드라이버 매니저에게 Connection 객체를 달라고 요청한다.
            // Connection을 얻기 위해 필요한 url 역시, 벤더사마다 다르다.
            // mysql은 "jdbc:mysql://localhost/사용할db이름" 이다.
            String url = "jdbc:mysql://localhost/dev";

            // @param  getConnection(url, userName, password);
            // @return Connection
            conn = DriverManager.getConnection(url, "dev", "dev");
            System.out.println("연결 성공");

        }
        catch(ClassNotFoundException e){
            System.out.println("드라이버 로딩 실패");
        }
        catch(SQLException e){
            System.out.println("에러: " + e);
        }
        finally{
            try{
                if( conn != null && !conn.isClosed()){
                    conn.close();
                }
            }
            catch( SQLException e){
                e.printStackTrace();
            }
        }
    }
}
```

- 먼저 mysql-connector-java-버전-bin.jar 파일이 라이브러리에 추가되어 있어야 합니다.

- 다음으로 Class.forName() 메서드를 호출하여, mysql에서 제공하는 Driver 클래스를 JVM method area에 로딩시킵니다.

- - 그러면 여러 Driver 객체를 다루는 **DriverManager**의 static 메서드를 사용할 수 있게 됩니다.

- DriverManager 클래스의 static 메서드인 getConnection() 메서드를 호출해서, mysql에 연결하기 위한 커넥션 정보(url, user, password)를 입력합니다.

- getConnection() 메서드 수행 결과로 Connection 객체를 반환하는데, 이 객체를 통해 쿼리를 날리는 statement를 작성할 수 있습니다.

- - 다음 예제에서 살펴보겠지만, SELECT 쿼리에서는 createStatement() , INSERT에서는 prepareStatement()를 호출합니다.

이 프로그램이 정상적으로 실행이 되려면, mysql에 dev라는 database가 있어야 하며, 비밀번호가 dev인 dev 유저가 있어야 합니다.

자세한 내용은 코드의 주석을 참고해주시기 바랍니다.



**3-2. SELECT 쿼리 실행**

```
package test;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class SelectTest {
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;

        try{
            // 1. 드라이버 로딩
            Class.forName("com.mysql.jdbc.Driver");

            // 2. 연결하기
            String url = "jdbc:mysql://localhost/dev";
            conn = DriverManager.getConnection(url, "dev", "dev");


            // 3. 쿼리 수행을 위한 Statement 객체 생성
            stmt = conn.createStatement();

            // 4. SQL 쿼리 작성
            // 주의사항
            // 1) JDBC에서 쿼리를 작성할 때는 세미콜론(;)을 빼고 작성한다.
            // 2) SELECT 할 때 * 으로 모든 칼럼을 가져오는 것보다
            //   가져와야 할 칼럼을 직접 명시해주는 것이 좋다.
            // 3) 원하는 결과는 쿼리로써 마무리 짓고, java 코드로 후작업 하는 것은 권하지 않음
            // 4) 쿼리를 한 줄로 쓰기 어려운 경우 들여쓰기를 사용해도 되지만 띄어쓰기에 유의 !!
            String sql = "SELECT name, owner, date_format(birth, '%Y년%m월%d일' date FROM pet";


            // 5. 쿼리 수행
            // 레코드들은 ResultSet 객체에 추가된다.
            rs = stmt.executeQuery(sql);

            // 6. 실행결과 출력하기
            while(rs.next()){
                // 레코드의 칼럼은 배열과 달리 0부터 시작하지 않고 1부터 시작한다.
                // 데이터베이스에서 가져오는 데이터의 타입에 맞게 getString 또는 getInt 등을 호출한다.
                String name = rs.getString(1);
                String owner = rs.getString(2);
                String date = rs.getString(3);

                System.out.println(name + " " + owner + " " + date);
            }
        }
        catch( ClassNotFoundException e){
            System.out.println("드라이버 로딩 실패");
        }
        catch( SQLException e){
            System.out.println("에러 " + e);
        }
        finally{
            try{
                if( conn != null && !conn.isClosed()){
                    conn.close();
                }
                if( stmt != null && !stmt.isClosed()){
                    stmt.close();
                }
                if( rs != null && !rs.isClosed()){
                    rs.close();
                }
            }
            catch( SQLException e){
                e.printStackTrace();
            }
        }
    }
}
```

- SELECT 쿼리를 수행하기 전에, 먼저 Connection 객체를 얻어야 합니다.

- 이어서 Connection 객체의 createStatement() 메서드를 호출하여, 쿼리를 실행할 수 있는 Statement 객체( stmt )를 얻습니다.

- - 해당 쿼리에는 동적으로 할당되는 값이 없으므로 createStatement() 메서드를 호출합니다. ( 동적으로 할당되는 값은 다음 예제에서 살펴보도록 하겠습니다. )

- 다음으로 쿼리를 작성하면 되는데, 쿼리를 작성할 때 주의 할 것들이 있으니 주석을 참고해주세요.

- 작성한 쿼리( sql )를 stmt.executeQuery() 메서드의 인자로 전달하여 호출하면 쿼리가 실행됩니다.

- 그 결과로 ResultSet 객체( rs )가 반환 되며, 이 객체에는 SELECT 쿼리 결과의 레코드들이 담겨있습니다.





이 예제에서는 결과를 조회하기 위해 반복문 while을 사용했는데, 일반적으로 VO 객체를 사용하는 편입니다.

**VO 객체**란 테이블의 칼럼들을 멤버 변수로 갖는 객체를 의미합니다. ( DAO, VO - [참고 링크](https://victorydntmd.tistory.com/149) )



**3-3. Insert 쿼리 실행**

```
package test;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class InsertTest {
    public static void main(String[] args) {
        // pet 테이블에는 이름/소유자/종/성별/출생일 칼럼이 있습니다.
        insert("봄이", "victolee", "페르시안", "m", "2010-08-21", null);
    }

    public static void insert(String name, String owner, String species,
                              String gender, String birth, String death){
        Connection conn = null;
        PreparedStatement pstmt = null;

        try{
            // 1. 드라이버 로딩
            Class.forName("com.mysql.jdbc.Driver");

            // 2. 연결하기
            String url = "jdbc:mysql://localhost/dev";
            conn = DriverManager.getConnection(url, "dev", "dev");


            // 3. SQL 쿼리 준비
            // 추가하려는 데이터의 값은 전달된 인자를 통해 동적으로 할당되는 값이다.
            // 즉 어떤 값이 전달될지 모르므로 Select 할 때와 달리
            // stmt = conn.createStatement(); 를 작성하지 않고
            // pstmt = conn.prepareStatement(sql); 로 작성하여 데이터를 추가할 것임을 알립니다.
            // 물론 sql 쿼리 내에서 + 연산자로 한 줄로 작성할 수 있지만 가독성이 너무 떨어지게 되므로
            // 이 방법을 권합니다.
            String sql = "INSERT INTO pet VALUES (?,?,?,?,?,?)";
            pstmt = conn.prepareStatement(sql);


            // 4. 데이터 binding
            pstmt.setString(1, name);
            pstmt.setString(2, owner);
            pstmt.setString(3, species);
            pstmt.setString(4, gender);
            pstmt.setString(5, birth);
            pstmt.setString(6, death);


            // 5. 쿼리 실행 및 결과 처리
            // SELECT와 달리 INSERT는 반환되는 데이터들이 없으므로
            // ResultSet 객체가 필요 없고, 바로 pstmt.executeUpdate()메서드를 호출하면 됩니다.
            // INSERT, UPDATE, DELETE 쿼리는 이와 같이 메서드를 호출하며
            // SELECT에서는 stmt.executeQuery(sql); 메서드를 사용했었습니다.
            // @return     int - 몇 개의 row가 영향을 미쳤는지를 반환
            int count = pstmt.executeUpdate();
            if( count == 0 ){
                System.out.println("데이터 입력 실패");
            }
            else{
                System.out.println("데이터 입력 성공");
            }
        }
        catch( ClassNotFoundException e){
            System.out.println("드라이버 로딩 실패");
        }
        catch( SQLException e){
            System.out.println("에러 " + e);
        }
        finally{
            try{
                if( conn != null && !conn.isClosed()){
                    conn.close();
                }
                if( pstmt != null && !pstmt.isClosed()){
                    pstmt.close();
                }
            }
            catch( SQLException e){
                e.printStackTrace();
            }
        }
    }
}
```

- Insert 쿼리를 수행할 때도 먼저 Connection 객체를 얻어야 합니다.
- INSERT는 일반적으로 동적으로 값이 할당되므로 createStatement()를 호출하지 않고, 쿼리를 준비하는 statement라는 의미로 prepareStatement() 메서드를 호출합니다.
- 그러면 PreparedStatement 객체( pstmt )를 반환하는데, pstmt.setString() 메서드를 통해 동적으로 값을 할당할 수 있습니다.
- 값이 할당되면 pstmt.executeUpdate() 메서드를 실행하여 INSERT 쿼리를 실행 할 수 있습니다.
- 반환 값은 영향을 미친 row의 개수입니다.



이상으로 JDBC의 기본적인 사용법을 알아보았습니다.

마지막으로 몇 가지 주의 사항과 정리를 해보면 다음과 같습니다.

- 쿼리를 수행할 때 동적으로 할당해야 하는 값이 있으면 PreparedStatement 객체를 사용하고, 동적으로 할당할 필요가 없으면 Statement 객체를 사용합니다.
- 쿼리의 결과가 있으면 executeQuery() 메서드를 호출하여 ResultSet 객체에 담고, 쿼리의 결과가 없으면 executeUpdate() 메서드를 호출하여 int형 변수에 결과 값을 할당합니다.