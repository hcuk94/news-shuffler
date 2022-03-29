import feedparser
import config
import re


def _remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, ' ', text)


def _truncate_text(text, length=config.summary_max_chars):
    """Truncate text over a certain char length"""
    if len(text) > length:
        text = text[0:length] + "..."
    return text


def process_feed(url, count=10):
    """Main feed processing function"""
    data = feedparser.parse(url)
    output = []
    i = 0
    for entry in data['entries']:
        if i < count:
            # Strip HTML & truncate summary
            if "summary" in entry:
                summ_raw = entry['summary']
                summ_strip = _remove_html_tags(summ_raw)
                entry['summary'] = _truncate_text(summ_strip)
            else:
                entry['summary'] = ''

            # Handle RSS feeds with no image
            if "media_content" not in entry:
                entry['media_content'] = [
                    {'url': ''}
                ]

            # Append item to output
            output.append(entry)
            i += 1
    return output
