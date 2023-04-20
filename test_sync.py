import httpx
from time import time, sleep


def http_call_sync(url):
    sleep(1)
    r = httpx.get(url)
    return r


def test():
    start = time()
    response = []
    for _ in range(4):
        res = http_call_sync("http://127.0.0.1:8888/sync/")
        response.append(res)

    print(time() - start)


if __name__ == '__main__':
    test()