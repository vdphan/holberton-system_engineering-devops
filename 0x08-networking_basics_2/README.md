# 0x08. Networking basics #1

## Description
What you should learn from this project:

* What is localhost/127.0.0.1
* What is 0.0.0.0
* What is /etc/hosts
* How to display your machine’s active network interfaces

## Requirements

- All files are created and compiled on Ubuntu 14.04.4 LTS
- All files are linted with Shellcheck

---

### [0. Localhost](./0-localhost)
* What is localhost?
1. A hostname that means this IP
2. A hostname that means this computer
3. An IP attached to a computer

### [1. All IPs](./1-wildcard)
* What is 0.0.0.0?
1. All IPv4 addresses on the local machine
2. All the IPs
3. It means null in networking

### [2. Change your home IP](./2-change_your_home_IP)
- Write a Bash script that configures an Ubuntu server with the below requirements.
  - localhost resolves to 127.0.0.2
  - facebook.com resolves to 8.8.8.8.

### [3. Show attached IPs](./3-show_attached_IPs)
* Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.

### [4. Port listening on localhost](./4-port_listening_on_localhost)
* Write a Bash script that listens on port 98 on localhost.

---

## Author
* **Van Phan** - [vdphan](https://github.com/vdphan)
