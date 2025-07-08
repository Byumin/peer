import streamlit as st
import pandas as pd
import subprocess

uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요", type=['xlsx'])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    selected_fields = st.multiselect("인적사항으로 사용할 열 선택", df.columns.tolist())
    if selected_fields:
        info_df = df[selected_fields]
        st.write("선택한 인적사항:")
        st.dataframe(info_df.head())

        if st.button('자동 응답 시작') :
            info_df.to_csv("info_temp.csv", index=False)
            subprocess.Popen(["python", "info_selenium_script.py"])
            st.success("자동 입력을 시작합니다.")