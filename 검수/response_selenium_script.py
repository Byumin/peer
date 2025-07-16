from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
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

# 지명 문항 자동 응답 
def auto_point_response(driver, info_selected_fields, row_i, info_df, point_item_df) : # info_selected_fields:선택 인적사항, row_i:행 번호, info_df:학급 전체 인적정보, point_item_df:특정 행
    time.sleep(1)

    try :
        # 학생 이름 -> 학급 번호 변환
        student_name_list = info_df[info_selected_fields[1]].to_list()
        student_name_list.remove(info_df.iloc[row_i, :][info_selected_fields[1]])
        print('본인을 제외한 학생 명단\n', student_name_list)
        point_student_number_list = []
        for n in range(len(point_item_df)) :
            print('응답 정보\n', point_item_df)
            print('디버깅용', point_item_df.iloc[n]) # 시리즈는 하나의 인덱스만 사용

            if pd.isna(point_item_df.iloc[n]) : # 지명이 null인 경우
                print(f'{n+1}번째 지명 문항은 응답이 없습니다.')
                point_student_number_list.append([len(info_df)])
            else :
                point_name_list = [name.strip() for name in point_item_df.iloc[n].split(',')]
                print(point_name_list)
                temp_no_list = []
                for name in point_name_list :
                    student_number = student_name_list.index(name) + 1
                    print(f"{name} → {student_number}")
                    temp_no_list.append(student_number)
                print('name -> student_number 변환',temp_no_list)
                point_student_number_list.append(temp_no_list)
        print(point_student_number_list)

        # 지명 문항 응답
        for item_number, point_number_list in enumerate(point_student_number_list) :
            print(point_number_list)
            time.sleep(1)
            for point_number in point_number_list :
                print(item_number+1, point_number)
                point_box = driver.find_element(By.XPATH, f'//*[@id="scroll-box"]/ul/li[{item_number+1}]/div[2]/div/button[{point_number}]')
                point_box.click()
                time.sleep(1)
            # 다음 
            print('진행 지명 문항번호', item_number +1)
            print('최대 문항 번호', len(point_student_number_list))
            if item_number +1 == len(point_student_number_list) : # 지명 마지막 문항인 경우
                next_box = driver.find_element(By.ID, 'objectiveQuestionSubmitBtnChk')
                next_box.click()
            else :
                next_box = driver.find_element(By.ID, 'objectiveQuestionNextBtn')
                next_box.click()
    except Exception as e:
        print("지명 응답 중 오류 발생:")
        traceback.print_exc()  # 전체 traceback 출력

# 자기보고 문항 자동 응답
def auto_self_response(driver, self_item_df) : # item_df는 특정 행
    self_item_list = self_item_df.to_list()
    print('자기보고 문항 값', self_item_list)
    for item_number in range(len(self_item_list)) :
        response_value = self_item_list[item_number]
        print('응답 값', response_value)
        print('응답 문항 번호', item_number+1)
        print(f'//*[@id="scroll-box"]/ul/li[{item_number+1}]/div[2]/ul/li[{response_value}]/label')
        time.sleep(1)
        self_response_box = driver.find_element(By.XPATH, f'//*[@id="scroll-box"]/ul/li[{item_number+1}]/div[2]/ul/li[{response_value}]/label')
        actions = ActionChains(driver)
        actions.move_to_element(self_response_box).perform()
        self_response_box.click()
    if item_number+1 == len(self_item_list) :
        next_box = driver.find_element(By.ID, 'objectiveQuestionSubmitBtnChk')
        next_box.click()
    else :
        pass

def auto_sct_response(driver, sct_item_df) :
    # SCT 첫번째 문항
    sct_item_list = sct_item_df.to_list()
    print('SCT 문항 값', sct_item_list)
    for item_number in range(len(sct_item_list)) :
        response_value = sct_item_list[item_number]
        print('응답 값', response_value)
        print('응답 문항 번호', item_number+1)
        print(f'//*[@id="scroll-box"]/ul/li[{item_number+1}]/div/h1/input')
        time.sleep(2)
        sct_response_box = driver.find_element(By.XPATH, f'//*[@id="scroll-box"]/ul/li[{item_number+1}]/div/h1/input')
        actions = ActionChains(driver)
        actions.move_to_element(sct_response_box).perform()
        sct_response_box.send_keys(response_value)

    if item_number+1 == len(sct_item_list) :
        next_box = driver.find_element(By.ID, 'objectiveQuestionSubmitBtnChk')
        next_box.click()
    else :
        pass