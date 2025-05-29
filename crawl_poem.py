import pandas as pd
import os
import requests
import time
import random
import argparse
from urllib.parse import urljoin

from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

# Thêm fake_useragent
try:
    from fake_useragent import UserAgent
    ua = UserAgent()
except ImportError:
    ua = None

WEBDRIVER_DELAY_TIME_INT = 10
MAX_RETRIES = 3
RETRY_DELAY = 5

class PoemCrawler:
    def __init__(self, base_url, max_poem_type, pages_per_type, output, start_poem_type=1):
        service = Service()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        # Random User-Agent
        if ua:
            user_agent = ua.random
        else:
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        chrome_options.add_argument(f'user-agent={user_agent}')
        # Chặn tải ảnh, font, css
        prefs = {"profile.managed_default_content_settings.images": 2,
                 "profile.managed_default_content_settings.fonts": 2,
                 "profile.managed_default_content_settings.stylesheets": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.headless = True
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, WEBDRIVER_DELAY_TIME_INT)
        self.base_url = base_url
        self.max_poem_type = max_poem_type
        self.pages_per_type = pages_per_type
        self.output = output
        self.datasets = []
        self.deletion_script = 'arguments[0].parentNode.removeChild(arguments[0]);'
        self.start_poem_type = start_poem_type

    def wait_for_element(self, by, value, timeout=WEBDRIVER_DELAY_TIME_INT):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            return None

    def get_category(self):
        header_xpath = '//header[@class="page-header"]'
        for retry in range(3):
            try:
                header_elem = self.driver.find_element(By.XPATH, header_xpath)
                b_elems = header_elem.find_elements(By.TAG_NAME, 'b')
                for b in b_elems:
                    text = b.text.strip()
                    if text:
                        return text
            except Exception:
                pass
            time.sleep(1)
        print("[WARNING] Không tìm thấy category header trên trang này.")
        return ""

    def process_poem(self, content_tag):
        try:
            # Extract title from header
            header = content_tag.find_element(By.CLASS_NAME, "list-item-header")
            a_title = header.find_element(By.TAG_NAME, "a")
            title = a_title.text.strip()
            poem_url = a_title.get_attribute('href')
            poem_url = urljoin("https://www.thivien.net", poem_url)

            # Extract detail div
            detail_divs = content_tag.find_elements(By.XPATH, './/div[contains(@class, "list-item-detail")]')
            if not detail_divs:
                print("[WARNING] Không tìm thấy detail_div trong content_tag này.")
                return None
            detail_div = detail_divs[0]

            # Get all <a> tags in detail_div
            a_tags = detail_div.find_elements(By.TAG_NAME, 'a')
            # Get author
            author = ""
            for a in a_tags:
                href = a.get_attribute('href')
                if href and '/author-' in href:
                    author = a.text.strip()
                    break

            # Get poem content
            current_url = self.driver.current_url
            for retry in range(MAX_RETRIES):
                try:
                    self.driver.get(poem_url)
                    time.sleep(random.uniform(1, 2))
                    content_elem = self.wait_for_element(By.XPATH, '//div[contains(@class, "poem-content")]')
                    content = content_elem.text if content_elem else ""
                    break
                except Exception as e:
                    if retry == MAX_RETRIES - 1:
                        print(f"Failed to get poem content after {MAX_RETRIES} retries: {e}")
                        content = ""
                    time.sleep(RETRY_DELAY)
            # Go back to the list page
            self.driver.get(current_url)

            return {
                'title': title,
                'author': author,
                'content': content,
                'category': self.get_category(),
                'poem_type': self.current_poem_type
            }
        except Exception as e:
            print(f"Error processing poem: {e}")
            return None

    def crawl_poem(self):
        for poem_type in tqdm(range(self.start_poem_type, self.max_poem_type + 1)):
            self.current_poem_type = poem_type
            for page_idx in range(1, self.pages_per_type + 1):
                url = f"{self.base_url}?PoemType={poem_type}&Page={page_idx}"
                for retry in range(MAX_RETRIES):
                    try:
                        self.driver.get(url)
                        time.sleep(random.uniform(2, 4))  # tăng thời gian chờ
                        # Lưu HTML để debug nếu cần
                        with open(f"debug_{poem_type}_{page_idx}.html", "w", encoding="utf-8") as f:
                            f.write(self.driver.page_source)
                        # Sửa XPATH cho chắc chắn
                        content_tags_xpath = '//div[contains(@class, "list-item")]'
                        content_tags = self.driver.find_elements(By.XPATH, content_tags_xpath)
                        if not content_tags:
                            print(f"[WARNING] Không tìm thấy bài thơ nào với XPATH này trên {url}")
                            break
                        print(f"[DEBUG] PoemType={poem_type}, Page={page_idx}, Found {len(content_tags)} poems at {url}")
                        poem_infos = []
                        for content_tag in content_tags:
                            try:
                                # Kiểm tra tồn tại header
                                header_list = content_tag.find_elements(By.TAG_NAME, "h4")
                                if not header_list or not header_list[0].get_attribute("class") or "list-item-header" not in header_list[0].get_attribute("class"):
                                    continue  # Bỏ qua nếu không có header đúng
                                header = header_list[0]
                                a_title = header.find_element(By.TAG_NAME, "a")
                                title = a_title.text.strip()
                                poem_url = urljoin("https://www.thivien.net", a_title.get_attribute('href'))
                                detail_div_list = content_tag.find_elements(By.CLASS_NAME, "list-item-detail")
                                if not detail_div_list:
                                    continue
                                detail_div = detail_div_list[0]
                                a_tags = detail_div.find_elements(By.TAG_NAME, 'a')
                                author = ""
                                for a in a_tags:
                                    href = a.get_attribute('href')
                                    if href and '/author-' in href:
                                        author = a.text.strip()
                                        break
                                poem_infos.append({'title': title, 'poem_url': poem_url, 'author': author})
                            except Exception as e:
                                print(f"Error extracting poem info: {e}")
                                continue
                        for info in poem_infos:
                            content = ""
                            for retry2 in range(MAX_RETRIES):
                                try:
                                    self.driver.get(info['poem_url'])
                                    time.sleep(random.uniform(1, 2))
                                    content_elem = self.wait_for_element(By.XPATH, '//div[contains(@class, "poem-content")]')
                                    content = content_elem.text if content_elem else ""
                                    break
                                except Exception as e:
                                    if retry2 == MAX_RETRIES - 1:
                                        print(f"Failed to get poem content after {MAX_RETRIES} retries: {e}")
                                        content = ""
                                    time.sleep(RETRY_DELAY)
                            self.datasets.append({
                                'title': info['title'],
                                'author': info['author'],
                                'content': content,
                                'category': self.get_category(),
                                'poem_type': self.current_poem_type
                            })
                        break  # Success, exit retry loop
                    except Exception as e:
                        if retry == MAX_RETRIES - 1:
                            print(f"Failed to process page {url} after {MAX_RETRIES} retries: {e}")
                        time.sleep(RETRY_DELAY)
                if page_idx % 10 == 0:
                    pd.DataFrame(self.datasets).to_csv(self.output, index=False)
                    print(f"[INFO] Saved {len(self.datasets)} poems to {self.output}")
        pd.DataFrame(self.datasets).to_csv(self.output, index=False)
        print(f"[INFO] Tổng số bài thơ đã crawl: {len(self.datasets)}")

def main():
    parser = argparse.ArgumentParser(description='Crawl all Vietnamese poem types from thivien.net')
    parser.add_argument('--base_url', type=str, default='https://www.thivien.net/search-poem.php?&Content=tình+yêu&ViewType=1&Country=2',
                        help='Base URL for crawling poems')
    parser.add_argument('--max_poem_type', type=int, default=50,
                        help='Maximum PoemType to crawl (tăng lên nếu muốn lấy nhiều hơn)')
    parser.add_argument('--pages_per_type', type=int, default=50,
                        help='Number of pages to crawl per PoemType')
    parser.add_argument('--output', type=str, default='src/data/poem_dataset.csv',
                        help='Output CSV file path')
    parser.add_argument('--start_poem_type', type=int, default=1,
                        help='PoemType bắt đầu crawl (ví dụ: 15 để bắt đầu từ 15)')
    args = parser.parse_args()

    crawler = PoemCrawler(
        base_url=args.base_url,
        max_poem_type=args.max_poem_type,
        pages_per_type=args.pages_per_type,
        output=args.output,
        start_poem_type=args.start_poem_type
    )
    crawler.crawl_poem()

if __name__ == "__main__":
    main() 