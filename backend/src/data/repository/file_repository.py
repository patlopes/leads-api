from data.clients.minio_client import MinioClient

class FileRepository:

    def __init__(self):
        self.minio = MinioClient()

    def upload_file(self, file):
        self.minio.upload_file(file)

    def download_file(self, file_name):
        return self.minio.download_file(file_name)

    def delete_file(self, file_name):
        self.minio.delete_file(file_name)

    def get_presigned_url(self, file_name):
        return self.minio.get_file_url(file_name, expireDays=1)