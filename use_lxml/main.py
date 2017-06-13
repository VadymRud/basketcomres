from urllib.request import urlopen
import lxml.html as html
import lxml.etree as etree
from pyquery import PyQuery as pq
dol = pq(url='http://basket.com.ua/')
datas = dol('#part1_1').children()
print(len(datas[4]))

for data in datas[4]:
    if data.attrib['class'] == 'date':
        date = data.text
        print(data.text.strip())

# #     aft2 = dol2('div')
#     for af in aft2:
#         if af.attrib['class'] == 'date':
#             print(af.attrib['class'])
#             break
#     # next_dat = aft.getroot().find_class('date')
#     # if next_dat != None:
#     #     break
#     print(aft2.text)

# page = html.parse('http://basket.com.ua')
#
# e = page.getroot().find_class('date')
# for el in e:
#     print(el.text)

