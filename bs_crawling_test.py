from bs4 import BeautifulSoup as bs
import requests
import sys
import io
import csv

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


page = requests.get('http://coreyms.com').text

soup = bs(page, 'lxml')

# try:
#     with open('파일명.html') as html_file:
#     soup = bs(html_file, 'lxml')
# except Exception as e:
#     print(e)

# print(soup.prettify())

# match = soup.title.text
# return text in <title>text</title>

# match = soup.find('div')
# = soup.div

# match = soup.find('div', class_='클래스명')
# return div classed '클래스명'

# for div in soup.find_all('div'):
#     print(div.text)

# article = soup.find('article')
# print(article.prettify())

# headline = article.h2.a.text
# print(headline)

# summary = article.find('div', class_='entry-content').p.text
# print(summary)

# vid_src = article.find('iframe', class_='youtube-player')['src']
# print(vid_src)

# vid_id = vid_src.split('/')[4]
# vid_id = vid_id.split('?')[0]

# yt_link = 'https://youtube.com/watch?v={}'.format(vid_id)
#          = f'https://youtube.com/watch?v={vid_id}'
# print(yt_link)

with open('cms_scrape.csv', 'w', encoding='UTF-8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['Headline', 'Summary', 'Link'])

    for article in soup.find_all('article'):

        headline = article.h2.a.text
        summary = article.find('div', class_='entry-content').p.text
        # print(headline)
        # print(summary)

        try:
            vid_src = article.find('iframe', class_='youtube-player')['src']
            vid_id = vid_src.split('/')[4]
            vid_id = vid_id.split('?')[0]
            yt_link = f'https://youtube.com/watch?v={vid_id}'
        except Exception as e:
            print(e)
        # print(yt_link)

        csv_writer.writerow([headline, summary, yt_link])
