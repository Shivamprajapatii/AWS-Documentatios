# Setup WAF&Shield to the CloudFront  : 
Protect your web applications from common web exploits

    Go to WAF&Shield Dashboard > Click on Create Web ACL
<img src="./images/image-1.png">
    ✅: You will Redirect to Fill Details Section


## Step 1: Describe web ACL and associate it to AWS resources 
<img src="./images/image-2.png">

### Section 1: Web ACL details
    ✅ Resource type: 
    i) Global resource :- CloudFront Distributions, CloudFront Distribution Tenants and AWS Amplify Applications 
    ii) Regional resources :- Application Load Balancers, Amazon API Gateway REST APIs and AWS AppSync APIs

    > If You Choose Global resource you does not need to choose region
    ✅ Region : Choose the region where your source is present

    ✅ CloudWatch metric name: deleveinsight-cloudwatch
<img src="./images/image-3.png">
    > Click on Add AWS resources

<img src="./images/image-4.png">      
    > Click on Default and Clikc on Next

## Step 2: Add rules and rule groups 
    ✅ AWS Have Manage Rule Group Where Rules are already written by AWS.

    ✅ AND you have option of Add my Own rules and rules Group Where you can define your own rule set.

 <img src="./images/image-5.png"> 
    - Click On Add Managed rule Group > after that AWS managed rule groups Expands this

 <img src="./images/image-6.png"> 

***Add Rules Based On Requirements***
 <img src="./images/image-7.png"> 

 ***Click on Add Rules***
You will redirect to Again Rule Section

<img src="./images/image-8.png"> 

- Now Add Your OWN Rule Set: **Click on Add own Rules and rule groups**

<img src="./images/image-9.png"> 


 






