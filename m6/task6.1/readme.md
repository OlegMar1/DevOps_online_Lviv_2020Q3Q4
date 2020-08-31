# <p align="center"> __TASK 6.1__ </p>

---

1. Create virtual machines connection according to figure 1:

![1](screenshots/0.png)

2. VM2 has one interface (internal), VM1 has 2 interfaces (NAT and internal). Configure all network
interfaces in order to make VM2 has an access to the Internet (iptables, forward, masquerade).

  * set "Internal network" for VM2

  ![1](screenshots/8.png)


  * edit `/etc/network/interfaces` for VM2

  ![1](screenshots/1.png)


  * `$ ip a` for VM2

  ![1](screenshots/2.png)


  * set "NAT" with port forwarding and "Internal network" for VM1

  ![1](screenshots/9.png)

  ![1](screenshots/10.png)


  * edit `/etc/network/interfaces` for VM1

  ![1](screenshots/3.png)


  * `$ ip a` for VM1

  ![1](screenshots/4.png)


  * enable ip forwarding

  ![1](screenshots/5.png)


  * add some rules for `iptables` and run `$ iptables -S` to see our rules

  ![1](screenshots/6.png)


  * save iptables rules using `$ sudo netfilter-persistent save`

  ![1](screenshots/7.png)

---

3. Check the route from VM2 to Host.

  * `$ route -n` for VM2

  ![1](screenshots/11.png)

---

4. Check the access to the Internet, (just ping, for example, 8.8.8.8).

  * `$ ping 8.8.8.8`

  ![1](screenshots/12.png)

---

5. Determine, which resource has an IP address 8.8.8.8. (hint: dns.google)

  * `$ host 8.8.8.8`

  ![1](screenshots/13.png)

---

6. Determine, which IP address belongs to resource epam.com

  * `$ nslookup epam.com` and `$ host epam.com` (hint: 3.214.134.159)

  ![1](screenshots/14.png)

---

7. Determine the default gateway for your HOST and display routing table.

  * `ipconfig` from HOST

  ![1](screenshots/16.png)

---

8. Trace the route to google.com

  * `$ mtr google.com`

  ![1](screenshots/17.png)

---

# <p align="center"> __THE END__ </p>
