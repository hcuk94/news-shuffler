import config
from datetime import date
from tmr_modules import tmr_feedprocessor
from tmr_modules import tmr_shuffleandcut
from tmr_modules import tmr_htmlify
from tmr_modules import tmr_emailer

if __name__ == '__main__':
    all_data = []

    # Iterate over sources and process them if enabled
    for source in config.sources:
        if config.sources[source]['enabled'] is True:
            feed = config.sources[source]['url']
            items_in = tmr_feedprocessor.process_feed(feed, config.num_items_in)
            items_out = tmr_shuffleandcut.shuffle_cut(items_in, config.num_items_out)
            for item in items_out:
                item['source'] = config.sources[source]['name']
                all_data.append(item)

    # Shuffle, cut & htmlify data
    s_all_data = tmr_shuffleandcut.shuffle_cut(all_data, config.num_items_total)
    h_all_data = tmr_htmlify.htmlify(s_all_data)

    # Send Email
    today = date.today()
    date = today.strftime("%B %d, %Y")
    email_subject = f'The Morning Report for {date}'
    tmr_emailer.send_email(from_email=config.from_email, to_email=config.to_email
                           , subject=email_subject, sg_api_key=config.sendgrid_api_key
                           , html_content=h_all_data)
