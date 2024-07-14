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

# API
# Question: How do you read data from the CoinCap API given below and write the data to a DuckDB database?
# URL: "https://api.coincap.io/v2/exchanges"
# Hint: use requests library
import duckdb
import requests

# API endpoint
url = "https://api.coincap.io/v2/exchanges"
response = requests.get(url)
data = response.json()["data"]

# Connect to the DuckDB
duckdb_conn = duckdb.connect("duckdb.db")

# Insert data into the DuckDB Exchanges table
insert_query = """
INSERT INTO Exchanges (id, name, rank, percentTotalVolume, volumeUsd, tradingPairs, socket, exchangeUrl, updated)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

# Prepare data for insertion
insert_data = [
    (
        exchange["exchangeId"],
        exchange["name"],
        int(exchange["rank"]),
        (
            float(exchange["percentTotalVolume"])
            if exchange["percentTotalVolume"]
            else None
        ),
        float(exchange["volumeUsd"]) if exchange["volumeUsd"] else None,
        exchange["tradingPairs"],
        exchange["socket"],
        exchange["exchangeUrl"],
        int(exchange["updated"]),
    )
    for exchange in data
]

duckdb_conn.executemany(insert_query, insert_data)

# Commit and close the connection
duckdb_conn.commit()
duckdb_conn.close()

# Web scraping
# Questions: Use beatiful soup to scrape the below website and print all the links in that website
# URL of the website to scrape
import requests
from bs4 import BeautifulSoup

url = 'https://example.com'

# Send a GET request
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.content, 'html.parser')

# Find and print all the links on the webpage
for link in soup.find_all('a'):
    print(link.get('href'))

https://www.iana.org/domains/example

