from time import sleep

import fake_useragent
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

USER_AGENT = fake_useragent.UserAgent()

def url_pages(url: str, count_pages: int):
    pages = []
    for i in range(1, count_pages):
        headers = {
            'User-Agent': USER_AGENT.random
        }
        session_requests = requests.Session()
        requests_content = session_requests.get(f'https://www.freepik.com/search?format=search&page={str(i)}&query=fabric%20care%20symbols&type=photo', headers=headers)
        pages.append(BeautifulSoup(requests_content.content))
        sleep(3)
    return pages

def download_images(url: str, count_pages: int):
    list_url_pages = url_pages(url, count_pages)
    j = 0
    for i in tqdm(list_url_pages, 'Extracting_Pages'):
        for img in i.findAll('img'):
            img_url = img.attrs.get("data-src")
            if img_url is not None:
                p = requests.get(img_url)
                out = open(f"C:/Users/opacho/Documents/dataset_CARE_LABEL/img_{str(j)}.jpg", "wb")
                out.write(p.content)
                out.close()
                j += 1

if __name__ == "__main__":
    download_images('url', count_pages=12)
