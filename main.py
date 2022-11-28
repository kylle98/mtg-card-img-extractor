from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getImgLink(url, usingBrowser):
    with usingBrowser as driver:
        driver.get(url)
        try:
            waitCondition = WebDriverWait(driver, 10)
            waitCondition.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.card-image-front[_ngcontent-serverApp-c57]')))
            htmlCode = driver.page_source
            bsParser = BeautifulSoup(htmlCode, "html.parser")
            result = bsParser.find('img', class_="card-img-top")
            if (result != None):
                if (result['src']):
                    return result['src']
                else:
                    return "Link didn't found"
            else:
                return None
        finally:
            driver.quit()

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    usingBrowser = webdriver.Chrome(options=options)

    url = str(input("Enter the link from mtg.dragonshield.com\n"))
    print("Searching in progress...\n")
    print(getImgLink(url, usingBrowser))
