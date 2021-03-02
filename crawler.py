from bs4 import BeautifulSoup
import pandas as pd
import requests

count = 0
with open("C:\work\INFOSEC_CERlT_PA_ExportReport2021_02_25_11_33_17.csv") as file:
    reader = pd.read_csv(file)
    url_col = reader['Infosec URL']
    for row in url_col:
        for count in range(0, 10):
            count = count + 1
            page = requests.get(row)
            print(page.content)
            # soup = BeautifulSoup(page.content, "html.parser")

# URL="https://infosec.cert-pa.it/analyze/f15c38ca92588c369b59dd4bcdba4523.html"
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, "html.parser")
# eee = soup.find('div', "co-sm-6")
# print(eee)
