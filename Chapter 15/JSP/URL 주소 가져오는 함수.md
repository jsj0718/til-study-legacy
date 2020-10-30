## URL 주소 가져오는 함수



> 1. **request.getContextPath() 함수 = 프로젝트 Path만 가져옵니다.**
>
> 
>
> 2. **request.getRequestURI() 함수 = 프로젝트 + 파일경로까지 가져옵니다.**
>
> 
>
> 3. **request.getRequestURL() 함수 = 전체 경로를 가져옵니다.   (L만 바뀜)**
>
> 
>
> 4. **request.ServletPath() 함수 = 파일명만 가져옵니다.**
>
> 
>
> 5. **request.getRealPath("") 함수 =** **서버 or 로컬 웹 애플리케이션 절대결로 가져옵니다.**