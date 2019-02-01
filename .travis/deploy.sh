#!/bin/bash


git config --global push.default matching
git remote add deploy ssh://den@$IP:$PORT$DEPLOY_DIR
git push deploy master

# Skip this command if you don't need to execute any additional commands after deploying.
ssh den@$IP -p $PORT <<EOF
  cd $DEPLOY_DIR
  sudo docker-compose up -d
EOF