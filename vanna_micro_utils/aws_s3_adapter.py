import boto3, os
from botocore.exceptions import ClientError
import logging
from vanna_micro_utils.exceptions import FileUploadFailed

logger = logging.getLogger()


# TODO - Remove credentials locally and use env

class S3Adapter:
    def __init__(self):
        self.AWS_SERVER_PUBLIC_KEY = os.environ.get('AWS_S3_SERVER_PUBLIC_KEY')
        self.AWS_SERVER_SECRET_KEY = os.environ.get('AWS_S3_SERVER_SECRET_KEY')
        self.REGION_NAME = os.environ.get('AWS_S3_REGION')
        self.BUCKET_NAME = os.environ.get('AWS_S3_BUCKET_NAME')
        self.FOLDER_NAME = os.environ.get('AWS_S3_FOLDER_NAME')
        self.session = boto3.Session(
            aws_access_key_id=self.AWS_SERVER_PUBLIC_KEY,
            aws_secret_access_key=self.AWS_SERVER_SECRET_KEY,
        )
        self.s3_client = boto3.client('s3',
                                      aws_access_key_id=self.AWS_SERVER_PUBLIC_KEY,
                                      aws_secret_access_key=self.AWS_SERVER_SECRET_KEY,
                                      region_name=self.REGION_NAME
                                      )

    def create_bucket(self, bucket_name, region=None):
        """Create an S3 bucket in a specified region

        If a region is not specified, the bucket is created in the S3 default
        region (us-east-1).

        :param bucket_name: Bucket to create
        :param region: String region to create bucket in, e.g., 'us-west-2'
        :return: True if bucket created, else False
        """

        # Create bucket
        try:
            if region is None:
                s3_client = boto3.client('s3')
                s3_client.create_bucket(Bucket=bucket_name)
            else:
                s3_client = boto3.client('s3', region_name=region)
                location = {'LocationConstraint': region}
                s3_client.create_bucket(Bucket=bucket_name,
                                        CreateBucketConfiguration=location)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def list_buckets(self):
        print(self.s3_client.list_buckets())

    # TODO: Implement once upload is tested
    def delete_file(self):
        pass


    def upload_file(self, data_stream, destination_path, overwrite=False):
        try:
            self.s3_client.upload_fileobj(data_stream, self.BUCKET_NAME, destination_path,
                                          ExtraArgs={'Metadata': {'CacheControl': 'max-age=86400'}})

            logger.debug(f'Uploaded: {self.BUCKET_NAME}|{destination_path}|{self.REGION_NAME}|{overwrite}')
            return True
        except ClientError as e:
            raise FileUploadFailed(
                f"Upload to S3 failed: {self.BUCKET_NAME}|{destination_path}|{self.REGION_NAME}|{str(e)}")
        except Exception as e:
            raise FileUploadFailed(
                f"Upload to S3 failed: {self.BUCKET_NAME}|{destination_path}|{self.REGION_NAME}|{str(e)}")


if __name__ == '__main__':
    pass
