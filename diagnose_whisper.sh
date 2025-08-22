#!/bin/bash
# ===================================================================
# AI Coder's Whisper API Diagnostic & Restart Script
# Purpose: Provides a clean-slate environment to reproduce and diagnose a crash.
# ===================================================================

echo "--- [Step 1/4] Stopping any previous instances of the server..."
# Use pkill to forcefully find and kill any running custom_app.py process.
# The -f flag matches the full command line.
pkill -f custom_app.py
sleep 1 # Give the OS a moment to release the port

echo "--- [Step 2/4] Clearing the old log file..."
rm -f log.txt

echo "--- [Step 3/4] Starting the server in a clean state..."
# Execute the start script. It will run in the background.
bash start.sh
echo "Server start command issued. Waiting 5 seconds for initialization..."
sleep 5

echo "--- [Step 4/4] Checking initial process status..."
# Check if the process started successfully.
ps aux | grep custom_app.py | grep -v grep
echo "--------------------------------------------------------"
echo ""
echo "DIAGNOSTIC ENVIRONMENT IS READY."
echo "1. Go to your PowerShell window and run the Test-HerikaSystem.ps1 script."
echo "2. The 'Whisper (STT API)' test will fail again."
echo "3. Come back to this WSL terminal and run the analysis commands below."
echo ""
