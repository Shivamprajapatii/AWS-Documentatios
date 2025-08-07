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

### 5. Advanced health check settings
   - Health check port : Ye woh port hai jisme se Load Balancer aapke server ko check karta hai ki chal raha hai ya nahi. Agar Jispe port pe app chal rha hai usi port pe helath check bhi chalna chahiye toh choose karo       Traffic  #Trafic port
- Aap chaho to alag port bhi de sakte ho (override karke).

- ### Healthy threshold
   💚 Kitni baar lagataar sahi reply aayega tab Load Balancer bolega: "Ha bhai, yeh server ab thik hai!"        
   🧠 Example:Agar 5 baar /health endpoint ne 200 OK diya → server Healthy maana jaayega.

- ### Unhealthy threshold
   💔 Kitni baar lagataar fail hoga toh Load Balancer bolega: "Yeh server to kharaab ho gaya bhai!"             
   🧠 Example:
   Agar 2 baar /health ka reply na aaye ya galat aaye → server ko Unhealthy mark kar diya jaayega.

- ### Time Out 
   ⏰ Kitne second tak wait karega Load Balancer ek health check ka reply aane ka?                               
   🧠 Example: Agar 5 second mein reply nahi aaya /health se → Load Balancer bolega: "Fail!"
- ###  Interval
   🔁 Har kitne second mein Load Balancer dubara check karega server ko?                                        
   🧠 Example: Har 30 second mein ek baar check hoga /health par.

### 5. Click On Next
- You will Go on Next Page
### 6. Register targets
   - You will Get an Running Instances you just have to select those instances that you want to make in under target -group.                                                                                                
   - > Just Click Instances                                                                                        
   - > Click on Include as pending below                                                                          
   - > Click On Create target group  

All Set

```bash
Now You Can Attach this Target Group with your ALB.
Note: If You Use Auto Scaling Group So not Recommend to use Register targets this step keep it blanck and Just create
```


