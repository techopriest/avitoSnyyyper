import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
driver = uc.Chrome(options=options)

class avitoParse:
    def __init__(self, url: str, items: list, count = 10, version_main = None):
        self.url = url
        self.items = items
        self.count = count
        self.version_main = version_main

    def __set_up(self):
        self.driver = uc.Chrome(version_main= self.version_main)

    def __get_url(self):
        self.driver.get(self.url)

    def __paginator(self):
        while self.driver.find_element(By.CSS_SELECTOR, '[data-marker="pagination-button/nextPage"]') and self.count > 0:
            self.__parse_page()
            self.driver.find_element(By.CSS_SELECTOR, '[data-marker="pagination-button/nextPage"]').click()
            self.count -= 1

    def __parse_page(self):
        titles = self.driver.find_element(By.CSS_SELECTOR, '[data-marker="item"]')
        for title in titles:
            name = title.find_element(By.CSS_SELECTOR, '[itemprop="name"]').text
            description = title.find_element(By.CSS_SELECTOR, '[class*="item-description"]').text
            url = title.find_element(By.CSS_SELECTOR, '[dete-marker="item-title"]').get_attribute("href")
            price = title.find_element(By.CSS_SELECTOR, '[itemprop="price"]').get_attribute("content")
            data = {
                'name':name,
                'description': description,
                'url': url,
                'price': price 
            }
            self.data.append(data)
            # print(name, description, url, price)
        self.__save_data()

    def __save_data (self):
        with open("items.json", 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def parse(self):
        self.__set_up()
        self.__get_url()
        self.__paginator()

if __name__ == "__name__":
        avitoParse(url='https://www.avito.ru/habarovsk/bytovaya_elektronika?cd=1&q=%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE', count = 1, items = []).parse()