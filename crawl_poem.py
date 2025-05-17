import pandas as pd
import os
import requests
import time
import random

from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
WEBDRIVER_DELAY_TIME_INT = 10



class PoemCrawler:
    def __init__(self, url, pages) -> None:
        service = Service()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.headless = True
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, WEBDRIVER_DELAY_TIME_INT)
        self.datasets = []
        self.deletion_script = 'arguments[0].parentNode.removeChild(arguments[0]);'
        self.url = url
        self.pages = pages
    def crawl_poem(self):
        for page_idx in tqdm(range(1, 4)):
            # main_url = f'https://www.thivien.net/search-poem.php?PoemType=14&Page={page_idx}'
            main_url = self.url + f'&Page={page_idx}'
            self.driver.get(main_url)
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "list-item")))

            content_tags = self.driver.find_elements(By.XPATH, '//div[@class="list-item"]')

            for content_tag in content_tags:
                try:
                    title_elem = content_tag.find_element(By.XPATH, './/h4[@class="list-item-header"]/a')
                    poem_title = title_elem.text
                    poem_url = title_elem.get_attribute('href')

                    self.driver.get(poem_url)

                    # Lấy nội dung bài thơ
                    poem_content_tag = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'poem-content')))

                    # Xoá các thẻ phụ không cần thiết (nếu có)
                    for tag in ['i', 'b']:
                        try:
                            tag_elem = poem_content_tag.find_element(By.TAG_NAME, tag)
                            self.driver.execute_script(self.deletion_script, tag_elem)
                        except:
                            pass

                    poem_content = poem_content_tag.text

                    # Lấy nguồn bài thơ nếu có
                    try:
                        poem_src = self.driver.find_element(By.XPATH, '//div[@class="small"]').text
                    except:
                        poem_src = ''

                    poem_info = {
                        'title': poem_title,
                        'content': poem_content,
                        'source': poem_src,
                        'url': poem_url
                    }

                    self.datasets.append(poem_info)
                    self.driver.back()
                except Exception as e:
                    print("❌ Error at:", poem_url)
                    print("Reason:", e)


        df = pd.DataFrame(self.datasets)
        df.to_csv('poem_dataset.csv', index=True)

def main(): 
    crawler = PoemCrawler()
if __name__ == "__main__":
    main() 