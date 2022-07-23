데이터베이스 생성

```mysql
CREATE DATABASE copang_main;
```



> sys라는 데이터베이스
>
> - MySQL 서버의 성능 관련 정보를 갖고 있는 데이터베이스
> - 백엔드, DBA : 데이터가 빠르고 안정적으로, 조회 및 저장될 수 있도록 개발 및 관리



테이블 생성

- SQL문으로 생성

- csv 파일 임포트해서 테이블 만들기

  



Primary key

테이블에서 하나의 row를 고유하게 식별할 수 있도록 해주는 column

primary key에는 2가지 종류가 있음

- Natural Key
  - 어떤 개체가 갖고 있는 속성을 나타내는 컬럼이 primary key가 되었을 때 natural key라 함.
  - 주민번호, ISBN 등
- Surrogate Key
  - 어떤 개체를 나타내는 직접적인 컬럼이 아님
  - pk로 쓰기 위해 인위적으로 생성한 컬럼
  - id
  - 보통 1부터 시작해 1씩 증가하는 정수값을 가짐

뭐가 더 좋고 나쁘고는 상황에 맞게 판단해야함. 보통 surrogate key를 씀. (natural key는 만약 값 변경이 생기면 다 수정해줘야하기때문에)



NN : Not Null (반드시 값이 존재해야함)

Null : 값이 존재하지 않는 상태

Null은 0, '' 이 아님(0, 빈문자열 자체가 값임)



MySQL에서 데이터 타입에 들어가 AI (Auto Increment)를 활성화 해주면 자동으로 row가 생길 때마다 id값에 1씩 더해 자동으로 pk를 채워줌
그래서, row만들때 id값을 지정안해줘도 됨(알아서 만듦)







### BETWEEN A AND B

30대만 조회

```mysql
SELECT * FROM member WHERE age BETWEEN 30 AND 39;
```

30대 제외

```mysql
SELECT * FROM member WHERE age NOT BETWEEN 30 AND 39;
```



2019년1월1일 이후로 가입한 사람

```mysql
SELECT * FROM member WHERE sign_up_day > '2019-01-01';
```



기간 사이 조회

```mysql
SELECT * FROM member WHERE sign_up_day BETWEEN '2018-01-01' AND '2018-12-31'
```









