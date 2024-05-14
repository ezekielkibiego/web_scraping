import requests
from bs4 import BeautifulSoup
import csv
zindua = requests.get('https://zinduaschool.com/')
# print(zindua.status_code)

if zindua.status_code == 200:
    soup = BeautifulSoup(zindua.content, 'lxml')
    h2_tags = soup.find_all('h2')
    h2_texts = [h2.text.strip() for h2 in h2_tags]
    csv_file_path = 'zindua_h2.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8' ) as csv_file:
    csv_writer = csv.writer(csv_file)
    
    csv_writer.writerow(['Zindua H2 Texts'])
    for index, text in enumerate(h2_texts, start=1):
        csv_writer.writerow([index,text])
        
        
print(f"Zindua Texts saved to '{csv_file_path}'")