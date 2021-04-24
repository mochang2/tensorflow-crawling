from requests import get
from bs4 import BeautifulSoup

"""
#당근마켓 중고거래 인기매물
source = get("https://www.daangn.com/hot_articles").content
soup = BeautifulSoup(source, "html.parser")
results = soup.select("img")

print(len(results))

for result in results:
    if "https://dnvefa72aowie.cloudfront.net/origin/article/202011/5b083e86126b9882390dfff26a7b\
ef11cfa3f11805046807fec6185713f62e6d.webp?q=82&s=300x300&t=crop" == result.get("src"):
        print(result.get("src"))
        break

"""

"""
#네이버 증권거래 사이트에서 주요 뉴스들을 발췌하는 코드

source = get("http://finance.naver.com/")
source.raise_for_status()
source.encoding = "euc-kr"
html = source.text

soup = BeautifulSoup(html, "html.parser")
results = soup.select("div.news_area ul")  #div아래의 ul 를 구분할 때는 띄어쓰기만 하면 됨
#select("ul")만 했을 경우 원하는 ul 만이 아닌 다른 ul도 나오게 됨.
print(len(results))
for result in results:
    print(result.text)
"""
