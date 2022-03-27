

def htmlify(data):
    html_list = []
    for item in data:
        item_html = f"""
            <div style="min-height: 100px;">
            <h1 style="font-size:20px;"><a href="{item['link']}">{item['title']}</a></h1>
            <i>{item['source']} | {item['published']}</i>
            <div style="float:left; margin-right: 5px;">
            <img src="{item['media_content'][0]['url']}"/>
            </div>
            <div>
            <p style="text-align: justify;">
              {item['summary']}
            </p>
            </div>
            </div>
        """
        html_list.append(item_html)
    return "".join(html_list)
