import random
import csv
import requests
from lxml import etree

headers = {
    "Cookie": "_lxsdk_cuid=182eda46939c8-0dfdc4b4d8a0a2-1b565635-13c680-182eda4693ac8; _lxsdk=182eda46939c8-0dfdc4b4d8a0a2-1b565635-13c680-182eda4693ac8; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _lxsdk_s=182ee5cd0b1-6e3-3f6-f24%7C%7C1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",

}


proxy ={
    "http":"http://216.250.156.85:80"
}
csvHeaders=["rank","name","time","price","avg_price","cc"]
# 解析数据并写入
def date_parsee_and_write(data):
    html = etree.HTML(data)

    dict={}
    dict['name']=html.xpath('//ul/li/p[@class="first-line"]/text()')
    dict['time']=html.xpath('//ul/li/p[@class="second-line"]/text()')
    dict['rank']=html.xpath('//div[@id="ranks-list"]/ul/li[@class="col0"]/text()')
    dict['price'] = html.xpath('//div[@id="ranks-list"]/ul/li[contains(@class,"col3")]/text()')
    dict['avg_price'] = html.xpath('//div[@id="ranks-list"]/ul/li[contains(@class,"col3")]/text()')
    dict['cc'] = html.xpath('//div[@id="ranks-list"]/ul/li[contains(@class,"col4")]/text()')
    with open("maoyan.csv", mode='w', encoding="utf-8") as f:
        writer = csv.DictWriter(f, csvHeaders)
        writer.writeheader()
        for i in range(len(dict['name'])):
            try:
             dt={}
             dt['name']=dict['name'][i]
             dt['time'] = dict['time'][i]
             dt['rank'] = dict['rank'][i]
             dt['price'] = dict['price'][i]
             dt['avg_price'] = dict['avg_price'][i]
             dt['cc'] = dict['cc'][i]
             print(dt)
             writer.writerow(dt)
            except Exception as ex:
                print("写入错误")
                continue

# 获取页面
def get_page_data(url):
    try:
        resp = requests.get(url,timeout=10,headers=headers, proxies=proxy)
        if resp.status_code == 200:
            return resp.text
        else:
           return None
    except Exception:
        print("获取超时，正在重试......")
        get_page_data(url)


if __name__ == '__main__':
    url = "https://piaofang.maoyan.com/rankings/year"
    data = get_page_data(url)
    print(data)
    date_parsee_and_write(data)