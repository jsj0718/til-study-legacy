# Java.lang 패키지



> ## 1. java.lang 패키지
>
> - java.lang 패키지의 클래스들은 import문 없이도 사용 가능하다.
>
> 
>
> ## 2. Object 클래스
>
> - Object 클래스는 모든 클래스의 최고 조상
> - Object 클래스의 멤버들은 모든 클래스에서 바로 사용 가능
> - Object 클래스는 멤버변수는 없고 11개의 메소드만 있다.
>
> > - protected Object **clone()** : 객체 자신의 복사본 반환
> > - public boolean **equals(Object obj)** : 객체 자신과 객체 obj가 같은 객체인지 판단
> > - protected void **finalize()** : 객체가 소멸될 때 가비지콜렉터에 의해 자동으로 호출(거의 사용안함)
> > - public Class **getClasss()** : 객체 자신의 클래스 정보를 담고 있는 Class 인스턴스를 반환
> > - public int **hashCode()** : 객체 자신의 해시코드를 반환
> > - public String **toString()** : 객체 자신의 정보를 문자열로 반환
> > - public void **notify()** : 객체 자신을 사용하려고 기다리는 쓰레드를 하나만 깨운다.
> > - public void **notifyAll()** : 객체 자신을 사용하려고 기다리는 모든 쓰레드를 깨운다.
> > - public void **wait(long timeout, int nanos)** : 다른 쓰레드가 notify()나 notifyAll()을 호출할 때 까지 현재 쓰레드를 무한히 또는 지정된 시간동안 기다리게 한다.
>
> 
>
> ## 3. equals(Object obj)
>
> - Object 클래스로부터 상속받은 equals 메소드는 두 개의 참조변수가 같은 객체를 참조하는지(두 참조변수에 저장된 주소값이 같은지) 판단
> - equals 메소드로 Value 인스턴스가 가지고 있는 value값을 비교하려면,
>   Value 클래스에서 equals 메소드를 오버라이딩하여 주소가 아닌 객체에 저장된 내용을 비교하도록 변경해야 한다.
>
> 
>
> ## 4. hashCode()
>
> - 해시함수는 찾는 값을 입력하면, 그 값이 저장된 위치를 알려주는 해시코드(hash code)를 반환한다.
> - 일반적으로 해시코드가 같은 두 객체가 존재하는 것이 가능하지만,
>   Object 클래스에 정의된 hashCode 메소드는 객체의 주소값을 이용해서 해시코드를 만들어 반환하기 때문에
>   서로 다른 두 객체는 같은 해시코드를 가질 수 없다.
> - String 클래스는 문자열의 내용이 같으면 같은 해시코드를 반환하도록 hashCode메소드가 오버라이딩 되어 있기 때문에
>   문자열의 내용이 같은 str1과 str2에 대해 hashCode()를 호출하면 항상 동일한 해시코드 값을 얻는다.
>
> 
>
> ## 5. toString()
>
> - Object 클래스에 정의된 toString()
>
>   ```java
>   public String toString()  {
>       return getClass().getName()+"@"+Integer.toHexString(hashCode());
>   }
>   ```
>
> - 클래스를 작성할 때 toString()을 오버라이딩 하지 않고, toString()을 호출하면 클래스이름+16진수의 해시코드를 반환한다.
>
> - String 클래스의 toString()은 String 인스턴스가 갖고 있는 문자열을 반환하도록 오버라이딩 되어 있다.
>
> - Date 클래스의 경우, Date 인스턴스가 갖고 있는 날짜와 시간을 문자열로 반환하도록 오버라이딩 되어 있다.
>
> 
>
> ## 6. clone()
>
> - 자신을 복제하여 새로운 인스턴스를 생성한다.
> - Object 클래스에 정의된 clone()은 단순히 인스턴스 변수의 값만 복사하기 때문에
>   참조타입의 인스턴스 변수가 있는 클래스는 완전한 인스턴스 복제가 이루어지지 않는다.
> - clone()은 반드시 예외처리를 해줘야 한다.
>
> 
>
> ## 7. 공변 반환타입 (covariant return type)
>
> - JDK1.5부터 오버라이딩할 때 부모 메소드의 반환타입을 자식 클래스의 타입으로 변경 가능하다.
>
>   ```java
>   public Point clone()  { // 반환타입을 Object에서 Point로 변경
>       Object obj = null;
>       try {
>       obj = super.clone();
>       } catch(CloneNotSupportedException e) {}
>       return (Point)obj; //Point 타입으로 형변환
>   ```
>
> - 공변 반환타입을 사용하면 조상의 타입이 아닌, 실제로 반환되는 자손 객체의 타입으로 반환할 수 있어 번거로운 형변환이 줄었다.
>
>   - `Point copy = (Point)original.clone();` -> `Point copy = original.clone();`
>
> 
>
> ## 8. 배열 복사
>
> - 배열도 객체이기 때문에 Object 클래스를 상속받으며, 동시에 Cloneable 인터페이스와 Serializable 인터페이스가 구현되어 있다.
>
> - 일반적으로 배열을 복사할 때는 같은 길이의 새로운 배열을 생성한 다음
>
>    
>
>   ```
>   System.arraycopy()
>   ```
>
>   를 이용해서 내용을 복사하지만
>
>    
>
>   ```
>   clone()
>   ```
>
>   을 이용해서 간단하게 복사할 수 있다.
>
>   - ```java
>     int[] arr = {1,2,3,4,5};
>     int[] arrClone = arr.clone();
>     ```
>
>   - ```java
>     int[] arr = {1,2,3,4,5};
>     int[] arrClone = new int[arr.length];
>     System.arraycopy(arr,0,arrClone,0,arr.length);
>     ```
>
> - 배열 뿐만 아니라 `java.util` 패키지의
>
> > Vector
> > ArrayList
> > LinkedList
> > HashSet
> > TreeSet
> > HashMap
> > TreeMap
> > Calendar
> > Date와 같은 클래스들도 복제가 가능하다.
>
> 
>
> ## 9. 얕은 복사와 깊은 복사 (shallow copy & deep copy)
>
> - clone()은 객체에 저장된 값을 그대로 복제할 뿐, 객체가 참조하고 있는 객체까지 복제하지 않음
>   - 원본과 복제본이 같은 객체를 참조
>   - 이것이 얕은 복사(shallow copy)
>   - 얕은 복사에서는 원본을 변경하면 복사본도 영향을 받는다.
> - 원본이 참조하고 있는 객체까지 복제하는 것이 깊은 복사(deep copy)
>   - 원본과 복사본이 서로 다른 객체를 참조하기 때문에 원본의 변경이 복사본에 영향 없음
>
> 
>
> ## 10. getClass()
>
> - 자신이 속한 클래스의 Class 객체를 반환하는 메소드
>
> - Class 객체는 이름이 ‘Class’인 클래스의 객체이다.
>
>   ```java
>   public final class Class implements ... {
>     ...
>   }
>   ```
>
> - Class 객체는 클래스의 모든 정보를 담고 있으며, 클래스 당 1개만 존재한다.
>
> - 클래스 파일이 ‘ClassLoader’에 의해 메모리에 올라갈 때 자동으로 생성
>
>   - 파일 형태로 저장되어 있는 클래스를 읽어서 Class클래스에 정의된 형식으로 변환하는 것
>   - 즉, 클래스 파일을 읽어서 사용하기 편한 형태로 저장한 것이 클래스 객체
>
> - Class 객체 얻는 방법
>
>   - `Class cObj = new Card().getClass(); // 생성된 객체로 부터 얻기`
>   - `Class cObj = Card.class; // 클래스 리터럴(*.class)로 부터 얻기`
>   - `Class cObj = Class.forName("Card"); //클래스 이름으로 부터 얻기`
>
> - 객체 생성
>
>   - `Card c = new Card(); // new연산자로 객체 생성`
>   - `Card c = Card.class.newInstance(); // Class객체로 객체 생성`
>
> 
>
> ## 11. String 클래스
>
> - String 클래스는 문자열을 저장하기 위해 문자형 배열 변수(char[]) value를 인스턴스 변수로 정의되어있다.
>
>   ```java
>   public final class String implements java.io.Serializable, Comparable {
>       private char[] value;
>       ...
>   }
>   ```
>
> - 인스턴스 생성 시 생성자의 매개변수로 입력받는 문자열은 인스턴스 변수 `value`에 문자형 배열 `char[]`로 저장되는 것이다.
>
> - String 클래스는 앞에 final이 붙어 있으므로 다른 클래스의 부모가 될 수 없다.
>
> - 변경 불가능한(Immutable) 클래스다.
>
>   - 예를 들어 ‘+’ 연산자를 이용해서 문자열을 결합하는 경우, 인스턴스 내의 문자열이 바뀌는 것이 아니라 새로운 문자열이 담긴 String 인스턴스가 생성되는 것이다.
>   - 즉, 매 연산 마다 새로운 문자열을 가진 String 인스턴스가 생성되어 메모리 공간을 차지한다.
>
> 
>
> ### 11.1. 문자열을 만드는 방법 2가지
>
> - `String str1 = "abc";` // 문자열 리터럴 “abc”의 주소를 str1에 저장
>
> - `String str2 = new String("abc");` // 새로운 String 인스턴스 생성
>
> - 문자열 리터럴은 이미 존재하는 것을 재사용 하는 것이다. (문자열 리터럴은 클래스가 메모리에 로드될 때 자동으로 미리 생성된다.)
>
> - ```java
>   String str1 = "abc";
>   String str2 = "abc";
>   str1 == str2 ? true
>   str1.equals(str2) ? true
>   
>   String str3 = new String("abc");
>   String str4 = new String("abc");
>   str3 == str4 ? false
>   str3.equals(str4) ? true
>   ```
>
> 
>
> ### 11.2. 문자열 리터럴
>
> - 클래스 파일에는 소스파일에 포함된 모든 리터럴의 목록이 있다.
> - 해당 클래스 파일이 클래스 로더에 의해 메모리에 올라갈 때, 리터럴 목록에 있는 리터럴들이 JVM내에 있는 상수 저장소(constant pool)에 저장된다.
>
> 
>
> ### 11.3. 빈 문자열
>
> - 길이가 0인 배열은 존재한다.(C언어는 불가능)
> - char형 배열도 길이가 0인 배열 생성할 수 있고, 이 배열을 내부적으로 가지고 있는 문자열이 빈 문자열이다.
> - `String s = "";` 에서 참조변수 `s`가 참조하고 있는 String 인스턴스는 내부에 `new char[0]` 같이 길이가 0인 char형 배열을 저장하고 있는 것이다.
> - `char[] chArr = new char[0];`
> - `int[] iArr = {};`
>
> 
>
> ### 11.4. `join()`과 `StringJoiner` (jdk1.8부터 추가)
>
> - ```
>   join()
>   ```
>
>   은 문자열 사이에 구분자를 넣어서 결합
>
>   ```java
>   String[] arr = { "dog", "cat", "bear"};
>   String str = String.join("-", arr);
>   ```
>
> - ```
>   java.util.StringJoiner
>   ```
>
>   클래스 사용하여 문자열 결합
>
>   ```java
>   StringJoiner sj = new StringJoiner("," , "[" , "]");
>   String[] strArr = { "aaa", "bbb", "ccc" };
>   
>   for(String s : strArr)
>       sj.add(s.toUpperCase());
>   
>   System.out.println(sj.toString()); // [AAA,BBB,CCC]
>   ```
>
> 
>
> ### 11.5. 기본형-String 변환
>
> - 숫자에 빈문자열(“”) 더하기
>
> - `valueOf()` 사용
>
> - ```java
>   String str1 = 100 + ""; // 100 > "100"
>   String str2 = String.valueOf(100); // 100 > "100"
>   int i = Integer.parseInt("100") // "100" > 100
>   int i2 = Integer.valueOf("100") // "100" > 100
>   ```
>
> - valueOf()의 반환타입은 int가 아니라 Integer지만 오토박싱에 의해 자동변환
>
> - `valueOf(String s)` 는 메소드 내부에 `parseInt(String s)`를 호출할 뿐이므로, 두 메소드는 반환 타입만 다르고 같은 메소드다.
>
> 
>
> ## 12. StringBuffer & StringBuilder 클래스
>
> ```java
> public final class StringBuffer implements java.io.Serializable {
>     private char[] value;
>     ...
> }
> ```
>
> - String클래스는 Immutable이므로 인스턴스를 생성할 때 지정된 문자열을 변경할 수 없지만, StringBuffer클래스는 가능하다.
> - 내부적으로 문자열 편집을 위한 buffer를 가지고 있으며, StringBuffer 인스턴스를 생성할 때 그 크기를 지정할 수 있다.
> - buffer의 크기를 지정하지 않으면 16개의 문자를 저장할 수 있는 크기의 버퍼 생성
>
> 
>
> ### 12.1 append()
>
> - ```
>   append()
>   ```
>
>   는 반환타입이 StringBuffer이며 자신의 주소를 반환한다.
>
>   ```java
>     StringBuffer sb = new StringBuffer("abc");
>     sb.append("123").append("ZZ");
>     
>   ```
>
> - 위의 코드에서 `sb.append("123")`이 `sb`를 반환하므로 연속적으로 append()를 호출할 수 있다.
>
> - StringBuffer 클래스는 equals() 메소드를 오버라이딩 하지 않아서 `==`로 비교한 것과 같은 결과를 얻는다.
>
> - StringBuffer 인스턴스에 담긴 문자열을 비교하기 위해서는 인스턴스에 `toString()`을 호출해서 String인스턴스를 얻은 후에 `equals()`사용해야 한다.
>
> 
>
> ### 12.2. StringBuilder 클래스
>
> - StringBuffer는 멀티쓰레드에 안전(thread safe)하도록 동기화 되어있다.
> - 동기화가 StringBuffer의 성능을 떨어트리므로, StringBuffer에서 쓰레드의 동기화만 뺀 것이 StringBuilder.
>
> 
>
> ## 13. java.util.Random 클래스
>
> - `Math.random()`은 내부적으로 Random클래스의 인스턴스를 생성해서 사용한다.
> - `Math.random()`과 `Random`의 가장 큰 차이는 종자값(seed)을 설정할 수 있다는 것이다.
> - 종자값이 같은 `Random`인스턴스들은 항상 같은 난수를 같은 순서대로 반환
> - 생성자 `Random()`은 종자값을 `System.currentTimeMillis()`로 하기 때문에 실행할 때마다 얻는 난수가 달라진다.
>
> 
>
> ## 14. java.util.StringTokenizer 클래스
>
> - StringTokenizer는 긴 문자열을 지정된 구분자(delimeter)를 기준으로 토큰(token)이라는 여러 개의 문자열로 잘라내는 데 사용
> - StringTokenizer는 구분자로 단 하나의 문자만 사용 가능하기 때문에 복잡한 형태의 구분자는 정규식을 사용해야 한다.
> - `StringTokenizer (String str, String delim, boolean returnDelims)` - returnDelims 값을 true로 하면 구분자도 토큰으로 간주한다.
> - `split()`은 빈 문자열도 토큰으로 인식, StringTokenizer는 빈 문자열을 토큰으로 인식 안함
> - `split()`은 데이터를 토큰으로 잘라낸 결과를 배열에 담아서 반환
> - StringTokenizer는 데이터를 토큰으로 바로바로 잘라서 반환하므로 `split()`보다 성능 좋음

