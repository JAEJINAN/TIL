# MVC 개발 패턴

Model, View, Controller

장고같은 경우 Controller만 Template로 변경된다.

명칭만 다르다. MVT 패턴



# Model

django와 database간의 통신을 하게 해주는 편리한 도구

유저 생성, 글 쓰기 객체를 database에 저장해야하는데 model이 이를 대신 해준다.

model을 생성하면 알아서 db에 저장해준다.



# View

django에서 계산하는 대부분의 작업을 해주는 곳

User와 서버간의 요청과 응답, 예를 들어

- check if authenticated
- check request valid
- collect data from db
- render response
- ....



# Template

HTML, CSS, JS의 Front와 직접적인 관련된 곳

User Interface의 내용을 어떻게 생성하는지를 담당 하는 곳



