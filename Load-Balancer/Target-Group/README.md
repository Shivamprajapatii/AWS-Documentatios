# Target Group
A Target Group is a collection of servers (like EC2 instances) that a Load Balancer sends traffic to.
## Steps
   ### 1. Go to the EC2 Console
- Open the AWS Console
- Navigate to **EC2 > Target Groups**
- Click **Create Target Group**

### 2. Choose Target Type
- Select **Instances**

### 3. Configure Basic Settings
- **Name**: `my-app-target-group`
- **Protocol**: HTTP
- **Port**: 80
- **VPC**: Select your existing VPC
- **VPC**: HTTPs

### 4. Health Check
-   Health Check = A way for AWS to automatically check if your application is working (alive and healthy).
👉 If your app is not healthy, AWS will stop sending traffic to that instance.
/health
