# Launch Template: 
A launch template is a pre-saved form in which you pre-fill all the settings to create an EC2 instance - such as AMI, instance type, key pair, security groups, user data, etc.                                               
(A Launch Template is a blueprint for launching EC2 instances.) it support Versioning also.

It saves your EC2 configuration like: 
- AMI ID
- Instance type
- Key pair
- Security group
- User data script
- IAM role                                                                                                      
So instead of configuring all this every time you launch an instance, you just use the Launch Template.

## ✅ Steps to Create Launch Template (Manual via AWS Console)                                                  
### Step 1: Go to Launch Templates 
    > Click on Create Launch Template
### Step 2: Fill in Basic Details
   - Launch template name: my-webserver-template
   - Template version description (optional): Initial version
   - Template tags: Add if needed
### Step 3: Application Settings 
   - AMI ID (Choose your preferred AMI) => note if you dont have dont go with AMI
   - Instance type: e.g., t2.micro    => Since we know that our AMI is just like Bundle of Software package but i have to choose on what type of configuration my server should be. 
   - Key pair - Select your key pair (or create a new one)

### Step 4: Network Settings
### Step 5: Storage
### Step 6: Advanced Details (Optional)
   - User data (if you want to automate script execution at launch)
   ## 📌 Example: User Data Script
     #!/bin/bash
     sudo apt update -y
     sudo apt install nginx -y
     sudo systemctl start nginx

### Step 7: Click Create launch template
