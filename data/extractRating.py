import os
from pathlib import Path
from collections import defaultdict
from xml.etree import ElementTree as ET

def extract_rating(path="D:/xml_temp/ratings"):
    ratings = defaultdict(list)

    for p in Path(path).iterdir():
        if p.is_file():
            user = os.path.basename(p).split('.')[0]
            root = ET.parse(p).getroot()

            for i, r in zip(root.iter('book'), root.iter('rating')):
                if r.text != '0':
                    ratings['user_id'].append(user)
                    ratings['book_id'].append(i.find('id').text)
                    ratings['isbn13'].append(i.find('isbn13').text)
    return ratings

if __name__ == "__main__":
    print('Use this module within other program...')