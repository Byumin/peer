from selenium.webdriver.common.by import By
import time

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