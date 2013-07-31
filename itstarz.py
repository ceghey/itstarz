"""
Доброе утро!
чтоб не потратить весь день в ожидании заданий написал скриптик
который каждую минуту парсит комменты и при появлении коментов
от Дарьи издаёт сигнал и выводит комент в экране терминала.

"""

import feedparser
from time import sleep
last_updated = ""
last_published = ""
AUTHOR="Daria  Zvedeninova"
while True :
    d = feedparser.parse("http://itstarz.disqus.com/it_starz_55/latest.rss")
    if d.feed.updated > last_updated :
        last_updated = d.feed.updated
        for x in reversed(range(len(d))):
            if d.entries[x].published > last_published :
                last_published = d.entries[x].published
                if d.entries[x].author == AUTHOR :
                    print('\a')
                    print(d.entries[x].published,d.entries[x].author)
                    print(d.entries[x].description)

            
    sleep(60)
