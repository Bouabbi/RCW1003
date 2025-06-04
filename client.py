import requests

#url = 'http://localhost:8000'
url = 'https://rcw1003--inst01-bubbh6gbgrhcb4ad.canadaeast-01.azurewebsites.net/'

response = requests.get(url)
response =response.json()
print(response['message'])
