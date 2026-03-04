# Python - Object-relational mapping

- **[0. Get all states](./0-select_states.py)**

- Write a script that lists all states from the database hbtn_0e_0_usa:
  - Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
  - You must use the module MySQLdb (import MySQLdb)
  - Your script should connect to a MySQL server running on localhost at port 3306
  - Results must be sorted in ascending order by states.id
  - Results must be displayed as they are in the example below
  - Your code should not be executed when imported

- **[1. Filter states](./1-filter_states.py)**

- Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
  - Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
  - You must use the module MySQLdb (import MySQLdb)
  - Your script should connect to a MySQL server running on localhost at port 3306
  - Results must be sorted in ascending order by states.id
  - Results must be displayed as they are in the example below
  - Your code should not be executed when imported

- **[2. Filter states by user input](./2-my_filter_states.py)**

- Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
  - Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
  - You must use the module MySQLdb (import MySQLdb)
  - Your script should connect to a MySQL server running on localhost at port 3306
  - You must use format to create the SQL query with the user input
  - Results must be sorted in ascending order by states.id
  - Results must be displayed as they are in the example below
  - Your code should not be executed when imported

- **[3. SQL Injection...](./3-my_safe_filter_states.py)**

- Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?
```
guillaume@ubuntu:~/$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/$
```
- What? Empty?
- Yes, it's an SQL injection to delete all records of a table…
- Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!
  - Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
  - You must use the module MySQLdb (import MySQLdb)
  - Your script should connect to a MySQL server running on localhost at port 3306
  - Results must be sorted in ascending order by states.id
  - Results must be displayed as they are in the example below
  - Your code should not be executed when imported

- **[4. Cities by states](./4-cities_by_state.py)**

- Write a script that lists all cities from the database hbtn_0e_4_usa
  - Your script should take 3 arguments: mysql username, mysql password and database name
  - You must use the module MySQLdb (import MySQLdb)
  - Your script should connect to a MySQL server running on localhost at port 3306
  - Results must be sorted in ascending order by cities.id
  - You can use only execute() once
  - Results must be displayed as they are in the example below
  - Your code should not be executed when imported

- **[5. Full description](./5-full_table.sql)**

- Write a script that prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server.
  - The database name will be passed as an argument of the mysql command
  - You are not allowed to use the DESCRIBE or EXPLAIN statements

- **[6. List all in table](./6-list_values.sql)**

- Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
  - All fields should be printed
  - The database name will be passed as an argument of the mysql command

- **[7. First add](./7-insert_value.sql)**

- Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
  - New row:
  - id = 89
  - name = Best School
  - The database name will be passed as an argument of the mysql command

- **[8. Count 89](./8-count_89.sql)**

- Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
  - The database name will be passed as an argument of the mysql command

- **[9. Full creation](./9-full_creation.sql)**

- Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
  - second_table description:
  - id INT
  - name VARCHAR(256)
  - score INT
  - The database name will be passed as an argument to the mysql command
  - If the table second_table already exists, your script should not fail
  - You are not allowed to use the SELECT and SHOW statements
  - Your script should create these records:
  - id = 1, name = "John", score = 10
  - id = 2, name = "Alex", score = 3
  - id = 3, name = "Bob", score = 14
  - id = 4, name = "George", score = 8

- **[10. List by best](./10-top_score.sql)**

- Write a script that lists all databases of your MySQL server.

- **[11. Select the best](./11-best_score.sql)**

- Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
  - Results should display both the score and the name (in this order)
  - Records should be ordered by score (top first)
  - The database name will be passed as an argument of the mysql command

- **[12. Cheating is bad](./12-no_cheating.sql)**

- Write a script that updates the score of Bob to 10 in the table second_table.
  - You are not allowed to use Bob's id value, only the name field
  - The database name will be passed as an argument of the mysql command

- **[13. Score too low](./13-change_class.sql)**

- Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
  - The database name will be passed as an argument of the mysql command

- **[14. Average](./14-average.sql)**

- Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.
  - The result column name should be average
  - The database name will be passed as an argument of the mysql command

- **[15. Number by score](./15-groups.sql)**

- Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
  - The result should display:
  - the score
  - the number of records for this score with the label number
  - The list should be sorted by the number of records (descending)
  - The database name will be passed as an argument to the mysql command

- **[16. Say my name](./16-no_link.sql)**

- Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
  - Don't list rows where the name column does not contain a value
  - Results should display the score and the name (in this order)
  - Records should be listed by descending score
  - The database name will be passed as an argument to the mysql command

- **[17. Go to UTF8](./100-move_to_utf8.sql)**

- Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
- You need to convert all of the following to UTF8:
  - Database hbtn_0c_0
  - Table first_table
  - Field name in first_table

- **[18. Temperatures #0](./101-avg_temperatures.sql)**

- Import in hbtn_0c_0 database this table dump: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/272/temperatures.sql)
- Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

- **[19. Temperatures #1](./102-top_city.sql)**

- Import in hbtn_0c_0 database this table dump: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/272/temperatures.sql) (same as Temperatures #0)
- Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

- **[20. Temperatures #2](.103-max_state.sql)**

- Import in hbtn_0c_0 database this table dump: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/272/temperatures.sql) (same as Temperatures #0)
- Write a script that displays the max temperature of each state (ordered by State name).
