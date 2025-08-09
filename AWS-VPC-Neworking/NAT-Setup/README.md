# NAT (Network Address Translation)
    In AWS, NAT Gateway (or NAT Instance) is a service that lets private subnet instances connect to the internet without exposing them to incoming traffic from the internet. 
    Think of NAT like a middleman: When you want anything from the internet it will go and take for you.        
    => But this will be always in Public Subnet.

##  Why use NAT
    Without NAT, anything inside a private subnet can’t access the internet (because it has no public IP).
    But sometimes, your private EC2 needs internet to:
    Download OS updates (e.g., apt update, yum update)
    Install packages from online repos
    Connect to external APIs (outbound only)

## 3. When to use NAT?
    Use NAT when:
    Your instance is in a private subnet (no public IP).
    You still need to download or send data to the internet.

#### How traffic flows:
    > App Server sends request to yum update (needs internet).
    > Request goes → Private Subnet Route Table → NAT Gateway in Public Subnet → Internet Gateway → Internet.
    > Internet replies → NAT Gateway → Private Subnet → App Server.

# NAT Setup 
### Step 1 — Create VPC
    > Go to VPC service → Your VPCs → Create VPC.
### Step 2: Create Internet Gateway
    > Go to Internet Gateway Click on Create > Select VPC > and click on create
      After that Attach that internet Gateway to VPC 
### Step 3: Create Subnets 
    > Ex 
      public-subnet-A: CIDR 10.0.1.0/24, AZ us-east-1a
      public-subnet-B: CIDR 10.0.2.0/24, AZ us-east-1b
      private-subnet-A: CIDR 10.0.101.0/24, AZ us-east-1a
      private-subnet-B: CIDR 10.0.102.0/24, AZ us-east-1b

### Step 4: Create Route Table
- Public Route Table:
      Route tables → Create route table → Name: prod-public-rt → Select vpc
       Select Routes → Click on Edit routes → Add route 0.0.0.0/0 → Target: Internet Gateway (prod-igw) → Save.
- Private Route Table : 
      Create another RT: Name: prod-private-rt → VPC: prod-vpc
#### Subnet Association For Public Route Table 
    > Public Route Table > Associate all public subnet 
    > Select the new RT → Routes → Edit routes → Add route 0.0.0.0/0 → Target: Internet Gateway (prod-igw) → Save.

#### Subnet Association For Private Route Table 
    > Private Route Table > Associate all private subnet
    Till Now No Internet Access we will attach NAT latter

### Step 5: Create NAT
    In VPC → NAT Gateways → Create NAT Gateway 
    > Name: prod-nat
    > Subnet: Public-A (one per AZ if HA is required)
    > Allocate Elastic IP and assign.
    > Create.
    (Note This NAT Will In Public Subnet)

### Step 6: Modify Route Tabel
    > Go to Private Route Table > inside your private Subnet is Associated 
    > click on Edit Route > add 0.0.0.0/0 and destination NAT 
    (all set)
 