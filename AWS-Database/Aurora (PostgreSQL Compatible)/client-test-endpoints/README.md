# Test The RDS Using Clients is IT Working Or Not 

## Quick Method to Verify That DB is Ready to Connect Using Endpoint

## 🔹 Step 1: ✅ Use AWS CloudShell
<img src="../images/29.png" width="full">
<img src="../images/30.png" width="full">

### 🔹 Install PostgreSQL client in CloudShell 
    sudo yum install postgresql15 -y

### 🔹 After install, connect with psql
    psql --host=mydb.abcdefghij.us-west-2.rds.amazonaws.com \
     --port=5432 \
     --username=mydbuser \
     --dbname=mydbname

- Chnage DB End Point 
- Change username
- Change dbname

<img src="../images/31.png" width="full">
    🔹 It will Ask for Password

<img src="../images/32.png" width="full">
    🔹 In My Case i took password from Secret Manager and paste here

<img src="../images/33.png" width="full">
   ✅ All Done I Connected with My PayementDB 





## 🔹 Step 2: ✅ Use PgAdmin Local on My Laptop
    Download the PG Admin On Laptop

<img src="../images/34.png" width="full">
<img src="../images/35.png" width="full">
    Right Click on Server > Click on Register > Click on Server

<img src="../images/37.png" width="full">
<img src="../images/36.png" width="full">


<img src="../images/38.png" width="full">

✅ All Done I Connected with My PayementDB 







