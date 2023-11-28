import feedparser


def get_news():
    news_list = []
    for category in CATEGORIES:
        for news in get_news_by_category(category):
            news_list.append(news)

    return news_list

def get_news_by_category(category):
    url = f'https://rss.nytimes.com/services/xml/rss/nyt/{category}.xml' 
    d = feedparser.parse(url)
    news_list = []
    for news in d['entries']:
        news_list.append({
            'Description': news['description'],
        })
    return news_list

CATEGORIES = [
    'Arts',
    'Climate',
    'Space',
    'Technology',
    'Science'
]

