import os
from pathlib import Path
import sqlite3
os.chdir(Path(__file__).parent)


# 1. DB Connection
conn = sqlite3.connect("./employeedb.db")


# 2. Create a Cursor
cursor = conn.cursor()


# 3. SQL Statement
data = ("Mean", "Meier", 2, 66)
sql = "INSERT INTO Employee (FirstName, LastName, FK_CityID, Age) VALUES(?,?,?,?);"


# 4. Execute the SQL Statement
with conn:
    cursor.execute(sql, data)
    print(cursor.lastrowid)

# 5.


print()

# 6. Close connection
conn.close()
