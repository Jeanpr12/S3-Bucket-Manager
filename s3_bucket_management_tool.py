import boto3
import os

# Create a session with explicit credentials and region
session = boto3.Session(
    aws_access_key_id='Access_key',
    aws_secret_access_key='secret_key',
    region_name='us-east-2'
)

def create_bucket(bucket_name, region='us-east-2'):
    s3 = session.client('s3', region_name=region)
    if region == 'us-east-1':
        s3.create_bucket(Bucket=bucket_name)
    else:
        s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
    print(f'Bucket {bucket_name} created successfully')

def list_buckets():
    s3 = session.client('s3')
    response = s3.list_buckets()
    if len(response['Buckets']) == 0:
        print('No buckets listed')
    else:
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')

def upload_file(bucket_name, file_name, object_name=None):
    s3 = session.client('s3')
    if object_name is None:
        object_name = file_name
    print(f'Uploading {file_name} to bucket {bucket_name} as {object_name}')
    print(f'Current working directory: {os.getcwd()}')
    if not os.path.isfile(file_name):
        print(f'Error: The file {file_name} does not exist in the current directory.')
        return
    s3.upload_file(file_name, bucket_name, object_name)
    print(f'File {file_name} uploaded to bucket {bucket_name}')

def download_file(bucket_name, object_name, file_name=None):
    s3 = session.client('s3')
    if file_name is None:
        file_name = object_name
    s3.download_file(bucket_name, object_name, file_name)
    print(f'File {object_name} downloaded from bucket {bucket_name} to {file_name}')

def list_bucket_contents(bucket_name):
    s3 = session.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            print(f'  {obj["Key"]}')
    else:
        print(f'Bucket {bucket_name} is empty')

def delete_bucket(bucket_name):
    s3 = session.client('s3')
    s3.delete_bucket(Bucket=bucket_name)
    print(f'Bucket {bucket_name} deleted')

def delete_bucket_contents(bucket_name):
    s3 = session.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
            print(f'Deleted {obj["Key"]} from bucket {bucket_name}')
    else:
        print(f'Bucket {bucket_name} is already empty')

def set_bucket_policy(bucket_name, policy):
    s3 = session.client('s3')
    s3.put_bucket_policy(Bucket=bucket_name, Policy=policy)
    print(f'Policy set for bucket {bucket_name}')

def enable_versioning(bucket_name):
    s3 = session.client('s3')
    versioning = s3.put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={
            'Status': 'Enabled'
        }
    )
    print(f'Versioning enabled for bucket {bucket_name}')

def set_bucket_encryption(bucket_name):
    s3 = session.client('s3')
    encryption = s3.put_bucket_encryption(
        Bucket=bucket_name,
        ServerSideEncryptionConfiguration={
            'Rules': [
                {
                    'ApplyServerSideEncryptionByDefault': {
                        'SSEAlgorithm': 'AES256'
                    }
                }
            ]
        }
    )
    print(f'Server-side encryption enabled for bucket {bucket_name}')

def main():
    while True:
        print("\nS3 Bucket Management Tool")
        print("1. Create a new S3 bucket")
        print("2. List S3 buckets")
        print("3. Upload a file to S3")
        print("4. Download a file from S3")
        print("5. List bucket contents")
        print("6. Delete a bucket")
        print("7. Delete bucket contents")
        print("8. Set bucket policy")
        print("9. Enable versioning")
        print("10. Set bucket encryption")
        print("11. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            bucket_name = input("Enter bucket name: ")
            region = input("Enter region (default: us-east-2): ")
            if region == '':
                region = 'us-east-2'
            create_bucket(bucket_name, region)
        elif choice == '2':
            list_buckets()
        elif choice == '3':
            bucket_name = input("Enter bucket name: ")
            file_name = input("Enter file name to upload (must be in the current directory): ")
            object_name = input("Enter object name (optional): ")
            if object_name == '':
                object_name = None
            upload_file(bucket_name, file_name, object_name)
        elif choice == '4':
            bucket_name = input("Enter bucket name: ")
            object_name = input("Enter object name to download: ")
            file_name = input("Enter file name (optional): ")
            if file_name == '':
                file_name = None
            download_file(bucket_name, object_name, file_name)
        elif choice == '5':
            bucket_name = input("Enter bucket name: ")
            list_bucket_contents(bucket_name)
        elif choice == '6':
            bucket_name = input("Enter bucket name to delete: ")
            delete_bucket(bucket_name)
        elif choice == '7':
            bucket_name = input("Enter bucket name to delete contents from: ")
            delete_bucket_contents(bucket_name)
        elif choice == '8':
            bucket_name = input("Enter bucket name: ")
            policy = input("Enter bucket policy JSON: ")
            set_bucket_policy(bucket_name, policy)
        elif choice == '9':
            bucket_name = input("Enter bucket name: ")
            enable_versioning(bucket_name)
        elif choice == '10':
            bucket_name = input("Enter bucket name: ")
            set_bucket_encryption(bucket_name)
        elif choice == '11':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
