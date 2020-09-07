# <p align="center"> __TASK 3.1__ </p>

---

1. Download MySQL server for your OS on VM.
2. Install MySQL server on VM.

  ![1](screenshots/1.png)

  ![1](screenshots/2.png)

---

3. Describe the database schema, (minimum 3 tables)

  ![1](screenshots/3.png)

---

4. Create a database on the server through the console.

  * create a table with guns and a table with heroes.

  ![1](screenshots/4.png)


  * run `DESC gun` and `DESC hero`

  ![1](screenshots/5.png)



  * create table with players and run `DESC player`

  ![1](screenshots/6.png)


---

5. Fill in tables.

  * fill table with heroes

  ![1](screenshots/7.png)


  * fill table with guns

  ![1](screenshots/8.png)


  * fill table with players

  ![1](screenshots/9.png)


  * some information about players

  ![1](screenshots/10.png)


---

6. Execute SQL queries DDL, DML, DCL,

  * DDL (CREATE, ALTER, DROP...) you can see at the previous and next images.

  * DML (SELECT, INSERT, UPDATE, DELETE...) you can see at the previous images.

  * DCL (GRANT, REVOKE) you can see at the next images.

---

7. Create database users with different rights.

  * create user `oleh1` with `CREATE` and `SELECT` permissions and user `oleh2` with `DROP` permissions.

  ![1](screenshots/11.png)


  * try to do something from `oleh1`

  ![1](screenshots/12.png)


  * try to do something from `oleh2`

  ![1](screenshots/13.png)

---

8. Make a selection from the main table DBMySQL.

  * `SELECT user,authentication_string,plugin,host FROM mysql.user;` (I chose the most important variables)

  ![1](screenshots/14.png)
