
import requests
import csv
from bs4 import BeautifulSoup



def scraper(number): 
    #This scrapes the data for asingle skin from CSGO stash Put in a loop so that it scrapes every page. 
    url = 'https://csgostash.com/skin/'+ str(number)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error accessing {url}: HTTP {response.status_code}")
            return
    except Exception as e:
        print(f"Exception occurred while accessing {url}: {e}")
        return
    
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    #with open(f'skin_{number}.html', 'w', encoding='utf-8') as file:
    #    file.write(soup.prettify())
    
    #with open('output.html', 'w', encoding='utf-8') as file:
    #    file.write(soup.prettify())

    title = soup.find('title').get_text(strip=True) 
    if title == 'Not Found':
        return
    skin_name = title.replace(" - CS2 Stash", "")  # Make sure the replacement text matches exactly
    weapon_name, skin = skin_name.split(" | ")
    skin_name = skin
    
    tier = tierfinder(soup)

    collection_p = soup.find('p', {'class':'collection-text-label'})
    collection = collection_p.get_text(strip=True) if collection_p else "Contraband"
    min_float_div = soup.find('div', {'class': 'marker-wrapper wear-min-value'})
    min_float = min_float_div.get_text(strip=True) if min_float_div else '0'
    max_float_div = soup.find('div', {'class': 'marker-wrapper wear-max-value'})
    max_float = max_float_div.get_text(strip=True) if max_float_div else '0'
    StatTrak = is_stattrak(soup)
    
    

    data = [skin_name, weapon_name, collection, tier, min_float, max_float, StatTrak]
    return data

def tierfinder(soup):
    tier_text = soup.find('p', {'class':'nomargin'}).get_text(strip=True)
    tiers = ['Covert', 'Classified', 'Restricted', 'Mil-Spec', 'Industrial', 'Consumer', ]
    for tier in tiers:
        if tier in tier_text:
            return tier
    return 'other'

def is_stattrak(soup):
    divs = soup.find_all(lambda tag: tag.name == "a" and 'StatTrak' in tag.get_text())
    for div in divs:
        if 'bitskins-button' not in div.get('class', []):  # Adding default empty list for safety
            price_span = div.find('span', class_='pull-right')
            if price_span:
                price = price_span.get_text(strip=True).replace("A$ ", "")
                return 1  # StatTrak available
    return 0  # StatTrak not available or conditions not met

filename = 'skindata210224v2.csv'
headings= ['Skin Name', 'Weapon Name', 'Collection', 'Tier', 'Min Float', 'Max Float', 'Is_Stattrak']
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headings)

for i in range(1, 1620):
    print(i)
    data = scraper(i)
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if data:
            writer.writerow(data)
        

