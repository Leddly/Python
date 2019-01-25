from bs4 import BeautifulSoup as bs
import requests
import csv
import sys
import io
import datetime
import schedule
from apscheduler.schedulers.blocking import BlockingScheduler
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


page = requests.get("https://naver.com").text

soup = bs(page, 'lxml')

# print(soup.prettify())


def get_keywords():
    try:
        with open('top_20_keys.csv', 'w', encoding='UTF-8') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['Time', 'Rank', 'Keyword', 'Link'])

            for article in soup.find_all('li', class_='ah_item')[20:40]:
                # print(article.text)
                rank = article.find('span', class_='ah_r').text
                keyword = article.find('span', class_='ah_k').text
                link = article.find('a', class_='ah_a')['href']
                print(rank)
                print(keyword)
                print(link)
                now_time = str(datetime.datetime.now())
                print(now_time)
                csv_writer.writerow([now_time, rank, keyword, link])

    except Exception as e:
        print(e)


if __name__ == '__main__':
    # sch = BlockingScheduler()
    # sch.add_job(get_keywords, 'interval', seconds=30)
    # sch.start()
    # while True:
    #     schedule.every(1).minutes.do(get_keywords)
    #     schedule.run_pending()
    while True:
        get_keywords()
        time.sleep(60)
