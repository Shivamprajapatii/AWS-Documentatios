# User Data
    #!/bin/bash
    export PATH=$PATH:/home/ubuntu/.nvm/versions/node/v22.18.0/bin
    cd /home/ubuntu/simple-express-server
    git pull 
    npm install
    pm2 start index.js --name simple-server
