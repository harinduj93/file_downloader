import requests
from xml.etree import ElementTree as ET

def download(url):
    print(url)
    file_name = url.split('/')[-1]

    try:
        resource = requests.get(url)
        if resource.status_code == 200:
            with open(file_name,'wb') as file:
                file.write(resource.content)
                print('file created')
    except Exception as e : print(e)


def get_urls(xml_file):

    tree = ET.parse(xml_file)
    root = tree.getroot()
    for url_elements in root.findall('.//loc'):
        file_url = url_elements.text
        print(root)

url = 'https://www.spy-shop.ro/media/custom/upload/000008718696131312_fisa_tehnica.pdf'

#download(url)
get_urls('sitemap_manuale.xml')