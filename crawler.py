from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import datetime

count = 1

start_row = 1

print('Crawler starting...')

with open("list.csv", encoding="ISO-8859-1") as file:
    df = pd.DataFrame()
    reader = pd.read_csv(file)
    url_col = reader['Infosec URL']

    script_start_time = datetime.now()
    for row in url_col:

        row_start_time = datetime.now()

        flag_append = 0

        if count >= start_row:
            try:
                print('currently on row {}: {} '.format(count, datetime.now() - script_start_time))

                flag_append = 0

                page = requests.get(row)
                print('  Checkpoint 1: {}'.format(datetime.now() - row_start_time))
                soup = BeautifulSoup(page.content, "html.parser")
                tab = soup.find_all('div', "col-sm-6")
                Packer = tab[3].find('tbody').find_all('td')
                p = []
                print('  Checkpoint 2: {}'.format(datetime.now() - row_start_time))
                for packers in Packer:
                    p.append(packers.string)
                print('  Checkpoint 3: {}'.format(datetime.now() - row_start_time))
                df = df.append([p], ignore_index=False)
                flag_append = 1

                print('  Checkpoint 4: {}'.format(datetime.now() - row_start_time))
                # to_append = p
                # df.loc[len(df)] = to_append
                # print(p)
                # print(count)
                df.to_csv("result.csv", header=False)
                print('  Checkpoint 5: {}'.format(datetime.now() - row_start_time))

            except:
                print('!ERROR! - row {}'.format(count))
                error_data = ['']
                if flag_append == 0:
                    df = df.append(error_data, ignore_index=False)
                else:
                    pass
            finally:
                pass

        elif count % 500 == 0:
            print('currently on row {}'.format(count))

        count = count + 1

        # pac = pd.DataFrame([p], columns=['Packers1', 'Packers2', 'Packers3', 'Packers4', 'Packers5'])
        # pac.to_csv(list.csv)
        # pac = []
        # pac.append(packers.string)
        # pac_col = reader['Packer1']
        # pac_col[count] = pac
        # reader.to_csv("list.csv")
