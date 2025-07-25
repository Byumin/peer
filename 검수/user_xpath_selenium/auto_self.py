from selenium.webdriver.common.by import By
import streamlit as st
from selenium.webdriver.common.action_chains import ActionChains

def run(context):
    print("자기보고 입력 모듈 실행")
    driver = context["driver"]
    self_df = context["self_df_row"]
    self_xpath_row = context["self_xpath"]
    item_start_idx = int(context["item_start_idx"])
    item_idx_step = int(context["item_idx_step"])
    value_offset = int(context["value_offset"])
    self_next_page_xpath = context["self_next_page_xpath"]
    
    self_next_button_xpath = context["self_next_button_xpath"]

    # 검사 실시 화면 통제 전환 
    window = driver.window_handles
    print("현재 창 핸들:", window)  # Debugging line
    window_handle = window[-1]  # 마지막 창 핸들
    driver.switch_to.window(window_handle)
    print("현재 창 핸들로 전환:", window_handle)  # Debugging line


    row = self_df.iloc[0].to_list()
    # row의 각 원소값에 value_offset을 적용
    row = [str(int(value) + value_offset) for value in row]
    # item_start_idx, item_idx_step을 적용해 item_idx 생성
    item_idx = [item_start_idx + i * item_idx_step for i in range(len(row))]
    for item_idx, item_value in zip(item_idx, row):
        print(f"자기보고 항목 {item_idx}: {item_value}")
        # //*[@id="test-area"]/div/ul/li[{0}]/div[2]/ul/li[{1}]/label
        # //*[@id="test-area"]/div/ul/li[1]/div[2]/ul/li[1]/label
        try :
            actions = ActionChains(driver)
            self_xpath = self_xpath_row.format(item_idx, item_value)
            print(f"자기보고 XPath: {self_xpath}")  # Debugging line
            self_element = driver.find_element(By.XPATH, self_xpath)
            actions.move_to_element(self_element).perform()
            self_element.click()  # 클릭하여 입력 필드 활성화
        except Exception as e:
            print(f"XPath 오류: {self_xpath} - {e}")
            st.error(f"XPath 오류: {self_xpath} - {e}")
            st.stop()
    try :
        next_button = driver.find_element(By.XPATH, self_next_button_xpath)
        next_button.click()  # 다음 버튼 클릭
    except Exception as e:
        print(f"다음 버튼 클릭 오류: {e}")
        st.error(f"다음 버튼 클릭 오류: {e}")
        st.stop()