import streamlit as st
import time

# --- 기존 함수들은 그대로 두거나 약간 수정 ---
def print_slow(text):
    # 웹에서는 한 글자씩 보이는 효과 대신, 전체 텍스트를 바로 보여주는 것이 더 좋습니다.
    # st.write()가 그 역할을 대신합니다.
    pass 

def run_branding_consulting():
    # Streamlit은 위에서 아래로 순차적으로 실행되며, 사용자의 인터랙션을 기다립니다.
    
    st.title("✨ 나만의 인스타그램 브랜드 찾기 컨설팅 ✨")
    st.write("당신의 고유한 매력과 전문성을 발견하고, 인스타그램에 매력적으로 표현할 수 있도록 돕는 프로그램입니다.")

    # st.session_state를 사용해 답변을 저장합니다.
    if 'answers' not in st.session_state:
        st.session_state.answers = {}

    with st.expander("**Phase 1: 나만의 페르소나 발견하기**", expanded=True):
        st.write("가장 먼저, 당신이라는 사람의 핵심을 들여다보는 시간을 갖겠습니다.")
        st.session_state.answers['passion'] = st.text_input("[질문 1/5] 시간 가는 줄 모르고 이야기할 수 있는 주제는 무엇인가요? (당신의 '열정')")
        st.session_state.answers['expertise'] = st.text_input("[질문 2/5] 다른 사람들에게 '이것만큼은 내가 자신 있다'고 말할 수 있는 분야는 무엇인가요? (당신의 '전문성' 또는 '경험')")
        st.session_state.answers['value'] = st.text_input("[질문 3/5] 살면서 가장 중요하게 생각하는 가치 3가지는 무엇인가요? (예: 성장, 자유, 안정)")
        st.session_state.answers['target_problem'] = st.text_input("[질문 4/5] 당신의 지식이나 경험으로 어떤 사람들의 어떤 문제를 해결해주고 싶나요? (당신이 도울 '타겟')")
        st.session_state.answers['differentiation'] = st.text_input("[질문 5/5] 비슷한 주제의 다른 사람들과 비교했을 때, 당신만의 차별점이나 독특한 관점은 무엇인가요?")

    with st.expander("**Phase 2: 브랜드 정체성 수립하기**"):
        st.write("좋습니다. 이제 발견한 당신의 핵심을 바탕으로 '브랜드'의 얼굴을 만들어 보겠습니다.")
        st.session_state.answers['brand_core_message'] = st.text_input("[질문 1/4] 당신의 팔로워들에게 궁극적으로 전달하고 싶은 핵심 메시지를 한 문장으로 정의한다면 무엇일까요?")
        st.session_state.answers['keywords'] = st.text_input("[질문 2/4] 당신의 브랜드를 표현하는 핵심 키워드 5개를 꼽아주세요. (해시태그로 활용됩니다)")
        st.session_state.answers['tone_and_manner'] = st.selectbox("[질문 3/4] 팔로워들과 어떤 어조와 태도로 소통하고 싶나요?", ('친한 친구처럼 다정하게', '전문가처럼 신뢰감 있게', '유머러스하고 위트있게'))
        st.session_state.answers['visual_concept'] = st.text_input("[질문 4/4] 당신의 계정을 시각적으로 어떻게 표현하고 싶나요? (색감, 구도, 분위기 등)")

    with st.expander("**Phase 3: 콘텐츠 전략 기획**"):
        st.write("이제 팔로워들에게 어떤 가치를 전달할지 구체적인 계획을 세울 차례입니다. 콘텐츠 기둥(Pillar)은 당신의 채널을 단단하게 지탱해줍니다.")
        st.session_state.answers['content_pillar_1'] = st.text_input("[질문 1/3] 당신의 첫 번째 콘텐츠 기둥(주제 카테고리)은 무엇인가요?")
        st.session_state.answers['content_pillar_2'] = st.text_input("[질문 2/3] 두 번째 콘텐츠 기둥은 무엇인가요?")
        st.session_state.answers['content_pillar_3'] = st.text_input("[질문 3/3] 세 번째 콘텐츠 기둥은 무엇인가요? (없다면 비워두세요)")

    if st.button("**🎉 최종 브랜딩 가이드 생성하기!**"):
        st.balloons()
        st.header("✨ 당신만의 퍼스널 브랜딩 가이드 ✨")
        
        st.subheader("--- [나의 브랜드 정체성] ---")
        st.markdown(f"1.  **핵심 페르소나:** {st.session_state.answers['passion']}에 열정을 느끼고, {st.session_state.answers['expertise']}에 전문성을 가진 사람.")
        st.markdown(f"2.  **핵심 가치:** {st.session_state.answers['value']}")
        st.markdown(f"3.  **타겟 고객:** {st.session_state.answers['target_problem']} 문제를 겪는 사람들")
        st.markdown(f"4.  **차별점:** {st.session_state.answers['differentiation']}")
        
        st.subheader("--- [인스타그램 프로필 적용안] ---")
        st.markdown(f"5.  **한 줄 소개 (Bio):** \"{st.session_state.answers['brand_core_message']}\"")
        st.markdown(f"6.  **핵심 해시태그:** {st.session_state.answers['keywords']}")
        st.markdown(f"7.  **소통 방식 (톤앤매너):** {st.session_state.answers['tone_and_manner']}")
        st.markdown(f"8.  **시각적 컨셉 (Visual):** {st.session_state.answers['visual_concept']}")
        
        st.subheader("--- [콘텐츠 전략] ---")
        st.markdown("9.  **콘텐츠 기둥:**")
        st.markdown(f"    - Pillar 1: {st.session_state.answers['content_pillar_1']}")
        st.markdown(f"    - Pillar 2: {st.session_state.answers['content_pillar_2']}")
        if st.session_state.answers['content_pillar_3']:
            st.markdown(f"    - Pillar 3: {st.session_state.answers['content_pillar_3']}")

# --- 메인 실행 부분 ---
if __name__ == "__main__":
    run_branding_consulting()