import feedparser


def get_news():
    news_list = []
    for category in CATEGORIES:
        category_news = get_news_by_category(category)
        for i in range(7):
            try:
                news_list.append(category_news[i])
            except IndexError:
                pass
    print(news_list)
    return news_list


def get_news_by_category(category):
    url = f"https://rss.nytimes.com/services/xml/rss/nyt/{category}.xml"
    d = feedparser.parse(url)
    news_list = []
    for news in d["entries"]:
        news_list.append({
            "Description": news["description"],
        })
    return news_list


CATEGORIES = ["Climate", "Space", "Technology", "Science", "Arts", "Music"]
