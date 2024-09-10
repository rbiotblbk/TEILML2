import os
from pathlib import Path
import sqlite3
os.chdir(Path(__file__).parent)


# 1. DB Connection
conn = sqlite3.connect("./employeedb.db")


# 2. Create a Cursor
cursor = conn.cursor()


# 3. SQL Statement
sql = "SELECT * FROM Employee;"


# 4. Execute the SQL Statement
cursor.execute(sql)

# 5. Read the results
results = cursor.fetchall()


print(results)

# 6. Close connection
conn.close()
