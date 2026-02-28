# 🚀 Deploy a static website in AWS using Amazon S3 and CoudFront
This project hosts a static website on Amazon S3 and delivers it globally through Amazon CloudFront.

## 🔐 Key Steps overview
- Created an S3 bucket for static content
- Set up a CloudFront distribution with S3 as the origin
- Selected the recommended option to allow private S3 access (CloudFront automatically created the Origin Access Control — love how seamless this is now!)
- Applied the required bucket policy for secure access
- Configured CloudFront settings for smooth and efficient content delivery


## 🔧 Implementation
### Create an IAM User(named AWS-User) with required least privileges
![IAM User Creation](images/1.png)
![IAM User Creation](images/2.png)
### Create an EC2 Instance(named AWS-Instance with default settings)
Note: : Choose Ubuntu AMI for the EC2 instance
### Create a S3 bucket
![S3 Bucket Creation](images/s3.png)
Note: **Block Public Access settings for this bucket** should be disabled
### Upload the file into S3 bucket
![S3 Bucket File Upload](images/s31.png)
### Create Access key
![Access Key Generation](images/iam1.png)
![Access Key Generation](images/iam2.png)
![Access Key Generation](images/iam3.png)
### Open terminal and connect to EC2 instance
![Connection to EC2](images/ec21.png)
### Run the following code
```
sudo apt update
sudo apt install unzip

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Note: check AWS version using **aws --version**


### Setup AWS credentials using **aws configure**
Enter the access key and secret access key here that was fetched from AWS console


### Verify the access using aws commands
![S3 Access Verification](images/verify.png)

## It is a great hands-on exercise in IAM, EC2, S3, and AWS CLI, reinforcing how important secure and minimal-access configurations are in cloud engineering.







