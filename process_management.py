#!/usr/bin/env python3
"""
OS Lab Assignment 1: Process Creation and Management
Course: ENCS351 Operating System
Student: [Your Name]
"""

import os
import subprocess
import time
import multiprocessing

def task1_process_creation():
    """Task 1: Create child processes and show process information"""
    print("=" * 50)
    print("TASK 1: Process Creation Utility")
    print("=" * 50)
    
    print(f"👨 Parent Process:")
    print(f"   - PID: {os.getpid()}")
    print(f"   - Parent PID: {os.getppid()}")
    print(f"   - Current Directory: {os.getcwd()}")
    
    # Create multiple processes using multiprocessing
    def child_worker(process_id):
        print(f"👶 Child Process {process_id}:")
        print(f"   - PID: {os.getpid()}")
        print(f"   - Parent PID: {os.getppid()}")
        print(f"   - Message: Hello from Child {process_id}!")
        time.sleep(1)  # Simulate some work
        return f"Child {process_id} completed successfully"
    
    print("\n🔄 Creating child processes...")
    num_processes = 3
    
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(child_worker, range(1, num_processes + 1))
    
    print("\n✅ All child processes completed:")
    for result in results:
        print(f"   - {result}")

def task2_command_execution():
    """Task 2: Execute system commands using subprocess"""
    print("\n" + "=" * 50)
    print("TASK 2: Command Execution Using subprocess")
    print("=" * 50)
    
    commands = [
        {"name": "List Files", "cmd": ["dir", "/B"]},
        {"name": "Current Date", "cmd": ["echo", "%DATE%"]},
        {"name": "Current User", "cmd": ["whoami"]},
        {"name": "System Info", "cmd": ["systeminfo", "|", "findstr", "/B", "/C:OS Name"]},
        {"name": "Network Info", "cmd": ["ipconfig", "|", "findstr", "IPv4"]}
    ]
    
    for i, command in enumerate(commands, 1):
        print(f"\n🔧 Command {i}: {command['name']}")
        print(f"   Executing: {' '.join(command['cmd'])}")
        
        try:
            result = subprocess.run(
                " ".join(command['cmd']), 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=10
            )
            
            if result.returncode == 0:
                print(f"   ✅ Output: {result.stdout.strip()}")
            else:
                print(f"   ❌ Error: {result.stderr.strip()}")
                
        except subprocess.TimeoutExpired:
            print("   ⏰ Command timed out")
        except Exception as e:
            print(f"   💥 Execution failed: {e}")

def task3_zombie_orphan_explanation():
    """Task 3: Explain zombie and orphan processes"""
    print("\n" + "=" * 50)
    print("TASK 3: Zombie & Orphan Processes Explanation")
    print("=" * 50)
    
    print("""
🧟 ZOMBIE PROCESSES:
- A zombie process is a process that has completed execution but still has an entry in the process table
- Occurs when parent doesn't call wait() for its child
- In Windows: Similar to processes that have exited but parent hasn't called WaitForSingleObject()

👶 ORPHAN PROCESSES:
- An orphan process is a process whose parent has terminated
- In Windows/Linux: Orphan processes are adopted by the system (init process - PID 1 in Linux, System - PID 4 in Windows)

🛠️ How to check in Windows:
1. Open Task Manager (Ctrl + Shift + Esc)
2. Go to 'Details' tab
3. Check Parent PID column
4. Use command: `tasklist /fo table` or `wmic process get ProcessId,ParentProcessId,Name`

🔍 Demonstration:
- Creating a process that becomes orphan (parent exits first)
- Showing process hierarchy
""")
    
    # Simulate orphan process concept
    print("\n🔄 Simulating orphan process concept...")
    def orphan_simulation():
        print("   Child process would continue even if parent exits")
        print("   In real scenario, this would be adopted by system")
    
    # Create a process
    p = multiprocessing.Process(target=orphan_simulation)
    p.start()
    print("   Parent process created child and could exit now")
    p.join()  # Wait for child to finish

def task4_proc_inspection():
    """Task 4: Inspect process information"""
    print("\n" + "=" * 50)
    print("TASK 4: Process Information Inspection")
    print("=" * 50)
    
    current_pid = os.getpid()
    print(f"🔍 Inspecting Current Process (PID: {current_pid}):")
    
    # Basic process info
    print(f"   - Process ID: {current_pid}")
    print(f"   - Parent Process ID: {os.getppid()}")
    print(f"   - Executable: {__file__}")
    print(f"   - Working Directory: {os.getcwd()}")
    print(f"   - User: {os.getlogin() if hasattr(os, 'getlogin') else 'N/A'}")
    
    # Memory information (approximate)
    try:
        import psutil
        process = psutil.Process()
        print(f"   - Memory Usage: {process.memory_info().rss / 1024 / 1024:.2f} MB")
        print(f"   - CPU Percent: {process.cpu_percent()}%")
        print(f"   - Status: {process.status()}")
        print(f"   - Create Time: {time.ctime(process.create_time())}")
    except ImportError:
        print("   - Install 'psutil' for detailed memory info: pip install psutil")
    
    # File descriptors (open files)
    print(f"\n📁 Current Directory Files:")
    try:
        files = os.listdir('.')
        for file in files[:5]:  # Show first 5 files
            print(f"   - {file}")
        if len(files) > 5:
            print(f"   - ... and {len(files) - 5} more files")
    except Exception as e:
        print(f"   - Error listing files: {e}")

def task5_priority_simulation():
    """Task 5: Process priority and scheduling"""
    print("\n" + "=" * 50)
    print("TASK 5: Process Priority Simulation")
    print("=" * 50)
    
    print("🎯 Process Priority in Windows:")
    
    try:
        import psutil
        
        current_process = psutil.Process()
        current_priority = current_process.nice()
        
        priority_names = {
            psutil.IDLE_PRIORITY_CLASS: "Idle (Lowest)",
            psutil.BELOW_NORMAL_PRIORITY_CLASS: "Below Normal", 
            psutil.NORMAL_PRIORITY_CLASS: "Normal",
            psutil.ABOVE_NORMAL_PRIORITY_CLASS: "Above Normal",
            psutil.HIGH_PRIORITY_CLASS: "High",
            psutil.REALTIME_PRIORITY_CLASS: "Realtime (Highest)"
        }
        
        print(f"   - Current Priority: {current_priority} ({priority_names.get(current_priority, 'Unknown')})")
        
        print("\n📊 Available Priority Classes:")
        for value, name in priority_names.items():
            print(f"   {value}: {name}")
            
        # Demonstrate CPU-bound work with different "priorities"
        print("\n🔄 Simulating work with different intensities:")
        
        def cpu_intensive_work(work_id, intensity):
            start_time = time.time()
            print(f"   Process {work_id} started (Intensity: {intensity})")
            
            # Simulate work based on intensity
            result = 0
            for i in range(intensity * 100000):
                result += i * i
                
            end_time = time.time()
            print(f"   Process {work_id} finished in {end_time - start_time:.2f}s")
            return result
        
        # Run different intensity works
        with multiprocessing.Pool(processes=3) as pool:
            results = pool.starmap(cpu_intensive_work, [(1, 10), (2, 5), (3, 15)])
            
        print(f"\n✅ Work simulation completed")
        
    except ImportError:
        print("   ℹ️  Install psutil for priority management: pip install psutil")
        print("   💡 On Windows, you can set priority in Task Manager:")
        print("      1. Open Task Manager")
        print("      2. Go to Details tab")
        print("      3. Right-click process → Set Priority")

def create_sample_files():
    """Create sample files for the assignment"""
    print("\n" + "=" * 50)
    print("CREATING SAMPLE FILES")
    print("=" * 50)
    
    files_to_create = {
        "sample_data.txt": "This is sample data for OS Lab Assignment 1\nCreated by process management script\n",
        "results.log": f"OS Lab Assignment Execution Log\nDate: {time.ctime()}\nPID: {os.getpid()}\n",
        "config.ini": "[Settings]\nversion=1.0\nauthor=Student\ncourse=ENCS351\n"
    }
    
    for filename, content in files_to_create.items():
        try:
            with open(filename, 'w') as f:
                f.write(content)
            print(f"✅ Created: {filename}")
        except Exception as e:
            print(f"❌ Failed to create {filename}: {e}")

def main():
    """Main function to run all tasks"""
    print("🎓 OS LAB ASSIGNMENT 1: PROCESS MANAGEMENT")
    print("=" * 60)
    print("Course: ENCS351 Operating System")
    print("Student: [Your Name]")
    print("Date:", time.ctime())
    print("=" * 60)
    
    # Run all tasks
    task1_process_creation()
    task2_command_execution()
    task3_zombie_orphan_explanation()
    task4_proc_inspection()
    task5_priority_simulation()
    create_sample_files()
    
    # Summary
    print("\n" + "=" * 60)
    print("🎉 ASSIGNMENT SUMMARY")
    print("=" * 60)
    print("✅ Task 1: Process Creation - Completed")
    print("✅ Task 2: Command Execution - Completed") 
    print("✅ Task 3: Zombie/Orphan Explanation - Completed")
    print("✅ Task 4: Process Inspection - Completed")
    print("✅ Task 5: Priority Simulation - Completed")
    print("✅ Sample Files Created - Completed")
    print("\n📁 Files generated:")
    files = os.listdir('.')
    for file in files:
        if file.endswith(('.py', '.txt', '.log', '.ini', '.md')):
            print(f"   - {file}")
    
    print(f"\n🏁 All tasks completed successfully!")
    print("💡 Remember to:")
    print("   1. Upload to GitHub")
    print("   2. Submit on LMS")
    print("   3. Update README with your name")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    # Check and install required packages
    try:
        import psutil
    except ImportError:
        print("📦 Installing required package: psutil")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
        print("✅ psutil installed successfully")
        import psutil
    
    main()
