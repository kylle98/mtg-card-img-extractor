from bs4 import BeautifulSoup
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
UsingBrowser = webdriver.Chrome(options=options)

def getImgLink(url):

    UsingBrowser.get(url)
    time.sleep(1)

    html = UsingBrowser.page_source

    sourceCode = BeautifulSoup(html, "html.parser")
    searchingResults = sourceCode.find('img', class_="card-img-top")

    return searchingResults['src']

if __name__ == "__main__":
    url = str(input("Enter the link from mtg.dragonshield.com "))
    print(getImgLink(url))
