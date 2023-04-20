import httpx
import asyncio
from time import time


async def http_call_async(url):
    async with httpx.AsyncClient() as client:
        await asyncio.sleep(1)
        r = await client.get(url)
        print(r.content)


async def test():
    start = time()
    tasks = []
    for _ in range(4):
        res = http_call_async("http://127.0.0.1:8888/async/")
        tasks.append(res)

    await asyncio.gather(*tasks)
    print(time() - start)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())