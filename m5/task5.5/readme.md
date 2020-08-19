# <p align="center">__TASK 5.5__</p>

---

0. I had some troubles with this because i chose to use Virtual Machine from GCP. But the Google Compute Engine quota module is not in the kernel. So I tryed a lot of different  ways to solve this problem. And eventually I won. In the next image you can see one of many problems.

![11](screenshots/0.png)

---

1. Connect to GCP Virtual Machine with SSH

![11](screenshots/1.png)


2. Download the packages I need

![11](screenshots/2.png)


3. I have one more hard drive (sdb)

![11](screenshots/3.png)


4. Create disk part(sdb1) with `$ parted`

![11](screenshots/4.png)


5. Create group and user "test".

![11](screenshots/5.png)



6. Open `/etc/fstab` and add one more field (previosly a created a directory `/mnt/hard`)

![11](screenshots/6.png)


7. Check for packets.

![11](screenshots/7.png)


8. Install the missing linux-generic package and additional packages. (because GCP Linux kernel don't have it)

![11](screenshots/8.png)


9. `$ mkfs.ext4 /dev/sdb1` and `$ mount /mnt/hard`

![11](screenshots/9.png)


10. We need to add quota modules to start the download.

![11](screenshots/10.png)


11. Check does it work

![11](screenshots/11.png)


12. `$ sudo quotacheck -umc /mnt/hard`

![11](screenshots/12.png)


13. Edit quotas for user "test"

![11](screenshots/13.png)


14. Check this quota for user "test"

![11](screenshots/14.png)


15. Enable quotas for `/mnt/hard`

![11](screenshots/15.png)


16. Download payload from GitHub (SP_Lab_1.rar weights 70 MB)

![11](screenshots/16.png)


17. Copy one this file. (now I have to switch to the `cmd.exe` from the `cmder.exe` because `cmder.exe` doesn't show me `mc` window )

![11](screenshots/17.png)


18. Try to copy thirt copy of my file (it will weights 210 MB so disk quota doesn't allow to copy)

![11](screenshots/18.png)


19. I choose "delete" incomplete file.

![11](screenshots/19.png)


20. `$ sudo repquota /mnt/hard`

![11](screenshots/20.png)

---

__<p align="center"> TASK  SUCCESSFULLY COMPLEATED :)</p>__
