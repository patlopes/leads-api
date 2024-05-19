from fastapi import HTTPException, UploadFile, status
from minio import Minio
from infrastructure.config import Config
from os import fstat
from datetime import timedelta


class MinioClient:

    def __init__(self):
        self.config = Config()
        self.client = Minio(
            endpoint=self.config.API_MINIO_HOST,
            access_key=self.config.MINIO_ROOT_USER,
            secret_key=self.config.MINIO_ROOT_PASSWORD,
            secure=self.config.MINIO_SECURE
            
        )
        self.bucket = self.config.MINIO_BUCKET

    def upload_file(self, file: UploadFile):
        try:
            self.client.put_object(
                bucket_name=self.bucket,
                object_name=file.filename,
                data=file.file,
                length=self._file_size(file)
            )
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    def download_file(self, file_name: str):
        try:
            response = self.client.get_object(self.bucket, file_name)
            return response.read()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        

    def get_file_url(self, file_name: str, expireDays: int) -> str:
        try:
            return self.client.get_presigned_url(
                method='GET',
                bucket_name=self.bucket,
                object_name=file_name,
                expires=timedelta(days=expireDays)
            )
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    def delete_file(self, file_name: str):
        try:
            self.client.remove_object(self.bucket, file_name)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    def _file_size(self, file: UploadFile) -> int:
        return fstat(file.file.fileno()).st_size