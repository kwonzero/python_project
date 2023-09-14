import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 이 부분은 간단한 코드라서 따로 클래스화하지 않았음
# driver 부분을 클래스 객체 변수 형태로 빼는 방식으로 클래스를 작성해볼 수는 있을 듯
def crawl_naver(query):
    driver = webdriver.Chrome() # 작동할 때 크롬 웹브라우저 사용
    driver.get('https://naver.com')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#query'))) # #query가 나올 때까지 최대 10초 기다림
    search_input = driver.find_element(By.CSS_SELECTOR, '#query')
    search_input.send_keys(query)
    search_button = driver.find_element(By.CSS_SELECTOR, '#search-btn')
    search_button.click()
    time.sleep(5)
    driver.quit() 