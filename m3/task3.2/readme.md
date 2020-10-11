# <p align="center"> __TASK 3.2__ </p>

---

1. Make backup of your database.

  ![1](screenshots/1.png)

---

2. Delete the table and / or part of the data in the table.

  ![1](screenshots/2.png)

---

3. Restore your database.

  ![1](screenshots/3.png)

---

4. Transfer your local database to RDS AWS.

  * so, i tried to connect to RDS database, but I couldn't do it because my default VPS forbade me to do so. And i needed to create a new VPC group.

  * create new VPC

  ![1](screenshots/4.png)


  * create two subnets for my new VPC

  ![1](screenshots/5.png)


  * create new Internal fateway

  ![1](screenshots/6.png)


  * create new route table and add one rule.

  ![1](screenshots/7.png)


  * add two rules for default security group

  ![1](screenshots/8.png)


  * turn on `Public accessibility` in the finished database

  ![1](screenshots/9.png)


  * also, when I was creating my instance, i added an empty DB with the same name as the DB in the backup file.


  * copy endpoint

  ![1](screenshots/10.png)


  * run `mysql -h database-3.cepkgcv3gubv.eu-central-1.rds.amazonaws.com -u admin -p -P 3306 < gamedb.sql` and as you can see, I did it successfully! My DB is in RDS.

  ![1](screenshots/11.png) 
