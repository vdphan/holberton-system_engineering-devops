# 0x05. Processes and signals

## Description
What you should learn from this project:

* What is a PID
* What is a process
* How to find a process’ PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored

## Requirements

- All files are created and compiled on Ubuntu 14.04.4 LTS
- All files are linted with Shellcheck

---

### [0. What is my PID](./0-what-is-my-pid)
* Write a Bash script that displays its own PID.


### [1. List your processes](./1-list_your_processes)
* Write a Bash script that displays a list of currently running processes.
  - Must show all processes, for all users, including those which might not have a TTY
  - Display in a user-oriented format
  - Show process hierarchy

### [2. Show your Bash PID](./2-show_your_bash_pid)
* Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
  - You cannot use pgrep
  - The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error here)

### [3. Show your Bash PID made easy](./3-show_your_bash_pid_made_easy)
* Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
- You cannot use ps

### [4. To infinity and beyond](./4-to_infinity_and_beyond)
* Write a Bash script that displays To infinity and beyond indefinitely. 
- Write a Bash script that displays To infinity and beyond indefinitely.


### [5. Kill me now](./5-kill_me_now)
* We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.
- Write a Bash script that kills 4-to_infinity_and_beyond process.
  - You must use kill

### [6. Kill me now made easy](./6-kill_me_now_made_easy)
* Write a Bash script that kills 4-to_infinity_and_beyond process.
- You cannot use kill or killall

### [7. Highlander](./7-highlander)
* Write a Bash script that displays: 
- To infinity and beyond indefinitely
  - With a sleep 2 in between each iteration
  - I am invincible!!! when receiving a SIGTERM signal
- Make a copy of your 6-kill_me_now_made_easy script, name it 67-kill_me_now_made_easy, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.


### [8. Beheaded process](./8-beheaded_process)
* Write a Bash script that kills the process 7-highlander.

### [9. Process and PID file](./100-process_and_pid_file)
* Write a Bash script that: 
- - Creates the file /var/run/holbertonscript.pid containing its PID
  - Displays To infinity and beyond indefinitely
  - Displays I hate the kill command when receiving a SIGTERM signal
  - Displays Y U no love me?! when receiving a SIGINT signal
  - Deletes the file /var/run/holbertonscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal
  

### [10. Manage my process](./101-manage_my_process)
- Indefinitely writes I am alive! to the file /tmp/my_process
  - In between every I am alive! message, the program should pause for 2 seconds
  - Write Bash (init) script 101-manage_my_process that manages manage_my_process. (both files need to be pushed to git)
- Requirements:
  - When passing the argument start:
    - Starts manage_my_process
    - Creates a file containing its PID in /var/run/my_process.pid
    - Displays manage_my_process started
  - When passing the argument stop:
    - Stops manage_my_process
    - Deletes the file /var/run/my_process.pid
    - Displays manage_my_process stopped
  - When passing the argument restart
    - Stops manage_my_process
  - Deletes the file /var/run/my_process.pid
    - Starts manage_my_process
    - Creates a file containing its PID in /var/run/my_process.pid
    - Displays manage_my_process restarted
  - Displays Requirements: manage_my_process {start|stop|restart} if any other argument or no argument is passed


### [11. Zombie](./102-zombie.c)
- Write a C program that creates 5 zombie processes.
  - For every zombie process created, it displays Zombie process created, PID: ZOMBIE_PID
  - Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
  - When your code is done creating the parent process and the zombies, use the function bellow

---

## Author
* **Van Phan** - [vdphan](https://github.com/vdphan)
