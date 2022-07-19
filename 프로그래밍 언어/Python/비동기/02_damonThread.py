# 필요 패키지 임포트(내장)
import logging
import threading
import time

# 스레드 실행 함수
def thread_func(name, d):
    logging.info("Sub-Thread %s: starting", name)
    for i in d:
        print(i)
        # if i % 1000 == 0:
        #     print(i)
    logging.info("Sub-Thread %s: finishing", name)


# 메인 영역 (메인 스레드)
if __name__ == "__main__": # 메인 영역을 만들어주는 문장
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")

    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('First', range(20000)), daemon=True)
    y = threading.Thread(target=thread_func, args=('Second', range(10000)), daemon=True)

    logging.info("Main-Thread: before running thread")

    # 서브 스레드 시작
    x.start()
    y.start()

    # Daemonthread인지 확인
    print(x.isDaemon())
    
    # x.join()
    # y.join()

    logging.info("Main-Thread: wait for the thread to finish")

    logging.info("Main-Thread: all done")