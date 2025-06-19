import requests

debt_url = 'https://api.worldbank.org/v2/country/all/indicator/DT.DOD.DECT.CD.?format=json'

response = requests.get(debt_url)
data = response.json()
print(data)

