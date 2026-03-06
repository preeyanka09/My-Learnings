# 🚀 Connect an EC2 Instance to RDS MySQL database
This project demonstrates a clean approach for connecting an Amazon EC2 instance to Amazon RDS MySQL database.
## 🔐 Key Steps overview
- Created an IAM Role.
- Created an EC2 instance with minimal free tier configuration.
- Created RDS Database.
- Modified the security group for RDS access.
- Established connection between EC2 and RDS.

## 🔧 Implementation
### Step 1: Create an IAM Role(named EC2-RDS) 
- Use Case: EC2
- Allowed Permissions: RDSFullAccess anf CloudWatchEventsFullAccess

### Step 2: Create an EC2 Instance(named AWS-Instance with default settings)
Note: : Choose Ubuntu AMI for EC2 instance

### Step 3: Create a RDS Database
- Choose a database creation method: Easy Create
- Engine Type: MySQL
- DB Instance size: Free Tier
- Settings:
  - DB Instance Identifier: database-1
  - Master Username: admin
  - Master Password: admin123
 
### Step 4: Modify the Security Group on EC2 for RDS Access
- Edit Inbound Rules -> Add MySQL (Port 3306) from Source: Security Group of EC2 (launch-wizard-1)

### Step 5: SSH into EC2 Instance and install mysql-client to it
```
sudo apt update
sudo apt install mysql-client
```
### Step 6: Establish the connection between EC2 and RDS
`
mysql -h database-1.c07m8igqcg94.us-east-1.rds.amazonaws.com -P 3306 -u admin -p
`
![RDS Connection](images/verify3.png)

### Step 7: Test the database
![Test Database](images/verify3.png)


Note: Both EC2 Instance and RDS must be in the same VPC.








