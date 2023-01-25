# 조코딩 학습 내용 정리



1. 코딩을 배워야하는 이유
   * 개발이 쉬워짐(Framework, Cloud, API 등)
   * 아이디어와 운이 좋다면 돈을 벌 수 있음
   * 실생활에서 유용 (웹서핑, 업무 등)



2. 코딩 공부 순서 정리

   * 웹 (브라우저를 통해 접속할 수 있는 모든 사이트)
     * API를 활용하면 다양한 서비스 생성 가능
     * 프론트엔드 / 백엔드
     * 백엔드 프레임워크로 Ruby on Rails 추천

   

3. 코딩이란?

   * 코드를 작성하다(컴퓨터에게 명령하다)
   * 기계어 : 0과 1로 구성된 언어
   * 프로그래밍 언어 : 인간이 사용하기 쉽게 가공한 언어
   * 저급 언어 : 기계어에 가까움 (사용하기 어렵지만 속도가 빠르며 세부적인 조절 가능)
   * 고급 언어 : 인간의 언어에 가까움(사용하기 쉽지만 속도가 느리고 세부적인 조절 불가능)
   * 프레임워크 : 코딩을 할 때 자주 사용되는 도구들을 모아 놓고 쉽게 활용할 수 있는 환경을 조성
     * 라이브러리, API, SDK 등으로 부르기도 함



4. HTML 기초강좌 1편
   * F12 : 개발자 도구
   * ctrl + shift + c로 마우스를 통해 해당 부분을 수정할 수 있음
   * HTML 강의 추천 사이트
     * 코드카데미
     * 생활코딩



5. HTML 기초강좌 2편(내가 만든 사이트 인터넷에 공개)
   * 내 컴퓨터를 서버로 만들기
   * 외부 서버 활용하기 (netlify 활용)
     * HTML 무료 템플릿 다운로드 
     * netlify 로그인 후 HTML 파일 업로드하기
     * 사이트 주소 변경하기
     * The End



6. HTML 기초강좌 3편(검색엔진에 등록하기)

   1. 검색 엔진에 내 사이트 등록하기

      * 네이버 웹마스터도구 검색
      * 연동 사이트 목록에서 사이트 추가 클릭
      * 원하는 사이트 주소 추가

   2. 내 사이트임을 인증하기

      * 사이트 소유 확인 과정 거치기
      * HTML 태그 방식 클릭 (간단함)
        * 내 홈페이지의 HTML 파일에 요구하는 메타 태그를 추가한 뒤 재업로드를 하면 됨 (netlify에서 deploy 태그에 있음)

   3. 관련 문서 제출하기

      * 검색엔진 원리

      > 1. 정보를 수집하는 로봇 존재
      >
      > 2. 각 사이트의 정보를 모아 검색엔진에 돌려줌 (이 로봇을 크롤러라고 부름)
      > 3. 검색엔진에 나오고 싶지 않은 정보가 보여지는 것을 방지하기 위해 robots.txt 파일로 약속함
      > 4. robots.txt에서 로봇을 허용하면 검색 O, 허용하지 않으면 검색 X
      > 5. sitemap.xml 파일로 우리 사이트를 더 정확하고 효율적으로 탐색할 수 있게 만들어줌

      * 사이트 등록 리스트에서 해당 주소 클릭 후 검증 탭에서 robots.txt 클릭
      * robots.txt 간단 생성 하고 다운로드 받은 후 HTML 폴더 최상단에 robots.txt 넣기
      * 구글에 create sitemap 검색
      * https://www.xml-sitemaps.com 들어가서 **Just enter your website URL to create a sitemap** 부분에 주소 입력 후 sitemap.xml 다운로드 받고 HTML 폴더 최상단에 넣기
      * robots.txt에 **Sitemap: https://jsj0718.netlify.app/sitemap.xml** 입력하기
      * https://jsj0718.netlify.app/sitemap.xml 검색해서 잘 되었는지 확인하기

   4. SEO, Search Engine Optimization(검색 엔진 최적화 하기)

      * 검색엔진 상단에 위치하기 위해 최적화 필요





7. URL(Uniform Resource Locator) : 언어로 된 주소(IP 주소: 휴대폰 번호, URL: 주소록에 텍스트로 저장한 것)
   * DNS(Domain Name System) : IP주소와 URL을 연결하여 저장한 공간

> Step 1) 나만의 도메인 구입하기
>
> 1. **freenom**에서 원하는 도메인 주소 유무 확인
> 2. 무료인것 Get it now! 선택 후 checkout 선택
> 3. 메일 인증 필요 (**임시 메일 이용**하기 -> moakt 이용)
> 4. 완료 후 인증 메일과 설정한 비밀번호로 로그인
> 5. Services > My Domains > 구입한 도메인 복사 > netlify에서 Domain settings 클릭 > Add a Custom Domain 클릭 > 구입한 도메인 입력
> 6. DNS 설정하기
>    1. Check DNS 설정하기 클릭 > jsj0718.tk A 104.198.14.52 (**A타입 레코드**, IP주소와 URL을 연결해주는 방식) > freenom에서 Manage Domain 버튼 클릭 > Manage Freenom DNS 배너 클릭 > 위 형식에 맞게 입력 후 save changes 클릭하면 완료
>    2. HTTPS(보안 연결)는 netlify에서 무료로 제공
>
> Step 2) 내 사이트와 연결해 DNS 등록하기

