# 0x0B. SSH

## Description
What you should learn from this project:

* What is a server
* Where servers usually live
* What is SSH
* How to create an SSH RSA key pair
* How to connect to a remote host using an SSH RSA key pair
* The advantage of using  #!/usr/bin/env bash instead of /bin/bash 

## Requirements

- All files are created and compiled on Ubuntu 14.04.4 LTS
- All Bash scripts are linted with Shellcheck
- All Puppet scripts are linted with Puppet Lint 2.1.1

---

### [0. Use a private key](./0-use_a_private_key)
* Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu.
  - Only use ssh single-character flags
  - You cannot use -l
  - You do not need to handle the case of a private key protected by a passphrase



### [1. Create an SSH key pair](./1-create_ssh_key_pair)
* Write a Bash script that creates an RSA key pair.
  - Name of the created private key must be holberton
  - Number of bits in the created key to be created 4096
  - The created key must be protected by the passphrase betty
 

### [2. Client configuration file](./2-ssh_config)
* Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password.
  - Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
  - Your SSH client configuration must be configured to refuse to authenticate using a password

Share your SSH client configuration in your answer file.


### [3. Let me in!](./4-puppet_ssh_config.pp)
* Now that you have successfully connected to your server, we would also like to join the party.

### [4. Client configuration file (w/ Puppet)](./4-puppet_ssh_config.pp)

Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.

- Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
- Your SSH client configuration must be configured to refuse to authenticate using a password


---

## Author
* **Van Phan** - [vdphan](https://github.com/vdphan)
