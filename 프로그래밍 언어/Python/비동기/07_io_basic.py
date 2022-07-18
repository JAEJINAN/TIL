import requests  # 동기 패키지다.
import time
import os
import threading


def fetcher(session, url):
    print(f'{os.getpid()} process | {threading.get_ident()} url : {url}')
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://google.com", 'https://apple.com'] * 50
    # session = requests.Session()
    # session.get(url)
    # session.close()
    # 위의 3줄과 같은 내용
    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start)  # 동기로 했을 때 12초 정도 나옴
