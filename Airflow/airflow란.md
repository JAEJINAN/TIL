# Apache Airflow

에어비앤비에서 개발한 워크플로우 스케줄링, 모니터링 플랫폼

(실제로 데이터 처리가 일어나는 곳은 아니다.)



## 언제 쓰일까?

회사들의 공통적인 문제 - 워크플로우 관리 문제

<u>만약 10시에 주기적으로 돌아가는 데이터 파이프라인을 만들려면?</u>

한 가지의 플로우만 있다면 단순히 CRON Script를 작성해서 관리를 하면된다. (기존)

기존 방식의 문제점

- 실패 복구 : 언제 어떻게 다시 실행할 것인가? Backfill?
- 모니터링 : 잘 돌아가고 있는지, 어떤지 확인하기 힘들다.
- 의존성 관리 : 데이터 파이프라인간 의존성이 있는 경우 상위 데이터 파이프라인이 잘 돌아가고 있는지 파악하기 힘들다.
- 확장성 : 중앙화 해서 관리하는 툴이 없기 때문에 분산된 환경에서 파이프라인들을 관리하기 힘들다.
- 배포 : 새로운 워크플로우를 배포하기 힘들다.

 

위의 파이프라인이 수십개, 수백개가 있다면?

각각 파이프라인에서 문제가 터지면 어떤곳에서 어떻게??

그렇기에 Airflow가 개발됨.

Airflow는 워크플로우를 작성하고 스케줄링하고 모니터링 하는 작업을 프로그래밍 할 수 있게 해주는 플랫폼

- 파이썬으로 되어있어 프래그래밍에 용이
- 분산된 환경에서 확장성이 있음
- 웹 대시보드 (UI)
- 커스터마이징이 가능



## 워크플로우란

- 의존성으로 연결된 작업(task)들의 집합

- DAG (Directed Acyclic Graph)

  방향성이 있고 순환하지 않는 그래프



## Airflow components

- 웹 서버 : 웹 대시보드 UI
- 스케줄러 : 워크플로우가 언제 실행되는지 관리
- Metastore : 메타데이터 관리
- Executor : 테스크가 어떻게 실행되는지 정의
- Worker : 테스크를 실행하는 프로세스



## Operator

하나의 작업(task)를 정의하는 사용

- Action Operators : 실제 연산을 수행
- Transfer Operators : 데이터를 옮김
- Sensor Operators : 테스크를 언제 실행시킬 트리거를 기다림



## Task

Operator를 실행하면 Task가 된다.

즉, `Task = Operator Instance`



## 쓰이는 곳

여러 데이터 엔지니어링 환경에서 유용하게 쓰일 수 있다.

- 데이터 웨어하우스
- 머신러닝
- 분석
- 실험
- 데이터 인프라 관리





# Airflow Structure

에어플로의 작동 방식, 즉 에어플로우 구조에 대해 알아보자.



## One Node Architecture

가장 간단한 아키텍처



- 구성
  - Web Server
  - Scheduler
  - Metastore
  - Executor (Queue가 존재해 task 순서 결정 가능)

<img src="C:\Users\jay\Desktop\code\DE\apache-airflow-work-200422.png" alt="apache-airflow-work-200422" style="zoom:80%;" />

Celery Broker (Queue)
Metastore (Database)

Master노드에서 스케줄러와 익스큐터가 celery broker로 작업을 보내고 각 워커노드들이 가져가서 작업을 하고 다시 마스터 노드로 가서 작업에 대해 보고함.



## 동작 방식

1. DAG를 작성하여 Workflow를 만든다. DAG는  Task로 구성되어 있다.
2. Task는 operator가 인스턴스화 된 것
3. DAG를 실행시킬 때 Scheduler는 DagRun 오브젝트를 만든다.
4. DagRun 오브젝트는 Task Instance를 만든다.
5. Worker가 Task를 수행 후 DagRun의 상태를 "완료"로 바꿔놓는다.





