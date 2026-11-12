
# What is S3 storage?

- simple storage service
- used to store and retrieve any amount of data from anywhere, you are connected to the internet
- easy to configure to host a static website on the cloud
- provides built in redundancy
- highly available 
- -- a copy in all 3 availability zones in the region
- can be accessed from aws console & aws cli
- equivalent to azure blob storage

commands:
```
sudo apt update
sudo apt install -y unzip curl
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
then:
```
aws --version
```
also for python:

```
sudo apt install -y python3-pip
pip3 --version
```

run ``` aws configure```

AWS Access Key ID [None]: 

AWS Secret Access Key [None]: 

Default region name [None]: eu-west-1

Default output format [None]: json

to see buckets:

aws s3 ls 

make bucket:
```
aws s3 mb s3://tech613-daria-first-bucket 
```

To upload files:
```
aws s3 cp test.txt s3://teach613-daria-first-bucket
```

Download files:
```
aws s3 sync s3://tech
```
Remove a single file from bucket:
```
aws s3 rm s3://teach613-daria-first-bucket/<filename>
```
to remove contents of the bucket:
```
aws s3 rm s3://teach613-daria-first-bucket --recursive
```

remove bucket with files:
```
aws s3 rb s3://teach613-daria-first-bucket --force 
```
