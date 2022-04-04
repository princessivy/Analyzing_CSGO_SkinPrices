import time
from random import randrange
import pandas as pd
import requests
import json
from os.path import exists


def crawl(url, headers, payload):
    return requests.request("GET", url, headers=headers, data=payload)


def getitems(len_data, new_content):
    print(len_data)
    new_content = json.loads(new_content.text)

    new_content = new_content['items']
    new_content[0]

    dataframe = pd.DataFrame()
    for x in range(len(new_content)):
        dataframe = dataframe.append(new_content[x], ignore_index=True)

    filename = 'otheritems.csv'
    file_exists = exists(filename)

    if file_exists:
        importdata = pd.read_csv(filename)

        importdata = importdata.append(dataframe)

        importdata.to_csv(r'otheritems.csv', index=False, header=True)

    else:
        dataframe.to_csv(r'otheritems.csv', index=False, header=True)

    print('sleep between 5 and 8')
    time.sleep(randrange(5, 8))

    if len_data % 200 == 0:
        print('sleep between 15 and 20')
        time.sleep(randrange(15, 20))

    return len_data + len(new_content)


# ------------------------- "MAIN" ---------------------
# niederländisch
headers = {
    'authority': 'skinport.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://skinport.com/market',
    'accept-language': 'en-US,en;q=0.9,de;q=0.8',
    'cookie': '_csrf=aSHXW0i0BqHR5Fgz0XaXvYSa; _ga_JQVJ6LN9T1=GS1.2.1648471793.33.1.1648472362.0; _uetsid=3e247ac0aa7a11ec948c9dfb3e28890e; _uetvid=ecbbbf709b2911ec963d7fb4fccb78de; _ga=GA1.2.1986073750.1647510032; i18n=en',
    #'cookie': '_ga=GA1.2.1386586545.1647510646; _ga_JQVJ6LN9T1=GS1.2.1648199171.7.1.1648200308.0; _csrf=JIdz0aIFwmBDMJkpEbWUhb-1; i18n=en; _uetsid=d0c24b30ac1a11eca9829791195b73df; _uetvid=b7744a50a5d711ecab65a78535785b0d',
    'if-none-match': 'W/"1a245-K9N7ToUaxCvUjzLf8iNCzUooBug"'
}


# englischer header
payload = {}
headers = {
    'authority': 'skinport.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://skinport.com/market',
    'accept-language': 'en-US,en;q=0.9,de;q=0.8',
    'cookie': '_ga=GA1.2.1386586545.1647510646; _ga_JQVJ6LN9T1=GS1.2.1648199171.7.1.1648200308.0; _csrf=JIdz0aIFwmBDMJkpEbWUhb-1; i18n=en; _uetsid=d0c24b30ac1a11eca9829791195b73df; _uetvid=b7744a50a5d711ecab65a78535785b0d',
    'if-none-match': 'W/"1a245-K9N7ToUaxCvUjzLf8iNCzUooBug"'
}
# get Categories from CSGO
answ_categories = requests.request("GET", 'https://skinport.com/static/locales/en.df9c27ab181f2324499d.json',
                                   headers=headers, data=payload)
answ_categories = json.loads(answ_categories.text)
categories = answ_categories['games']['730']['cat']
categories = list(categories.values())
categories  # all categories

# get Subcategories from CSGO
subcategories = answ_categories['games']['730']['subcat']
subcategories = list(subcategories.values())
subcategories

categories_w_subcategories = categories[0:6]
categories_w_subcategories  # categories with subcategories
# Knife
knifetype = ['Bayonet', 'Bowie Knife', 'Butterfly Knife', 'Classic Knife', 'Falchion Knife', 'Flip Knife', 'Gut Knife',
             'Huntsman Knife', 'Karambit', 'M9 Bayonet', 'Navaja Knife', 'Nomad Knife', 'Paracord Knife',
             'Shadow Daggers', 'Skeleton Knife', 'Stiletto Knife', 'Survival Knife', 'Talon Knife', 'Ursus Knife']
for x in range(len(knifetype)):
    knifetype[x] = knifetype[x].replace(" ", "+")
# Pistol
pistoltype = ['CZ75-Auto', 'Desert Eagle', 'Dual Berettas', 'Five-SeveN', 'Glock-18', 'P2000', 'P250', 'R8 Revolver',
              'Tec-9', 'USP-S']
for x in range(len(pistoltype)):
    pistoltype[x] = pistoltype[x].replace(" ", "+")
# Rifle
rifletype = ['AK-47', 'AUG', 'FAMAS', 'Galil AR', 'M4A1-S', 'M4A4', 'SG 553', 'AWP', 'G3SG1', 'SCAR-20', 'SSG 08']
for x in range(len(rifletype)):
    rifletype[x] = rifletype[x].replace(" ", "+")
# SMG
smgtype = ['MAC-10', 'MP5-SD', 'MP7', 'MP9', 'P90', 'PP-Bizon', 'UMP-45']
for x in range(len(smgtype)):
    smgtype[x] = smgtype[x].replace(" ", "+")
# heavy
heavytype = ['MAG-7', 'Nova', 'Sawed-Off', 'XM1014', 'M249', 'Negev']
for x in range(len(heavytype)):
    heavytype[x] = heavytype[x].replace(" ", "+")
# gloves
glovestype = ['Bloodhound Gloves', 'Driver Gloves', 'Hand Wraps', 'Hydra Gloves', 'Moto Gloves', 'Specialist Gloves',
              'Sport Gloves', 'Broken Fang Gloves']
for x in range(len(glovestype)):
    glovestype[x] = glovestype[x].replace(" ", "+")

for cat in categories_w_subcategories:
    if cat == "Knife":
        specifictype = knifetype
    elif cat == "Pistol":
        specifictype = pistoltype
    elif cat == "Rifle":
        specifictype = rifletype
    elif cat == "SMG":
        specifictype = smgtype
    elif cat == "Heavy":
        specifictype = heavytype
    elif cat == "Gloves":
        specifictype = glovestype
    else:
        break

    for type in specifictype:
        namesubsub = []
        for countsub in range(1, 10):
            url = "https://skinport.com/api/item-menus/find?appid=730&category=" + str(cat) + "&page=" + str(
                countsub) + "&type=" + str(type)
            answer = requests.request("GET", url, headers=headers, data=payload)
            subsub = json.loads(answer.text)
            for anzahl in range(0, 50):
                try:
                    namesubsub.append(subsub['result']['items'][anzahl]['family'])
                except:
                    break
        for x in range(len(namesubsub)):
            namesubsub[x] = namesubsub[x].replace(" ", "+")
        # ab hier ziehe daten aus subsub; davor: hole subsub
        len_data = 0
        for items in namesubsub:
            for length in range(0, 21):
                print("we're on page " + str(length))
                url = "https://skinport.com/api/browse/730?cat=" + str(cat) + "&type=" + str(type) + "&item=" + str(
                    items) + "&skip=" + str(length)
                print(url)
                new_content = crawl(url, headers, payload)
                try:
                    len_data = getitems(len_data, new_content)
                except:
                    break

            print("sleep 30 secs between subcategories")
            time.sleep(30)

##### TEST

categories_wo_subcategories = categories[6:]
categories_wo_subcategories
res = ['Container', 'Graffiti', 'Music Kit', 'Pass', 'Patch', 'Sticker']

for cat in res: #categories_wo_subcategories:
    namesub = []
    for countsub in range(1, 25):
        url = "https://skinport.com/api/item-menus/find?appid=730&category=" + str(cat) + "&page=" + str(countsub)
        answer = requests.request("GET", url, headers=headers, data=payload)
        subsub = json.loads(answer.text)
        for anzahl in range(0, 50):
            try:
                namesub.append(subsub['result']['items'][anzahl]['family'])
            except:
                break

    for x in range(len(namesub)):
        namesub[x] = namesub[x].replace(" ", "+")
        namesub[x] = namesub[x].replace("|", "%7C")
        namesub[x] = namesub[x].replace("'", "%27")

    len_data = 0
    for items in namesub:
        for length in range(0, 21):
            print("we're on page " + str(length))
            url = "https://skinport.com/api/browse/730?cat=" + str(cat) + "&item=" + str(items) + "&skip=" + str(length)
            print(url)
            new_content = crawl(url, headers, payload)
            try:
                len_data = getitems(len_data, new_content)
            except:
                break

        print("sleep 20 secs between subcategories")
        time.sleep(30)

daten = pd.read_csv("allitems.csv")
daten
daten['salePrice'].tail(13)
len(daten)
list(daten)
daten

r = requests.get("https://api.skinport.com/v1/items", params={
    "app_id": 730,
    "currency": "EUR",
    "tradable": 0
}).json()

len(r)
r[2]

r = requests.get("https://api.skinport.com/v1/sales/out-of-stock", params={
    "app_id": 730,
    "currency": "EUR"
}).json()

r[2]

'''
# war kaputt hier
url = "https://skinport.com/api/browse/730?cat=Container&item=Shattered+Web+Case&skip=3"

antw = requests.request("GET", url, headers=headers, data=payload)

new_content = json.loads(new_content.text)

new_content = new_content['items']

new_content
'''