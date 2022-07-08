# TFX - Tensorflow Extended



> 아파치 빔
>
> - 데이터 유효성 검사, 데이터 전처리같은 처리 단계를 TFX 컴포넌트 내부에서 수행
> - 파이프라인 오케스트레이터로 사용
> - 사용자 지정 컴포넌트를 작성하기 위해 필요



## TFX

파이프라인은 분산 처리가 필요 (TFX는 아파치 빔을 활용), 대규모 시스템이서 중요



TFX를 사용한 일반적인 파이프라인 아키텍처

<img src="C:\Users\jay\Desktop\code\DE\pipeline구축\살아움직이는 머신러닝 파이프라인 설계\1-2.PNG" alt="1-2" style="zoom:100%;" align="Left"/>

파이프라인 오케스트레이션 툴은 작업을 실행하는 기반

중간 파이프라인 결과를 추적하는 데이터 저장소도 필요

개발 컴포넌트는 데이터 저장소에서 필요한 입력 데이터를 가져와서 작업하고, 그 결과물을 다시 데이터 저장소에 저장

저장된 결과물은 다음 작업의 입력 데이터로 사용됨

TFX는 이런 모든 도구를 결합하는 계층을 제공, 또한 주요 파이프라인 작업에 대한 개별 구성 요소를 제공



### TFX 제공 컴포넌트

- ExampleGen : 데이터 수집
- StatisticsGen, SchemaGen, ExampleValidator : 데이터 검증
- Transform : 데이터 전처리
- Trainer : 모델 학습 실시
- ResolverNode : 이전에 학습한 모델 확인
- Evaluator : 모델 분석 및 ㄱ머증
- Pusher : 모델 배포

<img src="C:\Users\jay\Desktop\code\DE\pipeline구축\살아움직이는 머신러닝 파이프라인 설계\2-1.PNG" alt="2-1" style="zoom:100%;" align="Left"/>





### TFX 설치

```bash
pip install tfx==1.2.0
```

설치 후 `import`를 통해 개별 파이썬 패키지처럼 쓸 수 있다.

예시)

```python
import tensorflow_data_validation as tfdv
import tensorflow_transform as tft
import tensorflow_transform.beam as tft_beam
# ...
```

가져온 라이브러리 내 컴포넌트를 아래와 같이 불러와 쓰면된다.

```python
from tfx.components import ExampleValidator
from tfx.components import Evaluator
from tfx.components import Transform
# ...
```



### TFX 컴포넌트 개요

컴포넌트는 단일 태스크의 실행보다 더 복잡한 프로세스를 처리한다.

모든 머신러닝 파이프라인 컴포넌트는 메타데이터 스토어에서 입력 아티팩트를 가져온다.

그리고 메타데이터스토어에서 제공한 경로에서 데이터가 로드되고 처리된다.

컴포넌트의 출력인 처리된 데이터가 다음 파이프라인 컴포넌트에 제공된다.



컴포넌트의 내부에서는 다음과 같은 작업이 처리된다.

- 입력 수신
- 작업 수행
- 최종 결과 저장



컴포넌트 내부 = 드라이버(driver) + 실행자(executor) + 배포자(publisher)

- 드라이버 : 메타데이터스토어에서 입력 데이터를 가져오는 역할

- 실행자 : 컴포넌트의 작업을 수행

- 배포자 : 최종 결과의 메타데이터를 메타데이터스토어에 저장, 관리

> 드라이버와 배포자는 데이터를 이동시키지 않는다. 메타데이터스토어에서 데이터의 주소를 읽고 쓰는 역할

<img src="C:\Users\jay\Desktop\code\DE\pipeline구축\살아움직이는 머신러닝 파이프라인 설계\2-2.PNG" alt="2-2" style="zoom:100%;" align="Left"/>

아티팩트란? -- 컴포넌트의 입력 및 출력

- 원시 입력 데이터, 전처리된 데이터, 학습된 모델 등
- 각각 아티팩트는 메타데이터스토어에 저장된 메타데이터와 연결된다.
  - 아티팩트 메타데이터는 아티팩트 유형과 아티팩트 속성으로 구성된다.
  - 아티팩트 설정을 통해 컴포넌트가 데이터를 효과적으로 교환할 수 있다.



### ML 메타데이터

TFX 컴포넌트는 메타데이터로 소통한다. 직접 아티팩트를 주고받지 않고 아티팩트에 대한 참조를 주고 받는다.

컴포넌트가 아티팩르르 주고 받는 대신 메타데이터를 사용하면 모든 정보를 한 곳에 저장, 관리 할 수 있다.

컴포넌트 실행시 MLMD (Machine Learning MetaData) 라이브러리 API를 통해 메타데이터를 저장.

MLMD는 메타데이터를 메타데이터스토어에 지속적으로 저장한다.

메타데이터스토어와 스토리지 백엔드를 MLMD가 연결을 해서 참조하는 것. (계속 메타데이터 저장)
지원 스토리지 백엔드(RDBMS)는

- SQLite를 이용한 메모리 내 DB (In-memory인가???)
- SQLite
- MySQL



각 컴포넌트가 메타데이터스토어와 상호작용, 메타데이터스토어는 제공된 데이터베이스 백엔드에 메타데이터를 저장하는 모습 (MLMD를 사용한 메타데이터 저장하는 모습)

<img src="C:\Users\jay\Desktop\code\DE\pipeline구축\살아움직이는 머신러닝 파이프라인 설계\2-3.PNG" alt="2-3" style="zoom:100%;" align="Left"/>





### 대화형 파이프라인

파이프라인은 주피터 노트북에서 실행되며, 구성 요소의 아티팩트를 즉시 컴토할 수 있다.



- 예시) ExampleGen -> StatisticsGen

```python
import tfx
import tensorflow as tf
from tfx.orchestration.experimental.interactive.interactive_context import \ InteractiveContext
```

컨텍스트 객체는 컴포넌트 실행을 처리하고 컴포넌트의 아티팩트를 표시한다.

```python
context = InteractiveContext()
```



파이프라인 컴포넌트를 설정한 후 컨텍스트 객체의 `run` 함수로 각 컴포넌트 개체를 실행할 수 있다. (예 : StatisticsGen)

```python
from tfx.components import StatisticsGen

statistics_gen = StatisticsGen(examples=example_gen.outputs['examples'])
context.run(statistics_gen)
```

컴포넌트 자체는 생성자의 매개변수로 이전 컴포넌트의 출력을 수신한다.

컴포넌트의 태스크를 실행한 후, 컴포넌트는 출력 아티팩트의 메타데이터를 메타데이터스토어에 자동으로 기록한다.

일부 컴포넌트 출력은 노트북에 표시될 수 있다. 결과를 즉시 확인하고, 바로 시각화할 수 있어 매우 편리하다.





(추가)







## 아파치 빔

다양한 TFX 컴포넌트와 라이브러리는 아파치 빔을 사용하여 파이프라인 데이터를 효율적으로 처리한다.

아파치 빔은 다양한 환경에서 실행할 수 있는 데이터 처리 단계를 설명하는 오픈 소스 방식을 제공

- 배치 프로세싱

- 스트리밍 작업

- 데이터 파이프라인 설명

데이터 처리 과정을 추상화하며 여러 분산 처리 런타임 환경에서 실행될 수 있다.
(Spark, Google Cloud Dataflow에서 동일한 데이터 파이프라인 실행할 수 있다.)



### 설치

```bash
pip install apache-beam

// GCP에서 쓰려면
pip install 'apache-beam[gcp]'

// AWS에서 쓰려면
pip install 'apache-beam[boto]'
```



### 기본 데이터 파이프라인

아파치 빔의 추상화는 컬렉션과 변환이라는 두 가지 개념을 기반으로 함

- 컬렉션
  - 지정된 파일 또는 스트림에서 데이터를 읽거나 쓰는 작업을 설명
- 변환
  - 데이터를 조작하는 방법을 설명

컬렉션과 변환은 파이프라인 컨텍스트에서 실행된다. (context manager 명령을 통해 파이썬으로 표시됨)



#### 기본 컬렉션 예제

데이터 파이프라인은 대게 데이터를 읽거나 쓰며 시작하고 끝난다.

D.P는 보통 PCollections라는 컬렉션을 통해 beam에서 처리된다. 그 다음, 컬렉션을 변환하고 최종 결과는 다시 컬렉션으로 표현되어 파일 시스템에 기록할 수 있다.



txt file을 읽고 모든 행을 반환하는 명령

```python
import apache_beamn as beam

# 컨텍스트 관리자를 사용하여 파이프라인을 정의
with beam.Pipeline() as p:
    lines = p | beam.io.ReadFromText(input_file)
    # 텍스트를 PCollection(PCollection)으로 읽는다.
```







