# TheMorningReport Config File

# News Sources
sources = {
    'dailymail': {
        'enabled': True,
        'name': 'Daily Mail',
        'url': 'https://www.dailymail.co.uk/articles.rss'
    },
    'guardian': {
        'enabled': True,
        'name': 'The Guardian',
        'url': 'https://www.theguardian.com/uk/rss'
    }
}

# These values control the randomisation element.
# Total items 'shuffled' per source
num_items_in = 10
# Total items output per source
num_items_out = 3
# Grand total items to allow in amalgamated data
num_items_total = 30

# Max number of chars allowed in article summary text
summary_max_chars = 200

