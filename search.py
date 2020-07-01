from bs4 import BeautifulSoup as bs
import urllib.request as req

class KonachanSearch:
    def __init__(self, tags, safe=True, questionable=False, explicit=False):
        self.tags = tags
        self.headers = None
        self.safe = {
            'Safe': safe,
            'Questionable': questionable,
            'Explicit': explicit
        }
    def init_headers(self, headers):
        self.headers = headers
    def __repr__(self):
        if self.url:
            return 'Konachan Search Object with tags %s' % "".join(self.tags)
        else:
            return 'Konachan Search Object with no tags.'
    def __str__(self):
        if self.url:
            return 'Konachan Search Object with tags %s' % "".join(self.tags)
        else:
            return 'Konachan Search Object with no tags.'
    def get(self, pages=1):
        print(self.tags)
        pagenumber = 1
        baseurl = "https://konachan.com/post?page={0}&tags=".format(str(pagenumber))
        listings = []
        while pagenumber != pages+1:
            baseurl = "https://konachan.com/post?page={0}&tags=".format(str(pagenumber))
            url = baseurl + "+".join(self.tags)
            if self.headers:
                htmldata = req.urlopen(req.Request(url, headers=self.headers))
            else:
                htmldata = req.urlopen(req.Request(url))
                
            htmldata = bs(htmldata, features="html.parser")
            
            listings_html = htmldata.select("ul#post-list-posts li div.inner a")
            for listing in listings_html:
                rating = listing.contents
                for item in rating:
                    item = str(item).split(" ")
                    for i in item:
                        if i in ['Safe', 'Questionable', "Explicit"]:
                            if self.safe[i] == True:
                                listing_link = listing['href']
                                if listing_link.startswith("/"):
                                    listing_link = "https://konachan.com" + listing_link
                                listings.append(listing_link)
            pagenumber += 1
        return listings
