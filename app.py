import requests
from bs4 import BeautifulSoup

google = requests.get('https://www.google.com/')
# print(google.status_code)
# print(google.headers)
src = google.content
soup = BeautifulSoup(src, 'lxml')
links = soup.find_all('a')

for link in links:
    url = link.get('href')
    print(url)