import requests
import csv
from bs4 import BeautifulSoup
'''
Todo:

Make a method for adding new skins into db. 
'''


def scraper(number): 
    url = 'https://csgostash.com/skin/'+ str(number)
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # with open('output.html', 'w', encoding='utf-8') as file:
    #     file.write(soup.prettify())

    title = soup.find('title').get_text(strip=True) 
    if title == 'Not Found':
        return
    if 'M4A4 | Howl' in title:  #howl returns er due to contraband tier status
        return
    else:
        skin_name = title.replace(" - CS2 Stash", "") 
    
    tier = tierfinder(soup)
    if tier == 'other': #prevents knifes from being parsed and throwing ers. 
        return 
    collection = soup.find('p', {'class':'collection-text-label'}).get_text(strip=True)
    min_float = soup.find('div', {'class': 'marker-wrapper wear-min-value'}).get_text(strip=True)
    max_float = soup.find('div', {'class': 'marker-wrapper wear-max-value'}).get_text(strip=True)
    
    BS_price = pricefinder_nostattrak('Battle-Scarred',soup)
    WW_price = pricefinder_nostattrak('Well-Worn',soup)
    FT_price = pricefinder_nostattrak('Field-Tested',soup)
    MW_price = pricefinder_nostattrak('Minimal Wear',soup)
    FN_price = pricefinder_nostattrak('Factory New',soup)

    ST_BS_price = pricefinder_stattrak('Battle-Scarred',soup)
    ST_WW_price = pricefinder_stattrak('Well-Worn',soup)
    ST_FT_price = pricefinder_stattrak('Field-Tested',soup)
    ST_MW_price = pricefinder_stattrak('Minimal Wear',soup)
    ST_FN_price = pricefinder_stattrak('Factory New',soup)

    Souv_BS_price = pricefinder_souvenir('Battle-Scarred',soup)
    Souv_WW_price = pricefinder_souvenir('Well-Worn',soup)
    Souv_FT_price = pricefinder_souvenir('Field-Tested',soup)
    Souv_MW_price = pricefinder_souvenir('Minimal Wear',soup)
    Souv_FN_price = pricefinder_souvenir('Factory New',soup)

    data = [skin_name, collection, tier, min_float, max_float, BS_price, WW_price, FT_price, MW_price, FN_price, 
     ST_BS_price, ST_WW_price, ST_FT_price, ST_MW_price, ST_FN_price,Souv_BS_price,Souv_WW_price,Souv_FT_price, Souv_MW_price, Souv_FN_price]
    return data

def tierfinder(soup):
    tier = soup.find('p', {'class':'nomargin'}).get_text(strip=True)
    if 'Covert' in tier:
        tier = 'Covert'
    if 'Classified' in tier:
        tier = 'Classified'
    if 'Restricted' in tier:
        tier = 'Restricted'
    if 'Mil-Spec' in tier:
        tier = 'Mil-Spec'
    if 'Industrial' in tier:
        tier = 'Industrial'
    else:
        tier ='other'
    return tier

def pricefinder_stattrak(condition, soup):
    divs = soup.find_all(lambda tag: tag.name == "a" and condition in tag.get_text() and 'StatTrak' in tag.get_text())
    for div in divs:
        if 'bitskins-button' not in div.get('class'):
            price_span = div.find('span', class_='pull-right')
            if price_span:
                price = price_span.get_text(strip=True).replace("A$ ", "")
                return price
            else:
                return None
        return None

def pricefinder_nostattrak(condition, soup):
    divs = soup.find_all(lambda tag: tag.name == "a" and condition in tag.get_text() and 'StatTrak' not in tag.get_text())
    for div in divs:
        if 'bitskins-button' not in div.get('class'):
            price_span = div.find('span', class_='pull-right')
            if price_span:
                price = price_span.get_text(strip=True).replace("A$ ", "")
                return price
            else:
                return None
        return None

def pricefinder_souvenir(condition, soup):
    divs = soup.find_all(lambda tag: tag.name == "a" and condition in tag.get_text() and 'Souvenir' in tag.get_text())
    for div in divs:
        if 'bitskins-button' not in div.get('class'):
            price_span = div.find('span', class_='pull-right')
            if price_span:
                price = price_span.get_text(strip=True).replace("A$ ", "")
                return price
            else:
                return None
        return None


filename = 'skindata22022024.csv'
headings= ['Skin Name', 'Collection', 'Tier', 'Min Float', 'Max Float', 'BS Price A$', 'WW Price A$', 'FT Price A$', 'MW Price A$', 'FN Price A$',
           'ST BS Price A$', 'ST WW Price A$', 'ST FT Price A$', 'ST MW Price A$', 'ST FN Price A$', 'Souv BS Price A$' 'Souv WW Price A$', 'Souv FT Price A$' , 'Souv MW Price A$', 'Souv FN Price A$',]
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headings)

for i in range(1, 1587):
    print(i)
    data = scraper(i)
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if data:
            writer.writerow(data)
        

