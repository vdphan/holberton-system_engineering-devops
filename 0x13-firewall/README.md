# 0x13. Firewall

## Tasks

### [0. Firewall ABC](./0-firewall_ABC)

Pick one answer for every question.

- What is a firewall?

  - A hardware security system
  - A hardware or software security system
  - A software security system

- What are the 2 types of firewall:

  - Soft and hard firewall
  - Incoming and outgoing firewall
  - Network and host-based firewall

- What is the main function of a firewall?
  - To filter incoming and outgoing network traffic
  - To filter incoming and outgoing TCP traffic
  - To filter outgoing traffic


### [1. Block all incoming traffic but](./1-block_all_incoming_traffic_but)
* Let’s install the ufw firewall and setup a few rules on web-01.
- The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)
- Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
  - 22 (SSH)
  - 443 (HTTPS SSL)
  - 80 (HTTP)
- Share the ufw commands that you used in your answer file


### [2. Port forwarding](./100-port_forwarding)
* Firewalls can not only filter requests, they can also forward them.
- Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.
- Your answer file should be a copy of the ufw configuration file that you modified to make this happen

---

## Author
* **Van Phan** - [vdphan](https://github.com/vdphan)
