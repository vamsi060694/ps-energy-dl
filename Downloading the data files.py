from os.path import basename
import requests
from bs4 import BeautifulSoup

url = 'https://www.cnlopb.ca/information/statistics/#rm'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


sources = []
for link in soup.find_all('a'):
    if 'pdf' in link['href']:
        sources.append(link.get('href'))


websites = []
for source in sources:
    websites = list(filter(lambda source: (source.split('/')[-2] == 'hebstats' or source.split('/')[-2] == 'hibstats'
                                           or source.split('/')[-2] == 'nastats' or source.split('/')[-2] == 'tnstats'
                                            or source.split('/')[-2] == 'wrstats'), sources))

for website in websites:
    req = requests.get(website)
    with open(basename(website), 'wb') as file:
        file.write(req.content)
