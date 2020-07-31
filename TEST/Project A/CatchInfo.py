import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://car.bitauto.com/xuanchegongju/?l=8&mid=8"

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}

html = requests.get(url, headers=headers, timeout=10)

content = html.text

soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
print(soup.title)
print(soup.title.name)
print(soup.title.string)

temp = soup.find('div', class_="search-result-list")
df = pd.DataFrame(columns=['id','car_model','lowprice','highprice','piclink'])
a_list = temp.find_all('a')

i = 0
for a_item in a_list:
    # print(a_item)

    img = a_item.find_all('img')
    # src = img['src']
    print(img[0]['src'])

    car = a_item.find(class_="cx-name text-hover")
    print(car.string)

    price = a_item.find(class_="cx-price")
    price_split = price.string.replace("万","")
    price_split = price_split.split('-')
    print(price_split)

    df = df.append({'id':i,
                    'car_model':car.string,
                    'lowprice':price_split[0],
                    'highprice': price_split[1] if len(price_split) > 1  else "",
                    'piclink':img[0]['src']}, ignore_index=True )
    i = i + 1
    # j = 0
    # td_list = tr.find_all('td')
    # for td in td_list:
    #     j = j + 1;
    #     #print(td)
    # if j != 0:
    #     #print("aa")
    #     #print(td_list, j)
    #     df = df.append({'id': td_list[0].string,
    #                     'brand': td_list[1].string,
    #                     'car_model': td_list[2].string,
    #                     'type': td_list[3].string,
    #                     'desc': td_list[4].string,
    #                     'problem': td_list[5].string,
    #                     'datetime': td_list[6].string,
    #                     'status': td_list[7].em.string}, ignore_index=True)
    # else:
    #     print("empty")
#    for td in td_list:
#        print(td)
#    print(td_list)
print(df)
df.to_csv('temp.csv', index=False)
