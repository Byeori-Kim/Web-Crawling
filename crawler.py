from bs4 import BeautifulSoup
import pandas as pd
import requests

count = 0
# with open("list.csv") as file:
#     reader = pd.read_csv(file)
#     url_col = reader['Infosec URL']
#     for row in url_col:
#         for count in range(0, 10):
#             count = count + 1
#             page = requests.get(row)
#             soup = BeautifulSoup(page.content, "html.parser")

URL="https://infosec.cert-pa.it/analyze/36e7f674ff9146b0c6555ecfe9a124fc.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
tab = soup.find_all('div', "col-sm-6")
Packer = tab[3].find('tbody').find_all('td')
for packers in Packer:
    print(packers)
