# Rubi on Rails (2)



### 강의 내용

1. DB 이론
   * DB : 데이터를 효율적으로 관리하는 것
     * 관계형 DB (RDB) : 정해진 틀에 정해진 정보를 입력하는 것
     * NoSQL : 정해진 틀이 없이 자유롭게 정보를 입력하는 것
     * DBMS : DataBase Management System
     * CRUD : Create Read Update Delete
       * Create : 정보 생성
       * Read : 정보 검색
       * Update : 정보 수정
       * Delete : 정보 삭제
     * Columns은 속성, rows는 레코드이며 하나의 row가 하나의 데이터를 뜻한다.
     * 엑셀에 여러 탭이 있는 것처럼 DB에도 여러 테이블로 나눠서 데이터를 저장한다.
2. Model을 활용해 DB 다루기





## 게시글 만들기

1. rails g scaffold Post title:string content:string (CRUD 생성)
2. rails db:migrate (DB 생성)



* 순서도 

1. rails g controller board(컨트롤러 이름) index(뷰 이름) : controller, view 동시 생성하기
   *  이렇게 하면 컨트롤러, 라우터, index 파일 생성까지 세 가지가 동시에 처리된다.



2. rails g model post(모델 이름) : 모델 생성하기
   * models > concerns > post.rb 파일 생성
   * db > migrate > 20201114101356_create_posts.rb 파일 생성
     * migrate 파일은 어떤 Columns이 들어갈지 작성해주는 칸
     * activerecord migration에 자세한 설명 참조

```
class CreatePosts < ActiveRecord::Migration[6.0]
  def change
    create_table :posts do |t|
		t.string :title # 칼럼 추가 
      	t.text :content # 칼럼 추가 

		t.timestamps # 생성일, 수정일은 자동 생성
    end
  end
end

# Primary Key는 따로 설정하지 않으면 rails에서 자동으로 관리해준다.
```

3. rails db:migrate
   * migration을 통해 post라는 table 생성



4. Create 생성하기

   * controller에 create 추가

   ![image-20201114230847980](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201114230847980.png)

   

   * view에서 정보를 전달하는 form 필요

   ![image-20201114193515935](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201114193515935.png)

   

   * view에 form 형식을 저장하고 날려보면 에러 발생 (action을 받는 파일이 없기 때문)

   ![image-20201114193458848](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201114193458848.png)

   

   * 에러 화면에서 request 부분에서 원하는 정보가 잘 전달되고 있는지 확인 가능

   ![image-20201114193442180](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201114193442180.png)

   

   * 라우터에 뷰를 추가한 것 처럼 create 추가

   ![image-20201114230808204](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201114230808204.png)

   

   * InvalidAuthenticityToken 문제 해결하기

   ![image-20201114231204052](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201114231204052.png)

   

   * > * rails에서 제공하는 보안 기능으로 인해 발생
     >
     > * CSRF(Cross-Site request Forgery) : 사이트 간 요청 위조 공격에 대비하기 위함
     >
     > * ![image-20201114231453664](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201114231453664.png)
     >
     > * 다른 사이트에서 DB를 조작하면 안되기 때문에 무작위로 바뀌는 토큰을 제공하고 이 토큰이 일치해야만 같은 사이트임을 인증해서 요청을 받아들이는 구조
     >
     > * generate AuthenticityToken on rails 검색으로 토큰 삽입 가능
     >
     > * ```rb
     >   <input name="authenticity_token" value="<%= form_authenticity_token %>" type="hidden">
     >   ```
     >
     > * 구름 IDE에서 제공하기 때문에 https 대신 http 이용



5. DB에 Columns 생성 및 Model에 Data 삽입 코딩 후 board로 돌아가기

![image-20201114232550900](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201114232550900.png)



6. Rubygem 이용하기 (보조 프로그램)
   1. rubygems.org 이동
   2. 검색창에 rails_db 검색
   3. gemfile 경로 복사
   4. gemfile에 복사 후 bundle install 명령어 입력
   5. http://crud-ewlfx.run.goorm.io/rails/db > posts에 입력받은 테이블을 확인 가능
   6. Export를 통해 쌓인 데이터를 csv 파일로 엑셀에서 볼 수 있다. (수정, 검색, Query 가능)



7. Read 구현하기

![image-20201114235011520](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201114235011520.png)

* @posts 변수 선언 후 Post로 모델을 불러와서 모든 것을 변수에 대입한다.



![image-20201114235107638](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201114235107638.png)

* @posts에 담긴 변수를 each로 하나씩 빼서 post에 담은 후 출력한다.
* <% %>는 화면 출력 X, <%= %>는 화면 출력