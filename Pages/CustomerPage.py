import dataclasses

from selenium.webdriver.remote.webelement import WebElement

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


@dataclasses.dataclass
class Customer:
    CustomerId: str
    CustomerName: str
    ContactName: str
    Address: str
    City: str
    PostalCode: str
    Country: str


class AdminSeacrhLocators:
    # LOCATOR_CUSTOMER_CAT = (By.XPATH, '//table[@xclass= "ws-table-all notranslate"]/tbody')
    LOCATOR_BUTTON_RESTORE = (By.XPATH, '//button[@id="restoreDBBtn"]')
    LOCATOR_BUTTON_RUN = (By.XPATH, '//button[@class="ws-btn"]')
    LOCATOR_TABLE = (By.XPATH, '//table[@class= "ws-table-all notranslate"]/tbody')
    LOCATOR_INSERT_RESULT = (By.XPATH, '//div[@id="divResultSQL"]/div')


class ElementsFinder(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser

    def check_customer_table(self):
        return self.find_element(AdminSeacrhLocators.LOCATOR_TABLE)

    # def check_customer_categorie(self):
    #     return self.find_element(AdminSeacrhLocators.LOCATOR_CUSTOMER_CAT)

    def check_success_insert(self) -> WebElement:
        is_present = self.find_present_text(AdminSeacrhLocators.LOCATOR_INSERT_RESULT,
                                            "You have made changes to the database. Rows affected: 1")
        assert is_present, "Text is not found"
        return self.find_element(AdminSeacrhLocators.LOCATOR_INSERT_RESULT)

    def check_success_restore(self) -> WebElement:
        is_present = self.find_present_text(AdminSeacrhLocators.LOCATOR_INSERT_RESULT,
                                            "The database is fully restored.")
        assert is_present, "Text is not found"
        return self.find_element(AdminSeacrhLocators.LOCATOR_INSERT_RESULT)

    def click_on_run_button(self):
        return self.find_element(AdminSeacrhLocators.LOCATOR_BUTTON_RUN).click()

    def click_on_restore_button(self):
        return self.find_element(AdminSeacrhLocators.LOCATOR_BUTTON_RESTORE).click()

    def run_sql(self, sql: str):
        self.insert_sql_statement(sql, self.browser)
        self.click_on_run_button()
