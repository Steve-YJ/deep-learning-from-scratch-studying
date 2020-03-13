# https://itmining.tistory.com/122
# 시작: Python은 파일 경로 또는 디렉토리와 관련한 코드가 많이 필요하다.
# 파일 및 디렉터리 경로에 관한 함수는 모두 os 모듈을 사용하기 때문에 os 모듈을 import한다.

import os

#1. 현재 작업 폴더 보기
print(os.getcwd())  # get current working directory
                    # C:\Users\Lee\Documents\steve-home

# 2. 디렉토리 변경
os.chdir("/Users")
print(os.getcwd())  # expect /Users

# 3. 특정 경로에 대해 절대 경로 얻기
print(os.path.abspath("__file__"))  # 특정 파일의 절대 경로를 출력해준다.ArithmeticError

# 4. 경로 중 디렉토리명만 얻기
# 이것만 제대로 활용해도 실전 코딩에서 상당히 많은 도움을 받을 수 있다.
print(os.path.dirname(os.path.abspath("__file__")))  
