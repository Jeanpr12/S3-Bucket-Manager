# S3-Bucket-Manager


This Python script provides a command-line tool for managing AWS S3 buckets. It allows you to create, list, upload to, download from, and delete S3 buckets and their contents. Additionally, you can set bucket policies, enable versioning, and configure server-side encryption.

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.x** installed on your computer. You can download it from [python.org](https://www.python.org/).
2. **boto3** library installed. This is the AWS SDK for Python.
3. An **AWS account** with proper IAM permissions to manage S3 buckets.
4. Your **AWS credentials** (access key and secret key).

## Installation

### 1. Install Python

If you don't already have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

### 2. Install boto3

Install boto3 using pip:

```bash
pip install boto3
```

### 3. Clone or Download the Repository

Download or clone the repository containing this script:

```bash
git clone <repository-url>
cd <repository-directory>
```

Replace `<repository-url>` and `<repository-directory>` with the appropriate values.

## Configuration

Update the script with your AWS credentials and region. Modify the following section in the script:

```python
# Create a session with explicit credentials and region
session = boto3.Session(
    aws_access_key_id='YOUR_AWS_ACCESS_KEY_ID',
    aws_secret_access_key='YOUR_AWS_SECRET_ACCESS_KEY',
    region_name='us-east-2'  # Replace with your desired region
)
```

Replace `'YOUR_AWS_ACCESS_KEY_ID'` and `'YOUR_AWS_SECRET_ACCESS_KEY'` with your actual AWS credentials. Replace `'us-east-2'` with your preferred region if necessary.

## Running the Script

To run the script, navigate to the directory containing the script and execute the following command:

```bash
python s3_bucket_management_tool.py
```

The script will present you with a menu of options to manage your S3 buckets.

## Features

1. **Create a new S3 bucket**
2. **List S3 buckets**
3. **Upload a file to S3**
4. **Download a file from S3**
5. **List bucket contents**
6. **Delete a bucket**
7. **Delete bucket contents**
8. **Set bucket policy**
9. **Enable versioning**
10. **Set bucket encryption**
11. **Exit**

### Usage

1. **Create a new S3 bucket:**
   - Enter the bucket name and region when prompted.

2. **List S3 buckets:**
   - Displays a list of all your S3 buckets.

3. **Upload a file to S3:**
   - Enter the bucket name, file name (must be in the current directory), and an optional object name.

4. **Download a file from S3:**
   - Enter the bucket name, object name, and an optional file name for saving.

5. **List bucket contents:**
   - Enter the bucket name to list its contents.

6. **Delete a bucket:**
   - Enter the bucket name to delete it.

7. **Delete bucket contents:**
   - Enter the bucket name to delete all its contents.

8. **Set bucket policy:**
   - Enter the bucket name and the bucket policy JSON.

9. **Enable versioning:**
   - Enter the bucket name to enable versioning.

10. **Set bucket encryption:**
    - Enter the bucket name to enable server-side encryption.

11. **Exit:**
    - Exit the script.

