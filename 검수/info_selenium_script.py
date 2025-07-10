from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

import os
import sys

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

# 스쿨 프렌즈 인적사항 자동 입력
def auto_info(driver, info_selected_fields, info_df) : # info_df 특정 행만
    # 번호
    num_box = driver.find_element(By.ID, 'studentNum')
    num_box.send_keys(str(info_df[info_selected_fields[0]]))
    time.sleep(1)

    # 이름
    name_box = driver.find_element(By.ID, 'studentName')
    name_box.send_keys(str(info_df[info_selected_fields[1]]))
    time.sleep(1)

    # 시작하기
    start_box = driver.find_element(By.ID, 'studentPsyLoginBtn')
    start_box.click()
    time.sleep(1)
    start_alert = driver.find_element(By.XPATH, '//*[@id="swal2-html-container"]/div[3]/a[2]')
    start_alert.click()

# 전체 실행
def run():
    # 현재 스크립트가 있는 경로로 이동
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(script_dir)
    info_df = pd.read_csv("info_temp.csv", encoding="utf-8-sig")
    driver = start_browser()
    control_browser(driver, "https://www.schoolfriends.co.kr/testing/loginForm/P20250708740B-AC000120256016589")
    auto_info(driver, info_df)

if __name__ == "__main__":
    run()