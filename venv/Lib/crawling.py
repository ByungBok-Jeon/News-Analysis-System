import requests
from bs4 import BeautifulSoup
import bs4.element
import datetime


def get_naver_news_top3(date):
    # 뉴스를 가져올 링크 주소 지정
    base_url = "https://news.naver.com"
    news_params = "/main/ranking/popularDay.nhn?rankingType=popular_day&date=" + date + "&sectionId="

    # 뉴스 결과를 담아낼 dictionary
    news_dic = dict()

    # sections : '정치', '경제', '사회', '생활/문화', '세계', 'IT/과학'
    # section_ids :  URL에 사용될 뉴스  각 부문 ID
    sections = ["pol","eco", "soc", "lif", "wor", "its"]
    section_ids = ["100","101", "102", "103", "104", "105"]
    for sec, sid in zip(sections, section_ids):
        # 해당 분야 상위 뉴스 목록 주소
        news_link = base_url + news_params + sid

        # 해당 분야 상위 뉴스 HTML 가져오기
        res = requests.get(news_link)
        soup = BeautifulSoup(res.text, 'lxml')


        lis30 = soup.find_all('li', class_='ranking_item', limit=30)

        # 가져온 뉴스 데이터 정제하기
        news_list3 = []
        default_img = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=naver#"
        for li in lis30:
            news_link = base_url + li.a.attrs.get('href')

            res = requests.get(news_link)
            soup = BeautifulSoup(res.text, 'lxml')
            body = soup.find('div', class_="_article_body_contents")

            # 뉴스 본문 가져오기
            news_body = ''
            for content in body:
                if type(content) is bs4.element.NavigableString:
                    news_body += content.strip() + ' '

            news_info = {
                "title": li.a.attrs.get('title'),
                "views": li.find('div', class_="ranking_view").text,
                "link": news_link,
                "news_body": news_body,
                "image_url": li.img.attrs.get('src') if li.img else default_img
            }

            news_list3.append(news_info)

        news_dic[sec] = news_list3

    return news_dic

def crawling(date,num):
    news_dic = get_naver_news_top3(date)
    if num==4:
        for k in range(30):
            f = open(f"C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/all/news{k + 1}.txt", "w",
                     encoding="UTF8")
            f.write(news_dic['pol'][k]['news_body'])
            f.close()

        for k in range(30):
            f = open(f"C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/all/news{k + 31}.txt", "w",
                     encoding="UTF8")
            f.write(news_dic['eco'][k]['news_body'])
            f.close()

        for k in range(30):
            f = open(f"C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/all/news{k + 61}.txt", "w",
                     encoding="UTF8")
            f.write(news_dic['soc'][k]['news_body'])
            f.close()

        for k in range(30):
            f = open(f"C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/all/news{k + 91}.txt", "w",
                     encoding="UTF8")
            f.write(news_dic['lif'][k]['news_body'])
            f.close()

        for k in range(30):
            f = open(f"C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/all/news{k + 121}.txt", "w",
                     encoding="UTF8")
            f.write(news_dic['wor'][k]['news_body'])
            f.close()

        for k in range(30):
            f = open(f"C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/all/news{k + 151}.txt", "w",
                     encoding="UTF8")
            f.write(news_dic['its'][k]['news_body'])
            f.close()

    else:
        for k in range(30):
            f = open(f"C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/pol/news{k+(num*30)+1}.txt","w",encoding="UTF8")
            f.write(news_dic['pol'][k]['news_body'])
            f.close()

        for k in range(30):
            f = open(f"C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/eco/news{k+(num*30)+1}.txt", "w", encoding="UTF8")
            f.write(news_dic['eco'][k]['news_body'])
            f.close()


        for k in range(30):
            f = open(f"C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/soc/news{k+(num*30)+1}.txt", "w", encoding="UTF8")
            f.write(news_dic['soc'][k]['news_body'])
            f.close()


        for k in range(30):
            f = open(f"C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/lif/news{k+(num*30)+1}.txt", "w", encoding="UTF8")
            f.write(news_dic['lif'][k]['news_body'])
            f.close()


        for k in range(30):
            f = open(f"C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/wor/news{k+(num*30)+1}.txt", "w", encoding="UTF8")
            f.write(news_dic['wor'][k]['news_body'])
            f.close()


        for k in range(30):
            f = open(f"C:/Users/sam/PycharmProjects/sam2/venv/Lib/TextFile/its/news{k+(num*30)+1}.txt", "w", encoding="UTF8")
            f.write(news_dic['its'][k]['news_body'])
            f.close()


crawling("20200630",0)
crawling("20200629",1)
crawling("20200628",2)
crawling("20200627",3)
crawling("20200630",4)