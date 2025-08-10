# Sync Bucket Data From One Account to Another Account

# AWS Accounts
|**Buckets**| **Account A(7317477989)** | **Account B(7317477989)**| 
|-----------|---------------------------|--------------------------|
|Bucket Name| hotel-image-bucket        |  prod-hotel-image-bucket |


## ✅ Question?
- I Want to Sync my **hotel-image-bucket** to **prod-hotel-image-bucket**


# Step to Do
### Step 1: 
    Go to the Source Account A > inside hotel-image-bucket > click on permission                                        
 
> 
   ```bash
    {
    "Version": "2008-10-17",
    "Statement": [
        {
            "Sid": "AllowPublicReadWriteOnObjects",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": [
                "s3:PutObject",
                "s3:PutObjectAcl",
                "s3:GetObject",
                "s3:GetObjectAcl",
                "s3:DeleteObject"
            ],
            "Resource": "arn:aws:s3:::hotel-image-bucket/*"
        },
        {
            "Sid": "AllowListBucket",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::hotel-image-bucket"
        }
    ]
}
```

### Step 2: 
    Go to the Destination Account B > inside prod-hotel-image-bucket > click on permission 

> 
```bash
{
	"Version": "2012-10-17",
	"Id": "Policy1611277539797",
	"Statement": [
		{
			"Sid": "Stmt1611277535086",
			"Effect": "Allow",
			"Principal": {
				"AWS": "arn:aws:iam::983822652251:user/aws-server-migratrions"
			},
			"Action": "s3:PutObject",
			"Resource": "arn:aws:s3:::prod-cordelia-hms-s3/*",
			"Condition": {
				"StringEquals": {
					"s3:x-amz-acl": "bucket-owner-full-control"
				}
			}
		},
		{
			"Sid": "Stmt1611277877767",
			"Effect": "Allow",
			"Principal": {
				"AWS": "arn:aws:iam::983822652251:user/aws-server-migratrions"
			},
			"Action": "s3:ListBucket",
			"Resource": "arn:aws:s3:::prod-cordelia-hms-s3"
		}
	]
}
```

### Step 3: Change AWS Account ID Inside Principal Section
    "AWS": "arn:aws:iam::983822652251:user/aws-server-migratrions" add your source Account Details


# Command To Sync 
### First Configure Your Destination Account inside your Laptop
```bash
    > aws configure
    > access key
    > secret key
    > region
    > josn
```
## Final Command to Sync 
```bash
    >  aws s3 sync s3://hotel-image-bucket s3://prod-hotel-image-bucket --acl bucket-owner-full-control
```





