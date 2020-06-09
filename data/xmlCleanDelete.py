import os
from pathlib import Path
from collections import defaultdict
from xml.etree import ElementTree as ET

def extract_rating(folder='/home/bexx/Projects/xml_temp/ratings'):
    """Open all the XML files in a specified folder.

    Extract user_id, book_id, & isbn13 and append to a dict.
    """
    ratings = defaultdict(list)
    for f in Path(folder).iterdir(): # Iterates through the folder
        """The File should exist in the folder and must be over 1 KB in size."""
        if f.is_file(): 
            user = os.path.basename(f).split('.')[0]
            root = ET.parse(f).getroot()

            for i, r in zip(root.iter('book'), root.iter('rating')):
                if r.text != '0':
                    ratings['user_id'].append(int(user))
                    ratings['book_id'].append(int(i.find('id').text))
                    ratings['rating'].append(int(r.text))
    return dict(ratings)


def extract_meta(folder='/home/bexx/Projects/xml_temp/metadata'):
    metadata = defaultdict(list)
    for f in Path(folder).iterdir(): # Iterates through the folder

        """The File should exist in the folder."""
        if f.is_file(): 
            user = os.path.basename(f).split('.')[0] # Grabs the book id
            root = ET.parse(f).getroot()

            """Extracts metadata about the book from the XML file."""
            for b in root.findall('book'):
                metadata['book_id'].append(int(user))
                metadata['title'].append(getattr(b.find('title'), 'text', None))
                metadata['author'].append(getattr(b.find('authors//name'), 'text', None))
                metadata['isbn13'].append(getattr(b.find('isbn13'), 'text', None))
                metadata['published'].append(getattr(b.find('work//original_publication_year'), 'text', None))
                metadata['pages'].append(getattr(b.find('num_pages'), 'text', None))
                metadata['avg_rating'].append(getattr(b.find('average_rating'), 'text', None))
                metadata['count'].append(getattr(b.find('ratings_count'), 'text', None))
                metadata['lang'].append(getattr(b.find('language_code'), 'text', None))
                metadata['cover_url'].append(getattr(b.find('image_url'), 'text', None))
    return dict(metadata)


def deleter(folder='/home/bexx/Projects/xml_temp/ratings', kb=25):
    count = 0
    for f in Path(folder).iterdir():
        if os.path.getsize(f) < (1000 * kb):
            os.remove(f)
            count += 1
    print(count, "files have been deleted!")

if __name__ == "__main__":
    print("If you want to proceed with `deleter()` please input the path to the folder")
    deleter(input("Path ==> "))