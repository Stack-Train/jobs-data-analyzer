#!/bin/env/sh
# Script to simulate trial run
# Scratchpad 

cd ./APIs/exp-API
start_api=$(npm start)
echo "Navigate to http://localhost:4000" on your local computer

cd ../../JDA-12/v1
npm start
