import pytest

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("user name is" + getData["username"])
        homepage.getName().send_keys(getData["username"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getPassword().send_keys("123456")
        homepage.selectCheckbox().click()
        homepage.selectEmploymentStatus().click()

        #dropdown = homepage.getGenderDropdown()
        #dropdown.select_by_visible_text("Female")
        self.selectOptionByText(homepage.getGenderDropdown(),getData["gender"])
        #dropdown.select_by_index(0)
        self.selectOptionByIndex(homepage.getGenderDropdown(), 0)

        homepage.submitForm().click()
        message = homepage.getSuccessMessage()
        print(message)
        assert "Success" in message
        self.driver.refresh()

    print("develop1")  # 깃 실습용
    print("develop2")  # 깃 실습용
    print("develop3")  # 깃 실습용

    @pytest.fixture(params=HomePageData.test_Homepage_data)
    def getData(self, request):
        return request.param
