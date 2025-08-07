# Application Load Balancer(ALB)
    It distributes incoming traffic across multiple targets (like EC2 instances) to:
    - Improve availability
    - Handle more load
    - Provide fault tolerance

## 🧩 Scenarios: At least 1 EC2 instance running (2 recommended for high availability)

### 🧭 Step 1: Go to EC2 Dashboard
   - Go to Load Balancer
### 🧱 Step 2: Click on "Create Load Balancer"
- since we are going with Application Load Balancer Choose ALB > Click on Create   
    - Section 1: Basic Configuration
      >Choose Internet Facing                                                                                   
      >IPv4
    - Section 2: Network mapping 
      >Select VPC                                                                                               
      >Choose Avaialiblity Zones and Subnets
      - Mandatory to have two Subnet for High Availaiblity 
    - Section 3 : Security groups 
      > user will only hit http request to the load balancer either on HTTP or HTTPs so Give the Security Group based on that
    - Section 4: Listeners and routing                                                                          
    A listener is like a gate on the load balancer that waits for incoming traffic on a specific port (like 80 or 443) and protocol (like HTTP or HTTPS). we can add both Http and Https                                    
      > ✅ Example:
        You have a web app with:                                                                                
        /api → goes to API servers                                                                                  
        /images → goes to image servers                                                                                                
        /login → goes to auth servers
    - Section 5: Taget Group 
      > If you already Created that then Choose it from the Drop Down else refer this link

    






