# 파일명: app.py
# Streamlit을 사용하여 웹 앱으로 실행하는 코드입니다.

import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="어드밴스드 브랜딩 컨설턴트 v3.0",
    page_icon="🚀",
    layout="wide", # 넓은 레이아웃으로 변경하여 가이드 내용을 더 잘 보여줍니다.
    initial_sidebar_state="auto",
)

def ultimate_branding_consultant():
    """
    상세 가이드와 AI 프롬프트 제안 기능이 포함된 v3.0 브랜딩 컨설팅 프로그램
    """
    # session_state 초기화
    if 'answers' not in st.session_state:
        st.session_state.answers = {}

    st.title("🚀 어드밴스드 퍼스널 브랜딩 컨설턴트 v3.0")
    st.write("당신의 잠재력을 끌어내어 사람들의 마음을 움직이는 강력한 브랜드를 구축합니다.")
    st.markdown("---")

    # 컬럼을 사용하여 레이아웃을 구성
    col1, col2 = st.columns(2)

    with col1:
        # --- Phase 1: 자기 탐색 및 핵심 가치 발견 ---
        with st.expander("✅ Phase 1: 자기 탐색 (Self-Discovery)", expanded=True):
            st.subheader("나의 본질과 핵심 가치 찾기")
            st.session_state.answers['passion'] = st.text_input("Q. 시간 가는 줄 모르고 이야기할 수 있는 '열정'의 주제는 무엇인가요?")
            st.session_state.answers['expertise'] = st.text_input("Q. 다른 사람들에게 '이것만큼은 자신 있다'고 말할 수 있는 '전문성' 또는 '경험'은 무엇인가요?")
            st.session_state.answers['value'] = st.text_input("Q. 살면서 가장 중요하게 생각하는 핵심 '가치' 3가지는 무엇인가요?")

        # --- Phase 2: 타겟 고객(페르소나) 심층 분석 ---
        with st.expander("🎯 Phase 2: 타겟 고객 심층 분석 (Audience Deep Dive)"):
            st.subheader("누구의 마음을 얻고 싶은가요?")
            st.info("Tip: '모두'를 위한 콘텐츠는 '아무도'를 위한 콘텐츠가 아닙니다. 단 한 사람을 구체적으로 그려보세요.")
            st.session_state.answers['target_avatar'] = st.text_area("Q. 당신의 이상적인 고객 '아바타'를 한 명 그려본다면 어떤 사람인가요?")
            st.session_state.answers['target_pain'] = st.text_area("Q. 그 사람이 밤에 잠 못 이루게 하는 가장 큰 '고민(Pain Point)'은 무엇인가요?")
            st.session_state.answers['target_gain'] = st.text_area("Q. 그 사람이 마음속 깊이 바라는 궁극적인 '욕망(Gain Point)'은 무엇인가요?")

        # --- Phase 3: 브랜드 정체성 및 개성(원형) 수립 ---
        with st.expander("🎭 Phase 3: 브랜드 정체성 및 개성 수립 (Brand Identity & Archetype)"):
            st.subheader("당신의 브랜드에 인격과 목소리 입히기")
            st.session_state.answers['brand_mission'] = st.text_input("Q. 당신이 고객의 '고민'을 해결해주고 '욕망'을 채워주기 위해 존재하는 이유, 즉 '브랜드 미션'을 한 문장으로 정의한다면?")
            
            archetypes = {
                "선택 안함": "브랜드의 성격을 정의합니다.", "The Sage (현자)": "지혜, 진실, 전문성으로 사람들을 안내합니다.", "The Innocent (순수주의자)": "순수, 긍정, 행복을 추구하며 안전함을 줍니다.",
                "The Explorer (탐험가)": "자유, 탐험, 발견을 통해 새로운 길을 제시합니다.", "The Hero (영웅)": "용기, 극복, 구원을 통해 세상에 긍정적 영향을 미칩니다.",
                "The Creator (창조자)": "창의성, 혁신, 예술로 새로운 것을 만듭니다.", "The Ruler (지배자)": "통제, 리더십, 권위를 통해 최고가 되는 길을 보여줍니다.",
                "The Magician (마법사)": "비전, 변화, 신비를 통해 꿈을 현실로 만듭니다.", "The Everyman (보통 사람)": "공감, 현실, 소박함으로 친근하게 다가갑니다.",
                "The Lover (연인)": "사랑, 관계, 감성을 통해 친밀한 유대감을 형성합니다.", "The Jester (광대)": "유머, 즐거움, 긍정으로 현재를 즐기게 합니다.",
                "The Caregiver (조력자)": "보호, 봉사, 이타심으로 타인을 돕고 지지합니다.", "The Outlaw (무법자)": "혁명, 파괴, 자유를 통해 기존의 틀을 깹니다."
            }
            selected_archetype = st.selectbox("Q. 당신의 브랜드 '성격(Archetype)'은 무엇에 가장 가깝나요?", options=list(archetypes.keys()), format_func=lambda x: f"{x} - {archetypes[x]}")
            st.session_state.answers['brand_archetype'] = selected_archetype
            st.session_state.answers['brand_keywords'] = st.text_input("Q. 당신의 브랜드를 검색할 때 사용될 '핵심 키워드' 5가지는 무엇인가요?")
            st.session_state.answers['visual_concept'] = st.text_area("Q. 당신의 브랜드 '시각적 컨셉'을 구체적으로 묘사해주세요.")

    with col2:
        # --- Phase 4 & 5: 전략 및 목표 설정 ---
        with st.expander("💡 Phase 4: 콘텐츠 및 실행 전략 고도화 (Content & Action Strategy)", expanded=True):
            st.subheader("고객의 마음을 사로잡을 콘텐츠 설계하기")
            st.session_state.answers['pillar1'] = st.text_input("Q. 고객의 문제를 해결해 줄 첫 번째 '콘텐츠 기둥(Pillar)'은 무엇인가요?")
            st.session_state.answers['pillar2'] = st.text_input("Q. 고객과 공감대를 형성할 두 번째 '콘텐츠 기둥(Pillar)'은 무엇인가요?")
            st.session_state.answers['pillar3'] = st.text_input("Q. 고객의 참여를 유도할 세 번째 '콘텐츠 기둥(Pillar)'은 무엇인가요?")
            st.session_state.answers['content_format'] = st.multiselect("Q. 위 내용을 어떤 '콘텐츠 포맷'으로 주로 전달하고 싶나요?", ['릴스', '카드뉴스', '사진+글', '스토리', '라이브'])
            st.session_state.answers['cta'] = st.text_input("Q. 팔로워가 당신의 콘텐츠를 보고 어떤 '행동(Call to Action)'을 하길 바라나요?")

        with st.expander("🏆 Phase 5: 최종 목표 설정 (Ultimate Goal)"):
            st.subheader("브랜딩 여정의 목적지 설정하기")
            st.session_state.answers['ultimate_goal'] = st.selectbox("Q. 이 브랜딩을 통해 궁극적으로 이루고 싶은 '목표'는 무엇인가요?", ['선택 안함', '온라인 상품/서비스 판매', '오프라인 강의/컨설팅', '제휴/광고 수익 창출', '팬 기반 커뮤니티 구축', '개인의 영향력(책 출간 등) 확대'])
    
    st.markdown("---")

    # --- 최종 리포트 및 다음 단계 안내 생성 ---
    if st.button("🎉 최종 브랜딩 전략 리포트 & 다음 단계 가이드 생성하기", type="primary"):
        is_ready = all(st.session_state.answers.get(key) for key in ['passion', 'expertise', 'value', 'target_avatar', 'target_pain', 'target_gain', 'brand_mission', 'brand_archetype', 'brand_keywords', 'visual_concept', 'pillar1', 'pillar2', 'pillar3', 'content_format', 'cta', 'ultimate_goal'])
        
        if not is_ready:
            st.error("❗ 모든 질문에 답변을 입력해주세요. 리포트를 생성할 수 없습니다.")
        else:
            st.balloons()
            st.header("✨ 당신만의 퍼스널 브랜딩 전략 리포트 (자가 진단 결과) ✨")
            
            # 자가 진단 리포트 출력
            report_text = f"""
            ### 1. 나의 브랜드 한눈에 보기
            - **브랜드 미션:** "{st.session_state.answers['brand_mission']}"
            - **브랜드 성격:** {st.session_state.answers['brand_archetype']}
            - **나의 열정:** {st.session_state.answers['passion']}
            - **나의 전문성:** {st.session_state.answers['expertise']}
            - **나의 핵심 가치:** {st.session_state.answers['value']}

            ### 2. 나의 핵심 타겟 고객 (페르소나)
            - **아바타:** {st.session_state.answers['target_avatar']}
            - **가장 큰 고민(Pain Point):** {st.session_state.answers['target_pain']}
            - **궁극적 욕망(Gain Point):** {st.session_state.answers['target_gain']}

            ### 3. 인스타그램 프로필 최적화 제안
            - **BIO (한 줄 소개) 초안:** "{st.session_state.answers['brand_mission']} | {st.session_state.answers['ultimate_goal']} 준비 중"
            - **핵심 키워드/해시태그:** {st.session_state.answers['brand_keywords']}
            - **시각적 컨셉:** {st.session_state.answers['visual_concept']}

            ### 4. 심층 콘텐츠 전략
            - **콘텐츠 기둥 1 (정보/교육):** {st.session_state.answers['pillar1']}
            - **콘텐츠 기둥 2 (스토리/공감대):** {st.session_state.answers['pillar2']}
            - **콘텐츠 기둥 3 (소통/커뮤니티):** {st.session_state.answers['pillar3']}
            - **주요 포맷:** {', '.join(st.session_state.answers['content_format'])}
            - **핵심 행동 유도(CTA):** '{st.session_state.answers['cta']}'
            """
            st.markdown(report_text)
            st.markdown("---")

            # 다음 단계 안내 및 AI 프롬프트 제안
            st.header("🎉 다음 단계: AI 전문가와 함께 전략을 완성하세요")
            st.info("""
            **훌륭합니다! 브랜딩의 가장 중요한 첫 단추인 '자가 진단'을 마치셨습니다.**
            
            이 결과는 당신의 생각을 정리한 '최고의 재료'입니다. 이제 이 재료를 가지고 **AI 전문가(셰프)**에게 가서, 훨씬 더 깊이 있는 **'전략 요리'**를 만들 차례입니다. 
            아래 4단계 프로세스를 따라 당신의 브랜드를 완성하고, 수십 개의 콘텐츠 아이디어로 확장해보세요.
            """)

            st.subheader("STEP 2: AI 전문가에게 심층 컨설팅 요청하기")
            st.write("아래 '맞춤 프롬프트' 전체를 복사하여, 사용하고 계신 생성형 AI 서비스(예: Gemini, ChatGPT 등)에 그대로 붙여넣고 질문하세요. 당신의 답변을 바탕으로 제가 했던 것과 같은 전문가 수준의 심층 분석을 제공할 것입니다.")
            
            # 전문가 컨설팅을 위한 맞춤 프롬프트 생성
            prompt_for_ai = f"""
당신은 세계 최고의 SNS 브랜드 전략가입니다. 저는 지금 저만의 퍼스널 브랜딩을 구축하는 중이며, 아래는 제가 직접 작성한 '브랜드 자가 진단 리포트'입니다.

이 리포트의 내용을 바탕으로, 단순 요약이 아닌 전문가로서의 **'심층 분석 및 크리에이티브 컨설팅'**을 제공해주세요.

**[나의 브랜드 자가 진단 리포트]**

**1. 나의 브랜드 핵심:**
- **브랜드 미션:** "{st.session_state.answers['brand_mission']}"
- **브랜드 성격:** {st.session_state.answers['brand_archetype']}
- **나의 열정:** {st.session_state.answers['passion']}
- **나의 전문성:** {st.session_state.answers['expertise']}
- **나의 핵심 가치:** {st.session_state.answers['value']}

**2. 나의 핵심 타겟 고객:**
- **아바타:** {st.session_state.answers['target_avatar']}
- **가장 큰 고민(Pain Point):** {st.session_state.answers['target_pain']}
- **궁극적 욕망(Gain Point):** {st.session_state.answers['target_gain']}

**3. 콘텐츠 전략 초안:**
- **콘텐츠 기둥 1:** {st.session_state.answers['pillar1']}
- **콘텐츠 기둥 2:** {st.session_state.answers['pillar2']}
- **콘텐츠 기둥 3:** {st.session_state.answers['pillar3']}
- **최종 목표:** {st.session_state.answers['ultimate_goal']}

**[전문가에게 요청하는 컨설팅 내용]**

1.  **브랜드 재창조:** 제가 작성한 내용을 바탕으로, 타겟 고객의 심장을 뛰게 할 **더 매력적인 브랜드 미션과 페르소나**를 재정의해주세요.
2.  **프로필 최적화:** 재창조된 브랜드를 바탕으로, 사람들의 시선을 사로잡을 **인스타그램 BIO(한 줄 소개), 핵심 해시태그, 구체적인 시각적 컨셉**을 제안해주세요.
3.  **콘텐츠 전략 구체화:** 저의 콘텐츠 기둥들을 **고객의 관점에서 더 매력적인 카테고리 이름**으로 바꾸고, 각 카테고리별로 당장 실행할 수 있는 **구체적인 콘텐츠 아이디어(릴스, 카드뉴스, 스토리 등)를 3개 이상씩** 제안해주세요.
"""
            st.code(prompt_for_ai, language='text')
            st.write("")

            st.subheader("STEP 3 & 4: 핵심 키워드 추출 및 콘텐츠 마인드맵 확장하기")
            st.write("""
            **STEP 3:** AI 전문가의 컨설팅 답변을 받으면, 그 내용에서 **가장 중요하다고 생각하는 '핵심 전략 키워드'들을 직접 정리**해보세요. (예: 40대 여성의 자신감 회복, 호르몬 다이어트, 공감 스토리 등)

            **STEP 4:** 마지막으로, 정리한 핵심 키워드들을 다시 AI에게 보여주며 아래와 같이 요청하세요.
            """)
            st.code("위 핵심 키워드들을 중심으로, 제 인스타그램 콘텐츠 기획을 위한 마인드맵을 트리(tree) 형식으로 풍성하게 만들어주세요.", language='text')
            st.success("이 모든 과정을 통해 당신은 하나의 단단한 전략과 수십 개의 콘텐츠 아이디어를 모두 얻게 될 것입니다. 지금 바로 STEP 2를 시작해보세요!")

if __name__ == "__main__":
    ultimate_branding_consultant()