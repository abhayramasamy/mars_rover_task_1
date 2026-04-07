#!/bin/bash

LOG_FILE="rover_system_check.log"

echo "Starting pre-mission system check..."
echo "======================================"

# --- BATTERY CHECK ---
BATTERY=$((RANDOM % 101))
echo "Battery level: $BATTERY%"

if [ "$BATTERY" -lt 20 ]; then
    echo "Battery low! Return to base!" | tee -a "$LOG_FILE"
    exit 1
fi

echo "Battery check passed!"

# --- NETWORK CHECK ---
echo "Pinging google.com..."

if ! ping -c 3 google.com; then
    echo "Communication failure!" | tee -a "$LOG_FILE"
    exit 1
fi

echo "Network check passed!"

# --- SUCCESS ---
echo "All systems operational!" | tee -a "$LOG_FILE"
exit 0
