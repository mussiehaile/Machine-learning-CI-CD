import os
import wget
import requests

url = 'https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/383116/rawdata_new.csv?sequence=1&isAllowed=y'
csv_file = "data.csv"

response = requests.get(url)

if response.status_code == 200:
    with open(csv_file, 'wb') as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print("Error downloading file.")

