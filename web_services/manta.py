
import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

url = "hhttps://www.manta.com/mb_51_ALL_8LK/baltimore_md"
br = mechanize.Browser()
urls = [url]
visited = [url]
while len(urls)>0:
    try: 
        br.open(urls[0])
        urls.pop(0)    
        for link in br.links():
            newurl = urlparse.urljoin(link.base_url,link.url)
            b1 = urlparse.urlparse(newurl).hostname
            b2 = urlparse.urlparse(newurl).path
            newurl =  "http://"+b1+b2

            if newurl not in visited and urlparse.urlparse(url).hostname in newurl:
                urls.append(newurl)
                visited.append(newurl)
                print newurl
    except:
        print "error"
        urls.pop(0)