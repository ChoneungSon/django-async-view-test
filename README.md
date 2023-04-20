
- "https://weather.talkpython.fm/api/weather" 에서 cities 에 담긴 도시들의 날씨를 여러번의 요청으로 모아서 응답하는 엔드포인트 async 와 sync 가 존재

- `python3.8 -m venv venv` 을 이용해 가상환경을 세팅

- `source venv/bin/activate` 로 가상환경 활성화

- `pip install -r requirements.txt` 로 필요 라이브러리 설치

- `chmod a+x runserver.sh` 로 서버를 실행

- `python test_sync.py` 는 동기적으로 동작하는 엔드포인트에서 응답을 받아옵니다. 응답을 모두 받은 뒤에는 동작한 시간을 프린트 합니다.

- `python test_async.py` 는 비동기적으로 동작하는 엔드포인트에서 응답을 받아옵니다. 응답을 모두 받은 뒤에는 동작한 시간을 프린트 합니다.

- 결과를 확인해보면 sync 에서는 `time out`, async 에서는 약 3초의 시간이 걸리는 것을 확인할 수 있습니다.