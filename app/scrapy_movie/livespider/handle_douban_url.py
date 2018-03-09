import os

def handle_douban_url(url):

    print('start')
    os.system(('scrapy crawl movie_from_url -a' + 'category=' + url))
    print('done')

    print('start')
    os.system(('scrapy crawl movie_from_url_2 -a' + 'category=' + url))
    print('done')
