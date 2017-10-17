from bs4 import BeautifulSoup
import requests
from lxml import html

a = requests.get('http://basket.com.ua')
soup = BeautifulSoup(a.content, 'lxml')
els_ul_new = soup.find_all('div', {'class': 'ul_new'})
els_arr = []
# for el in els_ul_new:
#     a_href_el = html.fromstring(str(el))
#     urls = a_href_el.xpath('//a/@href')
#     els_arr.extend(urls)
#BeautifulSoup all
for el in els_ul_new:
    a_href_el = BeautifulSoup(str(el), 'lxml').find_all('a')
    for a_hef in a_href_el:
        print(a_hef.get(''))
        els_arr.extend(a_hef)

ur = requests.get('http://basket.com.ua/news/64893.htm')
soup_cont = BeautifulSoup(ur.content, 'lxml')

soup_cont_zagolovok = soup_cont.find('div', {'class': 'tema'}).find('h1')
soup_cont_date = soup_cont.find('div', {'class': 'tema'}).find('span').text


#//*[@id="part1_1"]/div[2]/div[2]/ul/li[1]/a
#//*[@id="wrapper"]/div[3]/div[2]/div[2]/div/div[1]/div[3]/div[1]

