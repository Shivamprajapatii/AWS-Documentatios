# AMI (Amazon Machine Image)
## ✅ 1. Create an AMI of an Existing EC2 Server (with configurations, files, and setup)

### Step 1: 
i) Go to the Amazon EC2 Console and Select the Running Server whome you want to create AMI.                     
ii) Click on Actions > Image and templates > Create image.                                                         
iii) Configure the Image                                                                                        
     > Image name: MyApp-AMI-Aug2025                                                                            
     > Image description: AMI with OpenVPN setup and all server configurations                                  
     > No reboot: (Uncheck for consistency) – unless you need it running continuously.                          
     > Add volume size/edit if needed.   
iv) Click on Create Image


### Step 2: Monitor/Verify AMI Creation
    Go to AMIs (left menu under "Images").
    Wait for the AMI to reach the "available" state.

✅ Done — You can now launch new EC2 instances using this AMI, and they will have everything pre-installed as per the original server.
