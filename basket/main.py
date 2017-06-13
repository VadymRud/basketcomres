from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html_page = urlopen("http://basket.com.ua")
soup = BeautifulSoup(html_page)
for link in soup.findAll(attrs={'class' : 'date'}):
    print(link)