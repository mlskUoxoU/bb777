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


rankerName = []
# ↓注意！文字列型です
rankerVal = []
vals = []

for s in soup.select('h2:-soup-contains("機種別データピックアップ") ~ div p a')[:20]:
    rankerName.append(s.get_text())
for i, s in enumerate(soup.select('h2:-soup-contains("機種別データピックアップ") ~ div td')[:80]):
    match (i+1)%4:
        case 0:
            # winrate計算
            text = s.get_text()
            pnum = text.find('/')
            rate = float(text[pnum-1]) /  float(text[pnum+1])
            
            vals.append({'WinRate':rate})
            rankerVal.append(vals)
            vals = []
        case 1:
            vals.append(s.get_text())
        case 2:
            vals.append(s.get_text())
        case 3:
            vals.append(s.get_text())

# (機種名, [機種別差枚,平均差枚,平均Ｇ数,勝率])
ranker = []

for name, val in zip(rankerName, rankerVal):
    ranker.append({name:val})

#items = bsObj.find_all("li")
#item = items.find("a").get("href")
print(ranker)