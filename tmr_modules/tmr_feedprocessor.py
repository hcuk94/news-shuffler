import feedparser


def process_feed(url, count=10):
    data = feedparser.parse(url)
    output = []
    i = 0
    for entry in data['entries']:
        if i < count:
            output.append(entry)
            i += 1
    return output
