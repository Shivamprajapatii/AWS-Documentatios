## AWS Auto Scaling 
#### Why We Need Autoscalling
Cause When Traffic Increase We will not go to the aws console and run the another server so on so forth multiple time. 
Better We use aws auto scalling Featur through that we can auto scale-out and scale-in our server based on the request. we does not need to care about. 

# Steps to Create Auto Scaling
### Requirements 1: Create a Launch Template

```bash
If You have already any running server (EC2) and if you want Dicto Copy Server then create the AMI(Amazon Machine Image) of that existing server. Means your Entire Operating System, Configuration, and folder and files etc will be Grouped and become a OS image.

Ex- if You run apache2 server and nginx already in server one => and when you create the ami of that server all the configuration of that server will be available in second server also.

## Ways 
1. If you want to go with your existing confiuration Take AMI of that and then use it into Launch Template.
2. If you want manually configure new setup create a fresh Laucnh Template with your configuration requirements.    
```




