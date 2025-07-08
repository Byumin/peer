from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# 웹 드라이버 최신화
def start_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # 브라우저 자동 종료 방지
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# 웹 제어 브라우저
def control_browser(driver, url) : 
    driver.get(url)

# 스쿨 프렌즈 자동 입력
def auto_info(driver, info_df) :
    # 번호
    num_box = driver.find_element(By.ID, 'studentNum')
    num_box.send_keys(info_df.iloc[0,0])
    time.sleep(1)

    # 이름
    name_box = driver.find_element(By.ID, 'studentName')
    name_box.send_keys(info_df.iloc[0,1])

# 전체 실행
def run():
    info_df = pd.read_csv("info_temp.csv")
    driver = start_browser()
    control_browser(driver, "https://www.schoolfriends.co.kr/testing/loginForm/P20250708740B-AC000120256016589")
    auto_info(driver, info_df)

if __name__ == "__main__":
    run()