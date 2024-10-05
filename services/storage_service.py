import os

import boto3


class StorageService:
    def __init__(self):
        env = os.environ
        self.endpoint_url = env.get("S3_ENDPOINT_URL")
        self.s3_secret_access_key = env.get("S3_SECRET_KEY")
        self.s3_access_key_id = env.get("S3_SECRET_ID")
        self.s3_bucket = env.get("S3_BUCKET")

    def upload_backup(self):
        session = boto3.Session()
        s3 = session.client(
            service_name='s3',
            endpoint_url=self.endpoint_url,
            aws_secret_access_key=self.s3_secret_access_key,
            aws_access_key_id=self.s3_access_key_id,
        )
        file_name = "db_data.dump"
        s3.upload_file("dump.dump", self.s3_bucket, file_name)
