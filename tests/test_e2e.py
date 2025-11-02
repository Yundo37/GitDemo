import time
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("getting all the product title")
        products = checkoutpage.getProductTitles()

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                #product.find_element(By.XPATH, "div/button").click()
                checkoutpage.getProductFooter(product).click()
                break

        self.driver.find_element(By.CSS_SELECTOR, "a[class*=btn-primary]").click()

        confirmPage = checkoutpage.CheckOutItems()
        log.info("Entering country name is ind")
        # self.driver.find_element(By.ID, "country").send_keys("ind")
        confirmPage.enterCountry("ind")
        self.verifyLinkPresence("India")


        #self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmPage.selectCountry().click()
        confirmPage.checkTerms().click()
        confirmPage.submitOrder().click()

        successText = confirmPage.getSuccessMessage()
        #print(successText)
        log.info("Text received from application is" + successText)
        assert "Success! Thank you!" in successText
        #assert "일부러 틀리기 ㅎ" in successText
        time.sleep(3)