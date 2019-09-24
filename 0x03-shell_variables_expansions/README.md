# 0x03. Shell, init files, variables and expansions

## Learning Objectives

Variables

- What is the difference between a local and a global variable
- What is a reserved variable
- How to create, update and delete shell variables
- What are the roles of the following reserved variables: HOME, PATH, PS1
- What are special parameters
- What is the special parameter \$??

Expansions

- What is expansion and how to use them
- What is the difference between single and double quotes and how to use them properly
- How to do command substitution with \$() and backticks

Shell Arithmetic

- How to perform arithmetic operations with the shell


## Requirements

- All files are created and compiled on Ubuntu 14.04.4 LTS
- All Bash scripts are linted with Shellcheck

## Tasks

### [0. o](./0-alias)

- Create a script that creates an alias.
  - Name: ls
  - Value: rm \*

```sh
julien@ubuntu:/tmp/0x03$ ls
0-alias  file1  file2
julien@ubuntu:/tmp/0x03$ source ./0-alias
julien@ubuntu:/tmp/0x03$ ls
julien@ubuntu:/tmp/0x03$ \ls
```

### [1. Hello you](./1-hello_you)

- Create a script that prints hello user, where user is the current Linux user.

```sh
julien@ubuntu:/tmp/0x03$ id
uid=1000(julien) gid=1000(julien) groups=1000(julien),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare)
julien@ubuntu:/tmp/0x03$ ./1-hello_you
hello julien
```

### [2. The path to success is to take massive, determined action](./2-path)

- Add /action to the PATH.
  /action should be the last directory the shell looks into when looking for a program.

```sh
julien@ubuntu:/tmp/0x03$ echo $PATH
/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
julien@ubuntu:/tmp/0x03$ source ./2-path
julien@ubuntu:/tmp/0x03$ echo $PATH
/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/action
```

### [3. If the path be beautiful, let us not ask where it leads](./3-paths)

- Create a script that counts the number of directories in the PATH.

```sh
julien@ubuntu:/tmp/0x03$ echo $PATH
/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
julien@ubuntu:/tmp/0x03$ . ./3-paths
11
julien@ubuntu:/tmp/0x03$ PATH=/home/julien/bin:/home/julien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:::::/hello
julien@ubuntu:/tmp/0x03$ . ./3-paths
12
```

### [4. Global variables](./4-global_variables)

- Create a script that lists environment variables.

```sh
julien@ubuntu:/tmp/0x03$ source ./4-global_variables
CC=gcc
CDPATH=.:~:/usr/local:/usr:/
CFLAGS=-O2 -fomit-frame-pointer
COLORTERM=gnome-terminal
CXXFLAGS=-O2 -fomit-frame-pointer
DISPLAY=:0
DOMAIN=hq.garrels.be
e=
TOR=vi
FCEDIT=vi
FIGNORE=.o:~
G_BROKEN_FILENAMES=1
GDK_USE_XFT=1
GDMSESSION=Default
GNOME_DESKTOP_SESSION_ID=Default
GTK_RC_FILES=/etc/gtk/gtkrc:/nethome/franky/.gtkrc-1.2-gnome2
GWMCOLOR=darkgreen
GWMTERM=xterm
HISTFILESIZE=5000
history_control=ignoredups
HISTSIZE=2000
LOGNAME=franky
[...]
```

### [5. Local variables](./5-local_variables)

- Create a script that lists all local variables and environment variables, and functions.

```sh
julien@ubuntu:/tmp/0x03$ . ./5-local_variables
BASH=/bin/bash
BASHOPTS=checkwinsize:cmdhist:complete_fullquote:expand_aliases:extglob:extquote:force_fignore:histappend:interactive_comments:progcomp:promptvars:sourcepath
BASH_ALIASES=()
BASH_ARGC=()
BASH_ARGV=()
BASH_CMDS=()
BASH_COMPLETION_COMPAT_DIR=/etc/bash_completion.d
BASH_LINENO=()
BASH_REMATCH=()
BASH_SOURCE=()
BASH_VERSINFO=([0]="4" [1]="3" [2]="46" [3]="1" [4]="release" [5]="x86_64-pc-linux-gnu")
BASH_VERSION='4.3.46(1)-release'
[...]
```

### [6. Local variable](./6-create_local_variable)

- Create a script that creates a new local variable.
  - Name: BETTY
  - Value: Holberton

### [7. Global variable](./7-create_global_variable)

- Create a script that creates a new global variable.
  - Name: HOLBERTON
  - Value: Betty

### [8. Every addition to true knowledge is an addition to human power](./8-true_knowledge)

- Write a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.

```sh
julien@production-503e7013:~$ export TRUEKNOWLEDGE=1209
julien@production-503e7013:~$ ./8-true_knowledge | cat -e
1337$
```

### [9. Divide and rule](./9-divide_and_rule)

- Write a script that prints the result of POWER divided by DIVIDE, followed by a new line.
  - POWER and DIVIDE are environment variables

```sh
julien@production-503e7013:~$ export POWER=42784
julien@production-503e7013:~$ export DIVIDE=32
julien@production-503e7013:~$ ./9-divide_and_rule | cat -e
1337$
```

### [10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath](./10-love_exponent_breath)

- Write a script that displays the result of BREATH to the power LOVE
  - BREATH and LOVE are environment variables
  - The script should display the result, followed by a new line

```sh
julien@production-503e7013:~/$ export BREATH=4
julien@production-503e7013:~/$ export LOVE=3
julien@production-503e7013:~/$ ./10-love_exponent_breath
64
```

### [11. There are 10 types of people in the world -- Those who understand binary, and those who don't](./11-binary_to_decimal)

- Write a script that converts a number from base 2 to base 10.
  - The number in base 2 is stored in the environment variable BINARY
  - The script should display the number in base 10, followed by a new line

```sh
julien@production-503e7013:~/$ export BINARY=10100111001
julien@production-503e7013:~/$ ./11-binary_to_decimal
1337
```

### [12. Combination](./12-combinations)

- Create a script that prints all possible combinations of two letters, except oo.
  - Letters are lower cases, from a to z
  - One combination per line
  - The output should be alpha ordered, starting with aa
  - Do not print oo
  - Your script file should contain maximum 64 characters

```sh
julien@ubuntu:/tmp/0x03$ echo $((26 ** 2 -1))
675
julien@ubuntu:/tmp/0x03$ ./12-combinations | wc -l
675
julien@ubuntu:/tmp/0x03$
julien@ubuntu:/tmp/0x03$ ./12-combinations | tail -303 | head -10
oi
oj
ok
ol
om
on
op
oq
or
os
```

### [13. Floats](./13-print_float)

- Write a script that prints a number with two decimal places.
  - The number will be stored in the environment variable NUM.

```sh
ubuntu@ip-172-31-63-244:~/0x03$ export NUM=0
ubuntu@ip-172-31-63-244:~/0x03$ ./13-print_float
0.00
ubuntu@ip-172-31-63-244:~/0x03$ export NUM=98
ubuntu@ip-172-31-63-244:~/0x03$ ./13-print_float
98.00
ubuntu@ip-172-31-63-244:~/0x03$ export NUM=3.14159265359
ubuntu@ip-172-31-63-244:~/0x03$ ./13-print_float
3.14
```

### [14. Decimal to Hexadecimal](./14-decimal_to_hexadecimal)

- Write a script that converts a number from base 10 to base 16.
  - The number in base 10 is stored in the environment variable DECIMAL
  - The script should display the number in base 16, followed by a new line

```sh
julien@production-503e7013:~/$ export DECIMAL=16
julien@production-503e7013:~/$ ./14-decimal_to_hexadecimal
10
julien@production-503e7013:~/$ export DECIMAL=1337
julien@production-503e7013:~/$ ./14-decimal_to_hexadecimal | cat -e
539$
julien@production-503e7013:~/$ export DECIMAL=15
julien@production-503e7013:~/$ ./14-decimal_to_hexadecimal | cat -e
f$
```

### [17. Everyone is a proponent of strong encryption](./100-rot13)

- Write a script that encodes and decodes text using the rot13 encryption. Assume ASCII.

```sh
julien@production-503e7013:~/shell/fun_with_the_shell$ cat quote
"Everyone is a proponent of strong encryption."
- Dorothy E. Denning
julien@production-503e7013:~/shell/fun_with_the_shell$ ./100-rot13 < quote
"Rirelbar vf n cebcbarag bs fgebat rapelcgvba."
- Qbebgul R. Qraavat
```

### [18. The eggs of the brood need to be an odd number](./101-odd)

- Write a script that prints every other line from the input, starting with the first line.

```sh
ubuntu@ip-172-31-63-244:/$ \ls -1
bin
boot
dev
etc
home
initrd.img
lib
lib32
lib64
libx32
lost+found
media
mnt
opt
proc
root
run
sbin
srv
ubuntu@ip-172-31-63-244:/$ \ls -1 | ./101-odd
bin
dev
home
lib
lib64
lost+found
mnt
proc
run
srv
t
t~
usr
vmlinuz
```

## Author

- **Van Phan** - [vdphan](https://github.com/vdphan)
 
