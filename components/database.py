import requests

def databaseCatalog(data):
    url = 'http://localhost:2000/catalog'

    response = requests.post(url, json=data, verify=False)

    if response.status_code == 200:
        print('Item added with sucess!')
    else:
        print('Failed to add item:', response.text)
