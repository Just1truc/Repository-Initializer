#!/bin/sh
echo "=> Erasing old code..."
if [ -d "~/init_scripts" ]
then
    sudo rm -rf ~/init_scripts/
fi
echo "=> Copying source code..."
sudo cp -rf . ~/init_scripts/
echo "=> Giving permissions..."
sudo chmod a+x /usr/local/lib/init
