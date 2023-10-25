import requests
from lxml import etree
import lxml.html
import csv

url = "https://www.amalgama-lab.com/songs/1/1975/about_you.html"

def parse(url):
    try:
        api = requests.get(url)
    except:
        return
    tree = lxml.html.document_fromstring(api.text)
    text_original = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
    text_translate = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/text()')
    with open('text.csv', 'w', newline='') as file:
        write = csv.writer(file)
        for i in range(len(text_original)):
            write.writerow([text_original[i]])
            write.writerow([text_translate[i]])

def main():
    parse(url)

if __name__ == '__main__':
    main()