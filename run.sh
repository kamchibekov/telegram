#!/bin/bash
# Source the .env file and export all variables
set -a
source .env
set +a
# Call your Python script with arguments
python3.9 telegram-bulk-operations.py $@
