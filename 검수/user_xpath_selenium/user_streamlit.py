import streamlit as st
import pandas as pd
import importlib

# 모듈 목록 정의
available_modules = {
    "인적사항": "auto_info",
    "자기보고": "auto_self",
    "알럿": "auto_alert",
}

import sys
import os
st.write("현재 파이썬 경로:", sys.path)
st.write("현재 작업 디렉토리:", os.getcwd())

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(script_dir) # 현재 작업 디렉토리를 스크립트 디렉토리로 변경

st.write("작업 디렉토리 변경 후:", os.getcwd())

st.title("🔧 사용자 정의 자동화 파이프라인")

# 기본 변수 초기화
df = pd.DataFrame()
info_selected_fields = []
info_xpath_list = []
self_xpath = ""
module_selection = []
col = []

# 파일 업로드 및 URL 입력
uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요", type=["xlsx"])
url = st.text_input("자동 입력에 사용할 URL을 입력하세요")

# 드라이버 실행 버튼
# session_state에 driver 초기화
if "driver" not in st.session_state:
    st.session_state.driver = None

# 브라우저 실행 버튼
if st.button("브라우저 실행"):
    if not url:
        st.warning("URL을 먼저 입력하세요.")
    else:
        from start_driver import launch_browser
        st.session_state.driver = launch_browser(url)
        st.success("브라우저가 실행되었습니다. 검사 페이지로 직접 이동하세요.")

# 엑셀 업로드 시 처리
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    col = df.columns.tolist()

    # 특정 행부터 시작하기 위해 행 index를 선택할 수 있는 기능 추가
    start_row_idx_display = st.selectbox("시작할 행의 인덱스를 선택하세요 (엑셀 기준)", options=list(range(1, len(df)+1)), index=0)
    start_row_idx = start_row_idx_display - 1

    # 인적사항 선택 및 XPath 입력
    info_selected_fields = st.multiselect("인적사항으로 사용할 열 선택", col)
    info_xpath_raw = st.text_input("인적사항 xpath를 선택된 인적사항 필드 순서와 동일하게 입력하세요")
    info_xpath_list = [x.strip() for x in info_xpath_raw.split(",")] if info_xpath_raw else []

    # 자기보고 XPath
    self_xpath_raw = st.text_input("자기보고 xpath를 입력하세요")
    self_xpath = self_xpath_raw.strip()

    # 첫 번째 문항단 시작 열 선택
    # 첫번째 두번째 이렇게 나아갈 때 유동적 변화까지 향후에 고려해야함.
    first_items_start_field = st.selectbox("첫 번째 문항단이 시작되는 열 선택", col)
    first_items_start_index = col.index(first_items_start_field)

    # 모듈 선택 및 순서 지정
    st.subheader("모듈 선택 및 순서 지정")
    for module_name in available_modules:
        selected = st.checkbox(module_name, value=True)
        if selected:
            order = st.number_input(f"{module_name} 모듈 순서", min_value=1, max_value=len(available_modules), value=1)
            module_selection.append((order, module_name))

    # 유효성 검사
    if info_selected_fields and info_xpath_list:
        if len(info_xpath_list) != len(info_selected_fields):
            st.error("XPath 개수와 인적사항 필드 수가 다릅니다.")
        else:
            info_dict = {field: xpath for field, xpath in zip(info_selected_fields, info_xpath_list)}
            st.success("입력한 xpath가 유효합니다.")
            st.write("info_dict:", info_dict)
    elif info_selected_fields:
        st.warning("인적사항 XPath를 입력하세요.")

    if self_xpath:
        st.success("자기보고 xpath가 유효합니다.")
    else:
        st.warning("자기보고 xpath를 입력하세요.")

    # 자동 실행 버튼
    if st.button("자동 응답 시작"):
        if not url:
            st.error("URL을 입력하세요.")
        elif len(info_xpath_list) != len(info_selected_fields):
            st.error("XPath 개수와 필드 수가 맞지 않습니다.")
        elif not self_xpath:
            st.error("자기보고 XPath를 입력하세요.")
        elif not module_selection:
            st.error("모듈을 선택하세요.")
        else:
            st.success("자동 응답을 시작합니다!")

            # csv 저장
            df[info_selected_fields].to_csv("info_df_temp.csv", index=False, encoding="utf-8-sig")
            df.iloc[:, first_items_start_index:].to_csv("self_df_temp.csv", index=False, encoding="utf-8-sig")

            # 인자로 받는 모든 것
            # 딕셔너리 선언 시점에서 함수와 표현식은 실행됨
            context = {
                "driver": st.session_state.driver,
                "start_row_idx": start_row_idx,
                "info_df_all": pd.read_csv("info_df_temp.csv"),
                "info_dict": info_dict,
                "self_df_all": pd.read_csv("self_df_temp.csv"),
                "self_xpath": self_xpath,
            }

            # 모듈 순서 정렬
            module_selection.sort()
            print("선택된 모듈 순서:", module_selection)

            # 행 순서 통제
            for row_idx in range(start_row_idx, len(context["info_df_all"])):
                print(f"현재 행 인덱스:\n{row_idx}") # Debugging line
                print(f"현재 행 데이터:\n{context['info_df_all'].iloc[[row_idx]]}") # Debugging line
                print(f"현재 자기보고 데이터:\n{context['self_df_all'].iloc[[row_idx]]}") # Debugging line
                context["info_df_row"] = context["info_df_all"].iloc[[row_idx]]
                context["self_df_row"] = context["self_df_all"].iloc[[row_idx]]
                # 정렬된 순서로 모듈 실행
                for _, module_name in module_selection:
                    module_path = available_modules[module_name]
                    print(f"실행할 모듈: {module_name} ({module_path})")
                    try:
                        st.write(f"모듈 실행 중: {module_name}")
                        module = importlib.import_module(module_path) # 모듈을 직접 불러와서 -> 따로 import하지 않아도 됨
                        module.run(context) # 모듈의 run(context) 함수를 실행
                    except Exception as e:
                        st.error(f"{module_name} 실행 중 오류: {e}")
else:
    st.warning("엑셀 파일을 먼저 업로드하세요.")


# streamlit run c:/Users/USER/peer/검수/user_xpath_selenium/user_streamlit.py
# streamlit run /Users/mac/insight_/peer/검수/user_xpath_selenium/user_streamlit.py
# https://inpsyt.co.kr/login