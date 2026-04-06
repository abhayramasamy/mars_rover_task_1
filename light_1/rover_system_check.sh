#!/bin/bash

# ============================================================
# MaRs Rover - Pre-Mission System Check
# Author: [Your Name]
# ============================================================

LOG_FILE="rover_system_check.log"

echo "Starting pre-mission system check..."
echo "======================================"

# --- BATTERY CHECK ---
BATTERY=$((RANDOM % 101))
echo "Battery level: $BATTERY%"

if [ $BATTERY -lt 20 ]; then
    echo "Battery low! Return to base!" | tee -a $LOG_FILE
    exit 1
fi

echo "Battery check passed!"

# --- NETWORK CONNECTIVITY CHECK ---
echo "Pinging google.com..."

ping -c 3 google.com > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "Communication failure!" | tee -a $LOG_FILE
    exit 1
fi

echo "Network check passed!"

# --- ALL SYSTEMS GO ---
echo "All systems operational!" | tee -a $LOG_FILE
exit 0
