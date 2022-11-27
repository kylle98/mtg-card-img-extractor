from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getImgLink(url):
    with usingBrowser as driver:
        driver.get(url)
        try:
            waitingForLoad = WebDriverWait(driver, 5)
            waitingForLoad.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.card-image-front[_ngcontent-serverApp-c57]')))
            htmlCode = driver.page_source
            bsElement = BeautifulSoup(htmlCode, "html.parser")
            results = bsElement.find('img', class_="card-img-top")
            return results['src']
        finally:
            driver.quit()

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    usingBrowser = webdriver.Chrome(options=options)

    url = str(input("Enter the link from mtg.dragonshield.com "))
    print(getImgLink(url))
