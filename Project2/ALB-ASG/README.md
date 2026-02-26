# 🚀 Deploy a Scalable Web Application Using AWS Auto Scaling & Application Load Balancer (ALB)

This project deploys a fully scalable and highly available web application on AWS using an Auto Scaling Group (ASG) integrated with an Application Load Balancer (ALB). This setup ensures that the application automatically adjusts capacity based on traffic while maintaining continuous availability.


## 🔐 Key Steps overview
- Created a Launch Template to standardize EC2 configuration and automate app deployment
  - Defined AMI, instance type, OS, security groups, and user-data script for automatic application deployment on every EC2 instance.
- Set up an Auto Scaling Group to manage instance scaling during peak and low traffic
  - Attached the launch template.
  - Set the minimum, maximum, and desired number of EC2 instances.
  - Enabled dynamic scaling based on CPU utilization (or custom metrics).
  - Ensured new instances register automatically to the Target Group.
- Configured an Application Load Balancer to distribute incoming traffic efficiently
  - Created an ALB to distribute incoming HTTP/HTTPS requests.
  - Defined listeners and rules to route traffic to the appropriate Target Group.
- Integrated a Target Group for dynamic instance health checks and routing
  - All instances in the ASG automatically register to the Target Group.
  - ALB routes traffic only to healthy instances.
  - Works seamlessly during scale-in or scale-out events.
- Successfully tested End-to-End Deployment
  - Verified web page accessibility through the ALB DNS URL.
  - Simulated load to confirm instance scale-out.
  - Tested instance termination to confirm ALB routes traffic to healthy instances only.


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







