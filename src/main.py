# fastapi 모듈에서 FastAPI 클래스를 가져옵니다.
from fastapi import FastAPI

# FastAPI 클래스의 인스턴스를 선언합니다.
app = FastAPI()

# app 인스턴스를 데코레이터로 사용하여 HTTP 경로 및 HTTP 메서드를 처리합니다.
@app.get("/")
def read_index():
    """JSON 직렬화를 지원하는 Python Dictionary를 반환합니다."""
    return {"Hello": "World"}
