1. What sequence of commands will you typically follow in Python to work with an sqlite3 database?

= connect, get a cursor, execute a command, process the results

2. What is this loop usually used for?
 
for i in cur.execute("SELECT * from table")

= to iterate on all the rows in a table
= The SELECT statement returns all the rows, and then the loop iterates through each one.

3. Which statement is true regarding the execute() method?

= It can be used for both select and nonselect queries.
= This database method is used for all query executions, including select queries that return results.

4. How can you make your program more efficient when executing database commands, and reduce the resulting disk IO?

= Commit only after a few commands are executed.