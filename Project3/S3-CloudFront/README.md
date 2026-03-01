# 🚀 Deploy a static website in AWS using Amazon S3 and CloudFront
This project hosts a static website on Amazon S3 and delivers it globally through Amazon CloudFront.

## 🔐 Key Steps overview
- Created an S3 bucket for static content
- Set up a CloudFront distribution with S3 as the origin
- Selected the recommended option to allow private S3 access (CloudFront automatically created the Origin Access Control — love how seamless this is now!)
- Applied the required bucket policy for secure access
- Configured CloudFront settings for smooth and efficient content delivery


## 🔧 Implementation
### Step 1: Create a s3 bucket and upload your web pages
### Step 2: Go to Bucket properties -> Static Website Hosting -> Enable
- Hosting type: Host a static website
- Index document: index.html
- Error document: error.html
- Redirection rules: Find the below code snippet
```
[
    {
        "Condition": {
            "KeyPrefixEquals": "home/"
        }
        "Redirect": {
            "ReplaceKeyPrefixWith": "index.html"
        }
    }
]
```
Save changes, we will get a website URL: `http://aws-bucket-priya.s3-website-us-east-1.amazonaws.com/` 
<br>
Hit the URL, we will receive 403 Forbidden: Access Denied error.
<br>
![Access Denied Page](images/1.png)
<br>
We need to attach Read/GetObject policy to the bucket.
<br>
### Step 3: Attach GetObject policy to the bucket
Go to Permissions -> Bucket Policy -> Edit -> Paste the below code snippet
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::aws-bucket-priya/*"
        }
    ]
}
```
### Step 4: Hit the S3 Bucket endpoint
![S3 Bucket Creation](images/s3-endpoint.png)
<br><br>
The default webpage will be displayed.
<br><br>
![S3 Bucket Creation](images/s3.png)
<br><br>
Error webpage.
<br><br>
![S3 Bucket Creation](images/error.png)

### Step 5: Setting up the CloudFront CDN
- CloudFront -> Create Distribution
- Choose a plan: Pay as you go -> Next
- Distribution Name: Enter the distribution name (here CloudFront-S3)
- Distribution Type: Single website or app -> Next
- Origin type: Amazon S3
- S3 Origin: Select the bucket for which you want to deploy CloudFront (here aws-bucket-priya)
- Origin path(Optional)
- Settings(Use recommended settings) -> Next
- Enable Security: Donot enable security protection -> Next -> Create Distribution

Note: Edit the distribution to add the default root object as index.html. Default root object should not be empty: it should either be index.html. If Default Root Object isn’t set, CloudFront doesn’t know which file to load first, so it tries to fetch the directory root… which S3 rejects → XML AccessDenied.


Once the distribution is created, we get the CloudFront Domain Name as follows
![CloudFront](images/cloudfront_domainname.png)


### Step 5: Hit the CloudFront Domain Name: The content will be served.
![CloudFront](images/cloudfront.png)

## This way when a user visits our site, CloudFront delivers the content from the nearest edge location, dramatically reducing latency, speeding up load times, and improving the user experience. Hence we have a fast, secure, globally distributed static website running through CloudFront’s CDN.














