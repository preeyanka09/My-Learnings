# 🚀 Real-Time Production AWS VPC Architecture with Multi-AZ Deployment
This project focuses on designing and implementing a real-time, production-grade AWS VPC architecture with a Multi-Availability Zone (Multi-AZ) deployment to ensure high availability, fault tolerance, and scalability.

## 🔐 Key Steps overview
- Created VPC
- Created Launch Template in the VPC created
- Created ASG under the same VPC
- Created Bastion Host
- Logged into private EC2 instance from Bastion Host
- Installed the web application in private EC2 instances
- Created Load Balancer in public subnet under the same VPC

## 🔧 Implementation
### Step 1: Create a custom VPC to host the entire infrastructure with proper network isolation.

### Step 2: Create a Launch Template defining EC2 instance configurations such as AMI, instance type, key pair, and security groups
- Security Group configuration:
  - SSH from anywhere
  - TCP: Port 8000 from anywhere
 
### Step 3: Configure an Auto Scaling Group within the VPC to automatically manage and scale EC2 instances across multiple Availability Zones.
- The EC2 instances must be in private subnet (us-east-1, us-east-2)
- Desired: 2, Minimum: 1, Maximum: 4
- Scaling policies: None
- No Load Balancer in the private subnet, hence select No Load Balancer

Note: Check if the two instances are connected in two different AZs or not.


### Step 4: Create Bastion Host
Deploy a Bastion Host in the public subnet to securely access instances located in private subnets.

### Step 5: Copy the key (pem file) from local to Bastion Host



## It is a great hands-on exercise in IAM, EC2, S3, and AWS CLI, reinforcing how important secure and minimal-access configurations are in cloud engineering.




