# Java.util 패키지



> ## java.util 패키지에 포함되는 클래스들
>
> ```
> AbstractCollection, 
> AbstractList, AbstractSequentialList, LinkedList, ArrayList, Vector, Stack, 
> AbstractSet, HashSet, LinkedHashSet, TreeSet, 
> AbstractMap, HashMap, LinkedHashMap, TreeMap, 
> Arrays, BitSet, Calendar, GregorianCalendar, 
> Collection, Date, Dictionary, Hashtable, Properties, 
> EventObject, Locale, Observable, Random, Scanner, StringTokenizer
> ```
>
> 
>
> ## 날짜 관련 클래스
>
> 자바의 대표적인 날짜 관련 클래스로는 Date와 Calandar가 사용된다. [Java](http://www.incodom.kr/Java) 초기에 생성된 Date 클래스는 지역화 기능을 지원하지 않아 국가별로 시간과 날짜가 다른 것을 표현할 수 없었으나, Calendar와 Locale 클래스가 추가되어 지역화를 지원하게 되었다.
>
> 
>
> ```
> import java.util.Date;
> 
> public class DateClass {
>     public static void main(String[] args) {
>         Date date = new Date();
>         System.out.println(date);
>     }
> }
> 
> // 출력결과 
> Fri Sep 23 08:33:03 KST 2016
> ```
>
> 
>
> ## Random 클래스
>
> Random 클래스는 Seed값에 의한 난수를 생성해 반환하는 클래스로 정수, 실수, 부울값(true|false) 등으로 반환이 가능하다.
>
> Random 클래스를 이용한 정수형 난수 발생 예제
>
> ```
> import java.util.Random;
> public class RandomClass {
>     public static void main(String[] args) {
>         Random random = new Random();
>         System.out.println(random.nextInt());
>     }
> }
> 
> // 나수 발생 결과(실행할 때마다 새로운 값이 반환 됨) 
> -1212529769
> ```
>
> 
>
> ## ArrayList 클래스
>
> 배열의 기능과 가장 비슷한 클래스로 저장공간으로 배열을 사용한다. 저장 순서가 유지되고 중복이 허용된다. 기존에 사용되던 Vector 클래스를 대체하는 클래스로 비동기 방식 동작으로 Vector 가 갖고 있는 처리 속도가 개선되었다.
>
> ```
> add() : 해당 데이터를 리스트에 추가한다. 인덱스(index) 사용으로 입력 순서를 변경할 수 있다. 
> contains() : 해당 데이터가 자신의 리스트에 포함되어 있는지를 확인할 수 있다. 
> set() : 해당 데이터 자체를 대체하거나 순서를 변경할 때 사용한다. 
> get() : 인덱스에 해당하는 해당 데이터를 반환한다. 
> remove() : 인덱스 혹은 자료에 의한 데이터를 삭제한다. 
> size() : 현재 리스트의 크기를 반환한다.
> ```
>
> 
>
> ## LinkedList 클래스 
>
> Queue 인터페이스를 상속받은 클래스로 ArrayList와 동일한 메소드를 가지고 있으며, 데이터 추가시 첫번째 원소와 마지막 원소에 데이터를 추가할 수 있는 addFirst(), addLast() 메소드를 가지고 있다.
>
> ```
> peek() : 데이터를 반환한다. 복사 기능에 해당한다. 
> poll() : 데이터를 반환한다. 잘라내기 기능에 해당한다.
> ```
>
> 
>
> ## HashSet 클래스
>
> 집합을 구체화하기위한 Set 인터페이스를 상속받은 클래스로 자료의 중복을 허용하지 않으며, 순서가 존재하지 않는다.
>
> ```
> add() : 데이터를 추가한다. 중복된 자료가 있는 경우 제외시킨다.
> ```
>
> 
>
> ## Hashtable 클래스
>
> 키(key)와 값(value) 쌍을 이루는 데이터 집합으로 순서를 유지하지 않는다. 값의 중복은 허용되지만 키의 중복은 허용되지 않는다. 기존의 HashMap 클래스를 데체하기 위한 클래스로 비동기 방식 동작으로 처리 속도가 개선되었다.
>
> ```
> put(key, value) : 해당 키와 값을 저장한다. 
> containsKey() : 해당 키가 있는지 확인한다. 
> containsValue() : 해당 값이 있는지 확인한다. 
> keys() : 등록된 모든 키밧을 반환한다. 
> get() : 키에 해당하는 값을 반환한다.
> ```

