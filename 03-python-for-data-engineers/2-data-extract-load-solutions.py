# Databases: When reading or writing to a database we use a database driver. Database drivers are libraries that we can use to read or write to a database.
# Question: How do you read data from a sqlite3 database and write to a DuckDB database?

# SQLite
import sqlite3

path = 'C:/sqlite/chinook.db'
sqlite_conn = sqlite3.connect(path)

customers = sqlite_conn.execute(
    "SELECT * FROM customers LIMIT 10;"
).fetchall()

print(customers)

# DuckDb
import duckdb  # duckdb database driver

duckdb_conn = duckdb.connect("duckdb.db")
insert_query = f"""
INSERT INTO Customer (customer_id, zipcode, city, state_code, datetime_created, datetime_updated)
VALUES (?, ?, ?, ?, ?, ?)
"""

duckdb_conn.executemany(insert_query, customers)

duckdb_conn.commit()
sqlite_conn.close()
duckdb_conn.close()
