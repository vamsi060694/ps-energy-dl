from os.path import basename
import requests

urls = [
    'https://www.cnlopb.ca/wp-content/uploads/hebstats/heb_oil_2017.pdf',
    'https://www.cnlopb.ca/wp-content/uploads/hebstats/heb_oil_2018.pdf',
    'https://www.cnlopb.ca/wp-content/uploads/hebstats/heb_oil_2019.pdf',
    'https://www.cnlopb.ca/wp-content/uploads/hebstats/heb_oil_2020.pdf',
    'https://www.cnlopb.ca/wp-content/uploads/hebstats/heb_oil_2021.pdf'
    ]

for url in urls:
    req = requests.get(url)
    with open(basename(url), 'wb') as file:
        file.write(req.content)
