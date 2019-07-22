# 0x09. Web infrastructure design

## Description
What you should learn from this project:

* You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
* You must be able to explain what each component is doing
* You must be able to explain system redundancy
* Know all the mentioned acronyms: LAMP, SPOF, QPS

---

### [0. Simple web stack](./0-simple_web_stack)
- A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a LAMP stack.
Requirements:

- You must use:
  * 1 server
  * 1 web server (Nginx)
  * 1 application server
  * 1 application files (your code base)
  * 1 database (MySQL)
  * 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8


### [1. Distributed web infrastructure](./1-distributed_web_infrastructure)
- On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com.
 Requirements:

- You must add:
  * 2 servers
  * 1 web server (Nginx)
  * 1 application server
  * 1 load-balancer (HAproxy)
  * 1 set of application files (your code base)
  * 1 database (MySQL)



### [2. Secured and monitored web infrastructure](./2-secured_and_monitored_web_infrastructure)
- On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.
Requirements:

- You must add:
  * 3 firewalls
  * 1 SSL certificate to serve www.foobar.com over HTTPS
  * 3 monitoring clients (data collector for Sumologic or other monitoring services)

### [3. Scale up](./3-scale_up)
Requirements:

- You must add:
  * 1 server
  * 1 load-balancer (HAproxy) configured as cluster with the other one
  * Split components (web server, application server, database) with their own server

---

## Author
* **Van Phan** - [vdphan](https://github.com/vdphan)
