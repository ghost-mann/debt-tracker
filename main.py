import requests
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv


load_dotenv()

AIVEN_USER = os.getenv('AIVEN_USER')
AIVEN_PASSWORD = os.getenv('AIVEN_PASSWORD')
AIVEN_HOST = os.getenv('AIVEN_HOST')
AIVEN_PORT = os.getenv('AIVEN_PORT')
AIVEN_DBNAME = os.getenv('AIVEN_DBNAME')


debt_url = 'https://api.worldbank.org/v2/country/KE/indicator/DT.DOD.DECT.CD.?format=json'

response = requests.get(debt_url)
json_data = response.json()

records = json_data[1]

df = pd.DataFrame([{
    'country': d['country']['value'],
    'date': d['date'],
    'value': d['value']
} for d in records])


# drop rows with missing values
df = df.dropna(axis=0)


print(df)

engine = create_engine(f'postgresql://{AIVEN_USER}:{AIVEN_PASSWORD}@{AIVEN_HOST}:{AIVEN_PORT}/{AIVEN_DBNAME}?sslmode=require')
df.to_sql('external_debt', con=engine, if_exists='replace', index=False)