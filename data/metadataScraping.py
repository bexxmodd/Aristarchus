import requests
import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
from collections import defaultdict


class GoodReadsScraper():
    """This module scraps the information from the Goodreads webpage.

    Module take a list of ids as the argument it scraps the HTML pages.
    Attributes scraped: ISBN13, Author's name, Title, Number of pages, Edition,
                        Cover picture URL, Genres, Average rating, Total count.
    """
    
    def __init__(self, book_id):
        self.book_id = book_id
        # Iterates over the list of ids.
        # Gets HTMLs and stores as a list.
        self.soups = [BeautifulSoup(requests.get(f'https://www.goodreads.com/book/show/{i}').text, 'html.parser') for i in self.book_id]

    def __str__(self):
        return f"You just scrapped {len(self.book_id)} books from the Goodreads.com!"

    def html_listed(self):
        # If you want to store scraped HTML as a list
        return self.soups

    def metadata(self):
        """This method extracts full metadata from the HTML file."""
        details = defaultdict(list)
        for s, i in zip(self.soups, self.book_id):
            details['book_id'].append(i)
            details['author'].append(getattr(s.find(class_='authorName'), 'text', None))
            details['title'].append(getattr(s.find(class_="gr-h1 gr-h1--serif"), 'text', None))
            details['genre'].append(s.find_all(class_='actionLinkLite bookPageGenreLink')[:3])
            details['isbn13'].append(getattr(s.find(itemprop='isbn'), 'text', None))
            details['pages'].append(getattr(s.find(itemprop="numberOfPages"), 'text', None))
            details['released'].append(getattr(s.select_one('nobr'), 'text', None))
            details['edition'].append(getattr(s.find(itemprop="bookFormat"), 'text', None))
            details['rating'].append(getattr(s.find(itemprop="ratingValue"), 'text', None))
            details['count'].append(getattr(s.find(itemprop="ratingCount"), 'text', None))
        return details

    def cover_scraper(self):
        """This method grabs the cover picture URL.

        This portion of the text is a bit problematic
        so it's handled using a try-except function.
        """
        cover_url = defaultdict(list)
        for s, i in zip(self.soups, self.book_id):
            cover_url['book_id'].append(i)
            try:
                cover_url['url'].append(s.find(id='coverImage')['src'])
            except TypeError:
                cover_url['url'].append(np.NaN)
        return cover_url

    def description(self):
        """Extract description text in a raw format."""
        descr = defaultdict(list)
        for s, i in zip(self.soups, self.book_id):
            descr['bood_id'].append(i)
            try:
                descr['description'].append(s.find(id='description').text)
            except TypeError:
                descr['description'].append(np.NaN)
        return descr


if __name__ == "__main__":
    print('This method is intended to be used within Jupyter Notebook...')