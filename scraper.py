from random import sample

from bs4 import BeautifulSoup
from selenium import webdriver


url = 'https://color.adobe.com/explore/?filter=most-popular&time=all'

driver = webdriver.Firefox()
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
outer_divs = soup.find_all('div', 'ctooltip')

one_div = sample(outer_divs, 1)[0]
color_divs = one_div.find_all('div')
colors = set()
for div in color_divs:
    color = div['style'][-6:]
    colors.add(color)
    
for color in colors:
    print(color)



    