import feedparser

CATEGORIES = [
    'Arts',
    'ArtandDesign',
    'Music',
    'Theater',
    'Climate',
    'Space',
    'Technology',
    'Science'
]

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
            'Title': news['title'],
        })
    return news_list

