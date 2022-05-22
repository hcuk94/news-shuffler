from tmr_modules import tmr_feedprocessor

feed_url = 'https://www.theregister.com/headlines.atom'

print(tmr_feedprocessor.process_feed(feed_url))
