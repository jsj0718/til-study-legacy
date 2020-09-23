# [기초-출력] 출력하기08(설명) -> 유니코드 이용하여 출력
# 유니코드를 이용하기 때문에 한글을 출력할 때와 같이 소스 제출 페이지 상단에 있는 구문을 코드에 넣어 주어야 합니다.

import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

print("""\
\u250c\u252c\u2510
\u251c\u253c\u2524
\u2514\u2534\u2518\
""")