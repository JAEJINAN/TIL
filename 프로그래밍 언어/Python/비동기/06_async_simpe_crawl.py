import time
import asyncio
import aiohttp
import sys


async def fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10

    async with aiohttp.ClientSession() as session:
        # unpacking에 대해서 좀 공부하자.
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        # result = await fetcher(session, urls[0])
        print(result)
        # result = [fetcher(session, url) for url in urls]
        # print(result)


if __name__ == "__main__":
    py_ver = int(f"{sys.version_info.major}{sys.version_info.minor}")
    if py_ver > 37 and sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # window python 3.8+ 에서 aiohttp에러가남
    # 위에 코드가 해결방법 중 하나
    # https://gmyankee.tistory.com/330
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end-start)  # 비동기로 했을 때 5.7초 정도 나옴
