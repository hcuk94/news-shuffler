from tmr_modules import tmr_feedprocessor

feed_url = 'https://www.telegraph.co.uk/rss.xml'

print(tmr_feedprocessor.process_feed(feed_url))
