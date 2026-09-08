
import json
import os
import requests

# Secrets에서 넘겨받을 ricekey 환경변수 읽기
SERVICE_KEY = os.environ.get("ricekey")

if not SERVICE_KEY:
    raise ValueError("ricekey가 설정되지 않았습니다.")


def fetch_auction_data(date_str):
    url = "https://apis.data.go.kr/B552845/katRealTime2/trades2"
    params = {
        "serviceKey": SERVICE_KEY,
        "returnType": "JSON",
        "cond[trd_clcln_ymd::EQ]": date_str,
        "pageNo": "1",
        "numOfRows": "1000",
    }

    response = requests.get(url, params=params)
    return response.json()


# 데이터 처리 및 history.json 업데이트 로직 추가 예시
# ...
