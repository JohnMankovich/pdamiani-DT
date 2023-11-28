import requests
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_upload_endpoint():
    bucket = 'pre-pricing-mkt'
    object_name = 'test.txt'
    with open ('test.txt','r') as f:
        file_content = f.read()

    with requests.Session() as session:
        with session.post(
            f'http://127.0.0.1:8000/upload/?bucket={bucket}&object_name={object_name}',
            files={'file': ('test.txt', file_content)}
        ) as response:
            assert response.status_code == 200
            assert response.json() == {'message': 'File uploaded successfully'}




def test_download_endpoint():
    bucket = 'pre-pricing-mkt'
    object_name = 'test.txt'

    with requests.Session() as session:
        with session.get(f'http://127.0.0.1:8000/download/?bucket={bucket}&object_name={object_name}'
            ) as response:
            assert response.status_code == 200
            assert response.json() == {'message': 'File downloaded successfully'}



