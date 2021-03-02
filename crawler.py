from bs4 import BeautifulSoup
import pandas as pd
import requests

count = 0
with open("test.csv", encoding="ISO-8859-1") as file:
    df = pd.DataFrame()
    reader = pd.read_csv(file)
    url_col = reader['Infosec URL']
    for row in url_col:
        page = requests.get(row)
        soup = BeautifulSoup(page.content, "html.parser")
        tab = soup.find_all('div', "col-sm-6")
        Packer = tab[3].find('tbody').find_all('td')
        p = []
        for packers in Packer:
            p.append(packers.string)
        df = df.append([p], ignore_index=False)
        # to_append = p
        # df.loc[len(df)] = to_append
        # print(p)
        # print(count)
        count = count + 1
    df.to_csv("result.csv", header=True)

        # pac = pd.DataFrame([p], columns=['Packers1', 'Packers2', 'Packers3', 'Packers4', 'Packers5'])
        # pac.to_csv(list.csv)
        # pac = []
        # pac.append(packers.string)
        # pac_col = reader['Packer1']
        # pac_col[count] = pac
        # reader.to_csv("list.csv")
