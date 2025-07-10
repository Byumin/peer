from info_selenium_script import start_browser, control_browser, auto_info
from instructions_selenium_script import auto_instructions
from response_selenium_script import auto_point_response, auto_self_response
import pandas as pd
import os, sys

def driver_entry(filename_info, filename_point_item, filename_self_item, filename_sct_item, url, info_selected_fields_str):
    # 작업 디렉토리 설정
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(script_dir)
    # info_selected_fields_str 리스트 변환
    info_selected_fields = info_selected_fields_str.split(',')

    info_df = pd.read_csv(filename_info, encoding="utf-8-sig")
    point_item_df = pd.read_csv(filename_point_item, encoding="utf-8-sig")
    self_item_df = pd.read_csv(filename_self_item, encoding="utf-8-sig")
    sct_item_df = pd.read_csv(filename_sct_item, encoding="utf-8-sig")

    driver = start_browser()
    control_browser(driver, url)

    for row_i in range(len(info_df)) :
        auto_info(driver, info_selected_fields, info_df.iloc[row_i,:])
        auto_instructions(driver)
        auto_point_response(driver, info_selected_fields, row_i, info_df, point_item_df.iloc[row_i,:])
        auto_self_response(driver, self_item_df.iloc[row_i,:])
        auto_sct_response(driver, sct_item_df.iloc[row_i,:])


if __name__ == "__main__":
    driver_entry('info_temp.csv', 'point_item_temp.csv', 'self_item_temp.csv', 'sct_item_temp.csv', sys.argv[1], sys.argv[2])