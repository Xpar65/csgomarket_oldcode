import requests
import csv
from bs4 import BeautifulSoup
def pricefinder_souvenir(condition, soup):
    divs = soup.find_all(lambda tag: tag.name == "a" and condition in tag.get_text() and 'Souvenir' in tag.get_text())
    for div in divs:
        if 'bitskins-button' not in div.get('class'):
            price_span = div.find('span', class_='pull-right')
            if price_span:
                price = price_span.get_text(strip=True)
                return price
            else:
                return None
        return None

url = 'https://csgostash.com/skin/432' # make a for loop to loop through all skins
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

Souv_BS_price = pricefinder_souvenir('Battle-Scarred',soup)
Souv_WW_price = pricefinder_souvenir('Well-Worn',soup)
Souv_FT_price = pricefinder_souvenir('Field-Tested',soup)
Souv_MW_price = pricefinder_souvenir('Minimal Wear',soup)
Souv_FN_price = pricefinder_souvenir('Factory New',soup)

print(Souv_BS_price)
print(Souv_WW_price)
print(Souv_FT_price)
print(Souv_MW_price)
print(Souv_FN_price)
