# Bulker Modules
These are modules that will be in use when I create my Bulker program

## Konachan
Konachan is a Python Module with 3 classes: **Konachan**, **KonachanSearch**, and **KonachanImage**

### Konachan (Class)
This is what most people will be using to get Images. 
Parameters that the class takes:
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

**more coming soon**
