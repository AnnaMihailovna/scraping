import requests
from lxml import etree
import lxml.html
import csv

url = "https://www.amalgama-lab.com/songs/1/1975/about_you.html"

def parse(url):
    api = requests.get(url)
    tree = lxml.html.document_fromstring(api.text)
    text_original = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
    print(text_original)

def main():
    parse(url)

if __name__ == '__main__':
    main()