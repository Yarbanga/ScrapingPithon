import time

import requests
from bs4 import BeautifulSoup
import time

links = []

for i in range(25):
    url = 'http://example.webscraping.com/places/default/index/' + str(i)
    response = requests.get(url)
    print(response)
    if response.ok:
        print('page: ' + str(1))
        soup = BeautifulSoup(response.text)
        tds = soup.findAll('td')
        for td in tds:
            a = td.find('a')
            link = a['href']
            links.append('http://example.webscraping.com' + link)
        time.sleep(1)
    print(len(links))





















































# Code 1 crapping d'un site
# import urllib.request, urllib.error, urllib.parse
#
# url = 'https://smt-group.net/'
#
# reponse = urllib.request.urlopen(url)
# contenu_web = reponse.read().decode('UTF-8')
#
# f = open('obo-t17800628-33.html', 'w')
# f.write(contenu_web)
# f.close





















# nom = input("Quel est votre nom ? ")
# age = input("Quel est votre age ? ")

# try:
#     age_prochain = int(age) + 1
# except:
#     print("ERREUR: Vous devez rentrer un nombre pour l'âge")

# else:
#     print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
#     print("L'an prochain vous aurez " + str(age_prochain) + " ans")