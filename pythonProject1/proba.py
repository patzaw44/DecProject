import requests

response = requests.get(url='https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeId/440?format=json')
print(response)
print(response.status_code)

# data= response.json()['Results'][1]["Make_Name"]
# print(data)