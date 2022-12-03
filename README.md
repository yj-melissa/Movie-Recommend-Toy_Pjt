# 1. 개요

## 영화 커뮤니티 <우주인>

- 다양한 영화 데이터를 제공하는 동시에 유저간 소통을 지원하는 영화 커뮤니티를 목표로 개발
- 이름 <우주인>은 커뮤니티 컨셉인 우주와 연관 있는 동시에 **Would you** interested **in** the movie? **Would you** come **in**…? 등 다양한 청유형 문장에 사용되는 ***Would you … in …?***에서 착안

## 주요 특징

- tmdb에서 받아온 다양한 영화 데이터를 제공
- 아키네이터처럼 질문을 통해 유저가 좋아하는 영화를 맞추는 동시에 그 영화와 비슷한 장르 혹은 같은 배우가 출연한 영화를 추천
- 영화 좋아요, 한줄평 기능
- 커뮤니티 글, 댓글 기능
- 아이디 대신 이메일 사용
- 유저 프로필 사진 기능
- 영화 제목 검색 기능
- 페이지 골조로 대부분 카드를 사용

# 2. 기능 세부 사항

## 회원가입

![image-1.png](C:\Users\lyjun\OneDrive\Desktop\README_img\image-1.png)

- 별도 ID 없이 email로 가입
- 프로필 이미지 등록 및 선택한 이미지 미리 보기 지원
- 회원가입 후 자동으로 로그인 처리, 환영 메시지 출력 후 자동으로 홈으로 이동

## 로그인

![image-2.png](C:\Users\lyjun\OneDrive\Desktop\README_img\image-2.png)

로그인 성공시 서버에서 받은 기본 토큰 정보와 유저 정보를 클라이언트 측에서 저장하도록 함

## 메인 페이지

![image-3.png](C:\Users\lyjun\OneDrive\Desktop\README_img\image-3.png)

- 두 개의 컴포넌트(MovieCarousel, MovieItems)를 사용해 화면 구성
- axios를 이용해 영화 데이터를 요청, 받은 데이터를 각 컴포넌트에 전달
- Carousel은 최상위 영화 5개, MovieItems는 유저의 선택에 따라 인기순, 평점순, 최신순으로 영화를 정렬, 각각 9개의 영화를 출력
- 캐러셀은 Vue-carousel-3D를 사용해 구현
- 영화 포스터를 누르면 각 영화 상세페이지로 이동하도록 함

### 영화 상세 페이지

![image-4.png](C:\Users\lyjun\OneDrive\Desktop\README_img\image-4.png)

![image-5.png](C:\Users\lyjun\OneDrive\Desktop\README_img\image-5.png)




- Params로 선택한 영화의 id를 받아 서버에 전송, 서버에서 해당 영화 정보를 받아옴
- 영화 제목, 내용, 개봉일자, 장르, 평점, 출연진, 감독을 출력함
- 유튜브에서 예고편을 검색해 자동 실행하게 함
- 해당 영화에 한줄평과 별점을 남길 수 있음(최대 1개), 삭제 가능
- 좋아요를 표시할 수 있음
- 한줄평은 페이지네이션을 적용, 한 페이지에 최대 4개까지만 출력함

### 검색

![image-6.png](C:\Users\lyjun\OneDrive\Desktop\README_img\image-6.png)

![image-7.png](C:\Users\lyjun\OneDrive\Desktop\README_img\image-7.png)

![image-8.png](C:\Users\lyjun\OneDrive\Desktop\README_img\image-8.png)



- 모달을 사용, 검색어를 입력하면 params로 전달, SearchView로 이동

- QueryString으로 서버에 요청, 서버에서 검색어가 제목에 포함된 영화들을 반환

- 출력된 제목을 클릭하면 상세 페이지로 이동

- 검색결과가 없으면 검색결과가 없다는 결과 출력

### 커뮤니티

- ![image-9.png](C:\Users\lyjun\OneDrive\Desktop\README_img\image-9.png)
  
  제목과 작성자 출력
- 게시판 목록 페이지네이션 처리

### 커뮤니티 글 상세 페이지

![image-10.png](C:\Users\lyjun\OneDrive\Desktop\README_img\image-10.png)

- 댓글 출력(페이지네이션 적용)
- 글, 댓글 작성자에게만 수정, 삭제 버튼 보이도록 처리

### 커뮤니티 글 생성 페이지

![image-11.png](C:\Users\lyjun\OneDrive\Desktop\README_img\image-11.png)

- 글 등록 완료시 작성한 글 상세 페이지로 이동

### 프로필 페이지

![image-12.png](C:\Users\lyjun\OneDrive\Desktop\README_img\image-12.png)

![image-13.png](C:\Users\lyjun\OneDrive\Desktop\README_img\image-13.png)



- 작성한 글, 댓글, 리뷰, 좋아요 표시한 영화 확인 가능 (페이지네이션 처리)

- 각 제목 클릭시 해당 글/영화 상세 페이지로 이동

- 기본 설정한 프로필 출력 (미등록시 기본 프로필 출력)

- 닉네임, 프로필 사진, 비밀번호 수정 가능
  
  - 비밀번호 수정 시 로그아웃 처리

- 회원 탈퇴
  
  - 모달로 재확인 문구 출력

### 로그아웃

- 로그아웃시 자동으로 로그인 페이지로 이동
- 기존 로컬저장소와 state에 저장해뒀던 유저 정보 및 토큰 삭제

### 영화 추천 서비스 (무비 아키네이터)

![image-14.png](C:\Users\lyjun\OneDrive\Desktop\README_img\image-14.png)

기본 작동  원리

1. 컴퓨터는 임의의 영화 하나를 가장 가능성이 높은 영화로 선정함
2. 컴퓨터는 임의의 영화에 관한 정보를 질문하고 예, 아니오에 따라 서버로 결과를 전송
3. 서버는 결과에 따라 분류를 시작하고 분류된 데이터를 프론트로 전송
4. 프론트는 최초 이후 끝날때까지 주어진 정보로 스코프를 줄여가며 영화를 특정해나감
5. 질문은 배우, 감독, 영화 내 캐릭터, 연대, 개봉연도 등의 정보를 질문함.
6. 마지막 질문까지 마치고 난 후 가지고 있는 영화 리스트의 최상단에 있는 영화를 출력함
7. 결과로 나온 영화의 장르, 배우가 출연한 영화를 추천리스트로 만들어 캐러셀로 출력

![image-15.png](C:\Users\lyjun\OneDrive\Desktop\README_img\image-15.png)

![image-16.png](C:\Users\lyjun\OneDrive\Desktop\README_img\image-16.png)




### 프로젝트 후기

    조홍준 : 처음 시도해보는 온전한 웹 서비스 제작에 처음에는 어떻게 진행해야할 지 조금은 막막했습니다. 하지만 처음부터 욕심내기보다는 그동안 배웠던 것들을
            최대한 많이 활용해보면서 1학기를 정리하는 느낌의 프로젝트를 만들고싶었고 하나하나 기능들을 완성시켜나가다보니 어느덧 원하던 결과물을 얻을 수 있었습니다.
            저희 프로젝트가 1등을 차지한 프로젝트는 아니었지만 개인적으로 처음 계획했던 방향으로 끝까지 순항하며 다른 조보다 여유로운 일정을 가질 수 있었던 부분이
            만족스럽습니다. 이번 프로젝트를 겪으며 하나의 서비스를 만들어 보는 경험을 한 것과 더불어 처음 기획을 올바른 방향으로 하고 그 방향으로 마일스톤을 기획해서
            매일 진척도를 체크하며 차근차근 나아가본 경험을 한 것이 앞으로 프로젝트를 하면서도 정말 큰 도움이 될 것 같습니다.

```markdown
임유정: 나름대로 해야할 일과 순서, 구조들을 계획해두고 개발을 시작했음에도 불구하고 초반에 막막함을 느끼거나, 허둥지둥 하는 일이 많았습니다. 정신없이 진행하다보니 수업시간에 예시로 들었던 실수들을 제가 다 하고 있는 걸 깨닫고서야 마음의 여유를 조금이나마 찾을 수 있었던 것 같습니다. 
프로젝트를 진행하면서 전체적으로 한 학기 동안 배운 내용을 정리하는 동시에 기획의 중요성이나, 협업, 일정 관리 등을 배우는 기회가 되었습니다.
```
