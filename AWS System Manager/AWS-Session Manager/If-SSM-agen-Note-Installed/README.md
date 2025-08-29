# Installed SSM Agent Manually On Existing Server

## Step 1️⃣ : Login Inside Instance Using Bation Host and Install the SSM Agent 

### 1. For Amazon Linux / Amazon Linux 2
    sudo yum install -y amazon-ssm-agent
    sudo systemctl enable amazon-ssm-agent
    sudo systemctl start amazon-ssm-agent

    🪟 Chekc Status
    sudo systemctl status amazon-ssm-agent

### 2. For Ubuntu / Debian
    sudo snap install amazon-ssm-agent --classic
    sudo systemctl enable snap.amazon-ssm-agent.amazon-ssm-agent.service
    sudo systemctl start snap.amazon-ssm-agent.amazon-ssm-agent.service

    🪟 Chekc Status
    sudo systemctl status amazon-ssm-agent



