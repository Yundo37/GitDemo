from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

try:
    service_obj = ChromeService("C:/Users/YB/Documents/chromedriver/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    print("Chrome 드라이버 생성 성공")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    print(f"페이지 로드 성공: {driver.title}")

    driver.quit()
    print("테스트 완료")
except Exception as e:
    print(f"에러 발생: {e}")