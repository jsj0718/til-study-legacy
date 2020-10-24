### # [Windows MySQL UTF-8 설정](https://lazymankook.tistory.com/70)

국윤창 2018. 7. 23. 21:16

Eclipse에서 JDBC를 이용해 MySQL을 사용하는데 한글때문에 애를 먹어서 정리해놓는다.



C:\**ProgramData**\MySQL\MySQL Server 5.7 폴더에 간다. (버전에 따라 폴더명이 다를 수 있음)

경로가 Program Files 폴더가 아닌 ProgramData임을 주의하자.



my.ini 파일을 열고 아래의 내용을 맨 밑에 추가시키고 저장한다.



[client]

default-character-set=utf8



[mysqld]

character-set-client-handshake = FALSE

init_connect="SET collation_connection = utf8_general_ci"

init_connect="SET NAMES utf8"

character-set-server = utf8



[mysql]

default-character-set=utf8



[mysqldump]

default-character-set = utf8



윈도우 검색에서 "서비스"를 검색하여 연다. 아래 그림 1처럼 서비스에서 MySQL을 찾아서 다시 시작한다.

![img](https://t1.daumcdn.net/cfile/tistory/992E82465B55C32D35)[그림 1] MySQL 다시 시작



cmd에서 mysql을 켜고 status를 쳐서 아래 그림 2와 같이 characterset이 설정 돼있으면 성공이다.

![img](https://t1.daumcdn.net/cfile/tistory/99842B4E5B55C3BA16)[그림 2] characterset





이렇게 설정해도 이전에 만들어진 데이터베이스와 테이블은 여전히 UTF-8로 설정돼있지 않다. 이 경우에는 workbench를 켜고 데이터베이스를 수정하고 테이블을 다시 만들어야한다. cmd에서 테이블의 charset을 잠시 바꿀 수 있지만, 서비스를 종료하고 다시 시작하면 원래대로 돌아온다. 테이블을 삭제하지 않고 하는 방법은 모르니 각자 찾아보길 바람..



workbench에서 아래 그림 3처럼 DB우클릭->Alter Schema를 누른다.

![img](https://t1.daumcdn.net/cfile/tistory/991326465B55C5632E)[그림 3] Alter Schema



그러면 새로운 탭에 아래 그림 4처럼 Charset/Collation 항목이 나타날 것이다. 이 부분을 utf8과 utf8_general_ci로 바꾸면 된다. 처음엔 latin 같은 것으로 설정돼있다.

![img](https://t1.daumcdn.net/cfile/tistory/992BD4505B55C5FA24)[그림 4] charset 설정



설정을 마치고 아래의 Apply를 누르자. Apply 버튼을 누른 뒤 utf8_bin으로 Collation이 바뀔수도 있는데, 무시해도 된다.



마찬가지로, 테이블을 새로 만들 때는 아래 그림 5처럼 Charset/Collation 항목을 utf8과 utf8_general_ci로 설정하자. 

![img](https://t1.daumcdn.net/cfile/tistory/998BF7445B55C6C035)[그림 5] Table charset 설정