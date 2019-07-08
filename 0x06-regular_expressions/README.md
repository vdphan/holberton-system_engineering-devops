# 0x06. Regular expression

## Description
What you should learn from this project:
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.
Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

'''
s@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
s@ubuntu$
s@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
s@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
'''
---

### [0. Simply matching Holberton](./0-simply_match_holberton.rb)
* 
Requirements:

The regular expression must match Holberton
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Example:
'''
s@ubuntu$ ./0-simply_match_holberton.rb Holberton | cat -e
Holberton$
s@ubuntu$ ./0-simply_match_holberton.rb "Holberton School" | cat -e
Holberton$
s@ubuntu$ ./0-simply_match_holberton.rb "Holberton School Holberton" | cat -e
HolbertonHolberton$
s@ubuntu$ ./0-simply_match_holberton.rb "Grace Hopper" | cat -e
$

'''

### [1. Repetition Token #0](./1-repetition_token_0.rb)
* 
![alt text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/repetition-token-0.png)
Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

### [2. Repetition Token #1](./2-repetition_token_1.rb)
*
![alt text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/repetition-token-1.png)
Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

### [3. Repetition Token #2](./3-repetition_token_2.rb)
* 
![alt text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/repetition-token-2.png)
Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

### [4. Repetition Token #3](./4-repetition_token_3.rb)
* 
![alt text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/repetition-token-3.png)
Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

### [5. Not quite HBTN yet](./5-beginning_and_end.rb)
* Requirements:
Requirements:

The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Example:
'''
s@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
s@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
s@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
s@ubuntu$ ./5-beginning_and_end.rbb 'h8n' | cat -e
h8n$
s@ubuntu$
$
'''

### [6. Call me maybe](./6-phone_number.rb)
*
Requirement:

The regular expression must match a 10 digit phone number
Example:
'''
s@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
s@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
s@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
s@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
s@ubuntu$
'''
### [7. OMG WHY ARE YOU SHOUTING?](./7-OMG_WHY_ARE_YOU_SHOUTING.rb)
* 
Requirement:

The regular expression must be only matching: capital letters
Example:
'''
s@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
s@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
s@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
s@ubuntu$
'''
### [8. Textme](./100-textme.rb)
* 
For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.

Requirements:

Your script should output: [SENDER],[RECEIVER],[FLAGS]
The sender phone number or name (including country code if present)
The receiver phone number or name (including country code if present)
The flags that were used.
'''
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
Google,+16474951758,-1:0:-1:0:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-10 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE2] [SVC:] [ACT:] [BINF:] [FID:] [from:+17272713208] [to:+19172319348] [flags:-1:0:-1:0:-1] [msg:136:Orbiting this at a distance of roughly ninety-two million miles is an utterly insignificant little blue green planet whose ape-descended] [udh:0:]'
+17272713208,+19172319348,-1:0:-1:0:-1
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:18572406905] [to:14022180266] [flags:-1:0:-1:-1:-1] [msg:136:Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun.] [udh:0:]'
18572406905,14022180266,-1:0:-1:-1:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:12392190384] [to:19148265919] [flags:-1:0:-1:-1:-1] [msg:99:life forms are so amazingly primitive that they still think digital watches are a pretty neat idea.] [udh:0:]'
12392190384,19148265919,-1:0:-1:-1:-1
$
'''

### [9. Pass LinkedIn technical interview level0](./101-passed_linkedin_regex_challenge.jpg)
*
Requirements:

Solve LinkedIn regex puzzle: https://engineering.linkedin.com/puzzle
Provide as an answer file a screenshot containing your contact information, including your Holberton email address
---

## Author
* **Van Phan** - [vdphan](https://github.com/vdphan)
