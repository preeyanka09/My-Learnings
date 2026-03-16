# 🚀 Implement VPC from scratch
This project demonstrates how to design and implement a custom Virtual Private Cloud (VPC) architecture in AWS from scratch. It covers the core networking components required to build a secure and scalable cloud environment.

The goal of this project is to understand how AWS networking works by manually configuring each component instead of using automated wizards.

## 🔐Architecture overview
The setup includes:
- Custom VPC
- Public Subnet
- Private Subnet
- Internet Gateway
- Route Tables
- Security Groups
- EC2 Instances

This architecture allows public internet access for one instance while keeping another instance private and secure.

## 🔧 Implementation
### Step 1 : Create an Custom VPC
Create a VPC with the following configuration:
- Name: test-vpc
- IPv4 CIDR block: IPv4 CIDR manual input
- IPv4 CIDR: 10.0.0.0/16
- IPv6 CIDR block: No IPv6 CIDR block
- Tenacy: Default

### Step 2 : Create Public Subnet
- VPC ID: test-vpc
- Subnet Name: test-public-subnet
- AZ: us-east-1a
- IPv4 VPC CIDR block: 10.0.0.0/24
- IPv4 Subnet CIDR block: 10.0.0.0/16

### Step 3: Create Private Subnet
- VPC ID: test-vpc
- Subnet Name: test-private-subnet
- AZ: us-east-1b
- IPv4 VPC CIDR block: 10.0.0.0/24
- IPv4 Subnet CIDR block: 10.0.1.0/16

### Step 4: Luunch an EC2 Instance (named test-instance)
Network Settings:
- VPC: test-vpc
- Subnet: test-public-subnet
- Auto assign public IP: Enable
- Security groups: SSH, HTTP-> Custom: Source- 10.0.0.0/16 (test-vpc-CIDR block)

Connect to the EC2 instance from outside world, unable to establish connection. Hence, create an Internet Gateway.

### Step 5: Create Internet Gateway
- Name: test-igw
- Attach to VPC: test-vpc

### Step 6: Create Route Table and associate it with public subnet
- Name: test-rt
- VPC: test-vpc

Click on route table connected -> Subnet Associations -> Edit Subnet Associations -> Check on public subnet -> Save

### Step 7: Connect Internet Gateway to Route Table
Goto test-rt -> Routes -> Edit route -> Add route 
- Destination: 0.0.0.0/0 ---- where the traffic is going
- Target: Internet Gateway(test-igw) ----  how it gets there

### Step 8: Enable auto-assign public IPv4 address on Public Subnet
Click on Subnet created (test-public-subnet) -> Edit subnet settings -> Check on Enable auto-assign public IPv4 address

### At this point, the path is established : 
### Internet -> IGW -> Route Table -> Public Subnet. 
Now we can connect to the EC2 instance. Our next step is to launch an EC2 instance in private subnet and access it from the EC2 instance in public subnet

### Step 9: Launch an EC2 instance in private subnet (named test-private-instance)
Network Settings:
- VPC: test-vpc
- Subnet: test-private-subnet
- Auto assign public IP: Disable
- Configure security group(SG-test-private-instance) : SSH only from public EC2 instance, ICMP only from public EC2 instance

Now SSH to private EC2 instance from public EC2 instance.

### Steps to SSH into private EC2 instance from public EC2 instance.
- Step a: Copy the keypair file to public EC2 instance from laptop

`scp -i \mnt\c\Users\preey\Downloads\KeyPairNorth.pem \mnt\c\Users\preey\Downloads\KeyPairNorth.pem ubuntu@<public_ip_address_of_public_ec2>:/home/ubuntu `

- Step b: ssh into public EC2 instance
- Step c: ssh into private EC2 instance from public EC2 instance

`ssh -i KeyPairNorth.pem ubuntu@private_ip_address_of_private_ec2`

## 🔐Architecture Diagram
![VPC Architecture](/images/architecture.png)


## It is a great hands-on exercise in IAM, EC2, S3, and AWS CLI, reinforcing how important secure and minimal-access configurations are in cloud engineering.








