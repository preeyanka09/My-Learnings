# 🚀 Connect an EC2 Instance to RDS MySQL database
This project demonstrates a clean approach for connecting an Amazon EC2 instance to Amazon RDS MySQL database.
## 🔐 Key Steps overview
- Created an IAM Role.
- Created an EC2 instance with minimal free tier configuration.
- Created RDS Database.
- Modified the security group for RDS access.
- Established connection between EC2 and RDS.

## 🔧 Implementation
### Step 1: Create an IAM Role(named EC2-RDS-Role) 
- Use Case: EC2
- Allowed Permissions: AmazonRDSFullAccess anf CloudWatchEventsFullAccess

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

### Step 8: 
#### Install Python and pip
```
sudo apt update
sudo apt install python3 python3-pip -y
```

#### Check installation
```
python3 --version
pip3 --version
```

#### Install MySQL Python Library
`pip3 install pymysql`

Note: It will throw an error: externally-managed-environment. This error occurs because newer Debian/Ubuntu systems (Python 3.12+) follow PEP 668, which prevents pip from installing packages globally in the system Python. This is to avoid breaking OS-managed packages. Hence follow the next steps.

#### Install venv if not installed
`sudo apt install python3-venv`

#### Create a virtual environment
`python3 -m venv myenv`

#### Activate it
`source myenv/bin/activate`

Your prompt will change to something like:
(myenv) ubuntu@ip-xxx:~$

#### Install pymysql
`pip install pymysql`

#### Create Python Application
vim app.py
Place the following code in the file created.

```
import pymysql

host = "database-1.c07m8igqcg94.us-east-1.rds.amazonaws.com"
user = "admin"
password = "admin123"
database = "aws"

try:
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=3306
    )

    print("Connected to RDS MySQL!")

    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES;")

    for db in cursor.fetchall():
        print(db)


    cursor.execute("SELECT * FROM learners;")
    rows = cursor.fetchall()

    print("Rows under the table are as follows")
    for row in rows:
         print(row)

    connection.close()

except Exception as e:
    print("Connection failed:", e)

```
Note: Both EC2 Instance and RDS must be in the same VPC.









