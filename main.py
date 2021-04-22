import requests
from bs4 import BeautifulSoup
import lxml
import datetime as dt
from datetime import timedelta
import csv

#---Variables and Lists---#
start = dt.datetime(2017, 5, 14)
weeks = 200
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "PHPSESSID=ujcg3i01jv2r2scjnr3teep4d2; arp_scroll_position=196",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
week_list = []
book_ranks = []
book_titles = []
book_authors = []
book_publishers = []
book_agents = []

#---Functions---#
def dates (start, weeks):
    new_date = start + timedelta(days=7*weeks)
    new_date_f = new_date.strftime("%Y-%m-%d")
    return (new_date_f)

#---Scraping---#
for i in range (0,weeks):
    response = requests.get(f'https://www.amazon.com/charts/{dates(start,i)}/mostsold/nonfiction?ref=chrt_bk_nav_back', headers = headers)
    data = response.text
    soup = BeautifulSoup(data,"lxml")

    week_data = ((soup.find(name= 'span', class_ = "kc-title-week"))).getText().strip()
    rank_data = ((soup.find_all(class_ = "kc-rank-card-rank")))
    for item in rank_data[:20]:
        rank = item.getText().strip()
        book_ranks.append(rank)
        week_list.append(week_data)

    title_data = ((soup.find_all(class_ = "kc-rank-card-title")))
    for item in title_data[:20]:
        title = item.getText().strip()
        book_titles.append(title)

    author_data = ((soup.find_all(class_="kc-rank-card-author")))
    for item in author_data[:20]:
        author = item.getText().split("by")[1].strip()
        book_authors.append(author)

    publisher_data = ((soup.find_all(class_="kc-rank-card-publisher")))
    for item in publisher_data[:20]:
        pub = item.getText().split("PUBLISHER: ")[1].strip()
        book_publishers.append(pub)

    try:
        agent_data = ((soup.find_all(class_="kc-rank-card-agent")))
    except:
        book_agents.append("n/a")
    else:
        for item in agent_data[:20]:
            agent = item.getText().split("AGENT: ")[1].strip()
            book_agents.append(agent)

#---Testing---#
# print (week_list)
# print (book_ranks)
# print (book_titles)
# print (book_authors)
# print (book_publishers)
# print (book_agents)

#---Save as .csv---#
with open('books.csv', 'w') as file:
    books = csv.writer(file)
    books.writerows(zip(week_list, book_ranks, book_titles, book_authors, book_publishers, book_agents))


