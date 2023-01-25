# LIKE구문 (SQL)



> 쿼리문 WHERE절에 주로 사용되며 부분적으로 일치하는 칼럼을 찾을때 사용됩니다.
>
> SELECT * FROM [테이블명] WHERE LIKE [조건]
>
> 
>
> # 사용법
>
> '-' : 글자숫자를 정해줌(EX 컬럼명 LIKE '홍_동')
>
> '%' : 글자숫자를 정해주지않음(EX 컬럼명 LIKE '홍%')
>
> 
>
> ```
> --A로 시작하는 문자를 찾기--
> SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE 'A%'
> 
> --A로 끝나는 문자 찾기--
> SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '%A'
> 
> --A를 포함하는 문자 찾기--
> SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '%A%'
> 
> --A로 시작하는 두글자 문자 찾기--
> SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE 'A_'
> 
> --첫번째 문자가 'A''가 아닌 모든 문자열 찾기--
> SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE'[^A]'
> 
> --첫번째 문자가 'A'또는'B'또는'C'인 문자열 찾기--
> SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '[ABC]'
> SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '[A-C]'
> ```
>
> 
>
> # 예제
>
> ```
> --'김'으로 시작하는 사원 조회
> SELECT * FROM My_Talbe WHERE Nm_Kor LIKE '김%'
> 
> --김이 들어가는 시작하는 사원 조회
> SELECT * FROM My_Talbe WHERE Nm_Kor LIKE '%김%'
> 
> --김으로 끝나는 사원의 사원번호 조회
> SELECT No_Emp FROM My_Talbe WHERE Nm_Kor LIKE '%김'
> ```

