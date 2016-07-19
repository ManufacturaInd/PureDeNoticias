# -*- coding: utf-8 -*-
import feedparser
from itertools import chain

feeds = ['http://feeds.feedburner.com/PublicoRSS',
         'http://feeds.jn.pt/JN-Ultimas',
         'http://feeds.jn.pt/JN-Justica',
         'http://feeds.jn.pt/JN-Gente',
         'http://feeds.jn.pt/JN-Nacional',
         'http://feeds.jn.pt/JN-Mundo',
         'http://feeds.jn.pt/JN-Economia',
         'http://feeds.jn.pt/JN-Pais',
         'http://feeds.jn.pt/JN-Desporto',
         'http://feeds.feedburner.com/expresso-geral']

parsed_feeds = map(feedparser.parse, feeds)

items = chain(*map(lambda pf: pf.entries, parsed_feeds))

titles = [item.title for item in items if hasattr(item, 'title')]
for t in titles:
    print(t)
with open('headlines.txt', 'w') as fp:
    blob = '\n'.join(titles).encode('utf-8')
    fp.write(blob)
