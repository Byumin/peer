import streamlit as st
import pandas as pd

st.set_page_config(page_title="자동화 파이프라인 예시", layout="wide")

st.title("🔧 사용자 정의 자동화 파이프라인 (탭 UI 예시)")

tabs = st.tabs(["1️⃣ 파일 업로드", "2️⃣ 인적사항/설정", "3️⃣ 모듈 순서 지정", "4️⃣ 실행/결과"])

with tabs[0]:
    st.header("1. 파일 업로드")
    uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요", type=["xlsx"])
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.success("업로드 성공! 데이터 미리보기:")
        st.dataframe(df)
        st.session_state['uploaded_df'] = df

with tabs[1]:
    st.header("2. 인적사항/설정")
    df = st.session_state.get('uploaded_df')
    if df is not None:
        cols = df.columns.tolist()
        info_fields = st.multiselect("인적사항에 사용할 열 선택", cols)
        xpath_str = st.text_input("각 인적사항의 XPath (콤마로 구분)")
        xpath_list = [x.strip() for x in xpath_str.split(",")] if xpath_str else []
        st.session_state['info_fields'] = info_fields
        st.session_state['xpath_list'] = xpath_list
        if info_fields and xpath_list:
            if len(info_fields) == len(xpath_list):
                st.success("인적사항과 XPath 개수가 일치합니다.")
            else:
                st.warning("선택한 필드와 XPath 개수가 다릅니다!")
        else:
            st.info("필드와 XPath를 모두 입력하세요.")
    else:
        st.info("먼저 파일을 업로드 하세요.")

with tabs[2]:
    st.header("3. 모듈 순서 지정")
    available_modules = ["인적사항", "자기보고", "일반 알럿", "특정 알럿"]
    st.session_state.setdefault("module_flow", [])
    new_mod = st.selectbox("실행할 모듈 선택", available_modules)
    if st.button("모듈 추가"):
        st.session_state["module_flow"].append(new_mod)
    if st.session_state["module_flow"]:
        st.info("실행 순서: " + " → ".join(st.session_state["module_flow"]))
    else:
        st.info("실행할 모듈을 추가하세요.")

with tabs[3]:
    st.header("4. 실행 및 결과")
    if st.button("자동화 실행"):
        # 여기서 실제 자동화 실행 로직을 호출!
        st.success("자동화가 실행되었습니다!")
        # 결과/로그를 여기에 출력
    # 실행 후 결과, 로그, 다운로드 등 추가 가능


# streamlit run c:/Users/USER/peer/검수/user_xpath_selenium/user_streamlit_copy.py
# streamlit run /Users/mac/insight_/peer/검수/user_xpath_selenium/user_streamlit.py
# https://inpsyt.co.kr/login