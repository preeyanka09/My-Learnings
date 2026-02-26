# 🚀 Enable secure S3 Access from an EC2 Instance using IAM and AWS CLI
This project configures secure communication between an Amazon EC2 instance and an S3 bucket using only an IAM user with limited S3 and EC2 permissions — and all through the AWS CLI.

## 🔐 Key Steps overview:
- Created a least-privilege IAM user with custom S3 and EC2 permissions.
- Created an EC2 instance with minimal free tier configuration.
- Created a S3 bucket and uploaded a file on it.
- Created Access key for the IAM user.
- Set up AWS CLI credentials securely on the EC2 instance.
- Verified access and enabled data operations using commands like ws s3 ls, ws s3 cp

## 🔧 Implementation:
### Create an IAM User with required least privileges
![IAM User Creation](Project1/S3-Access-from-EC2/images/1.png)

