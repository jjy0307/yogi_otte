# ☘ yogi_otte

## 🔜 목차
1. 프로젝트 소개  
2. 팀 구성  
3. Stack
4. Stack & Library Version
5. 주요 기능  
6. Troubleshooting
7. Architecture
8. ERD
9. API
10. Layout

## 📄 프로젝트 소개

### ⏲ 개발 기간 : 2022.6.2 ~ 2022.6.14

### 소개 영상  [youtube](https://youtu.be/0nFCMUi_nic)

### Github  [Code](https://github.com/jjy0307/yogi_otte)

## 🧑 팀 구성 
* 4인 팀 프로젝트  <br>
* 맡은 역할 : AI Engineer

<table>
  <tr>
    <td align="center"><strong>구분</strong></td>
    <td align="center"><strong>Back-end</strong></td>
    <td align="center"><strong>Front-end</strong></td>
    <td align="center"><strong>Designer</strong></td>
    <td align="center"><strong>AI Engineer</strong></td>	  
  </tr>
  <tr>
    <td align="center"><strong>Position</strong></td>
    <td align="center">이승태</td>
    <td align="center">김민재</td>
    <td align="center">김민재</td>
    <td align="center">전진영</br>윤가현</td>
  </tr>
</table>

## ✨ Stack
* Language : Python, Javascript
* Framework : Django
* Database : MySQL

## 📖 Stack & Library Version
<img src="https://img.shields.io/badge/python-3.9.12-brightgreen"> <img src="https://img.shields.io/badge/django-4.0.6-brightgreen"> <img src="https://img.shields.io/badge/django_rest_framework-3.13.1-brightgreen"> <img src="https://img.shields.io/badge/django_rest_framework_simple_jwt-5.2.0-brightgreen"> <img src="https://img.shields.io/badge/django_cors_header-3.13.0-brightgreen"> <img src="https://img.shields.io/badge/mysql_client-2.1.1-brightgreen"> <img src="https://img.shields.io/badge/tensorflow-2.9.1-brightgreen"> <img src="https://img.shields.io/badge/konlpy-0.6.0-brightgreen"> <img src="https://img.shields.io/badge/boto3-1.24.40-brightgreen"> <img src="https://img.shields.io/badge/PyJWT-2.4.0-brightgreen"> <img src="https://img.shields.io/badge/urllib3-1.26.11-brightgreen"> <img src="https://img.shields.io/badge/requests-2.28.1-brightgreen">
</br>
## 🕹 주요 기능
### 로그인 / 회원가입
* JWT 토큰 방식으로 구현
* Local Storage에 저장
* 각 페이지마다 접속시 refresh token을 받게 설정
* 아이디를 고유값으로 지정하여 중복 방지

### 메인 페이지
* 로그인 유무에 따라 추천 커뮤니티 변경
    * 추천 커뮤니티는 무조건 공개 커뮤니티에 대해서만 제공
* 커뮤니티 별 하루 접속자 수 순위표 제공
* 가입되지 않은 커뮤니티에 가입 요청 / 요청 취소 가능
* 커뮤니티 카드를 누를시 해당 커뮤니티로 이동
    * 단 가입되지 않은 커뮤니티는 접속 불가능
* 커뮤니티 생성
    * 커뮤니티 생성자는 관리자로 자동 설정

### 마이 페이지
* 비밀번호 변경 가능
* 가입된 커뮤니티 관리
* 작성한 글 관리(이동은 미구현)
* 작성한 댓글 관리(이동은 미구현)
* 유저->커뮤니티 가입 요청 결과 조회 / 요청 철회 / 요청 삭제
* 커뮤니티->유저 가입 요청 승락 / 요청 거절

### 커뮤니티 페이지
* 게시판 생성
   * 생성자는 게시판 관리자도 자동 설정
* 게시글 작성
   * Quill Library로 게시글 작성 기능 구현
   * 게시글에서 이미지 업로드 가능
   * 파일 업로드 가능
   * 게시글 제목, 내용중 하나라도 누락이 있을시 작성 불가능
* 게시글 수정
   * 게시글 제목, 내용중 하나라도 누락이 있을시 작성 불가능
* 댓글 작성
   * 생성시 날짜, 아이디 노출
   * 시간순으로 배치
   * 내용이 없으면 작성 불가능

## 😣 TroubleShooting
1. User와 Community가 ManyToMany 관계일때 커뮤니티 관리자 저장할 Table 설정
    * 해결 : UserAndCommunity라는 중간 테이블을 만들고 User, Community를 참조
    * User에 Admin을 설정할 시 어떤 커뮤니티에 해당되는지 설정하기 어려움
    * 마찬가지로 Community에 Admin에 설정을 해도 같은 문제 발생

2. 동시에 여러 개의 serializer 정보 저장 중 오류 발생으로 일정 부분만 저장될 때
    * 해결 : transaction을 사용하여 모든 serializer가 동시에 저장되게끔 설정

## 🏚 Architecture
![image](https://user-images.githubusercontent.com/90381057/186589235-d27760f4-2d18-4642-90be-950eca5e2a92.png)


## ⚙ [ERD](https://www.erdcloud.com/d/EL9ztjydoLhqhysPe)
![image](https://user-images.githubusercontent.com/90381057/186103025-070baeb8-083d-4394-9153-207b4751c940.png)

## 🚀 **API 설계**
[article](https://documenter.getpostman.com/view/16204656/VUquLFrn#intro)  
[community](https://documenter.getpostman.com/view/16204656/VUquLFw9)  
[noticeboard](https://documenter.getpostman.com/view/16204656/VUquLajN)  
[user](https://documenter.getpostman.com/view/16204656/VUquLajQ)  

## 🗺 Layout
![Group 26](https://user-images.githubusercontent.com/90381057/186547234-04a9537b-2f48-4a3d-903b-bed3f7b3ba8d.png)

# 🍙 요기 어때?
### **서비스 아이디어**

**요기요 + 여기어때 를 합쳐서 ‘요기 어때’** 라는 네임을 짓게 되었습니다.<br>
![요기어때](https://velog.velcdn.com/images/soyoyun/post/5e382618-78a8-4123-a37e-768412455520/image.png)

프론트 제작시 백에서 받아온 데이터를 기반으로 요기요 사이트와 비슷한 느낌을 줄 수 있도록 제작되었습니다

---

### **서비스 소개**

**여러가지 검색 기능이 탑재된 사용자 기반 맛집 추천 시스템**

---

### 기능 소개

- **오늘 나의 기분은 ? (로그인 후 이용 가능, /mood로 연결됨) [핵심기능]**
    - **0-100 사이의 값을 입력하면 그 기분과 비슷한 기분을 느낀 사람들이 많이 먹은 음식을 볼 수 있다.**
        
        (만약 50정도 이하의 기분을 입력하면 100에서 그 기분값을 뺀 값에 해당되는 결과가 검색된다.)
        
    - 사용자의 기분과 비슷한 점수를 받은 리뷰를 검색할 수 있다. (별점이 기분점수로 표시된다)
- **현재 배고픈 위치가 어디신가요? 계신 지역을 알려주세요 (로그인 후 이용 가능, /location으로 연결됨)**
    - 위치에 따른 검색결과를 나타내준다.
- **최고 평점을 받은 가게를 알 수 있다. (로그인 후 이용 가능)**
    - 가장 좋은 평점이 있는 리뷰 가져와 랜덤하게 하나씩 보여준다.
- **1주간 주문 랭킹을 알 수 있다.  (로그인 후 이용 가능)**
    - 데이터를 스크래핑 해왔던 날을 기점으로 1주일간 가장 많은 리뷰가 달린 가게를 볼 수 있다.

<aside>
💡 로그아웃을 하면 카테고리를 이용한 검색 페이지만 보이게 구성해 놓았습니다.

</aside>

- **카테고리 클릭**
    - 해당 카테고리에 맞는 검색결과를 나타내준다.
- **검색 결과 페이지 내**
    - 카테고리별, 위치별로 보기가 가능하다. (JS를 이용하여 제작)
    - 최근에 사람들이 가장 많이 먹은 음식은?
        - 스크래핑 해왔던 날을 기점으로 최근 30일 동안 가장 많은 리뷰가 달린 가게를 볼 수 있다.

- **역할 분담**
    - **데이터 수집 (스크래핑, 모델 학습용) : 가현**
    - **AI 모델 제작 : 진영**
    - **백엔드 담당 : 승태**
    - **프론트앤드 담당 : 민재**
- **발표자 및 영상촬영**
    - **발표자 : 윤가현**
    - **영상촬영 : 김민재**
    
---

### 개발 일정
![](https://velog.velcdn.com/images/soyoyun/post/38729843-fe80-4829-b6ee-0e413e97343e/image.png)

---

### 최종 **레이아웃**
![](https://velog.velcdn.com/images/soyoyun/post/e36504a0-6bb5-426c-95cc-7bfdb2937ae2/image.png)

---

### 페이지 시연

**- 로그인 전 화면**
    
![](https://velog.velcdn.com/images/soyoyun/post/b6f37af4-adb7-4930-9603-1e55f7542de7/image.png)

![](https://velog.velcdn.com/images/soyoyun/post/1a8942b5-2018-444a-8154-94b6e8aaca05/image.png)

    
**- 로그인 후 화면**
    
![](https://velog.velcdn.com/images/soyoyun/post/4124fb34-068c-4ad0-b592-2eb5c42b8460/image.png)

![](https://velog.velcdn.com/images/soyoyun/post/35a6ecfd-eb83-4a49-99d7-345bfd4c4102/image.png)

![](https://velog.velcdn.com/images/soyoyun/post/b878cc1f-9f22-49fb-9075-133359fb9d23/image.png)


---

### 사용한 데이터

**카카오맵, 네이버맵 스크래핑을 이용해 제작한 csv 데이터를 훈련 데이터 및 테스트 데이터로 사용**

- 카카오맵 스크래핑 데이터
![](https://velog.velcdn.com/images/soyoyun/post/f0cff6f4-5b2f-4e94-bbe2-e452a8127e73/image.png)

    
- **pandas 이용하여 personal_star가 4점 이상일때만 label에 1을 할당했다. 그래서 4점이상인 경우는 라벨에 1이 할당되어있고, 3점이하는 label에 0이 할당되어서 이를 학습 데이터로 사용하였다.**
	 - **스크래핑 후 정제된 리뷰 1619개, 카테고리 66개, 스토어 395개의 데이터가 사이트 DB에 저장되어있으며, DB는 MySQL을 사용하였다.**
     <br>
 
- 네이버맵 스크래핑 데이터
    
![](https://velog.velcdn.com/images/soyoyun/post/a8097e22-cccd-44ba-8878-0fd155fbb890/image.png)

    
- **네이버 맵 스크래핑같은 경우 csv 파일 제작 이후 진행되는 모델 제작을 위해 리뷰, 개인별점, 라벨 값만을 동일하게 추출해 내어 테스트데이터로 이용했다. 데이터양은 학습 정확도가 90%가 넘을 정도로 가져왔다.**
---
### 사용한 모델, 감성분석

데이터 처리 이후 해당 리뷰가 긍정인 경우 1, 부정인 경우 0을 표시한 레이블로 구성되어져 있는 csv 파일을 가져와 자연어 처리를 진행했다. 이를 바탕으로 **감성분석**(**Sentiment Analysis, 텍스트에 나타나는 감정/기분 등의 주관적 요소를 분석**)을 해보았다.

자연어 처리(NLP, **Natural Laguage Processing**)를 위해 다대일 구조의 **LSTM 모델을 사용하였다.** 

이는 **마지막 시점에서 두 개의 선택지 중 하나를 예측하는 이진 분류 문제를 수행하는 모델이다. 이진 분류 문제여서 (출력층에 로지스틱 회귀를 사용해야 하므로) 활성화 함수로는 시그모이드 함수를 사용하고, 손실 함수로 크로스 엔트로피 함수를 사용했다.**

![](https://velog.velcdn.com/images/soyoyun/post/232e2b31-9fe3-461b-b113-0ae7f97a4bde/image.png)


사진을 보면 부정, 긍정리뷰 판단한 결과의 정확도가 높은 것을 확인할 수 있다.

이외에 KoNLPy에서 제공되는 형태소 분석기를 사용했다. 그리고 임의의 리뷰에 대해 부정인지 긍정인지 예측하는 함수를 만들었다. 이를 이용해 사용자의 기분과 비슷한 점수를 받은 리뷰를 검색할 수 있도록 추천 시스템을 구현하였다.
![](https://velog.velcdn.com/images/soyoyun/post/32af943b-1ad0-4227-bde0-729be3f16777/image.png)

---
### 장고 모델 설계

foreign key갖는 부분을 모델에서 one-to-many 로 구성했으며 다른건 전부 one-to-one으로 구성했다.

Review 모델 안에 store, user부분을 foreign key로 연결해주었고

![](https://velog.velcdn.com/images/soyoyun/post/42f0a2f7-f13f-4e69-af00-e157f52f2696/image.png)


Store모델 안에 category를 foreign key로 연결해주었다.
![](https://velog.velcdn.com/images/soyoyun/post/a9ee2106-1257-4968-98c1-c937510ed527/image.png)


---
### **KPT,** 피드백 반영

**GitHub** 

깃헙 브랜치를 활용할 때 저번 피드백을 반영해 커밋메세지를 통일하고 데일리로 머지를 했다. 

![](https://velog.velcdn.com/images/soyoyun/post/4513a88b-c73d-4eeb-a12f-430a1c89d1d9/image.png)


**ERD 설계**

DB설계를 미리 해두었다.
![](https://velog.velcdn.com/images/soyoyun/post/da53b7ac-cb5a-4c91-9075-4b00fee414b2/image.png)

---
### **KPT 회고**

**[ Keep ]**

- 프로젝트별 노션 페이지 개설
- API 사전 설계
- DB 사전 설계
- 파일 경로 통일
- 프로젝트 초기에 기능 추가시 개인 브랜치 활용
- 팀원이 잘 모르는 부분의 코드 설명 필요시 도움요청 및 설명
- 슬랙으로 자료 공유
- 초기 목표 달성 및 추가 목표 달성
- 슬랙, 게더타운 이용해 질문
- 하루마다 점검 후 매일 머지
- 커밋메세지 통일
- .gitignore로 필요없는 파일은 업로드 시키지 않기

**[ Problem ]**

- 깃허브 개인 브랜치를 메인 브랜치로 합쳤을 때 충돌이 발생해 전 파일내용이 지워지는 문제 발생
- 저번 프로젝트처럼 모두가 마감일을 동일한 날짜로 정하고 진행했었는데 이번 프로젝트에서는 빠르게 끝나야 할 부분은 빠른 마감이 필요했음
- 초반 기획단계에서 만든 레이아웃을 수정해야 했어서 수정되기 전까지 프론트 작업이 지연되는 일 발생
- 한글로 .png, .csv 파일 이름 저장시 추후에 풀, 푸시 하면서 파일이 깨지는 문제 발생

**[ Try ]**

- 더 빠른 복구를 위해 파일 하나당 한 커밋으로 하기
- 프로젝트가 진행되는 순서에 따라 마감기한을 세분화해 정해놓으면 팀원 서포트를 더 빠르게 할 수 있어서 진행이 빠르게 될 것 같다고 생각함
- 파일 이름을 왠만하면 영어로 작성하기

**[ FEEL ]**

- 가현 : DB와 연계하여 사이트에 결과가 뜰 수 있게 했는데 추후 크롤링 데이터를 실시간으로 가져와 매일 업데이트되는 방향으로 고쳐보아도 좋을것같다고 생각해보았다. 카테고리에 category라는 이름으로 스크래핑된게 있는데 이를 통해 데이터 정제작업이 중요하다는 것을 깨닫게 되었다. 스크래핑 단계에서 원하는 데이터를 추후에 알게되어 스크래핑 다음 단계를 진행하기까지 시간이 지체되었어서 다음번엔 스크래핑 코드 내에 데이터를 정제할수있는 함수까지 만들어놓았으면 좋을 것 같다.
- 민재 : 처음으로 프론트엔드 부분을 메인으로 맡아서 해보았습니다. 만들때는 생각보다 원하는대로 잘 만들어진다고 생각을 했는데 만들고 나서 나중에 다시 살펴보니 하자가 있는 부분들이 너무 많았던거 같았습니다. 그리고 django를 이용해서 처음에 기본 셋팅을 하면서 서로 연결하는 것을 해볼때 재미있었던거 같습니다. 이번에는 단순한 프론트 작업만 한거 같은데 다음에 하게된다면 좀 더 많은 기능들을 사용해보고 깔끔하게 설계해서 만들어 보고 싶습니다.
- 승태 : Django가 MySQL을 자동적으로 생성해줘서 편했다. 사용자 입력 기분을 통한 추천 로직을 좀더 다양하게 짜봤으면 재미있었을거 같다. 또한 id값을 사용하지 않고 name을 사용하거나 최대 평점을 고정하는 등 오류가 날 사항들을 인지하고 고치지 않은점에서 아쉬움이 있다.
- 진영 :  LSTM을 처음 사용해서 잘 이용할 수 있을까 걱정을 많이 했는데 예상보다 쉽게 해결한거 같아 다행이였다. 이번 프로젝트엔 장고기능을 거진 사용을 안해봤으니 다음 프로젝트땐 장고기능을 사용해 봐야겠다.

---

### 매일의 기록


**[ 매일 기록 _ 진영 ]**

- 0602~3/ 알맞는 모델링 찾아보기
- 0607/ 추천시스템 방향성이 달라진 후 LSTM을 이용한 감성 분류 사용
- 0608/ 팀원분이 크롤링한 csv파일을 전처리 후 모델링
- 0609/ pickle을 이용해 가공한 데이터 저장
- 0610/ pycharm 내 실행을 위해 머신러닝 코드정리
- 0613/ calc 수정

---

**[ 매일 기록 _ 가현 ]**

- 0602/발제 후 회의 진행
- 0603/크롤링을 위한 파이썬 기본기 다지기
- 0607/네이버 지도 맛집 데이터 스크래핑 후 데이터 전처리
    
    (리뷰, 별점을 가져와서 라벨값 달고 csv파일로 만들기)
    
- 0608/카카오맵 맛집 데이터 가공작업
    
    (리뷰, 개인별점, 카카오맵으로 가는 가게url, 가게이름, 카테고리, 총 별점, 위치, 리뷰날짜를 가져와서 라벨값 달고 csv파일로 만들기)
    
- 0609/추상적인 레이아웃을 구체적으로 수정하기, 네이버 스크래핑 파일 수정 후 프론트앤드 도움
- 0610/각종 오류 디버깅 (전처리 된 파일 중 리뷰 공백인 부분 삭제), CSS 파일 수정
- 0613/프로젝트 마무리, Konlpy 환경설정 이슈 해결, JS로 사이트 카테고리 부분 제작
- 0614/발표자료 제작 및 발표 후 KPT 진행

---

**[ 매일 기록 _ 승태 ]**

- 0607/ai 모델링
- 0608/백엔드 작업 시작, jwt 시도
- 0609/회원가입, 로그인 구현
- 0610/메인페이지, 카테고리&유저 기분&검색 결과 페이지 구현
- 0613/모달페이지 구현

---

**[ 매일 기록 _ 민재 ]**

- 0606 django 복습, 각 페이지 django로 연결, 메인 페이지 제작
- 0607 로그인 페이지 제작
- 0608 회원 가입 페이지 제작
- 0609 결과 페이지 제작
- 0610 결과 페이지 수정
- 0613 모든 페이지 부족한 부분들 수정

---

### 시연 영상

**아래 이미지 클릭시 시연영상으로 이동합니다 😁**
[![클릭시 시연영상으로 이동](https://velog.velcdn.com/images/soyoyun/post/a8097334-73dc-41e2-ad5f-dbc0b0a760ff/image.png)](https://www.youtube.com/watch?v=0nFCMUi_nic&ab_channel=%EA%B9%80%EB%AF%BC%EC%9E%AC)

---
### [깃허브 링크](https://github.com/Reinforcement-succeeded/yogi_otte)

### [노션으로 보기](https://tangy-note.notion.site/274af6aae9cb4d729ec5ee7db0dce9ca)

