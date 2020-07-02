# Bulker Modules
These are modules that will be in use when I create my Bulker program

## Konachan
Konachan is a Python Module with 3 classes: **Konachan**, **KonachanSearch**, and **KonachanImage**

### Konachan (Class)
This is what most people will be using to get Images. 
Parameters that the class takes on initilaization:
1. `destination`, which defaults to `C:\temp\`
2. `s`, a shortening of Safe to set whether or not to download Safe images off of KonaChan. Defaults to `True`
3. `q`, a shortening of Questionable to set whether or not to download Questionable images off of KonaChan. Defaults to `False`
4.  `e`, a shortening of Explicit to set whether or not to download Explicit images off of KonaChan. Defaults to `False`

Where `instance` is an instance of the Konachan class, there is one callable funciton (more to be added later) named `getImages`.
`getImages` takes in 2 parameters:
1. `tags`, which is to be passed as a list of strings, each of them being valid tags or else no pictures will be downloaded
2. `pages`, which is the amount of pages for the crawler to go through for images

`getImages` then uses the url of the image to generate a name for the image, places it in `directory` and finalizes the export of the image.
A built in feature, due to the continuity of id's, is that if an image file is found at a place with the same id as an image being exported, it will be skipped and no unneccesary network data will be received.

### KonachanImage (Class)
This represents an image on Konachan.
Parameters that this class takes on initialization:
1. `url`, the url of the post on Konachan

where `instance` is an instance of the KonachanImage class, there are 2 callable funcitons:
1. `instance.init_headers(headers)`This initialises any custom headers you would like to use in accesssing the image
    Parameters `init_headers()`takes:
    1. `headers`, a dict key:value set of http headers.
2. `instance.get()`, which takes no parameters and returns the bytes of the image at the post defined in the url of `__init__`


### KonachanSearch (Class)
This represents a search query on Konachan
Parameters this class takes on initialization:
1. `tags`, a list of tags.
2. `safe`, a boolean specifying whether or not to grab listings of Safe images on Konachan. Defaults to `True`
3. `questionable`, a boolean specifying whether or not to grab listings of Questionable images on Konachan. Defaults to `False`
4. `explicit`, a boolean specifying whether or not to grab listings of Explicit images on Konachan. Defaults to `False`

where `instance` is an instance of KonachanSearch there are 2 callable functions:
1. `instance.init_headers(headers)`This initialises any custom headers you would like to use in accesssing the search pages
    Parameters `init_headers()`takes:
    1. `headers`, a dict key:value set of http headers.
2. `instance.get(pages)`, which takes one parameter and returns a list of links to listings.
    Parameters `get()`takes:
    1. `pages`, an integer amounting to the number of pages to search through for listings. Defaults to `1`.

