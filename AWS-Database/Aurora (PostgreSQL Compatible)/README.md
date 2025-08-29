# Amazon Aurora PostgreSQL
    AWS Aurora is a managed database service this is 3x faster than normal mysql.

## Pre Requisite 
   🔹 Create A VPC 
   🔹 Create Internet Gateway
   🔹 Associate Internet Gateway to VPC  
   🔹 Create Subnets 
   🔹 Create Route Table
   🔹 Associate Subnets inside Route Table
   🔹 Associate Internet Gateway Inbout Access to Route Table

<h3><a href="./VPC/README.md">VPC Creatinon Steps</a></h3>


### Today I will Implement Amazon Postgress DB

## ✅ Step 1: Login AWS Console
<img src="./images/1.png" width="full">
    
<img src="./images/2.png" width="full">

    > Search for Aurora RDS > Click on that > Click on Create Database

<img src="./images/3.png" width="full">

    Choose a database creation method = Standerd Creation
    Engine Type = Aurora (PostgreSQL Compatible)

<img src="./images/4.png" width="full">

    Choose the Version as per your need
    I will go with = Aurora PostgreSQL (Compatible with PostgreSQL 17.5) - default for major version 17


<img src="./images/5.png" width="full">

    ✅ I will Go with Production

<img src="./images/6.png" width="full">

    ✅ Give the DB Cluster Name

<img src="./images/7.png" width="full">

    master username = shivam
    Credentials management = I will Store my DB username and Password inside Managed in AWS Secrets Manager - most secure. so no changes. i will not got with self managed

    ✅ Keep Encryption Key Default

<img src="./images/8.png" width="full">

    Aurora I/O-Optimized : If your app need more Input Output Operation 
    Aurora Standard : this is more costly than Aurora I/O-Optimized but very fast 

    ✅ I will go for now Aurora I/O-Optimized

<img src="./images/9.png" width="full">
    Choose DB Configuration 

    I will Go with Burstable classes (includes t classes) > Default value 

<img src="./images/10.png" width="full">

    Choose option one for an Aurora Replica for fast failover and high availability.

<img src="./images/11.png" width="full">

    ✅ Since i dont have any insatnce running i will manually do so i choose   Don’t connect to an EC2 compute resource > Choose IPv4 

<img src="./images/12.png" width="full">

    ✅ Choose VPC > Choose Public Access Yes (another keep Default)

<img src="./images/13.png" width="full">

    ✅ Give new Security Group Name

<img src="./images/14.png" width="full">
    ✅ Give the Port Default

<img src="./images/15.png" width="full">

    This mean if any query come which just insert then my primary replica will handle but if user is just crowsing and making get request menas just reading then it will go from read replica.

    ✅ select the Box

    Keep Tag or leave it.

<img src="./images/16.png" width="full">

    If you are Miigrating from SQL Server and want minimal code changes and your SQL Server Query Will Generate result and sotre in Aurora Posgress

    ✅ I am not selecting anything

    ✅ Levae Database authentication Dont select anything for Now 

<img src="./images/17.png" width="full">

    Choose Standerd Insight > Keepp Everything Default

<img src="./images/18.png" width="full">

    For now I want all log to view on cloudWatch so that i created that.

<img src="./images/19.png" width="full">

    ✅ Choose this This will Suggest RDS automatically detects performance anomalies for DB instances and provides recommendations.
    This will take charge.

<img src="./images/20.png" width="full">

    Give initial Database Name : hotelDB
    Keep everything default

 
<img src="./images/21.png" width="full">

    tier-0	Highest
    tier-12	Very low
    tier-15	Lowest possible

    So i choose 0

<img src="./images/22.png" width="full">

    Leave Default

<img src="./images/23.png" width="full">

    Click on Create database

<img src="./images/success.png" width="full">

### Writer : Handles all reads & writes
### Reader : Standby (for failover) & read scaling

