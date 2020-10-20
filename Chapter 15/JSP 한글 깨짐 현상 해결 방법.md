# **JSP 한글 깨짐 현상 해결 방법**

최신 IDE(통합 개발 환경)를 사용 하신다면, 기본적으로 인코딩 방식은 UTF-8로 설정이 되어 있을 것입니다.

하지만 Windows 운영체제는 기본 인코딩 값으로 여전히 euc-kr방식을 사용하기 때문에,

이 페이지가 UTF-8 방식으로 인코딩 되었음을 알려야 합니다.

 

HTML5의 경우 다음 코드를 <head> 태그 안에 삽입하여 페이지 언어셋이 utf-8임을 브라우저에 알립니다. (기본)

```
<meta charset="utf-8">
```

 

JSP의 경우 다음 코드를 <head> 태그 안에 삽입하면 됩니다.

```
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
```

 

메모장을 사용하신다면, 저장 전에 하단의 인코딩 드롭박스에서 UTF-8을 선택하셔야 합니다.