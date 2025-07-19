import streamlit as st

# 페이지 설정 (가장 먼저 호출되어야 함)
st.set_page_config(
    page_title="어드밴스드 브랜딩 컨설턴트",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto",
)

def advanced_branding_consultant():
    """
    전문적인 내용을 모두 포함한 v2.0 브랜딩 컨설팅 프로그램
    """
    # session_state 초기화
    if 'answers' not in st.session_state:
        st.session_state.answers = {}

    st.title("🚀 어드밴스드 퍼스널 브랜딩 컨설턴트 v2.0")
    st.write("당신의 잠재력을 끌어내어 사람들의 마음을 움직이는 강력한 브랜드를 구축합니다.")
    st.markdown("---")

    # --- Phase 1: 자기 탐색 및 핵심 가치 발견 ---
    with st.expander("✅ Phase 1: 자기 탐색 (Self-Discovery)", expanded=True):
        st.subheader("나의 본질과 핵심 가치 찾기")
        st.session_state.answers['passion'] = st.text_input("Q. 시간 가는 줄 모르고 이야기할 수 있는 '열정'의 주제는 무엇인가요?")
        st.session_state.answers['expertise'] = st.text_input("Q. 다른 사람들에게 '이것만큼은 자신 있다'고 말할 수 있는 '전문성' 또는 '경험'은 무엇인가요?")
        st.session_state.answers['value'] = st.text_input("Q. 살면서 가장 중요하게 생각하는 핵심 '가치' 3가지는 무엇인가요? (예: 성장, 자유, 안정, 정직, 즐거움)")

    # --- Phase 2: 타겟 고객(페르소나) 심층 분석 ---
    with st.expander("🎯 Phase 2: 타겟 고객 심층 분석 (Audience Deep Dive)"):
        st.subheader("누구의 마음을 얻고 싶은가요?")
        st.info("Tip: '모두'를 위한 콘텐츠는 '아무도'를 위한 콘텐츠가 아닙니다. 단 한 사람을 구체적으로 그려보세요.")
        st.session_state.answers['target_avatar'] = st.text_area("Q. 당신의 이상적인 고객 '아바타'를 한 명 그려본다면 어떤 사람인가요? (나이, 직업, 성격 등)")
        st.session_state.answers['target_pain'] = st.text_area("Q. 그 사람이 밤에 잠 못 이루게 하는 가장 큰 '고민(Pain Point)'은 무엇인가요?")
        st.session_state.answers['target_gain'] = st.text_area("Q. 그 사람이 마음속 깊이 바라는 궁극적인 '욕망(Gain Point)'은 무엇인가요?")

    # --- Phase 3: 브랜드 정체성 및 개성(원형) 수립 ---
    with st.expander("🎭 Phase 3: 브랜드 정체성 및 개성 수립 (Brand Identity & Archetype)"):
        st.subheader("당신의 브랜드에 인격과 목소리 입히기")
        st.session_state.answers['brand_mission'] = st.text_input("Q. 당신이 고객의 '고민'을 해결해주고 '욕망'을 채워주기 위해 존재하는 이유, 즉 '브랜드 미션'을 한 문장으로 정의한다면?")
        
        # 브랜드 원형(Archetype) 선택
        archetypes = {
            "선택 안함": "브랜드의 성격을 정의합니다.",
            "The Sage (현자)": "지혜, 진실, 전문성으로 사람들을 안내합니다. (예: 전문가, 분석가)",
            "The Innocent (순수주의자)": "순수, 긍정, 행복을 추구하며 안전함을 줍니다. (예: 오가닉 브랜드, 아동 브랜드)",
            "The Explorer (탐험가)": "자유, 탐험, 발견을 통해 새로운 길을 제시합니다. (예: 아웃도어, 여행 크리에이터)",
            "The Hero (영웅)": "용기, 극복, 구원을 통해 세상에 긍정적 영향을 미칩니다. (예: 스포츠 브랜드, 사회적 기업)",
            "The Creator (창조자)": "창의성, 혁신, 예술로 새로운 것을 만듭니다. (예: 디자이너, 아티스트, 작가)",
            "The Ruler (지배자)": "통제, 리더십, 권위를 통해 최고가 되는 길을 보여줍니다. (예: 명품, 고급 자동차, CEO)",
            "The Magician (마법사)": "비전, 변화, 신비를 통해 꿈을 현실로 만듭니다. (예: 혁신 기술, 뷰티 브랜드)",
            "The Everyman (보통 사람)": "공감, 현실, 소박함으로 친근하게 다가갑니다. (예: 생활용품, 커뮤니티 리더)",
            "The Lover (연인)": "사랑, 관계, 감성을 통해 친밀한 유대감을 형성합니다. (예: 향수, 주얼리, 커플 코치)",
            "The Jester (광대)": "유머, 즐거움, 긍정으로 현재를 즐기게 합니다. (예: 스낵, 엔터테인먼트)",
            "The Caregiver (조력자)": "보호, 봉사, 이타심으로 타인을 돕고 지지합니다. (예: 병원, 비영리단체, 코치)",
            "The Outlaw (무법자)": "혁명, 파괴, 자유를 통해 기존의 틀을 깹니다. (예: 바이크, 스트릿 패션)"
        }
        selected_archetype = st.selectbox(
            "Q. 당신의 브랜드 '성격(Archetype)'은 무엇에 가장 가깝나요?",
            options=list(archetypes.keys()),
            format_func=lambda x: f"{x} - {archetypes[x]}"
        )
        st.session_state.answers['brand_archetype'] = selected_archetype

        st.session_state.answers['brand_keywords'] = st.text_input("Q. 당신의 브랜드를 검색할 때 사용될 '핵심 키워드' 5가지는 무엇인가요? (해시태그, 검색 최적화용)")
        st.session_state.answers['visual_concept'] = st.text_area("Q. 당신의 브랜드 '시각적 컨셉'을 구체적으로 묘사해주세요. (메인 컬러, 서브 컬러, 분위기, 사진 톤, 폰트 등)")

    # --- Phase 4: 콘텐츠 및 실행 전략 고도화 ---
    with st.expander("💡 Phase 4: 콘텐츠 및 실행 전략 고도화 (Content & Action Strategy)"):
        st.subheader("고객의 마음을 사로잡을 콘텐츠 설계하기")
        st.session_state.answers['pillar1'] = st.text_input("Q. 고객의 문제를 해결해 줄 첫 번째 '콘텐츠 기둥(Pillar)'은 무엇인가요? (예: 정보/교육)")
        st.session_state.answers['pillar2'] = st.text_input("Q. 고객과 공감대를 형성할 두 번째 '콘텐츠 기둥(Pillar)'은 무엇인가요? (예: 스토리/경험)")
        st.session_state.answers['pillar3'] = st.text_input("Q. 고객의 참여를 유도할 세 번째 '콘텐츠 기둥(Pillar)'은 무엇인가요? (예: 소통/커뮤니티)")
        
        st.markdown("---")
        st.session_state.answers['content_format'] = st.multiselect(
            "Q. 위 내용을 어떤 '콘텐츠 포맷'으로 주로 전달하고 싶나요?",
            ['릴스 (새로운 잠재고객 도달)', '카드뉴스 (정보의 체계적 전달)', '사진+글 (진솔한 스토리 전달)', '스토리 (일상적 소통 및 관계 형성)', '라이브 (실시간 질의응답 및 깊은 소통)']
        )
        st.session_state.answers['cta'] = st.text_input("Q. 팔로워가 당신의 콘텐츠를 보고 어떤 '행동(Call to Action)'을 하길 바라나요? (예: 저장하기, 댓글 남기기, 프로필 링크 클릭)")

    # --- Phase 5: 최종 목표 설정 ---
    with st.expander("🏆 Phase 5: 최종 목표 설정 (Ultimate Goal)"):
        st.subheader("브랜딩 여정의 목적지 설정하기")
        st.session_state.answers['ultimate_goal'] = st.selectbox(
            "Q. 이 브랜딩을 통해 궁극적으로 이루고 싶은 '목표'는 무엇인가요?",
            ['선택 안함', '온라인 상품/서비스 판매', '오프라인 강의/컨설팅', '제휴/광고 수익 창출', '팬 기반 커뮤니티 구축', '개인의 영향력(책 출간 등) 확대']
        )
        
    st.markdown("---")

    # --- 최종 리포트 생성 ---
    if st.button("🎉 최종 브랜딩 전략 리포트 생성하기", type="primary"):
        # 모든 답변이 입력되었는지 간단히 확인
        if not all(st.session_state.answers.values()):
            st.error("❗ 모든 질문에 답변을 입력해주세요. 리포트를 생성할 수 없습니다.")
        else:
            st.balloons()
            st.header("✨ 당신만의 퍼스널 브랜딩 전략 리포트 ✨")

            # 1. 브랜드 핵심 요약
            st.subheader("1. 나의 브랜드 한눈에 보기")
            st.success(f"**\"{st.session_state.answers['brand_mission']}\"** 라는 미션을 가진, **{st.session_state.answers['brand_archetype']}** 유형의 브랜드입니다.")
            st.markdown(f"* **나의 열정:** {st.session_state.answers['passion']}")
            st.markdown(f"* **나의 전문성:** {st.session_state.answers['expertise']}")
            st.markdown(f"* **나의 핵심 가치:** {st.session_state.answers['value']}")

            # 2. 타겟 고객 페르소나
            st.subheader("2. 나의 핵심 타겟 고객 (페르소나)")
            st.markdown(f"**아바타:** {st.session_state.answers['target_avatar']}")
            st.markdown(f"**가장 큰 고민:** {st.session_state.answers['target_pain']}")
            st.markdown(f"**궁극적 욕망:** {st.session_state.answers['target_gain']}")
            st.info("💡 Tip: 이 사람의 '고민'을 해결하고 '욕망'을 채워주는 콘텐츠에 집중하세요.")

            # 3. 인스타그램 프로필 최적화안
            st.subheader("3. 인스타그램 프로필 최적화 제안")
            st.markdown("**BIO (한 줄 소개)**")
            st.code(f"{st.session_state.answers['brand_mission']}\n문의는 DM | {st.session_state.answers['ultimate_goal']} 준비 중", language='text')
            st.markdown("**핵심 키워드/해시태그**")
            st.code(st.session_state.answers['brand_keywords'], language='text')
            st.markdown("**시각적 컨셉**")
            st.markdown(f"> {st.session_state.answers['visual_concept']}")
            
            # 4. 콘텐츠 전략
            st.subheader("4. 심층 콘텐츠 전략")
            st.markdown(f"**콘텐츠 기둥 1 (정보/교육):** {st.session_state.answers['pillar1']}")
            st.markdown(f"**콘텐츠 기둥 2 (스토리/공감대):** {st.session_state.answers['pillar2']}")
            st.markdown(f"**콘텐츠 기둥 3 (소통/커뮤니티):** {st.session_state.answers['pillar3']}")
            st.markdown(f"**주요 포맷:** {', '.join(st.session_state.answers['content_format'])}")
            st.markdown(f"**핵심 행동 유도(CTA):** 모든 콘텐츠는 팔로워가 **'{st.session_state.answers['cta']}'** 하도록 유도합니다.")
            
            st.success(f"이 모든 활동은 최종 목표인 **'{st.session_state.answers['ultimate_goal']}'** 달성을 향해 정렬되어야 합니다. 이 리포트를 바탕으로 꾸준히 실행하며 당신만의 강력한 브랜드를 만들어가세요!")


if __name__ == "__main__":
    advanced_branding_consultant()