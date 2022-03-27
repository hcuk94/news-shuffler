import config
from tmr_modules import tmr_feedprocessor
from tmr_modules import tmr_shuffleandcut
from tmr_modules import tmr_htmlify

if __name__ == '__main__':
    all_data = []
    for source in config.sources:
        if config.sources[source]['enabled'] is True:
            feed = config.sources[source]['url']
            items_in = tmr_feedprocessor.process_feed(feed, config.num_items_in)
            items_out = tmr_shuffleandcut.shuffle_cut(items_in, config.num_items_out)
            for item in items_out:
                item['source'] = config.sources[source]['name']
                all_data.append(item)
    s_all_data = tmr_shuffleandcut.shuffle_cut(all_data, config.num_items_total)
    print(tmr_htmlify.htmlify(s_all_data))
