import streamlit as st
import pandas as pd
import importlib
from selenium.webdriver.common.by import By
import time
import sys
import os

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(script_dir) # 현재 작업 디렉토리를 스크립트 디렉토리로 변경

st.set_page_config(page_title="자동화 파이프라인", layout="wide")
st.title("🔧 사용자 정의 자동화 파이프라인")

tabs = st.tabs(["1️⃣ 파일 업로드", "2️⃣ 인적사항/설정", "3️⃣ 모듈 순서 지정", "4️⃣ 실행/결과"])

with tabs[0]:
    st.header("1. 파일 업로드")
    uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요", type=["xlsx"])
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        cols = df.columns.tolist()

        # 특정 행부터 시작하기 위해 행 index를 선택할 수 있는 기능 추가
        start_row_idx_display = st.selectbox("시작할 행의 인덱스를 선택하세요 (엑셀 기준)", options=list(range(1, len(df)+1)), index=0)
        start_row_idx = start_row_idx_display - 1
        
        st.session_state['uploaded_df'] = df
        st.session_state['columns'] = cols
        st.session_state['start_row_idx'] = start_row_idx
        st.success("업로드 완료, 데이터 미리보기:")
        st.dataframe(df.iloc[start_row_idx:])

with tabs[1]:
    st.header("2. 인적사항/설정")
    df = st.session_state.get('uploaded_df')
    if df is not None:
        cols = st.session_state.get('columns', [])
        info_fields = st.multiselect("인적사항에 사용할 열 선택", cols)
        info_xpath_str = st.text_input("각 인적사항의 XPath (콤마로 구분)")
        info_xpath_list = [x.strip() for x in info_xpath_str.split(",")] if info_xpath_str else []
        if info_fields and info_xpath_list:
            if len(info_fields) == len(info_xpath_list):
                st.success("인적사항과 XPath 개수가 일치합니다.")
                info_dict = {field: xpath for field, xpath in zip(info_fields, info_xpath_list)}
                # 세션 상태에 저장
                st.session_state['info_dict'] = info_dict
                df['BIRTHDAY'] = pd.to_datetime(df['BIRTHDAY'], errors='coerce') # Convert to datetime
                info_df = df[st.session_state['info_dict'].keys()]
                st.session_state['info_df'] = info_df
            else:
                st.warning("선택한 필드와 XPath 개수가 다릅니다.")
        else:
            st.info("필드와 XPath를 모두 입력하세요.")
    else:
        st.info("먼저 파일을 업로드 하세요.")

with tabs[2]:
    # 모듈 목록 정의
    available_modules = {
        "버전선택" : "auto_version",
        "인적사항": "auto_info",
        "검사안내" : "auto_guide",
        "자기보고": "auto_self",
        "일반알럿": "auto_alert",
        "특정알럿": "auto_specific_alert"
    }
    # 배경 df
    df = st.session_state['uploaded_df']

    st.header("3. 모듈 순서 지정")
    st.session_state.setdefault("module_flow", [])
    new_mod = st.selectbox("실행할 모듈 선택", list(available_modules.keys()))
    button1, button2 = st.columns([2,1])
    with button1:
        if st.button("모듈 추가"):
            st.session_state["module_flow"].append(new_mod)
    with button2:
        if st.button("모듈 제거"):
            st.session_state["module_flow"] = []

    if st.session_state["module_flow"]:
        st.info("실행 순서: " + " → ".join(st.session_state["module_flow"]))
    else:
        st.info("실행할 모듈을 추가하세요.")
    
    # 버전선택 XPath 설정
    if "버전선택" in st.session_state["module_flow"]:
        st.divider()
        st.subheader("버전 선택 XPath 설정")
        # 버전이 여러개 있을 경우를 대비하여
        # 버전명과 매칭되는 XPath를 입력받는 기능 추가
        version_excel_col = st.selectbox("엑셀에서 버전 열을 선택하세요.", cols)
        version_excel_col_index = cols.index(version_excel_col)
        st.session_state["version_excel_col_index"] = version_excel_col_index

        version_name = st.text_input("버전 이름을 입력하세요.", value='온라인, 답안입력형')
        version_name_list = [x.strip() for x in version_name.split(",")] if version_name else []
        st.session_state["version_name_list"] = version_name_list

        version_xpath = st.text_input("버전 xpath를 입력하세요.", value='//*[@id="form"]/div/div[2]/div[1]/label, //*[@id="form"]/div/div[2]/div[2]/label')
        version_xpath_list = [x.strip() for x in version_xpath.split(",")] if version_xpath else []
        st.session_state["version_xpath_list"] = version_xpath_list

        if all([version_name_list, version_xpath_list, len(version_name_list) == len(version_xpath_list)]):
            version_dict = {version: xpath for version, xpath in zip(st.session_state["version_name_list"], st.session_state["version_xpath_list"])}
            st.session_state["version_dict"] = version_dict
            st.session_state["version_df"] = df[[st.session_state["version_excel_col_index"]]].copy()
            st.success("버전 선택 xpath가 설정되었습니다.")
        elif len(version_name_list) != len(version_xpath_list):
            st.warning("버전 이름과 xpath의 개수가 일치하지 않습니다.")
        else:
            st.warning("버전 선택 xpath를 입력하세요.")
    
    # 자기보고 XPath 설정
    if "자기보고" in st.session_state["module_flow"]:
        st.divider()
        st.subheader("자기보고 XPath 및 패턴 설정")
        self_xpath_raw = st.text_input("자기보고 xpath를 입력하세요")
        item_start_idx = st.number_input("item_index 시작", min_value=0, value=0, key="start_idx")
        item_idx_step = st.number_input("item_index 간격", min_value=1, value=1, key="step")
        value_offset = st.text_input("item_value 오프셋", value="0", key="offset")
        # 페이지 처리 설정
        st.subheader("자기보고 페이지 처리 설정")
        self_page_num = st.number_input("자기보고 페이지 수", min_value=1, value=1, key="self_page_num")
        self_page_start_index = []
        self_next_page_xpath = []
        for n in range(self_page_num):
            label = f"자기보고 {n+1} 페이지 시작 열 선택"
            selected_col = st.selectbox(label, cols, key=f"self_item_start_col_{n+1}")
            selected_index = cols.index(selected_col)
            self_page_start_index.append(selected_index)
            self_next_page_xpath = st.text_input("자기보고 다음 페이지 버튼 xpath를 입력하세요", value='//*[@id="nextPageBtn"]/a')
            self_next_page_dict = 
        # 페이지 시작 열, 페이지 제출 버튼 XPath 설정


        # 자기보고 제출 버튼 XPath 설정
        st.subheader("자기보고 제출(다음) 버튼 XPath 설정")
        self_next_button_xpath = st.text_input("자기보고 제출 버튼 xpath를 입력하세요", value='//*[@id="nextPageBtn"]')
        # 자기보고 XPath 및 패턴 유휴성
        if all([self_xpath_raw, item_start_idx, item_idx_step, value_offset, self_next_page_xpath, self_page_start_index, self_next_button_xpath]):
            st.session_state["self_xpath"] = self_xpath_raw.strip() # 패턴, 자기보고 XPath
            st.session_state["item_start_idx"] = item_start_idx # 패턴, 자기보고 item index 시작
            st.session_state["item_idx_step"] = item_idx_step # 패턴, 자기보고 item index 간격
            st.session_state["value_offset"] = value_offset # 패턴, 자기보고 item value 오프셋
            st.session_state["self_next_page_xpath"] = self_next_page_xpath # 자기보고 다음 페이지 버튼 XPath
            st.session_state["self_page_start_index"] = self_page_start_index # 자기보고 페이지 시작 열 인덱스
            st.session_state["self_next_button_xpath"] = self_next_button_xpath # 자기보고 제출 버튼 XPath
            st.session_state["self_df"] = df.iloc[:, st.session_state["self_item_start_idx"]:]
            st.success("자기보고 xpath 및 패턴 설정되었습니다.")
        else:
            st.warning("xpath 및 패턴을 입력하세요.")

    if "특정 알럿" in st.session_state["module_flow"]:
        st.divider()
        st.subheader("특정 알럿 XPath 설정")
        specific_alert_xpath = st.text_input("특정 알럿 xpath를 입력하세요")
        if specific_alert_xpath:
            st.session_state["specific_alert_xpath"] = specific_alert_xpath
            st.success("특정 알럿 xpath가 설정되었습니다.")
        else:
            st.warning("특정 알럿 xpath를 입력하세요.")

with tabs[3]:
    st.header("4. 실행 및 결과")
    url = st.text_input("자동 입력에 사용할 URL을 입력하세요")
    if st.button("드라이버 실행"):
        if url:
            st.session_state["url"] = url
            from start_driver import launch_browser
            st.session_state['driver'] = launch_browser(url)
            st.success("드라이버가 실행되었습니다.")

    if st.button("자동화 실행"):
        if st.session_state.get('driver') is None:
            st.warning("드라이버가 실행되지 않았습니다. 먼저 드라이버를 실행하세요.")
        elif st.session_state.get('uploaded_df') is None:
            st.warning("엑셀 파일을 먼저 업로드하세요.")
        elif st.session_state.get('module_flow') is None:
            st.warning("실행할 모듈이 없습니다. 모듈을 추가하세요.")
        else:
            st.success("자동화가 실행됩니다.")

            # 모듈 별 데이터 분리 # 이걸 앞단에 놓아서 분리되어 처리될 수 있도록 리팩토링
            df = st.session_state['uploaded_df']
            df['BIRTHDAY'] = pd.to_datetime(df['BIRTHDAY'], errors='coerce') # Convert to datetime
            info_df = df[st.session_state['info_dict'].keys()]
            st.session_state['info_df'] = info_df

            self_df = df.iloc[:, st.session_state["self_item_start_idx"]:]
            st.session_state['self_df'] = self_df

            context = {
                "driver": st.session_state['driver'],
                "version_dict": st.session_state.get("version_dict", {}),
                "info_df_all": st.session_state.get("info_df", pd.DataFrame()),
                "self_df_all": st.session_state.get("self_df", pd.DataFrame()),
                "start_row_idx": st.session_state.get("start_row_idx", 0), # 시작 행 인덱스
                "info_dict": st.session_state.get("info_dict", {}), # 인적사항 XPath 딕셔너리
                "self_xpath": st.session_state.get("self_xpath", ""), # 패턴, 자기보고 XPath
                "item_start_idx": st.session_state.get("item_start_idx", 0), # 패턴, 자기보고 시작 열
                "item_idx_step": st.session_state.get("item_idx_step", 1), # 패턴, 자기보고 item index 간격
                "value_offset": st.session_state.get("value_offset", 0), # 패턴, 자기보고 item value 오프셋
                "self_page_start_index": st.session_state.get("self_page_start_index", []), # 자기보고 페이지 시작 열 인덱스
                "self_next_page_xpath": st.session_state.get("self_next_page_xpath", ""), # 자기보고 다음 페이지 버튼 XPath
                "self_next_button_xpath": st.session_state.get("self_next_button_xpath", ""), # 자기보고 제출 버튼 XPath
                "specific_alert_xpath": st.session_state.get("specific_alert_xpath", "") # 특정 알럿 XPath
            }

            # 행 순서 지정
            for row_idx in range(st.session_state['start_row_idx'], len(st.session_state['info_df'])):
                context["info_df_row"] = context["info_df_all"].iloc[[row_idx]]
                context["self_df_row"] = context["self_df_all"].iloc[[row_idx]]
                # 모듈 순서대로 실행
                for module_name in st.session_state["module_flow"]:
                    module_path = available_modules[module_name]
                    try:
                        module = importlib.import_module(module_path)
                        module.run(context)
                        st.success(f"{module_name} 모듈이 성공적으로 실행되었습니다.")
                    except Exception as e:
                        st.error(f"{module_name} 실행 중 오류: {e}")
                        st.stop()
                time.sleep(2)
                next_case = st.session_state['driver'].find_element(By.XPATH, "/html/body/div/div/div/div/div[3]/a[1]")
                next_case.click()  # 다음 케이스로 이동
                st.session_state['driver'].switch_to.alert.accept()
                time.sleep(1)
            st.success("모든 모듈이 성공적으로 실행되었습니다!")

# streamlit run c:/Users/USER/peer/검수/user_xpath_selenium/user_defined_automation_pipeline.py
# streamlit run /Users/mac/insight_/peer/검수/user_xpath_selenium/user_defined_automation_pipeline.py
# https://inpsyt.co.kr/login