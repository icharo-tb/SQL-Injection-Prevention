<div align='center'>
    <h1>SQL Injection Prevention (PostgreSQL)<h1>
</div>

This repository was mainly made as an investigation and trial about SQL Injection attacks. SQL Injection is one of the attacks that can deal a several impact over a database when using queries as inputs. Therefore, in PostgreSQL there is a ```PREPARE footable ([columns]) AS mode```.

If we take a look at the [official documentation](https://www.postgresql.org/docs/current/sql-prepare.html), we can see that a plan can be set for a certain table when we execute ```SELECT``` , ```INSERT```, ```UPDATE```, ```DELETE``` or ```VALUES``` statement.

I encountered several error when I tried to replicate this into my code, since once you call ```PREPARE```, it apparently cannot be called again, which makes it a one time statement on the actual table. Nonetheless, I could try other aspects like using a ```.ini``` file for database parameters or getting a deeper knowledge of how **psycopg2** works.

![](Assets/Screenshot_16.png)