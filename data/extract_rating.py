import os
from pathlib import Path
from collections import defaultdict
from xml.etree import ElementTree as ET

def extract_rating(path="D:/xml_temp"):
    ratings = defaultdict(list)
    for p in Path("D:/xml_temp").iterdir():
        if p.is_file():
            user = os.path.basename(p).split('.')[0]
            root = ET.parse(p).getroot()
            for i, r in zip(root.iter('book'), root.iter('rating')):
                if r.text != '0':
                    ratings['user_id'].append(user)
                    ratings['book_id'].append(i.find('id').text)
                    ratings['ratings'].append(r.text)
    return ratings

if __name__ == "__main__":
    extract_rating()