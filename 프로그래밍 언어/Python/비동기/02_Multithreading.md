# Multithreading



## 프로세스와 스레드의 차이

Key word : Process, Thread



1. 프로세스

- 운영체제에서 할당 받는 자원 단위(실행 중인 프로그램)

- CPU 동작 시간, 주소공간(메모리) 독립적이다.

- code, data, stack, heap -> 모두 독립적
- 최소 1개의 메인 스레드 보유
- 파이프, 파일, 소켓 등을 사용해서 프로세스간 통신이 가능
  - 잘 못 짜면 cost가 높아짐
  - context switching



2. 스레드

- 프로세스 내에 실행 흐름 단위
- 프로세스의 자원 사용
- Stack만 별도로 할당, 나머지는 공유(code, data, heap)
- 메모리 공유(변수 공유)
- 한 스레드의 결과가 다른 스레드에 영향 끼침
- 동기화 문제는 정말 주의 해야한다.(디버깅이 어려움)



3. 멀티 스레드

- 한 개의 단일 어플리케이션(응용프로그램) -> 여러 스레드로 구성 후 작업 처리
- 시스템 자원 소모 감소(효율성), 처리량 증가(cost 감소)
- 통신 부담 감소, 디버깅이 어려움, 단일 프로세스에는 효과 미약(하드웨어 성능이 뛰어나져서), 자원 공유 문제(교착 상태), 프로세스에 영향을 줄 수도 있음



4. 멀티 프로세스

- 한 개의 단일 어플리케이션(응용프로그램) -> 여러 프로세스로 구성 후 작업 처리
- 한 개의 프로세스 문제 발생은 확산 없음(프로세스 kill)
- 캐시 체인지, cost 비용이 매우 높음(오버헤드) -> 복잡한 통신 방식을 사용하기에



<font color="red">주의) 멀티 프로세스, 멀티 스레드로 짜든 코드 짜는 사람의 실력에 따라 안쓴것보다 성능이 안나올 수도 있음</font> 

많은 데이터를 한번에 빠르게 처리하려면 동시성 프로그램 필수!





## 파이썬 GIL이란?

Key word : CPython, 메모리 관리, GIL 사용 이유



Python GIL (Global Interpreter Lock)

- 작성한 파이썬 코드(.py)를 내부적으로 bytecode로 변환하고 CPython이 해석
- 이 때 여러 스레드를 사용할 경우 파이썬 인터프리터가 한 스레드만 하나의 바이트코드를 실행 시킬 수 있도록 lock을 해주는 것

- 하나의 스레드에 모든 자원을 허락하고 그 후에는 Lock을 걸어 다른 스레드는 실행할 수 없게 막아버리는 것

단일 스레드만이 python object에 접근 하게 제한하는 mutex



- CPython 메모리 관리가 취약하기 때문에 (즉, Thread-safe)

- 단일 스레드로도 충분히 빠르다.

- 멀티 프로세스를 사용하면 된다. (멀티 스레드 락의 단점을 보완가능, gil이 있어도 문제가 되지 않음)
  - numpy, scipy등 gil 외부 영역에서 효율적으로 코딩을 할 수 있게 해주는 라이브러리등이 많음
- 병렬 처리는 Multiprocessing, asyncio 등 선택지가 다양함
- thread 동시성 완벽 처리를 위해 -> Jython(파이썬 베이스 자바), IronPython, Stackless Python 등의 언어가 존재
  - 고성능 파이썬



한 프로세스 안에서는 단일 스레드만으로 제한하는 건가?



## Thread 기초

- 기초 thread 예제
- main thread & sub(child) thread



```python
# 필요 패키지 임포트(내장)
import logging
import threading
import time

# 스레드 실행 함수
def thread_func(name):
    logging.info("Sub-Thread %s: starting", name)
    time.sleep(3)
    logging.info("Sub-Thread %s: finishing", name)


# 메인 영역 (메인 스레드)
if __name__ == "__main__": # 메인 영역을 만들어주는 문장
    # logging format 설정
    format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")
    
    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('First',))
    
    logging.info("Main-Thread: before running thread")
    
    # 서브 스레드 시작
    x.start()
    
    # 주석 전후 결과 확인 : x.join()을 넣으면 서브 스레드가 종료될
    # 때 까지 메인 스레드에서 대기
    # x.join()
    
    logging.info("Main-Thread: wait for the thread to finish")
    
    logging.info("Main-Thread: all done")
```

```bash
10:53:22: Main-Thread: before creating thread
10:53:22: Main-Thread: before running thread
10:53:22: Sub-Thread First: starting
10:53:22: Main-Thread: wait for the thread to finish
10:53:22: Main-Thread: all done
10:53:25: Sub-Thread First: finishing
```

원래 대로면 순서대로 실행되니 `x.start()`가 끝나고 

10:53:22: Main-Thread: wait for the thread to finish
10:53:22: Main-Thread: all done

가 나와야 하는데 메인 스레드가 먼저 끝나고 서브 스레드는 할일 다하고 끝남

(메인 스레드가 종료된다해도 서브 스레드도 종료되는게 아님. 할일은 다하고 끝남)



## Daemon 스레드

- Daemon 스레드란?
- join의 개념



Daemon Thread란?

- 백그라운드에서 실행
- 메인스레드 종료시 즉시 종료
  - 위에 thread 기초에서 예제는 메인 스레드가 종료되도 서브 스레드는 끝까지 작업을 끝냈다. 데몬스레드는 메인 스레드 종료시 즉시 같이 종료
- 주로 백그라운드 무한 대기 이벤트 발생 실행하는 부분 담당
  - JVM(가비지컬렉션), 워드의 자동저장기능 등



```python
# 필요 패키지 임포트(내장)
import logging
import threading
import time

# 스레드 실행 함수
def thread_func(name, d):
    logging.info("Sub-Thread %s: starting", name)
    for i in d:
        if i % 1000 == 0:
            print(i)
    logging.info("Sub-Thread %s: finishing", name)


# 메인 영역 (메인 스레드)
if __name__ == "__main__": # 메인 영역을 만들어주는 문장
    # logging format 설정
    format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")
    
    # 함수 인자 확인 daemon 추가
    # Daemon : Default False
    x = threading.Thread(target=thread_func, args=('First', range(20000)), daemon=True)
    y = threading.Thread(target=thread_func, args=('Second', range(10000)), daemon=True)
    
    logging.info("Main-Thread: before running thread")
    
    # 서브 스레드 시작
    x.start()
    y.start()
    
    # Daemon Thread인지 확인 해주는 메소드
    print(x.isDaemon())
    
    # x.join()
    # y.join()
    
    logging.info("Main-Thread: wait for the thread to finish")
    
    logging.info("Main-Thread: all done")
```

```bash
Fatal Python error: _enter_buffered_busy: could not acquire lock for <_io.BufferedWriter name='<stdout>'> at interpreter shutdown, possibly due to daemon threads
Python runtime state: finalizing (tstate=0000018A98100E50)

Current thread 0x00000ff0 (most recent call first):
<no Python frame>
```

daemon thread때문에 interpreter가 shutdown된다.



daemon을 썼는데 join을 쓰는 경우.... 심히 고려해봐야할것 같다.



(while같은걸로 무한 루프 돌려놓고 이벤트가 들어오면 스레드를 실행하고 데몬같은걸로 종료시 같이 종료하도록 만들라고...?)













