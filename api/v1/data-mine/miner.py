#!/usr/bin/env python
# encoding: utf-8
"""
dumpimages.py
    Downloads all the images on the supplied URL, and saves them to the
    specified output file ("/test/" by default)

Usage:
    python dumpimages.py http://example.com/ [output]
"""

from bs4 import BeautifulSoup as bs
import urlparse
from urllib2 import urlopen
from urllib import urlretrieve
import os


class ParseRecipe(object):
    """ Base class for parsing recipes. """
    url = "http://www.budgetbytes.com/2012/10/curry-beef-with-peas/"
    recipe = {'itemtype': 'http://schema.org/Recipe'}

    def __init__(self):
        self.soup = ''
        self.parsed = ''
        self.get_raw_data()
        self.parse()

    def get_raw_data(self):
        """ Get raw data from the given URL """
        self.soup = bs(urlopen(self.url), "html.parser").find(attrs=self.recipe)
        self.parsed = list(urlparse.urlparse(self.url))

    def parse(self):
        self.parse_data()
        self.parse_directions()
        self.parse_ingredients()
        self.parse_image()

    def parse_data(self):
        pass

    def parse_directions(self):
        directions = self.soup.find_all(attrs='instruction')
        for direction in directions:
            print direction.decode_contents(formatter="html")

    def parse_ingredients(self):
        ingredients = self.soup.find_all(attrs='ingredient')
        for ingredient in ingredients:
            print ingredient.decode_contents(formatter="html")

    def parse_image(self):
        image = self.soup.find("img")["src"]
        filename = image.split("/")[-1]
        outpath = os.path.join('/tmp/', filename)
        urlretrieve(image, outpath)


if __name__ == "__main__":
    ParseRecipe()
