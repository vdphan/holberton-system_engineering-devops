# 0x0A Configuration management

## Description
What you should learn from this project:
- How to use Puppet

## Requirements

- All Bash files are created and compiled on Ubuntu 14.04.4 LTS
- All Puppet files are linted with Puppet Lint 2.1.1

---

### [0. Create a file](./0-create_a_file.pp)
* Using Puppet, create a file in /tmp.
  - File path is /tmp/holberton
  - File permission is 0744
  - File owner is www-data
  - File group is www-data
  - File contains I love Puppet

### [1. Install a package](./1-install_a_package.pp)
* Using Puppet, install puppet-lint.


### [2. Execute a command](./2-execute_a_command.pp)
* Using Puppet, create a manifest that kills a process named killmenow.
  - Must use the exec Puppet resource
  - Must use pkill
---

## Author
* **Van Phan** - [vdphan](https://github.com/vdphan)
