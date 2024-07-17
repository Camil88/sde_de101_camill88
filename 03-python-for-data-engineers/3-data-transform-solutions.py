# Question: How do you read data from a CSV file at ./data/sample_data.csv into a list of dictionaries?
import csv

data = []
data_csv = './data/sample_data.csv'
with open(data_csv, 'r') as input_data:
  reader = csv.DictReader(input_data)
  for row in reader:
	data.append(row)

# Question: How do you remove duplicate rows based on customer ID?
# ANSWER: there are no duplicated rows
unique_data = []
customer_ids = set()
duplicated_ids = set()
for row in data:
  if row['Customer_ID'] not in customer_ids:
	unique_data.append(row)
	customer_ids.add(row['Customer_ID'])
  else:
	duplicated_ids.add(row['Customer_ID'])

# Question: How do you handle missing values by replacing them with 0?
for row in data_unique:
  if not row['Age']:
	row['Age'] = 0
  if not row['Purchase_Amount']:
	row['Purchase_Amount'] = 0.0

# Question: How do you convert the Gender column to a binary format (0 for Female, 1 for Male)?
for row in data_unique:
  if row['Gender'] == 'Male':
	row['Gender'] = 1
  elif row['Gender'] == 'Female':
	row['Gender'] = 0

# Question: How do you split the Customer_Name column into separate First_Name and Last_Name columns?
for row in data_unique:
  row['Name'] = row['Customer_Name'].split()[0]
  row['Surname'] = row['Customer_Name'].split()[1]

# Question: How do you calculate the total purchase amount by Gender?	
