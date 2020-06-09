import requests
from xml.etree import ElementTree as ET

path = '/home/bexx/Projects/xml_temp/metadata'

def metadata_xml(booklist):
    for i in booklist:
        try:
            r = requests.get(f"https://www.goodreads.com/book/show/{i}.xml?key=NZvIBzkjE7u5asRBO8eHA")
            with open(f'{path}/{i}.xml', 'wb') as f:
                f.write(r.content)
        except:
            pass

if __name__ == '__main__':
    print("This function requieres list of book ids")