import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers_dic = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 "
                  "Safari/537.36 "
}

resp = requests.get(url, headers=headers_dic)


# 正则预编译
repex = re.compile(r'<em class="">(?P<rank>\d)</em>'
                   r'.*?<span class="title">(?P<name>.*?)</span>'
                   r'.*?<br>(?P<year>\s+\d{4})&nbsp'
                   r'.*?<span class="rating_num" property="v:average">(?P<score>\d.\d)</span>'
                   r'.*?<span>(?P<person_nums>\d+)人评价</span>', re.S)
reiter = repex.finditer(resp.text)

# 打开文件 需要添加 newline="" 否则会在文件中的每一行多一行空白行
with open("doubanTop250.csv", mode="w", encoding="utf-8", newline="") as f:
    # 创建csvWriter
    csvwriter = csv.writer(f)

    for it in reiter:
        print(it.groupdict())
        dic = it.groupdict()
        dic['year'] = it.group("year").strip()
        csvwriter.writerow(dic.values())
        # print("排名: %s,名称: %s, 年份: %s, 评分: % s, 评价人数: %s" %
        #       (it.group("rank"), it.group("name"), it.group("year").strip(), it.group("score"), it.group("person_nums")))
