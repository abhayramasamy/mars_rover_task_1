#!/bin/bash

# ============================================================
# LIGHT DOSE TASK 1: ABHAY RAMASAMY CS25I1067
# ============================================================


#ALL TASKS DONE IN SERIES: 

# 1) Create a new directory called rover_mission and navigate into it
mkdir rover_mission
cd rover_mission

# 2) Create three empty files
touch log1.txt log2.txt log3.txt

# 3) Rename log1.txt to mission_log.txt
mv log1.txt mission_log.txt

# 4) Find all files with .txt extension in current directory, use find [path] [type] [name]
find . -name "*.txt"

# 5) Display contents of mission_log.txt without opening an editor
cat mission_log.txt

# 6) Find and disply all lines containing "ERROR" in mission_log.txt
grep "ERROR" mission_log.txt

# 7) Count the number of lines in mission_log.txt
wc -l mission_log.txt

# 8) Show the system's current date and time
date

# 9) Display CPU usage
top -b -n 1 | head -20

# 10) Schedule a shutdown in 10 minutes
sudo shutdown -h +10
