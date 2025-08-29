# 🔑 AWS Session Manager
    Use AWS Systems Manager (SSM) Session Manager to connect to EC2 instances without a bastion host, SSH (22), or RDP (3389). This runbook gives you production‑ready steps (Console and CLI), hardening, logging, and troubleshooting.

## Step 1 🔎: First You Have to Create IAM User 
<h3><a href="./IAM-Role-Creation/README.md">Click Here</a>  </h3>  

## Step 2 🔎: Attach IAM Role to EC2 Instance
    GO to EC2 Dashboard → Click on Running Instances

<img src="./images/11.png" width="full">

    Click on Action → Click on Security → Click on Modify IAM Role

<img src="./images/12.png" width="full">

    You will Redirect to this

<img src="./images/13.png" width="full">

    Select The Role the you previously Created 

<img src="./images/14.png" width="full">

    Click on Update IAM Role

<img src="./images/15.png" width="full">

    You will Get Successfully IAM Role Attach

## verify the SSM Manager Login 
    You will Get this

<img src="./images/16.png" width="full">

    SSM Agent is not online
    The SSM Agent was unable to connect to a Systems Manager endpoint to register itself with the service.


## Step 3 🔎: Create Endpoints
    GO to VPC Console

<img src="./images/17.png" width="full">

    Search for VPC Endpoints
    Click on Create endpoints

<img src="./images/18.png" width="full">

   In Services Section

<img src="./images/19.png" width="full">

     Select there service
    
<img src="./images/20.png" width="full">
     Choose VPC as Per Your VPC and Enable DNS Name 

<img src="./images/21.png" width="full">
    👉: Pick the subnets in each AZ where your private EC2s run.

<img src="./images/22.png" width="full">
    in my case this.


<img src="./images/23.png" width="full">
    Select the Required Security Groups


<img src="./images/24.png" width="full">
    Give Full Access for Now.

<img src="./images/25.png" width="full">
    Let Everything be default and Click on create Endpoint

<img src="./images/26.png" width="full">
    VPC End Poitns Gets Created status is Pending wait for the Status to be Updagrade to Available.

<img src="./images/27.png" width="full">
    Now Status is Availaible now you can use this VPC endpoints.

## Step 4 🔎: Verify AWS Systems Manager
<img src="./images/28.png" width="full">

    Go to Explore nodes 

<img src="./images/29.png" width="full">
    Here in the VPC that i Choose there are 3 subnets right now inside that subnts 2 EC2 are Running that why 
    it is Showing 2 Node.

<img src="./images/30.png" width="full">
    Select Node ID > Click on Node Action > Connect > Start Terminal session

 








