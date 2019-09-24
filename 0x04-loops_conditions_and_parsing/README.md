# 0x04. Loops, conditions and parsing

## Description
* How to create SSH keys
* What is the advantage of using  #!/usr/bin/env bash over #!/bin/bash
* How to use while, until and for loops
* How to use if, else, elif and case condition statements
* How to use the cut command
* What are files and other comparison operators, and how to use them

## Requirements

- All files are created and compiled on Ubuntu 14.04.4 LTS
- All files are linted with Shellcheck
---

### [0. Create a SSH RSA key pair](./0-RSA_public_key.pub)
- Create a RSA key pair (ssh-keygen).

### [1. For Holberton School loop](./1-for_holberton_school)
* Write a Bash script that displays Holberton School 10 times.
- You must use the for loop (while and until are forbidden)

### [2. While Holberton School loop](./2-while_holberton_school)
* Write a Bash script that displays Holberton School 10 times.
- You must use the while loop (for and until are forbidden)


### [3. Until Holberton School loop](./3-until_holberton_school)
* Write a Bash script that displays Holberton School 10 times.
- You must use the until loop (for and while are forbidden)

### [4. If 9, say Hi!](./4-if_9_say_hi)
* Write a Bash script that displays Holberton School 10 times, but for the 9th iteration, displays Holberton School and then Hi on a new line.
- You must use the while loop (for and until are forbidden)
- You must use the if statement

### [5. 4 bad luck, 8 is your chance](./5-4_bad_luck_8_is_your_chance)
Write a Bash script that loops from 1 to 10 and:
- displays bad luck for the 4th loop iteration
- displays good luck for the 8th loop iteration
- displays Holberton School for the other iterations
- You must use the while loop (for and until are forbidden)
- You must use the if, elif and else statements

### [6. Superstitious numbers](./6-superstitious_numbers)
Write a Bash script that displays numbers from 1 to 20 and:
  - displays 4 and then bad luck from China for the 4th loop iteration
  - displays 9 and then bad luck from Japan for the 9th loop iteration
  - displays 17 and then bad luck from Italy for the 17th loop iteration
  - You must use the case statement

### [7. Clock](./7-clock)
* Write a Bash script that displays the time for 12 hours and 59 minutes:
  - display hours from 0 to 12
  - display minutes from 1 to 59

### [8. For ls](./8-for_ls)
* Write a Bash script that displays:
  - The content of the current directory
  - In a list format
  - Where only the part of the name after the first dash is displayed (refer to the example)
  - You must use the for loop (while and until are forbidden)
  - Do not display hidden files

### [9. To file, or not to file](./9-to_file_or_not_to_file)
* Write a Bash script that gives you information about the holbertonschool file.
- You must use if and, else (case is forbidden)
  - Your Bash script should check if the file exists and print:
    - if the file exists: holbertonschool file exists
    - if the file does not exist: holbertonschool file does not exist
  - If the file exists, print:
    - if the file is empty: holbertonschool file is empty
    - if the file is not empty: holbertonschool file is not empty
    - if the file is a regular file: holbertonschool is a regular file
    - if the file is not a regular file: (nothing)

### [10. FizzBuzz](./10-fizzbuzz)
* Write a Bash script that displays numbers from 1 to 100.
  - Displays FizzBuzz when the number is a multiple of 3 and 5
  - Displays Fizz when the number is multiple of 3
  - Displays Buzz when the number is a multiple of 5
  - Otherwise, displays the number in a list format



### [11. Read and cut](./100-read_and_cut)
- Write a Bash script that displays the content of the file /etc/passwd.
- Your script should only display:
    - username
    - user id
    - Home directory path for the user

### [12. Tell the story of passwd](./101-tell_the_story_of_passwd)
- Write a Bash script that displays the content of the file /etc/passwd, using the while loop + IFS.
Format: The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO


### [13. Let's parse Apache logs](./102-lets_parse_apache_logs)
* Write a Bash script that displays the visitor IP along with the HTTP status code from the Apache log file.


### [14. Dig the data](./103-dig_the-data)
* write a Bash script that groups visitors by IP and HTTP status code, and displays this data.
---

## Author
* **Van Phan** - [vdphan](https://github.com/vdphan)
