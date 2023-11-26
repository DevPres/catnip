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
        news_list.append(*get_news_by_category(category))

    return news_list

        


def get_news_by_category(category):
    url = f'https://rss.nytimes.com/services/xml/rss/nyt/{category}.xml' 
    d = feedparser.parse(category_url)
    news_list = []
    for news in d['entries']:
        news_list.append({
            'Title': news['title'],
            'Summary': news['summary'],
            'Link': news['links'][0]['href'],
            'Published': news['published']
        })
    return news_list

