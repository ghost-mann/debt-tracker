import requests
import pandas as pd

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