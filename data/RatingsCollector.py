import requests
from xml.etree import ElementTree as ET

class RatingsCollector:
    """This module calls Goodreads API and extracts
    an XML file for all the books on a member's shelf.
    
    Parameters: user_id range & folder's path to save XML.
    """
    params = {'shelf': 'read', 'per_page': 100}
    path = '/home/bexx/Projects/xml_temp/ratings'

    def __init__(self, start_user=1, end_user=1):
        self.start_user = start_user
        self.end_user = end_user
        from xml.etree import ElementTree as ET

    def save_xml(self):
        for n in range(self.start_user, self.end_user + 1):
            try:
                r = requests.get(f"https://www.goodreads.com/review/list/{n}.xml?key=NZvIBzkjE7u5asRBO8eHA&v=2", params=self.params)
                with open(f'{self.path}/{n}.xml', 'wb') as f:
                    f.write(r.content)
            except:
                pass

if __name__ == "__main__":
    RatingsCollector(int(input('Start number: ')), int(input('End number: '))).save_xml()