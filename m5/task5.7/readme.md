# <p align="center">__TASK 5.7__</p>

---

1. Check the implement ability of the most frequently used OPENSSH commands in the MS Windows operating system. (Description of the expected result from the commands + screenshots: command – result should be presented)

* execute command via SSH

![1](screenshots/1.png)


* send file via SSH

![1](screenshots/2.png)


* Delete the known server key

![1](screenshots/3.png)

---

2. Implement basic SSH settings to increase the security of the client-server connection (at least 3).

* change NAT to Host-only Adapter

![1](screenshots/7.png)


* check ip on this VM (hint: 192.168.56.101)

![1](screenshots/8.png)


* connecting to VM `ubuntu 2` from VM `ubuntu`

![1](screenshots/9.png)

>In the next steps I increase the security of the client-server connection

__2.1__ Change the Default SSH Port

* Change port number in `/etc/ssh/sshd_config`

![1](screenshots/10.png)


* `$ service sshd restart`

![1](screenshots/11.png)


* connecting to this VM via SSH with port 1234

![1](screenshots/13.png)


__2.2__ Enhance Linux SSH Security Using Key Pairs

* `$ ssh-kergen -t rsa` and `$ ssh-copy-id -p 1234 oleh2@192.168.56.101`

![1](screenshots/14.png)


* connecting to server (now we mustn't use password)

![1](screenshots/15.png)


__2.3__ Disable Password-Based Logins on Your Server

* Open `/etc/ssh/sshd_config`, find `PasswordAuthentication yes` and change to `PasswordAuthentication no`
![1](screenshots/16.png)

---

3. List the options for choosing keys for encryption in SSH. Implement 3 of them.

![1](screenshots/21.png)


Originally, with SSH protocol version 1 (now deprecated) only the RSA algorithm was supported. As of 2016, RSA is still considered strong, but the recommended key length has increased over time.

The SSH protocol version 2 additionally introduced support for the DSA algorithm. DSA is now considered weak and was disabled in OpenSSH 7.0.

Subsequently, OpenSSH added support for a third digital signature algorithm, ECDSA (this key format no longer uses the previous PEM file format for private keys, nor does it depend upon the OpenSSL library to provide the cryptographic implementation).

A fourth format is supported using ed25519, originally developed by independent cryptography researcher Daniel J. Bernstein.




__3.1__ RSA key pair (we can choose different bit size: 1024, 2048, 4096) It is secure (if we use bigger bit size)but also comes with an overhead in CPU time on both server and client to encrypt and decrypt with the bigger key.

* `$ ssh-keygen -t rsa -b 4096`

![1](screenshots/17.png)


* `$ ssh-copy-id -p 1234 oleh2@192.168.56.101` and `$ ssh -p 1234 oleh2@192.168.56.101`

![1](screenshots/18.png)


__3.2__ `ed25519` key pair (it's smaller and more secure than RSA)

* `$ ssh-keygen -t ed25519`

![1](screenshots/19.png)


* `$ ssh-copy-id -p 1234 oleh2@192.168.56.101` and `$ ssh -p 1234 oleh2@192.168.56.101`

![1](screenshots/20.png)


__3.3__ Elliptic Curve Digital Signature Algorithm (ECDSA) offers a variant of the Digital Signature Algorithm (DSA) which uses elliptic curve cryptography.

* `$ ssh-keygen -t ecdsa`

![1](screenshots/22.png)


* `$ ssh-copy-id -p 1234 oleh2@192.168.56.101` and `$ ssh -p 1234 oleh2@192.168.56.101`

![1](screenshots/23.png)


__3.4__ DSA (it's no longer supported)

* `$ ssh-keygen -t dsa`

![1](screenshots/24.png)


* `$ ssh-copy-id -p 1234 oleh2@192.168.56.101` and `$ ssh -p 1234 oleh2@192.168.56.101`

![1](screenshots/25.png)

* but when i try to enter to VM2 i should write my password. It happens because the new openssh version (7.0+) deprecated DSA keys and is not using DSA keys by default (not on server or client).

---

4. Implement port forwarding for the SSH client from the host machine to the guest Linux virtual machine behind NAT.

* set up NAT settings

![1](screenshots/4.png)

![1](screenshots/5.png)


* connecting to this VM using 8080 port.

![1](screenshots/6.png)

---

5. 
