# FastAPI

## 설치

fastapi와 서버 역할을 하는 uvicorn까지 한꺼번에 설치한다.

```
pip install fastapi[all]
```

따로 설치하려면

```
pip install fastapi

pip install uvicorn
```



## 첫걸음

```python
# main.py 파일
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hellow World"}
```

```python
# 런 서버
uvicorn main:app --reload
```

`uvicorn main:app` 명령은 다음을 의미한다

- `main`: 파일 `main.py` (파이썬 "모듈").
- `app`: `main.py` 내부의 `app = FastAPI()` 줄에서 생성한 오브젝트.
- `--reload`: 코드 변경 후 서버 재시작. 개발에만 사용.



다음 url로 접속해보자. 

자동 대화형 API 문서를 볼 수 있다.

```
http://127.0.0.1:8000/docs
```

대안 API 문서도 볼 수 있다.

```
http://127.0.0.1:8000/redoc
```



---

여긴 다시 보자.

### OpenAPI[¶](https://fastapi.tiangolo.com/ko/tutorial/first-steps/#openapi)

**FastAPI**는 API를 정의하기 위한 **OpenAPI** 표준을 사용하여 여러분의 모든 API를 이용해 "스키마"를 생성합니다.

#### "스키마"[¶](https://fastapi.tiangolo.com/ko/tutorial/first-steps/#_3)

"스키마"는 무언가의 정의 또는 설명입니다. 이를 구현하는 코드가 아니라 추상적인 설명일 뿐입니다.

#### API "스키마"[¶](https://fastapi.tiangolo.com/ko/tutorial/first-steps/#api_2)

이 경우, [OpenAPI](https://github.com/OAI/OpenAPI-Specification)는 API의 스키마를 어떻게 정의하는지 지시하는 규격입니다.

이 스키마 정의는 API 경로, 가능한 매개변수 등을 포함합니다.

#### 데이터 "스키마"[¶](https://fastapi.tiangolo.com/ko/tutorial/first-steps/#_4)

"스키마"라는 용어는 JSON처럼 어떤 데이터의 형태를 나타낼 수도 있습니다.

이러한 경우 JSON 속성, 가지고 있는 데이터 타입 등을 뜻합니다.

#### OpenAPI와 JSON 스키마[¶](https://fastapi.tiangolo.com/ko/tutorial/first-steps/#openapi-json)

OpenAPI는 API에 대한 API 스키마를 정의합니다. 또한 이 스키마에는 JSON 데이터 스키마의 표준인 **JSON 스키마**를 사용하여 API에서 보내고 받은 데이터의 정의(또는 "스키마")를 포함합니다.

#### `openapi.json` 확인[¶](https://fastapi.tiangolo.com/ko/tutorial/first-steps/#openapijson)

가공되지 않은 OpenAPI 스키마가 어떻게 생겼는지 궁금하다면, FastAPI는 자동으로 API의 설명과 함께 JSON (스키마)를 생성합니다.

여기에서 직접 볼 수 있습니다: http://127.0.0.1:8000/openapi.json.

다음과 같이 시작하는 JSON을 확인할 수 있습니다:





---















