# FastAPI S3 File Uploader/Downloader

This FastAPI project provides an API for uploading and downloading files to/from an AWS S3 bucket.

## Usage
This FastAPI project allows you to upload and download files to/from an AWS S3 bucket. Follow the instructions below to configure and use the project.
The "main.py" file is in charge of orchestrating the operation of the project, it reads the credentials form credentials.json and runs the FastAPI application using the uvicorn ASGI server

## AWS S3 Configuration:
Before running the application, make sure to provide your AWS S3 credentials in the credentials.json file. Fill in the following details in the 'credentials.json' file:

```json{
  "AWS_REGION": "your-aws-region",
  "AWS_ACCESS_KEY_ID": "your-access-key-id",
  "AWS_SECRET_ACCESS_KEY": "your-secret-access-key"
}
```

Replace your-aws-region, your-access-key-id, and your-secret-access-key with your actual AWS S3 credentials.


##Endpoints
Upload Endpoint:
/upload/: This endpoint allows you to upload a file to the specified AWS S3 bucket.

Download Endpoint:
/download/: This endpoint allows you to download a file from the specified AWS S3 bucket.


## Testing
Run the tests using the following command:
```bash
pytest
```

## Deployment
Follow these steps to deploy the FastAPI application.

``` bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Replace 0.0.0.0 and 8000 with your desired host and port.

