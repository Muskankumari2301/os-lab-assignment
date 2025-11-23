# OS Lab Assignment 1 - Complete Solution
print("=== OS LAB ASSIGNMENT 1 ===")
print("Process Management Using Python")
print()

import os
import subprocess
import time

# Task 1: Process Creation
print("TASK 1: Process Information")
print("-" * 30)
print(f"My Process ID (PID): {os.getpid()}")
print(f"Parent Process ID (PPID): {os.getppid()}")
print()

# Task 2: Command Execution
print("TASK 2: System Command Execution")
print("-" * 30)
print("1. Running 'dir' command:")
subprocess.run("dir", shell=True)
print()

print("2. Running 'whoami' command:")
subprocess.run("whoami", shell=True)
print()

print("3. Running 'echo %date%' command:")
subprocess.run("echo %date%", shell=True)
print()

# Task 3: Process Details
print("TASK 3: Process Details")
print("-" * 30)
print("Running 'tasklist' to show running processes:")
subprocess.run("tasklist | head -10", shell=True)
print()

# Task 4: File Operations
print("TASK 4: File Operations")
print("-" * 30)
print("Creating test files...")
with open("test_file.txt", "w") as f:
    f.write("This is a test file for OS Lab Assignment\n")
print("Created test_file.txt")
print()

print("=== ALL TASKS COMPLETED SUCCESSFULLY ===")
input("Press Enter to exit...")
