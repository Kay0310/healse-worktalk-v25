
import streamlit as st
from datetime import datetime
from PIL import Image
import base64
import os

# 로고 이미지 base64 인코딩 문자열 (WORK_TALK_small.png)
logo_base64 = """
iVBORw0KGgoAAAANSUhEUgAAAZAAAABcCAYAAAAqHjrSAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAA3dJREFUeJzt3d1uGzEUheHnNz1kWjcWgiV+ASkUw06YBA9Aj0cAZCDpCTrINRJdpJSt5zvtvTu3Nvz9+lJ9cC9PW3V0DgDAIAwCAMAjw1JzUk/fP8+Dj1zAgDAIAwCkz3zAgDAIAwCEMz3AgDAIAwCEMz3AgDAIAwCEMz3AgDAIAwCEMz3AgDAIAwCEMz3AgDAIAwCEMz3AgDAIAwCEMz3AgDAIAwCEMz3AgDAIAwCEMz3AgDAIAwCEMz3AgDAIAwCEMz3AgDAIAwCEMz3AgDAIAwCEMz3AgDAIAwCEMz3AgDAIAwCEMz3AgDAIAwCEMz3AgDAIAwCEAy/x9GnS0yAHqMcAAAAASUVORK5CYII=
"""

# 로고 표시
st.markdown("<h1 style='text-align: center;'><img src='data:image/png;base64," + logo_base64.strip() + "' width='200'/></h1>", unsafe_allow_html=True)
st.markdown("사진 1장 업로드 ➜ 질문 4개 응답 ➜ 저장 ➜ 다음 사진 순서대로 진행해 주세요.")

# 세션 초기화
if 'responses' not in st.session_state:
    st.session_state['responses'] = []
if 'step' not in st.session_state:
    st.session_state['step'] = 0

# 입력 폼
name = st.text_input("이름")
department = st.text_input("부서")
uploaded_file = st.file_uploader("📷 작업 사진 업로드", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, use_column_width=True)
    q1 = st.text_input("어떤 작업을 하고 있는 건가요?")
    q2 = st.text_input("이 작업은 왜 위험하다고 생각하나요?")
    q3 = st.radio("이 작업은 얼마나 자주 하나요?", ["연 1-2회", "반기 1-2회", "월 2-3회", "주 1회 이상", "매일"], key="q3")
    q4 = st.radio("이 작업은 얼마나 위험하다고 생각하나요?", ["약간의 위험: 일회용 밴드 치료 필요 가능성 있음", "조금 위험: 병원 치료 필요. 1-2일 치료 및 휴식", "위험: 보름 이상의 휴식이 필요한 중상 가능성 있음", "매우 위험: 불가역적 장애 또는 사망 가능성 있음"], key="q4")

    if st.button("💾 저장하기"):
        st.session_state.responses.append({
            "이름": name,
            "부서": department,
            "파일명": uploaded_file.name,
            "질문1": q1,
            "질문2": q2,
            "질문3": q3,
            "질문4": q4,
            "시간": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        st.success("💾 저장 완료! 다음 사진을 입력해 주세요.")
        st.session_state['step'] += 1
        st.experimental_rerun()
