# Git & Github

## #0. 다시 공부하는 Git & Github

- Remote 저장소에 있는 파일 저장 및 관리
- 협업이 가능하도록 저장소를 관리 하는 방법
- 기타 꼭 알아야하는 기본 지식부터 알아두면 좋은 팁까지!

⇒ 다시 공부하면서 하나하나 정복해나가자

## #1. Unit 1. Git & Github 소개

![Git%20Github/Untitled.png](Git%20Github/Untitled.png)

> 파일의 이름은 그대로 두고 버전 관리는 컴퓨터가 하게 하자

언제까지 model_v1.py, model_v2.py, model_v3.py... 이렇게 관리할래?

![Git%20Github/Untitled%201.png](Git%20Github/Untitled%201.png)

![Git%20Github/Untitled%202.png](Git%20Github/Untitled%202.png)

### Summary

- Git is version management tool using local repository
- Github is remote repository for collaboration by multiple git users

생각을 해보자...

git은 로컬 저장소를 사용하는 버전관리 툴이야

github은 원격 저장소야. 왜 원격 저장소지? 다양한 깃 유저들과 함께 협업하기 위함이야

keep going

## #2. Git& Github 개념

### git data transport commands

(git에서 데이터 전송 명령어들)

![Git%20Github/Untitled%203.png](Git%20Github/Untitled%203.png)

### Working Directory, Local Repository, Remote Repository

![Git%20Github/Untitled%204.png](Git%20Github/Untitled%204.png)

⇒ 그래서 각각의 역할이 뭔데요?

- **Working Directory**: 내 PC안의 작업공간들 중 git을 사용하는 작업공간
- **Index**: 임시 버전들이 올라가는 공간
- **Local Repository**: 최종 확정본이 올라가는 공간개인 PC에 파일이 저장되는 개인 전용 저장소
- **Remote Repository**: 파일이 원격저장소 전용 서버에 올라가는 공간

### git init, add, commit

![Git%20Github/Untitled%205.png](Git%20Github/Untitled%205.png)

내 pc안에서 작업하다가 저장 또는 관리가 필요한 파일을을 add한다.

add한 파일들 중 최종 확정본을 commit을 통해 Local Repository에 올린다.

### checkout

![Git%20Github/Untitled%206.png](Git%20Github/Untitled%206.png)

### Checkout → add → commit

![Git%20Github/Untitled%207.png](Git%20Github/Untitled%207.png)

- Local repository와 Remote repository란 무엇인가?

→ 그래서 Local repository와 Remote repository가 뭔데?

![Git%20Github/Untitled%208.png](Git%20Github/Untitled%208.png)

- Example
    - Local repository: 연구실 컴퓨터, 집 데스크탑, 맥북
    - Remote repository: 여러 사람이 공유하기 위한 저장소, [Steve-YJ github](https://github.com/Steve-YJ)

![Git%20Github/Untitled%209.png](Git%20Github/Untitled%209.png)

![Git%20Github/Untitled%2010.png](Git%20Github/Untitled%2010.png)

![Git%20Github/Untitled%2011.png](Git%20Github/Untitled%2011.png)

### Summary

*이것 만큼은 알고 넘어가자*

- Git이란 local repository의 버전관리를 위한 툴이다.
- Github은 원격서버를 통해 여러사람들이 협업할 수 있도록 파일을 저장하고 관리해준다.
- git init, git add, git commit

### Git의 다양한 명령어

![Git%20Github/Untitled%2012.png](Git%20Github/Untitled%2012.png)

Q. 내 깃에 있는 작업을 그대로 불러다가 하고 싶으면 git pull하면 되는거 아냐?!

⇒ 뒤에서 보다 자세히 배우게 됩니다.

## #3. 실습

### 1) Git add와 commit

- git add

![Git%20Github/Untitled%2013.png](Git%20Github/Untitled%2013.png)

- git commit

![Git%20Github/Untitled%2014.png](Git%20Github/Untitled%2014.png)

⇒ 이로써 Master branch에서 작업한 최종 확정본이 로컬 리퍼지토리(local repository)에 저장된다.

### 2) branch 생성과 merge

- test branch 생성과 Checkout 명령어를 통한 test 브랜치로 이동

![Git%20Github/Untitled%2015.png](Git%20Github/Untitled%2015.png)

- [a.py](http://a.py) 수정

![Git%20Github/Untitled%2016.png](Git%20Github/Untitled%2016.png)

—my name is Youngjeon Lee 라는 기존 a.py파일에

—2020.03.08 sun YJ git-learning를 추가한다.

- [b.py](http://b.py) 작업

![Git%20Github/Untitled%2017.png](Git%20Github/Untitled%2017.png)

- git status

![Git%20Github/Untitled%2018.png](Git%20Github/Untitled%2018.png)

⇒ Let's do it

*해석해보자!*

기존 master branch에서 test 브랜치로 이동을 한 상태에서 다음의 작업을 수행하였다.

1. [a.py](http://a.py) 파일 수정(맨 윗줄에 라인 추가)
2. b.py파일 생성

git status 명령어를 입력했을 때 위의 사진과 같은 출력을 얻게된다.

a.py의 경우 changes not staged for commit

업데이트 내역을 commit 하기 위해 git add 명령어 사용할 것을 권한다.

b.py의 경우 새로 생성했지만 git add를 해주지 않았기에 Untracked file이라는 메세지를 볼 수 있다.

⇒ 그렇다면 이제 내가 해야할 일은

git add [a.py](http://a.py) b.py가 아닐까?

- git add -A

git add -A명령어를 통해 워킹디렉터리(working directory)내에 있는 모든 파일들을 추적할 수 있다.

master에서 했던 작업과 마찬가지로 commit을 해줘야 원격저장소를 통해 관리할 수 있게 된다. 

![Git%20Github/Untitled%2019.png](Git%20Github/Untitled%2019.png)

- git commit -m "edit [a.py](http://a.py) and make b.py"

![Git%20Github/Untitled%2020.png](Git%20Github/Untitled%2020.png)

—commit message로 나는 a.py파일을 수정했고 b.py를 만들었어! 라고 입력한다.

- git log —branches —decorate —graph —oneline

![Git%20Github/Untitled%2021.png](Git%20Github/Untitled%2021.png)

---

지금까지는 test branch에서 작업을 했다.

1. Master branch에서 a.py파일을 만들었고 test branch로 이동해서 작업을 했다.
2. test branch에서는 a.py파일을 수정했으며 b.py파일을 만들었다.
3. 다시 master branch로 이동한다.

---

- master 브랜치 이동/edit a.py
    - master 브랜치 이동 및 [a.py](http://a.py) 수정

![Git%20Github/Untitled%2022.png](Git%20Github/Untitled%2022.png)

![Git%20Github/Untitled%2023.png](Git%20Github/Untitled%2023.png)

- 수정된 a.py를 tracking하도록 하고 commit해준다.

![Git%20Github/Untitled%2024.png](Git%20Github/Untitled%2024.png)

- git log —branches —decorate —graph —oneline

![Git%20Github/Untitled%2025.png](Git%20Github/Untitled%2025.png)

위의 그림은 지금까지 한 작업들을 보여준다. 해석해보면 지금까지 작업한 내용들에 대해서 보다 이해가 잘 가리라 생각한다.

---

- 해석
1. Master branch: 우리는 master branch에서 처음 작업을 했다. a.py파일을 생성하고 git이 a.py파일을 추적하도록 하여 first commit을 했다.
2. Checkout to test branch: master branch에서 test branch로 체크아웃을 했다. 여기서 주목할 점은 master branch에서 생성한 [a.py](http://a.py)수정과 b.py생성이다. master branch에서 생성한 a.py파일을 test branch로 이동해 작업을 했으며 b.py라는 새로운 파이썬 파일을 생성했다. 작업한 내용을 'edit a.py and make b.py'라는 메세지와 함께 commit 했다.
3. Checkout from test branch to master branch: test branch에서 다시 master branch로 돌아왔다. 여기서 한 작업은 [a.py](http://a.py) 파일을 수정한 것이다. 

⇒ 이제 버전관리가 어떻게 이루어지는지 살펴보도록 하자. 

---

### master 브랜치에서 test 브랜치 merge

![Git%20Github/Untitled%2026.png](Git%20Github/Untitled%2026.png)

master브랜치에서 test 브랜치를 merge했다. git log —branches —decorate —graph —oneline 명령어를 통해 작업한 내용들을 살펴보자.

![Git%20Github/Untitled%2027.png](Git%20Github/Untitled%2027.png)

예전에는 이 부분이 이해가 잘 안갔었는데 이제 알것 같다.

브랜치를 보면 지금까지 했던 작업들을 직관적으로 보여준다.

1. master branch - first commit
2. test branch — edit [a.py](http://a.py) and make b.py

    master branch — edit a.py

3. masterbranch — Merge branch 'test'

### 항상 merge가 잘 될까?

- 어떤 경우 merge가 되지 않는지 알아보자

### test2 브랜치 생성 후 이동 / edit a.py

![Git%20Github/Untitled%2028.png](Git%20Github/Untitled%2028.png)

![Git%20Github/Untitled%2029.png](Git%20Github/Untitled%2029.png)

### master 브랜치로 이동/edit a.py

![Git%20Github/Untitled%2030.png](Git%20Github/Untitled%2030.png)

![Git%20Github/Untitled%2031.png](Git%20Github/Untitled%2031.png)

⇒ **주의!**

test2 브랜치와 master 브랜치 모두 [a.py](http://a.py) 파일의 2번째 줄을 수정했다.

생각해보자. 회의록을 작성하는데 나는 두 번째 줄에 "우리 회사의 수익은 10000이다."라고 작성했는데 나의 동료는 "우리 회사의 수익은 20000이다."라고 작성을 했다. 이 때 두 파일을 합치면 버전관리가 될까?

10000이야? 20000이야?!
같은 문제가 코드에서 발생하는 것이다. 충돌이 나는 것이다.

![Git%20Github/Untitled%2032.png](Git%20Github/Untitled%2032.png)

> CONFLICT (content): Merge conflict in a.py

⇒ 다시 a.py에 들어가서 충돌이 일어난 부분을 수정해야 한다.

![Git%20Github/Untitled%2033.png](Git%20Github/Untitled%2033.png)

⇒ 충돌이 난 부분을 수정해주면 병합을 할 수 있게 된다. 

![Git%20Github/Untitled%2034.png](Git%20Github/Untitled%2034.png)

![Git%20Github/Untitled%2035.png](Git%20Github/Untitled%2035.png)

## #4. 유용한 팁

### 1. 원격저장소와 연결

- 원격저장소를 관리할 수 있는 명령어 git remote를 이용하여 연결
- git remote add origin 사용자명@호스트:/원격/저장소/경로

(git clone 사용자명@호스트:/원격/저장소/경로)

### 2. 원격 저장소에서 로컬 저장소로 업데이트하는 방법

### 원격 저장소 → 로컬 저장소 pull(fetch & merge)

- 원격 저장소의 내용을 로컬 저장소로 업데이트(다른 사람이 수정한 것을 받기 위해)
- git pull origin master(브랜치명) 실행
- origin의 내용이 master로 반영(fetch)되고 브랜치를 병합(merge)

### 3. git configuration

- git pull을 할 때는 깃허브의 유저이름과 비밀번호를 쳐야 하는 경우가 많다.
- 매번 비밀번호를 입력하기 싫다면
    - git config —global credmential.helper 'store —file 경로'하면 해당 경로에 비밀번호가 저장된 파일이 생성된다.
    - 단, 파일로 저장되는 만큼 보안에 취약하기 때문에 주의해야 한다.

### 4. 많이 쓰이는 패턴

### 많이 쓰이는 패턴

![Git%20Github/Untitled%2036.png](Git%20Github/Untitled%2036.png)

타인의 원격 저장소를 복사해 온다든지

원격 저장소의 내용을 로컬로 복사해온다든지

브랜치를 생성후 작업을 한다든지

원격 저장소의 관리자가 변경 내역을 확인 후  merge여부를 결정한다든지!

## #8. Reference

- 투빅스 11기 정규세션 - 정윤호의 Git&GitHub