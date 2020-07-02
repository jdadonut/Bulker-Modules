import random
from .search import KonachanSearch
from .image import KonachanImage
from pathlib import Path
class Konachan:
    def __init__(self, destination='C:\\temp\\s', s=True, q=False, e=False):
        self.init = True
        self.safe = (bool(s),bool(q),bool(e))
        self.dest = destination
    def ___repr__(self):
        return 'Konachan Download Service'
    def ___str__(self):
        return 'Konachan Download Service'
    def getImages(self, tags, pages=1):
        searcher = KonachanSearch(tags, safe=self.safe[0], questionable=self.safe[1], explicit=[self.safe[2]])
        listings = searcher.get(pages=pages)
        listings = list(dict.fromkeys(listings))
        for listing in listings:
            image = KonachanImage(listing)
            image_name = listing.split("/")
            for part in image_name:
                try:
                    image_name = int(part)
                except:
                    x=1
            if type(image_name) == "str":
                image_name = "Unnamed " + "".join([random.choice([1,2,3,4,5,6,7,8,9,0]) for i in range(6)])
            else:
                image_name = str(image_name)
            if len(image_name) > 6:
                image_name = image_name[:7]
            try:
                a = open(self.dest + image_name + image.extension)
                print("File " + image_name + image.extension + " already exists. Skipping...")
            except FileNotFoundError:
                print("File " + image_name + image.extension + " doesn't exist. Exporting.")
                Path(self.dest + image_name + image.extension).touch()
                with open(self.dest + image_name + image.extension, 'bw') as export:
                    photo_bytes = image.get()
                    export.write(photo_bytes)
                    print("File was successfully exported to " + self.dest + image_name + image.extension)