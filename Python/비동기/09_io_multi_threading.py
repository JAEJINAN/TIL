import requests  # 동기 패키지다.
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor  # 동기에 비동기를 쓸수 있게 해주는 패키지


def fetcher(params):
    print(params)
    session = params[0]
    url = params[1]
    print(f'{os.getpid()} process | {threading.get_ident()} url : {url}')
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://google.com", 'https://apple.com'] * 50
    executor = ThreadPoolExecutor(max_workers=10)  # 1이면 싱글스레드
    with requests.Session() as session:
        # result = [fetcher(session, url) for url in urls]
        # print(result)
        params = [(session, url) for url in urls]
        result = list(executor.map(fetcher, params))
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start)  # 동기로 했을 때 12초 정도 나옴
