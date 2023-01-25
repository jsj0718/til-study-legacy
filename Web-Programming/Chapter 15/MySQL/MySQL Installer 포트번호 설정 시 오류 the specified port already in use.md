## [MySQL] MySQL Installer 포트번호 설정 시 오류 the specified port already in use

![img](https://blog.kakaocdn.net/dn/qmzTS/btqFZjlC71i/vMnQEVPJAkDUXECgA42Okk/img.png)



위와 같이 포트번호에 경고 표시가 있는데 이는 MySQL 이전 버전이 아직 남아있기 때문에 발생한 오류였다.

어떻게 해결할 수 있나?

해결방법은 간단하다. 바로 남아있던 버전을 삭제해주면 된다.

 

삭제를 하기 위해 리소스 모니터 창을 띄워야한다.

작업표시줄의 검색창 또는 Win+R을 눌러 **resmon.exe**을 입력 후 확인을 클릭.



![img](https://blog.kakaocdn.net/dn/mgO8O/btqFZOeqZIn/bZzJWNlpnKQ6PyxdNfd5DK/img.png)



그럼 아래와 같은 리소스 모니터 창이 뜬다.



![img](https://blog.kakaocdn.net/dn/lwgRi/btqF0Zl6pjz/PFkEHydtg8jZUKa1cD1831/img.png)



 

수신 대기 포트 탭에서 포트번호가 3306인 PID를 찾고 해당 PID 번호를 이용하여 프롬프트에서 명령어를 실행시키면 삭제할 수 있다. 이때 주의할 점은 CMD를 관리자 권한으로 실행시켜야 한다.

 

다시 작업표시줄의 검색창에서 cmd을 입력 후 **관리자 권한으로 실행**을 클릭.

 



![img](https://blog.kakaocdn.net/dn/wxeF9/btqFZ4uFBXR/LospWi8khT5ZxM2DyaQ8KK/img.png)



 

그럼 명령 프롬프트 화면이 나오는데

taskkill /F /PID **해당 PID번호**

위의 명령어를 입력 후 엔터키를 누르면 프로세스가 종료되었다는 문구를 볼 수 있다.

 



![img](https://blog.kakaocdn.net/dn/EIT4Y/btqF0RokXOY/kSoKAkZaVNIsG3J0dwgkcK/img.png)



 

정말 성공적으로 이전 버전인 MySQL이 삭제되었는지 확인하기 위해 다시 MySQL Installer 화면으로.

 



![img](https://blog.kakaocdn.net/dn/c3s2qf/btqFZOyQ0Gt/QmF40t15JnPTksNQkQAfak/img.png)



 

Port 번호 입력란에 3306을 작성 → 느낌표 모양의 경고 표시가 나타나지 않는 것을 확인할 수 있다.

이로써 MySQL 설치 시 포트번호 오류를 해결했다!