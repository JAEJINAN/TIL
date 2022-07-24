# GraphQL이란?

A query language for your API



Part 1. 이론 위주

- GraphQL vs REST API



Part 2. 실습







---

## API란?

Application Programming Interface

API는 rest나 graphql api만을 의미하는 것은 아님. web api, browser api 등등도 있기에

interface : 무언가와 상호작용할 수 있게 해주는 면

예) 리모컨 : 사용자와 TV와 상호작용할 수 있게 해주는 것. 버튼을 누르면 작동



## REST api

의사소통을 위해 필요

어플리케이션과 서버가 통신하는 방법은 서버에 존재하는 버튼(api)을 누르는 것

rest api와 graphql api의 차이점은 이 버튼들이 어떻게 노출되어있는지에 차이가 있다. 해당 api에 어떻게 접근하는지, 서버와 어떻게 소통하는지.



rest는 url로 통신

- 작업이 간단, 이해하기 쉬움
- 전세계 거의 모든 디바이스들에 url로 요청을 보낼 수 있음
- json형태의 파일을 주고 받음. 이를 이용해 어떻게 꾸며서 보여줄지는 개발자에 달려있음

```js
nomadmovies.co/api/movies
nomadmovies.co/api/movies/1
nomadmovies.co/api/serach?rating=9
```

- 보통 rest는 컨벤션같은게 있어서 이해하기 쉬움 (명사는 복수형으로...)





REST API에 이제 HTTP method를 넣어서 통신할 수 있다.

GET, POST, DELETE ... 등



## GraphQL api

graphql은 왜 만들어졌을까? 무엇을 위해서?

2012년부터 페이스북 앱이 써왔음. 2015년에 graphql specification이 오픈소스화 되었다. 이 spec을 보고 누군가 js로 구현해놨음



REST API는 크게 2가지 문제점을 가지고 있다. 이를 해결하기 위해 graphql을 도입



- Over-fetching
  - api 요청을 해서 json을 받아오는데 사용자가 쓰든 말든 너무 많은 데이터를 가져옴
  - 필요이상의 데이터를 불러옴
  - 이는 내 backend나 database가 필요 이상의 일을 더 해야 한다는 것
  - data전송이 느려질 수도 있다.

-> graphql은 그냥 데이터를 요청하는게 아니라 **필요한 데이터**를 요청함

rest는 일단 url에 필요한 json파일을 요청함(json내에 어떤 데이터만 요청할수는 없음), graphql은 필요한것만 요청함



- Under-fetching

  - 우리가 필요한 것보다 덜 받는 것
  - over-fetching으로 받아온 json에서 또 필요한 데이터가 있으면 그 데이터의 정보에 대한 다른 url을 또 보내 받아야함
  - 내가 이해한 바론, 외래키참조 같은 문제가 발생할 거 같음.

  ```
  # 가수 정보를 받아옴
  GET web_page.co.kr/singers
  GET web_page.co.kr/singers/categories?value=10&value=15 <- 이런식인가
  
  # 가수들의 정보가 포함 (예)
  results: [
  {
  	이름 : 가수1
  	데뷔날 : 20xx-xx-xx
  	가수카테고리 : [
  		10,
  		15,
  	]
  	앨범 : [
  		1집: {
  			이름 : @@@@
  		}
  	]
  }
  ...
  ]
  ```

  (대충 만들어본 정보인데 그냥 보자.)

  가수 카테고리에 10, 15라는 숫자가 있다. 그냥 예를 들어보는건데 아이돌가수,  팝가수를 의미하는게 10, 15라고 하자.

  근데 데이터(json)에는 위의 정보가 없다. 즉, 아이돌, 팝을 불러오기 위해선 다른 json에 url을 날려 10, 15를 보내 query를 해야한다. 이게 바로 under-fetcing

  필요로 하는 데이터가 부족함



좀더 복잡해지면 request를 2번 뿐만아니라 3번 , 4번 이상을 보내야하는 불상사가... 이능 바로 성능문제로...(시간지연, 실패 위험 증가)



그렇기에 graphql은 한번의 request로 많은 resource들을 받을 수 있게 만들었음