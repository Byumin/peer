from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

import os
import sys

# 스쿨 프렌즈 검사안내 자동 입력
def auto_instructions(driver) :
    time.sleep(1)
    # 첫번째
    next_box = driver.find_element(By.XPATH, '//*[@id="nextBtn"]/span')
    next_box.click()
    time.sleep(1)
    # 두번째
    next_box = driver.find_element(By.XPATH, '//*[@id="nextBtn"]/span')
    next_box.click()
    time.sleep(1)
    # 세번째
    next_box = driver.find_element(By.XPATH, '//*[@id="nextBtn"]/span')
    next_box.click()
    time.sleep(1)
    # 네번째
    next_box = driver.find_element(By.XPATH, '//*[@id="nextBtn"]/span')
    next_box.click()
    time.sleep(1)
    # 다섯번째
    next_box = driver.find_element(By.XPATH, '//*[@id="nextBtn"]/span')
    next_box.click()

# 전체 실행
def run() :
    auto_instructions(driver)

if __name__ == "__main__":
    run()