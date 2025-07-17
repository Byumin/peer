from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def run(context):
    driver = context["driver"]
    info_df = context["info_df_row"]
    info_dict = context["info_dict"]

    # 검사 실시 화면 통제 전환
    window = driver.window_handles
    print("현재 창 핸들:", window)  # Debugging line
    window_handle = window[-1]  # 마지막 창 핸들
    driver.switch_to.window(window_handle)
    print("현재 창 핸들로 전환:", window_handle)  # Debugging line

    print("info_df_row:", info_df.head())  # Debugging line
    print("info_dict:", info_dict) # Debugging line 인자 잘 받는지

    for field, xpath in info_dict.items():
        try:
            if field == 'SEX' :
                print(f"성별 입력: {field}, XPath: {xpath}")
                sex_xpath = xpath.format(info_df[field].values[0])
                sex_element = driver.find_element(By.XPATH, sex_xpath)
                sex_element.click()
            elif field == 'BIRTHDAY' :
                print(f"생년월일 입력: {field}, XPath: {xpath}")
                birth_xpath = xpath
                birth_xpath.click()  # 클릭하여 입력 필드 활성화
                # 년 요소 선택
                dropdown_year = driver.find_element(By.CLASS_NAME, 'ui-datepicker-year')
                dropdown_year = Select(dropdown_year)
                dropdown_year.select_by_visible_text("{}".format(info_df[field].values.strftime('%Y')))
                # 월 요소 선택
                dropdown_month = driver.find_element(By.CLASS_NAME, 'ui-datepicker-month')
                dropdown_month = Select(dropdown_month)
                dropdown_month.select_by_visible_text("{}".format(info_df[field].values.strftime('%m')))
                # 일 요소 선택
                day_element = driver.find_element(By.XPATH, "//a[@class='ui-state-default' and test()= '{}']".format(info_df[field].values.strftime('%d')))
                day_element.click()
            elif field == 'REGION' :
                dropdown_element = driver.find_element(By.XPATH, xpath)
                dropdown_element = Select(dropdown_element)
                dropdown_element.select_by_visible_text(info_df[field].values[0])
            else :
                print(f"입력할 필드: {field}, XPath: {xpath}")
                element = driver.find_element(By.XPATH, xpath)
                value = info_df[field].values[0]
                element.send_keys(value)
        except Exception as e:
            print(f"입력 실패: {field} - {e}")

    time.sleep(2)