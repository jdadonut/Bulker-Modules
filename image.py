from bs4 import BeautifulSoup
import urllib.request as req
import urllib

class KonachanImage:
    def __init__(self, url):
        self.url = url
        self.headers = None
        self.extension = '.jpg'
    def init_headers(self, headers):
        self.headers = headers
    def __repr__(self):
        if self.url:
            return 'Konachan Photo Object with url %s' % self.url
        else:
            return 'Konachan Photo Object with no url.'
    def __str__(self):
        if self.url:
            return 'Konachan Photo Object with url %s' % self.url
        else:
            return 'Konachan Photo Object with no url.'
    def get(self):
        if self.headers:
            htmldata = req.urlopen(req.Request(self.url, headers=self.headers))
        else:
            htmldata = req.urlopen(self.url)
        htmldata = BeautifulSoup(htmldata, 'html.parser')
        image = htmldata.find(id="image")['src']
        alt = htmldata.find(id="image")['alt']
        if image.endswith('sample.jpg'):
            x=1
            image = htmldata.find(id="highres-show")['href']
        try:
            if self.headers:
                image_data = req.urlopen(req.Request(image, headers=self.headers))
            else:
                image_data = req.urlopen(image)
        except urllib.error.HTTPError:
            
            image = image.replace("image", "jpeg")
            if self.headers:
                image_data = req.urlopen(req.Request(image, headers=self.headers))
            else:
                image_data = req.urlopen(image)
        return image_data.read()

                


    
"""
https://konachan.net/sample/68261c849024411ce7c430d6c2f56130/Konachan.com%20-%20309823%20sample.jpg
https://konachan.net/image/68261c849024411ce7c430d6c2f56130/Konachan.com%20-%20309823%20black_hair%20bow%20brown_eyes%20kazuharu_kina%20long_hair%20original%20rain%20school_uniform%20skirt%20water%20wristwear.jpg
"""