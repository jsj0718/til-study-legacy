## Class.forName() 설명

JDBC 란 자바에서 제공하는 데이터베이스와 연결하여 데이터를 주고 받을 수 있도록 하는 인터페이스입니다.

JDBC를 사용하는 방법은 어떤 데이터베이스를 사용하던지 같습니다. 방법은 간략하게 다음과 같습니다. 

1. Class.forName() 을 이용해서 드라이버 로드
2. DriverManager.getConnection() 으로 연결 얻기
3. Connection 인스턴스를 이용해서 Statement 객체 생성
4. Statement 객체의 결과를 ResultSet 이나 int에 받기

```
Class.forName("oracle.jdbc.driver.OracleDriver");
// oracle parameter는 oracle.jdbc.driver.OracleDriver이다.
```



> #### forName
>
> ```
> public static Class<?> forName(String className)
>                         throws ClassNotFoundException
> ```
>
> A call to `forName("X")` causes the class named `X` to be initialized.
>
> Returns:
>
> the `Class` object for the class with the specified name.
>
> "X" 라는 이름의 클래스(혹은 인터페이스)를 초기화 해 준다고 하는데요, 이 초기화라는 말이 조금 애매모호 합니다.  그리고 Class 클래스의 오브젝트를 리턴한다고 하네요.
>
> 해서 또다시 검색...
>
> [http://heavyfive.tistory.com/entry/Class-%ED%81%B4%EB%9E%98%EC%8A%A4%EC%9D%98-%EC%9A%A9%EB%8F%84](http://heavyfive.tistory.com/entry/Class-클래스의-용도)
>
> 위 포스트와 아래 코드를 통해서 어느정도 이해하게 된 것 같습니다. 
>
> ```
> public class SomeDriver implements Driver {
>   static {
>     try {
>       DriverManager.registerDriver(new SomeDriver());
>     } catch (SQLException e) {
>       // TODO Auto-generated catch block
>     }
>   }
> 
>   //etc: implemented methods
> }
> ```
>
> 결론적으로 Class 클래스는 클래스들의 정보(클래스의 필드, 메서드, 클래스의 종류(인터페이스 등))를 담는 메타 클래스이고 JVM은 이 Class 클래스를 통해 클래스들에 대한 정보를 로드 합니다.
>
> 
>
> 따라서 위 API문서의 "class name x to be initialized."란 "JVM에게 해당 클래스의 정보를 로드한다." (클래스파일의 바이트코드 로드?, 제 생각입니다. 정확하지 않아요...)라고 이해하면 될 것 같습니다. 이 때 한 가지 생각해야 할 것은 JVM에게 해당 클래스의 정보가 로딩된다는 것은 JVM이 할당하는 메모리 (클래스 영역)에 로드되고 그 때 위의 static 절이 실행되면서 DriverManager에 해당 드라이버가 레지스터 되는 것입니다. 
>
> 따라서 DriverManager는 이 정보를 가지고 getConnection을 할 수 있는 것이죠.
>
> ### 결론
>
> 정리해보겠습니다. Class 클래스는 JVM에서 동작할 클래스들의 정보를 묘사하는 일종의 메타 클래스(Meta-Class)입니다. —> 클래스의 이름, 멤버 필드와 메소드, 클래스 종류(자바의 interface는 내부적으로 클래스와 동일하게 취급)
>
> 
>
> 클래스를 인스턴스화 하는 과정을 생각해 봅시다. 예를 들어 우리는 다음과 같은 코드로 클래스를 인스턴스화 합니다.
>
> ```
> A a = new A(); 
> ```
>
> 
>
> 위의 코드가 호출되는 순간 JVM은 A라는 클래스가 JVM에 로드되어 있는지 찾습니다.로드되어 있지 않다면 ClassLoader 클래스 혹은 그를 상속받은 클래스들을 이용하여 A 클래스를 로드하려고 할 겁니다. 많약 찾지 못하면 ClassNotFoundException이 발생하게 되는 것입니다.
>
> 
>
> 로드되어 있을 경우에는 A 클래스의 인스턴스를 하나 만들고, 생성자를 호출합니다. 생성자가 호출되면 인스턴스가 초기화 되겠지요.
>
> 
>
> 그런 다음 a라는 참조 변수가 생성된 인스턴스를 가리키게 합니다. 이 때 내부적으로 a라는 참조변수가 새로 생성된 인스턴스를 가리키고 있기 때문에 해당 인스턴스의 참조 카운트가 1이 됩니다. (참조 카운트가 0이라면 가비지 컬렉터의 대상이 됩니다.)
>
> 
>
> 자 이제 Class.forName("some.pakage.SomeClass").newInstance()를 생각해 보겠습니다. forName() 메소드에 의해서 반환된 Class 클래스의 인스턴스에는 some.pakage.SomeClass의 정보가 담겨 있을 겁니다. 후에 newInstance()를 호출하면 인스턴스를 생성한 다음 기본 생성자로 초기화하고 그 인스턴스를 리턴해 주겠죠.이 과정은 some.pakage.SomeClass obj = new some.pakage.SomeClass(); 와 같은 동작을 합니다.
>
> 
>
> 하지만 우리는 이 리턴된 인스턴스를 받는 참조 변수도 없고 대입도 없습니다. 그렇다면 참조 카운트가 0이 되어 카비지 컬렉션의 대상이 될 텐데 어떻게 우리가 사용할 수 있는 걸까요?
>
> 
>
> 답은 static 블럭에 있습니다. static 블럭은 클래스가 로딩된 직후 어떤 생성자보다도 먼저 실행되는 코드입니다. JDBC 드라이버와 같이 인스턴스를 별도로 관리하지 않는 대부분의 클래스의 경우 정적 블록을 통해 생성하고 관리합니다. 따라서 Class.forName() 메소드를 호출하면 인스턴스 생성과 초기화가 이루어 지는 겁니다.
>
> 
>
> 
>
> (추가) Class.forName()은 JDBC 4.0 이후로는 메소드를 호출하지 않아도 자동으로 드라이버를 초기화한다고 하네요.
>
> ```
> 이전 버전의 JDBC에서 연결을 얻으려면 먼저 Class.forName 메소드를 호출하여 JDBC 드라이버를 초기화해야했습니다. 이 메소드에는 java.sql.Driver 유형의 오브젝트가 필요합니다. 각 JDBC 드라이버는 java.sql.Driver 인터페이스를 구현하는 하나 이상의 클래스를 포함합니다.
> ...
> 클래스 경로에있는 JDBC 4.0 드라이버는 자동으로로드됩니다. (그러나 Class.forName 메서드를 사용하여 JDBC 4.0 이전의 드라이버를 수동으로로드해야합니다.)
> ```

