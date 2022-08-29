from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        try:
            return self.browser.get(url)
        except:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise

    def find_element(self, locator, time=5):
        try:
            return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                           message=f"Can't find element by locator {locator}")
        except:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise

    def find_elements(self, locator, time=5):
        try:
            return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                           message=f"Can't find elements by locator {locator}")
        except:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise

    def find_present_text(self, locator, text, time=5):
        try:
            return WebDriverWait(self.browser, time).until(EC.text_to_be_present_in_element(locator, text),
                                                           message=f"Can't find elements by locator {locator}")
        except:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise

    def insert_sql_statement(self, sql, browser):
        browser.execute_script(f'window.editor.setValue("{sql}");')

    def get_table_rows(self, tbl: WebElement, row_class) -> list:
        rows = []

        for row in tbl.find_elements(By.XPATH, ".//tr")[1:]:
            attrs = [column.text for column in row.find_elements(By.XPATH, ".//td")]
            cur_row = row_class(*attrs)
            rows.append(cur_row)

        return rows
