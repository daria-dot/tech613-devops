# Managing AWS S3 with Python boto3
 
## What is boto3?
boto3 is the official AWS SDK for Python. It lets Python code create, configure and manage AWS services such as S3, EC2 and IAM, doing in code what the AWS CLI does on the command line.
 
## Prerequisites
- An EC2 Ubuntu instance
- AWS CLI installed and authenticated with `aws configure`
- Python 3 with boto3 installed in a virtual environment
```bash
sudo apt update
sudo apt install -y python3-pip python3-venv
python3 -m venv ~/venv
source ~/venv/bin/activate
pip install boto3
python3 -c "import boto3; print(boto3.__version__)"
```
 
## How boto3 authenticates
boto3 needs no keys in the code. It looks for credentials automatically in this order (simplified):
1. Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
2. The `~/.aws/credentials` and `~/.aws/config` files created by `aws configure`
3. An IAM role attached to the EC2 instance
Because `aws configure` was run, the scripts simply use those saved credentials and the default region.
 
## Core concepts
- **Client**: `boto3.client("s3")` creates a low-level connection to S3. Every action is a method on the client.
- **Bucket**: a container for files. Names are globally unique across all AWS accounts.
- **Object**: a file stored in a bucket.
- **Key**: the object's name/path inside the bucket (e.g. `hello.txt` or `folder/hello.txt`).
- **Response**: most methods return a Python dictionary with the result.
## The scripts
 
### 1. List all buckets — `1_list_buckets.py`
```python
import boto3
 
s3 = boto3.client("s3")
 
response = s3.list_buckets()
 
for bucket in response["Buckets"]:
    print(bucket["Name"])
```
`list_buckets()` returns a dictionary; its `"Buckets"` entry is a list of buckets. The loop prints each bucket's name.
 
### 2. Create a bucket — `2_create_bucket.py`
```python
import boto3
 
s3 = boto3.client("s3", region_name="us-east-1")
 
s3.create_bucket(Bucket="techxxx-firstname-test-boto3")
 
print("Bucket created")
```
`create_bucket()` makes a new bucket with the given name. In any region other than `us-east-1`, the region must also be passed:
```python
s3.create_bucket(
    Bucket="techxxx-firstname-test-boto3",
    CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
)
```
 
### 3. Upload a file — `3_upload_file.py`
```python
import boto3
 
s3 = boto3.client("s3")
 
s3.upload_file("hello.txt", "techxxx-firstname-test-boto3", "hello.txt")
 
print("File uploaded")
```
`upload_file(local_file, bucket, key)` sends the local file `hello.txt` to the bucket and stores it under the key `hello.txt`.
 
### 4. Download a file — `4_download_file.py`
```python
import boto3
 
s3 = boto3.client("s3")
 
s3.download_file("techxxx-firstname-test-boto3", "hello.txt", "downloaded_hello.txt")
 
print("File downloaded")
```
`download_file(bucket, key, local_file)` is the reverse of upload: it fetches the object and saves it locally as `downloaded_hello.txt`.
 
### 5. Delete a file — `5_delete_file.py`
```python
import boto3
 
s3 = boto3.client("s3")
 
s3.delete_object(Bucket="techxxx-firstname-test-boto3", Key="hello.txt")
 
print("File deleted")
```
`delete_object()` removes the object with that key from the bucket.
 
### 6. Delete the bucket — `6_delete_bucket.py`
```python
import boto3
 
s3 = boto3.client("s3")
 
s3.delete_bucket(Bucket="techxxx-firstname-test-boto3")
 
print("Bucket deleted")
```
`delete_bucket()` removes the bucket. S3 only allows this when the bucket is empty, which is why script 5 runs first.
 
## Running and verifying
```bash
source ~/venv/bin/activate
echo "hello from boto3" > hello.txt
 
python3 1_list_buckets.py
python3 2_create_bucket.py
python3 1_list_buckets.py            # new bucket appears
python3 3_upload_file.py
aws s3 ls s3://techxxx-firstname-test-boto3   # hello.txt listed
python3 4_download_file.py
cat downloaded_hello.txt             # prints "hello from boto3"
python3 5_delete_file.py
python3 6_delete_bucket.py
python3 1_list_buckets.py            # bucket is gone
```