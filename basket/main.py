from bs4 import BeautifulSoup
import requests


a = requests.get(' http://basket.com.ua')
soup = BeautifulSoup(a.content, 'lxml')
els_ul_new = soup.find_all('div', {'class': 'ul_new'})
els_arr = []
for el in els_ul_new:
    a_href_el = BeautifulSoup(el, 'lxml')


