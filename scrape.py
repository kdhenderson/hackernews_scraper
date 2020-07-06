import requests
from bs4 import BeautifulSoup
import pprint

links = []
subtext = []

for pageNum in range(1,3):
    res = requests.get(f'https://news.ycombinator.com/news?p={pageNum}')
    soup = BeautifulSoup(res.text, 'html.parser')
    links.extend(soup.select('.storylink'))
    subtext.extend(soup.select('.subtext'))

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))