import mysql.connector
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_database = os.getenv('DB_DATABASE')
    
conn = mysql.connector.connect(
    host = db_host,
    user = db_user,
    password = db_password,
    database = db_database
)
cursor = conn.cursor()

df= pd.read_csv('companies_revenue.csv')

for _,row in df.iterrows():
    sql = '''INSERT INTO company_revenue_data
            (
                `rank`,
                `name`, 
                industry,
                revenue_usd_millions,
                revenue_growth,
                employees,
                headquarters
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
            '''
    
    values = (
                row['Rank'],
                row['Name'],
                row['Industry'],
                row['Revenue_(USD_millions)'],
                row['Revenue_growth'],
                row['Employees'],
                row['Headquarters']  
            )
    
    cursor.execute(sql,values)

conn.commit()
cursor.close()
conn.close()

print('Data successfully inserted')

