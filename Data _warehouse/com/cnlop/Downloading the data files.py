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

names = []
reference = ['hebstats', 'hibstats', 'nastats', 'wrstats', 'tnstats']


def get_urls(sources, reference):
    names = [n for n in sources if
             any(m in n for m in reference)]
    return names


websites = get_urls(sources, reference)

for website in websites:
    req = requests.get(website)
    with open(basename(website), 'wb') as file:
        file.write(req.content)
