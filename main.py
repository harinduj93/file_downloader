import requests
from xml.etree import ElementTree as ET



def calculate_total_size(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    total_size = 0
    current_url_number = 1

    # Define the namespace
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    # Iterate through each <loc> element and calculate file size
    for url_element in root.findall('.//ns:loc', namespaces=ns):
        file_url = url_element.text
        file_size = get_file_size(file_url)
        print(f'File URL: {file_url}, File Size: {file_size} bytes')
        total_size += file_size
        current_url_number += 1
        print(f'total fils size current {total_size} : bytes')
        print(f'Total file size: {total_size / (1024 * 1024):.2f} MB')
        print(f'Finished calculating: {current_url_number} of {root.__sizeof__()}')

    return total_size

def get_file_size(url):
    # Make a HEAD request to get file size without downloading the file
    response = requests.head(url, timeout=10)

    # Check if the HEAD request was successful (status code 200)
    if response.status_code == 200:
        # Extract and return the content length (file size)
        return int(response.headers.get('content-length', 0))
    else:
        return 0

def download_files_from_xml(xml_file):
    #total_size = calculate_total_size(xml_file)

    # Display total file size
    #print(f'Total file size: {total_size / (1024 * 1024):.2f} MB')

    # Ask for confirmation to download
    #confirmation = input('Do you want to download these files? (yes/no): ')

    #if confirmation.lower() != 'yes':
    #    print('Download aborted.')
    #    return

    # Parse the XML file and start downloading
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Define the namespace
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    for url_element in root.findall('.//ns:loc', namespaces=ns):
        file_url = url_element.text
        download_file(file_url)

def download_file(url):
    # Extract the file name from the URL
    file_name = url.split('/')[-1]

    # Make a request to download the file
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the file
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f'Successfully downloaded: {file_name}')
    else:
        print(f'Failed to download: {url}, Status code: {response.status_code}')

# Example usage


xml_file_path = 'sitemap_manuale.xml'
download_files_from_xml(xml_file_path)
