import json
from fastapi import FastAPI, UploadFile
from fastapi.responses import RedirectResponse
import boto3
from botocore.exceptions import NoCredentialsError


#Get credentials
with open('credentials.json','r') as f:
    credentials = json.load(f)


# AWS S3 configurations
AWS_REGION = credentials['AWS_REGION']
AWS_ACCESS_KEY_ID = credentials['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = credentials['AWS_SECRET_ACCESS_KEY']

# Initialize S3 client
s3 = boto3.client('s3', region_name =  AWS_REGION, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


@app.post('/upload/')
async def upload_file(bucket: str, object_name: str, file: UploadFile):
    try: 
        s3.upload_fileobj(file.file, bucket, object_name)
        return {'message': 'File uploaded successfully'}
    except NoCredentialsError:
        return {'error': 'Credentials not available'}
    except Exception as e:
        return {'error': e}


@app.get('/download/')
async def download_file(bucket: str, object_name: str):
    try:
        s3.download_file(bucket, object_name, object_name)
        return {'message': 'File downloaded successfully'}
    except NoCredentialsError:
        return {'error': 'Credentials not available'}
    except Exception as e:
        return {'error': e}
    


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)