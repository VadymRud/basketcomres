from grab import Grab

g = Grab()
url = 'http://basket.com.ua'
g.go(url)
g.setup(log_dir='log/grab')
date_div = g.doc.select('//div[@class="date"]')
news_item = g.doc.select('//div[@class="ul_new"]')
for v in news_item:
    print(v.text())

