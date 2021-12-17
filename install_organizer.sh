#!/bin/sh
echo "=> Erasing old code..."
FILE=~/init_scripts/
if [ -d $FILE ]
then
    sudo rm -rf ~/init_scripts/
fi
echo "=> Copying source code..."
sudo mkdir ~/init_scripts/
sudo cp -R . ~/init_scripts/
echo "=> Done copying code..."
echo "=> Creating alias..."
OUTPUT=$(sudo cat ~/.zshrc | grep "alias initialize")
if [[ $OUTPUT == "" ]]
then
    echo "alias initialize='sh ~/init_scripts/init.sh'" >> ~/.zshrc
    echo "=> Add alias..."
fi
echo "=> Alias created..."
echo "=> Erasing repo..."
sudo rm -R .
zsh
