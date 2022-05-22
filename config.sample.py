# TheMorningReport Config File

# News Sources
sources = {
    'bbc': {
        'enabled': True,
        'name': 'BBC News',
        'url': 'http://feeds.bbci.co.uk/news/uk/rss.xml'
    },
    'dailymail': {
        'enabled': True,
        'name': 'Daily Mail',
        'url': 'https://www.dailymail.co.uk/articles.rss'
    },
    'guardian': {
        'enabled': True,
        'name': 'The Guardian',
        'url': 'https://www.theguardian.com/uk/rss'
    },
    'independent': {
        'enabled': True,
        'name': 'The Independent',
        'url': 'https://www.independent.co.uk/rss'
    },
    'mirror': {
        'enabled': True,
        'name': 'The Mirror',
        'url': 'https://www.mirror.co.uk/?service=rss'
    },
    'sun': {
        'enabled': True,
        'name': 'The Sun',
        'url': 'https://www.thesun.co.uk/feed/'
    },
    'telegraph': {
        'enabled': True,
        'name': 'The Telegraph',
        'url': 'https://www.telegraph.co.uk/rss.xml'
    }
}

# Email Settings
from_email = ''
to_email = ''
sendgrid_api_key = ''


# These values control the randomisation element.
# Total items 'shuffled' per source
num_items_in = 50
# Total items output per source
num_items_out = 5
# Grand total items to allow in amalgamated data
num_items_total = 35

# Max number of chars allowed in article summary text
summary_max_chars = 200
