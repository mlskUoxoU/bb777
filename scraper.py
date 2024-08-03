import requests
from bs4 import BeautifulSoup

# HTMLの取得(GET)

#日程url
#url="https://ana-slo.com/%E3%83%9B%E3%83%BC%E3%83%AB%E3%83%87%E3%83%BC%E3%82%BF/%E9%9D%99%E5%B2%A1%E7%9C%8C/super-concorde%E5%B8%82%E9%87%8E-%E3%83%87%E3%83%BC%E3%82%BF%E4%B8%80%E8%A6%A7/"
#日程ごとurl (2022/12/01~)
urlpd="https://ana-slo.com/"+"2024-08-01"+"-super-concorde%e5%b8%82%e9%87%8e-data/"
req = requests.get(urlpd)
req.encoding = req.apparent_encoding # 日本語の文字化け防止

# HTMLの解析
soup = BeautifulSoup(req.text,"html.parser")

# 要素の抽出
title = soup.find("title").text
#aaa = soup.select("div table tbody tr td.table_cells")

ranker = []

for s in soup.select('h2:-soup-contains("機種別データピックアップ") ~ div td')[:80]:
    ranker.append(s.get_text())



#items = bsObj.find_all("li")
#item = items.find("a").get("href")
print(ranker)