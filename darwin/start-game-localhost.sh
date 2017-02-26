#!/bin/sh
cd ../

export DYLD_LIBRARY_PATH=`pwd`/Libraries.bundle
export DYLD_FRAMEWORK_PATH="Frameworks"

# Get the user input:
read -p "Username: " ttaUsername
read -p "Password: " ttaPsername

# Export the environment variables:
export ttaUsername=$ttaUsername
export ttaPassword=$ttaPassword
export TT_USERNAME=$ttaUsername
export TT_PASSWORD=$ttaPassword
export TT_GAMESERVER="127.0.0.1"

echo "==============================="
echo "Starting Toontown Project Altis..."
echo "Username: $TT_USERNAME"
echo "Gameserver: $TT_GAMESERVER"
echo "==============================="

ppython -m toontown.toonbase.ClientStart
