import requests
from bs4 import BeautifulSoup
response=requests.get('https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=New-Delhi')
# print(response.status_code)

soup=BeautifulSoup(response.content,'html.parser')
# print(soup.prettify())

'''methods -
find('a') -find first anker tag
find_all('div') -all 
find_parent('a')
find_next_sibiling(a)'''


cards = soup.find_all('div',attrs={'class':"l-srp__results flex__item"})
# print(card)

for card in cards:
    price= card.find('div',attrs={'class':"m-srp-card__price"})
    # print(price.text)
    title= card.find('span',attrs={'class':'m-srp-card__title__bhk'})
    # print(title.text.strip('\n'))
    carpet_area=card.find('div',attrs={'class':"m-srp-card__summary__info"})
    # print(carpet_area.text)
    data ="{} {} {}".format(title.text.strip('\n'),price.text,carpet_area.text)
    print(data)