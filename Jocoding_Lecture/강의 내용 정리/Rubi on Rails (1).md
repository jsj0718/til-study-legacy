# Rubi on Rails (1)



## Back-End 구조

MVC 패턴 : Model - View - Controller 로 이뤄진 구조

* Model : Data를 담당하는 Model
* View : 화면을 담당하는 View
* Controller : 전반적인 관리를 담당하는 Controller

![image-20201112175713592](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201112175713592.png)

> 과정 설명
>
> 1. Router가 URL 뒤의 board 부분을 Controller에 전송 (게시판에 접근한다는 것을 알아냄)
> 2. Controller에 게시판이 할 일을 저장했기에 그 일을 수행하게 됨
> 3. Controller가 Model을 통해 DB에서 게시글 정보를 가져오고, 가져온 정보를 HTML과 CSS 등 꾸며주는 요소를 추가함. 그리고 View를 통해 화면에 표시함.



## Rubi on Rails 사용법

1. ide.goorm.io 접속
2. 로그인(깃허브) 후 새 컨테이너 생성 클릭 (컨테이너 : 개발 환경이 갖춰진 하나의 컴퓨터)
3. IDE 구성 요소 (탐색기, 터미널, 편집기)
   * 탐색기 : 폴더, 파일을 볼 수 있는 공간
   * 터미널 : 명령어를 입력할 수 있는 공간
   * 편집기 : 소스 코드를 수정할 수 있는 공간



> 이용 방법
>
> 1. Controller 생성하기 
>
>    * rails g controller 이름 (lotto)
>      * rails에게 g(generate, 만들다)로 controller를 만들라고 명령하다.
>
> 2. view 생성하기
>
>    1. views 폴더에 생성한 controller와 연결된 view가 존재 (lotto 폴더 존재)
>    2. 해당 폴더(lotto)에 파일 만들기 (예시 : index.html.erb)
>       * index.html 파일인데 루비를 사용할 수 있어서 ERB(Embedded Ruby)확장자로 끝남
>    3. 파일에 내용을 작성하고, controller 폴더 내 파일을 이용해 연결
>
>    > 연결 방법
>    >
>    > ```
>    > class LottoController < ApplicationController
>    > 	def index	# view 파일 이름 작성
>    > 	end
>    > end
>    > ```
>
>    4. Router 설정하기
>
>       * config > routes.rb 파일에서 규칙 작성
>
>       * ```
>         get '/patients/:id', to: 'patients#show'
>         
>         # patients/:id는 어떤 것이여도 상관없음 (gogo라고 작성)
>         
>         # patients#show 는 controller#view를 적으면 됨
>         
>         # 실행 후 터미널에 나온 주소를 브라우저에서 실행시키면 된다. (주소 끝에 get 뒤에 넣은 것을 추가하면 코딩한 페이지가 실행된다.)
>         ```
>
>  
>
> ### 원리 설명
>
> : 주소창 뒤에 gogo를 붙이면 router에서 lotto 컨트롤러의 index view로 연결한다.
>
> ![image-20201112192036115](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201112192036115.png)
>
>  
>
> ### 변수 설정 및 출력 방법
>
> ![image-20201112192251315](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201112192251315.png)
>
> ![image-20201112192235402](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201112192235402.png)





## 본격 로또 번호 만들기

1. 1부터 45까지 번호 제작 후 6개 선택한 다음 정렬

![image-20201112194617146](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201112194617146.png)



2. 로또 사이트에서 공 양식을 복붙하고 컨트롤러에서 설정한 lotto 배열을 인덱스로 하나씩 출력

![image-20201112194654945](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201112194654945.png)



3. 로또 사이트에서 F12 > Network > css 파트 클릭 > common.css를 app> assets > stylesheets > application.css 에 저장

![image-20201112195022580](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201112195022580.png)



4. 부트스트랩으로 더 꾸미려면 app > views > layouts > application.html.erb에서 작성 가능
   * head 부분에 부트스트랩 import 코드 작성
   * body 부분의 <%= yield %> 사이에 우리가 작성한 view 파일이 들어가기 때문에 모든 코드가 적용이 된다.





### Tip

1. Alt + Shift + P : 자동 정렬





### 요약 정리

![image-20201112194332219](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201112194332219.png)