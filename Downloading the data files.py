import requests

file_url = 'https://www.cnlopb.ca/wp-content/uploads/hebstats/heb_oil_2017.pdf'

req = requests.get(file_url)
with open('Heborn_well_2017.pdf', 'wb') as file:
    file.write(req.content)
