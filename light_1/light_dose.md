# LINUX BASHING TASK

Light Dose question to write bash command files that executes a list of commands that linnux UBUNTU 24.04 executes different tasks

## Problem statement:
Given in task file, we need to write separate `.sh` files also known as bash files that consists of terminal commands to execute several commands
these include but not limited to:
- mkdir : create a directory
- cat   :display contents on terminal
- cd    :moving
- touch : create empty files
- grep  :find and display words in a txt file
- find  : find all files or items in current directory
- wc    : counting lines
- date  : date
- basic sudo commands  : ex: shutdown install

## input:
none, linux ubuntu 24.04

##output:
3 text files are created with possible output

## How to run??
`chmod: +X name_file.sh <br/>
./name_file.sh
` <br/>
` or simply:  bash file_name.sh`

## Bonus new commands learnt:
## Bonus: New Commands Learnt

| Command | Description |
|--------|-------------|
| `mkdir` | Create a new directory |
| `cd` | Navigate into a directory |
| `touch` | Create empty files |
| `mv` | Rename or move a file |
| `find` | Search for files in a directory |
| `cat` | Display file contents without opening an editor |
| `grep` | Search for specific text/patterns inside files |
| `wc -l` | Count the number of lines in a file |
| `date` | Display the system's current date and time |
| `top` | Display real-time CPU and system usage |
| `shutdown` | Schedule or trigger a system shutdown |
| `chmod +x` | Grant execute permission to a script |
| `ping` | Test network connectivity to a host |
| `tee` | Print output to terminal and save to a file simultaneously |
| `scrot` | Take a screenshot from the terminal |
| `sudo apt install` | Install packages on Ubuntu/Debian systems |
| `RANDOM` | Generate a random number in Bash |
| `$?` | Check if the last command succeeded or failed |
| `exit` | Exit a script with a status code |

## Learning experience and take aways:

*Well, what did I learn and take away from this Linux Bashing experiments?? looks like a lot... including setting up the VM here is some but definetely not the least:*


### Linux & Bash Fundamentals
- Gained hands-on experience navigating the Linux filesystem using
  the command line, moving beyond a GUI-dependent workflow
- Learned how to create, rename, and manage files and directories
  entirely through terminal commands
- Understood how Bash scripts can chain multiple commands together
  into a single automated workflow, making repetitive tasks faster
  and more efficient

### Text Processing & File Operations
- Discovered how powerful `grep` is for searching through files
  without manually opening them
- Learned to use `cat`, `wc -l`, and `find` to inspect and manage
  files directly from the terminal

### Scripting & Automation
- Wrote my first real-world Bash script (`rover_system_check.sh`)
  incorporating logic, conditionals, and exit codes
- Understood how scripts can simulate real engineering workflows,
  such as pre-mission system checks for a rover
- Learned how to use `RANDOM`, `$?`, `tee`, and `exit` to build
  smart, responsive scripts

### VMware & Virtual Environments
- Troubleshot a real network connectivity issue inside a VMware
  virtual machine, diagnosing it down to the NAT service level
- Learned how to use the Virtual Network Editor to restore default
  network settings and restore connectivity.
- Gained confidence working inside isolated virtual environments
  for safe, sandboxed development and testing.

### General Takeaways
- The terminal is intimidating at first but becomes incredibly
  powerful and fast once you know the right commands
- Debugging is a core skill reading error messages carefully
  and testing step by step leads to the solution
- Writing scripts forces you to think logically and sequentially.
