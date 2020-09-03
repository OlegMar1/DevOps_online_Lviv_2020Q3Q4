# <p align="center">__TASKK 6.2__</p>

---

1. Use  already created internal-network for three VMs (VM1-  VM3)  .  VM1 has NAT and internal, VM2, VM3 – internal only interfaces.

  * create three VM

  ![1](screenshots/1.png)


  * edit `/etc/netplan/*.yaml` for VM1 (after that run `$ netplan try` and `$ netplan apply`)

  ![1](screenshots/2.png)


  * `$ ip a` for VM1

  ![1](screenshots/3.png)


  * edit `/etc/netplan/*.yaml` for VM2 (after that run `$ netplan try` and `$ netplan apply`)

  ![1](screenshots/4.png)


  * edit `/etc/netplan/*.yaml` for VM3 (after that run `$ netplan try` and `$ netplan apply`)

  ![1](screenshots/5.png)

---

2. Install and configure DHCP server on VM1.

 2.1 __THE FIRST WAY (using dnsmasq)__

 * edit interface and listen-address in `/etc/dnsmasq.conf`

 ![1](screenshots/6.png)


 * edit dhcp-range in `/etc/dnsmasq.conf`

 ![1](screenshots/7.png)


 * check if it works: `$ systemctl restart dnsmasq` and `$ systemctl status dnsmasq`

 ![1](screenshots/10.png)

---

  2.2 __THE SECOND WAY (using VBoxManage)__

  * stop DNSMASQ

  ![1](screenshots/20.png)


  * enable dhcp for internal network "private" (range: 10.10.10.20-10.10.10.30)

  ![1](screenshots/15.png)


---

3. Check VM2 and VM3  for obtaining  network addresses from DHCP server.

  3.1 __for DMSMASQ__

  * `$ ip a` from VM2

  ![1](screenshots/11.png)


  * `$ ip a` from VM3

  ![1](screenshots/12.png)

---

  3.2 __for VBoxManage__

  * `$ dhclient -r` and `dhclient` to give a new ip for VM2. And later`$ ip a` from VM2

  ![1](screenshots/16.png)


  * `$ dhclient -r` and `dhclient` to give a new ip for VM3. And later`$ ip a` from VM3

  ![1](screenshots/17.png)


  * try to ping VM1 an VM3 from VM2

  ![1](screenshots/18.png)


  * try to ping VM1 an VM2 from VM3

  ![1](screenshots/19.png)

---

4. Using existed network for three VMs ( from p.1) install and configure DNS server on VM1. (using DNSMASQ)

   * unkoment `prepend domain-name-servers 127.0.0.1` in `/etc/dhcp/dhclient.conf`

   ![1](screenshots/8.png)


   * edit `/etc/resolv.conf`

   ![1](screenshots/9.png)

---

5. Check VM2 and VM3  for gaining access to DNS server ( naming services).

  * `$ systemd-resolve --status`

  ![1](screenshots/14.png)

---

6. ***Using the scheme which follows, configure dynamic routing using OSPF protocol.

  * looking at this scheme I didn't understand what I had to do. So I have done routing using OSPF a different way.

  ![1](screenshots/21.png)


  * edit `/etc/netplan/*.yaml` for R1

  ![1](screenshots/22.png)


  * `$ ip a` from R1 (enp0s3 = NAT; enp0s8 = INTERNAL; enp0s9 = INTERNAL)

  ![1](screenshots/23.png)


  * install `quagga `and edit `/etc/quagga/daemons`

  ![1](screenshots/24.png)


  * enable ip forwarding

  ![1](screenshots/25.png)


  * copy some files for quagga and give them `640` permissions

  ![1](screenshots/26.png)


  * change owner for this files

  ![1](screenshots/27.png)


  * add `extort VTYSH_PAGER=more` in `/etc/bash.bashrc`

  ![1](screenshots/28.png)


  * add `VTYSH_PAGER=more` in `/etc/environment`

  ![1](screenshots/29.png)


  * next I copied R1 and rename it R2


  * run `vtysh` and after that run some commands in R1

  ![1](screenshots/30.png)


  * `ip show ospf route` from R1

  ![1](screenshots/31.png)


  * edit `/etc/netplan/*.yaml` for R2

  ![1](screenshots/32.png)


  * `$ ip a` from R2 (enp0s3 = NAT; enp0s8 = INTERNAL; enp0s9 = INTERNAL)

  ![1](screenshots/33.png)


  * run `vtysh` and after that run some commands from R2 after that run `show ip ospf route`

  ![1](screenshots/34.png)


  * then i have created M1 and M2


  * edit `/etc/netplan/*.yaml` for M1

  ![1](screenshots/35.png)


  * `$ ip a` from M1 (enp0s3 = INTERNAL)

  ![1](screenshots/36.png)


  * edit `/etc/netplan/*.yaml` for M2

  ![1](screenshots/37.png)


  * `$ ip a` from M2 (enp0s3 = INTERNAL)

  ![1](screenshots/38.png)


  * ping everyone else from M1

  ![1](screenshots/39.png)


  * `mtr 10.10.2.2` from M1 (10.10.2.2 = M2)

  ![1](screenshots/40.png)


  * ping everyone else from M2

  ![1](screenshots/41.png)


  * `mtr 10.10.1.2` from M2 (10.10.1.2 = M1)

  ![1](screenshots/42.png)


  * So, ospf routing have some pitfalls, but  I think I have done it successfully. I hope you will accept this task for me! ^_^

---

__USEFUL LINKS__
* https://jonamiki.com/2020/01/29/dnsmasq-failed-to-create-listening-socket-for-port-53-address-already-in-use/
