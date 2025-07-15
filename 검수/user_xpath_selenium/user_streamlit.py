import streamlit as st
import pandas as pd

st.title("🧪 XPath 입력 테스트")

# 검수 케이스 엑셀 업로드
uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요", type=['xlsx'])
# 인적사항 필드 선택
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    col = df.columns.tolist()

    info_selected_fields = st.multiselect("인적사항으로 사용할 열 선택", col)
    st.write("선택된 인적사항 필드:", info_selected_fields)

# 인적사항 xpath 입력
info_xpath = st.text_input("인적사항 xpath를 선택된 인적사항 필드 순서와 동일하게 입력하세요")
info_xpath = info_xpath.split(",") if info_xpath else [] # 리스트 변환
info_xpath = [xpath.strip() for xpath in info_xpath]  # 공백 제거
if info_xpath and info_selected_fields:
    if len(info_xpath) != len(info_selected_fields):
        st.error("입력한 xpath의 개수가 선택된 필드의 개수와 일치하지 않습니다.")
    elif len(info_xpath) == len(info_selected_fields):
        info_dict = {field: xpath.strip() for field, xpath in zip(info_selected_fields, info_xpath)}
        print("info_dict:", info_dict)
        st.success("입력한 xpath가 유효합니다.")
    else:
        st.warning("인적사항 xpath를 입력하세요.")
else:
    st.warning("인적사항 xpath를 입력하세요")

# streamlit run c:/Users/USER/peer/검수/user_xpath_selenium/user_streamlit.py