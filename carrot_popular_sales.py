#매너온도와 채팅 간의 상관관계
#매너온도와 관심 간의 상관관계
#둘 중 무엇이 더 큰지 분석

from requests import get
from bs4 import BeautifulSoup
from csv import writer

#crawl link to hot_articles
homepage_url = "https://www.daangn.com"
hot_articles_url = "https://www.daangn.com/hot_articles"
contents = get(hot_articles_url).content
soup = BeautifulSoup(contents, "html.parser")
link_to_articles = soup.select("a.card-link")

print(len(link_to_articles))
count = 0
for link_to_article in link_to_articles:
    count +=1
    #crawl manner_temparture, chatting and interest in articles
    source = get(homepage_url+link_to_article["href"]).content
    bs = BeautifulSoup(source, "html.parser")
    
    #manner_temperature
    manner_temperature = float(bs.select("dl#temperature-wrap dd")[0].text.strip()[:4])
    
    #chatting and interest
    #article_counts: 채팅 ~~ ∙ 관심 ~~ ∙ 조회 ~~ 이렇게 생겼음
    article_counts = bs.select("p#article-counts")[0].text.strip()
    first = article_counts.find("∙")
    chatting = article_counts[2:first].strip()

    article_counts = article_counts[(first+2):]
    second = article_counts.find("∙")
    interest = article_counts[2:second].strip()

    #write on csv
    f = open("carrot_popular_sales.csv", "a", newline = "")
    wr = writer(f)
    wr.writerow([manner_temperature, chatting, interest])
    f.close()

print(count)


