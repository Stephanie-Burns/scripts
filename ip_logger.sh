#!/bin/bash

LOG_FILE="$HOME/ip_log.txt"
CURRENT_IP=$(curl -s ifconfig.me)

if [ ! -f "$LOG_FILE" ]; then
    echo "Log file does not exist. Creating..."
    echo "Current IP: $CURRENT_IP" > "$LOG_FILE"
    exit 0
fi

LAST_IP=$(tail -n 1 "$LOG_FILE" | awk '{print $NF}')
if [ "$CURRENT_IP" != "$LAST_IP" ]; then
    echo "$(date): IP changed from $LAST_IP to $CURRENT_IP" >> "$LOG_FILE"
else
    echo "$(date): IP is still $CURRENT_IP" >> "$LOG_FILE"
fi

