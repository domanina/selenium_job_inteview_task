import time

from Pages.CustomerPage import ElementsFinder, Customer


class TestScenarios:
    DEFAULT_CUSTOMER_COUNT = 91
    LONDON_CUSTOMER_COUNT = 6
    LINK = "https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all"

    def test_find_customer(self, browser, headless):
        site_page = ElementsFinder(browser)
        site_page.open(self.LINK)
        site_page.run_sql("SELECT * FROM Customers")

        customer_table = site_page.check_customer_table()
        customers = site_page.get_table_rows(tbl=customer_table, row_class=Customer)

        assert len(customers) == self.DEFAULT_CUSTOMER_COUNT, "Wrong default amount of customers"
        assert "Giovanni Rovelli" in [customer.ContactName for customer in customers], "No this customer in Table"

        for customer in customers:
            if customer.ContactName == "Giovanni Rovelli":
                assert customer.Address == "Via Ludovico il Moro 22", "Wrong Address for this customer"

    def test_find_london_customers(self, browser, url, headless):
        site_page = ElementsFinder(browser)
        site_page.open(self.LINK)
        site_page.run_sql("SELECT * FROM Customers WHERE City='London'")

        customer_table = site_page.check_customer_table()
        customers = site_page.get_table_rows(tbl=customer_table, row_class=Customer)

        assert len(customers) == self.LONDON_CUSTOMER_COUNT, "Wrong amount of customers from London"

    def test_insert_new_customer(self, browser, url, headless):
        new_customer = Customer("92", 'DAO', 'Alena Domanina', '1st street', 'Limassol', '000000', 'Cyprus')
        site_page = ElementsFinder(browser)
        site_page.open(self.LINK)
        site_page.run_sql("INSERT INTO Customers(CustomerId,CustomerName,ContactName,Address,City,PostalCode,Country) "
                          f"VALUES({new_customer.CustomerId},"
                          f"'{new_customer.CustomerName}',"
                          f"'{new_customer.ContactName}',"
                          f"'{new_customer.Address}',"
                          f"'{new_customer.City}',"
                          f"'{new_customer.PostalCode}',"
                          f"'{new_customer.Country}')")

        assert site_page.check_success_insert().text == "You have made changes to the database. Rows affected: 1", \
            "Probably unsuccessful Insert"

        site_page.run_sql("SELECT * FROM Customers")
        customer_table = site_page.check_customer_table()
        customers = site_page.get_table_rows(tbl=customer_table, row_class=Customer)

        assert len(customers) == self.DEFAULT_CUSTOMER_COUNT + 1, "Wrong amount of customers after inserting"
        assert new_customer.ContactName in [customer.ContactName for customer in customers], "No new customer in Table"

    def test_update_customer(self, browser, url, headless):
        new_customer = Customer("1", 'DAO', 'Alena Domanina', '1st street', 'Limassol', '000000', 'Cyprus')
        site_page = ElementsFinder(browser)
        site_page.open(self.LINK)

        site_page.run_sql(f"UPDATE Customers SET "
                          f"CustomerName='{new_customer.CustomerName}', "
                          f"ContactName='{new_customer.ContactName}', "
                          f"Address='{new_customer.Address}', "
                          f"City='{new_customer.City}', "
                          f"PostalCode='{new_customer.PostalCode}', "
                          f"Country='{new_customer.Country}' "
                          f"WHERE CustomerID={new_customer.CustomerId}"
                          )

        assert site_page.check_success_insert().text == "You have made changes to the database. Rows affected: 1", \
            "Probably unsuccessful Update"

        site_page.run_sql("SELECT * FROM Customers")
        customer_table = site_page.check_customer_table()
        customers = site_page.get_table_rows(tbl=customer_table, row_class=Customer)

        assert new_customer == customers[0], "No changes for customer in Table"

    def test_restore_db(self, browser, url, headless):
        site_page = ElementsFinder(browser)
        site_page.open(self.LINK)
        site_page.run_sql("DELETE FROM Customers")

        site_page.click_on_restore_button()

        alert = browser.switch_to.alert
        alert.accept()

        assert site_page.check_success_restore().text == "The database is fully restored.", \
            "Probably unsuccessful Restore"

        site_page.run_sql("SELECT * FROM Customers")
        customer_table = site_page.check_customer_table()
        customers = site_page.get_table_rows(tbl=customer_table, row_class=Customer)

        assert len(customers) == self.DEFAULT_CUSTOMER_COUNT, "Wrong default amount of customers"





