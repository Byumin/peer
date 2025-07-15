import streamlit as st
import pandas as pd
import subprocess
import os, sys

uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요", type=['xlsx'])
url = st.text_input("자동 입력에 사용할 URL을 입력하세요")

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    col = df.columns.tolist()

    info_selected_fields = st.multiselect("인적사항으로 사용할 열 선택", col)
    st.write("선택된 인적사항 필드:", info_selected_fields)
    point_item_start_field = st.selectbox("지명 문항이 시작되는 열 선택", col)
    st.write("지명 문항 시작 열:", point_item_start_field)
    self_item_start_field = st.selectbox("자기보고 문항이 시작되는 열 선택", col)
    st.write("자기보고 문항 시작 열:", self_item_start_field)
    sct_item_start_field = st.selectbox("문장완성 문항이 시작되는 열 선택", col)
    st.write("문장완성 문항 시작 열:", sct_item_start_field)
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(script_dir)

    point_item_start_index = col.index(point_item_start_field)
    self_item_start_index = col.index(self_item_start_field)
    sct_item_start_index = col.index(sct_item_start_field)

    if info_selected_fields:
        info_df = df[info_selected_fields]
        info_df.to_csv("info_temp.csv", index=False ,encoding="utf-8-sig")
        st.write("✅ 인적사항 미리보기")
        st.dataframe(info_df.head())
    
    if point_item_start_field :
        point_item_df = df.iloc[:, point_item_start_index:self_item_start_index]
        point_item_df.to_csv("point_item_temp.csv", index=False, encoding="utf-8-sig")
        st.write("✅ 문항 미리보기")
        st.dataframe(point_item_df.head())

    if self_item_start_field :
        self_item_df = df.iloc[:, self_item_start_index:sct_item_start_index]
        self_item_df.to_csv("self_item_temp.csv", index=False, encoding="utf-8-sig")
        st.write("✅ 문항 미리보기")
        st.dataframe(self_item_df.head())

    if sct_item_start_field :
        sct_item_df = df.iloc[:, sct_item_start_index:]
        sct_item_df.to_csv("sct_item_temp.csv", index=False, encoding="utf-8-sig")
        st.write("✅ 문항 미리보기")
        st.dataframe(sct_item_df.head())

        if st.button('자동 응답 시작') :
            script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
            print("Current script directory:", script_dir)
            os.chdir(script_dir)
            info_df.to_csv("info_temp.csv", index=False)

            info_selected_fields_str = ",".join(info_selected_fields)
            subprocess.Popen(["python", "selenium_driver_entry.py", url, info_selected_fields_str]) # subprocess.Popen() 문자열만 인자로 받기 때문에 리스트를 str로 변환해야함.
            st.success("자동 입력을 시작합니다.")

# streamlit run c:/Users/USER/peer/검수/streamlit_test.py
# streamlit run /Users/mac/insight_/peer/검수/streamlit_test.py
# https://www.schoolfriends.co.kr/testing/loginForm/P20250708740B-AC000120256016589