import streamlit as st

st.set_page_config(
    page_title="🧙‍♂️ 온도 마법사: 물의 3가지 변신!",
    layout="centered",
)

st.title("🧙‍♂️ 온도 마법사: 물의 3가지 변신!")
st.markdown("#### 마법 지팡이(슬라이더)를 움직여 물의 상태를 바꿔보세요!")

st.write("---")

temperature = st.slider(
    "마법 지팡이로 온도를 조절해요!",
    min_value=-20,
    max_value=120,
    value=20,
    step=1,
)

st.write("\n")

if temperature <= 0:
    state_title = "🧊 꽁꽁 얼어붙은 얼음 (고체)"
    concept_text = "모양과 부피가 변하지 않고 일정해요!"
    display_icon = "🧊🧊🧊"
    stage_text = "차가운 얼음 세상이에요."
    bar_color = "#7ed6df"
    st.snow()
elif temperature >= 100:
    state_title = "☁️ 피어오르는 수증기 (기체)"
    concept_text = "모양과 부피가 모두 변하고, 공간을 가득 채워요!"
    display_icon = "☁️☁️☁️"
    stage_text = "뜨거운 수증기가 하늘로 올라가요."
    bar_color = "#f6b93b"
    st.balloons()
else:
    state_title = "💧 넘실거리는 물 (액체)"
    concept_text = "부피는 일정하지만, 담는 그릇에 따라 모양이 변해요!"
    display_icon = "💧💧💧"
    if temperature <= 20:
        stage_text = "차가운 물이에요. 얼음이 막 녹았어요."
        bar_color = "#74b9ff"
    elif temperature <= 60:
        stage_text = "따뜻한 물이에요. 신나게 흔들어 보세요!"
        bar_color = "#38ada9"
    else:
        stage_text = "뜨거운 물이에요. 곧 김이 올라올 거예요!"
        bar_color = "#ff6b6b"

heat_level = int((temperature + 20) / 140 * 100)
heat_level = max(0, min(100, heat_level))

st.markdown(
    f"<div style='text-align:center; padding: 24px 18px; border: 3px solid {bar_color}; border-radius: 22px; background: linear-gradient(180deg, #ffffff 0%, #e3f2fd 100%); color:#0d3b66;'>"
    f"<h2 style='margin-bottom: 6px; color:#0d3b66;'>{state_title}</h2>"
    f"<p style='font-size: 1.1rem; margin: 8px 0 0 0; color:#1f3a93;'>{concept_text}</p>"
    f"<p style='font-size: 1rem; margin: 8px 0 0 0; color:#3867d6;'>{stage_text}</p>"
    f"<p style='font-size: 2.8rem; margin: 16px 0 0 0;'>{display_icon}</p>"
    f"</div>",
    unsafe_allow_html=True,
)

st.write("\n")

st.markdown(
    f"<div style='max-width:620px; margin: 0 auto;'>"
    f"<div style='height: 20px; width: 100%; background: #dfe6e9; border-radius: 999px; overflow: hidden;'>"
    f"<div style='width: {heat_level}%; height: 100%; background: linear-gradient(90deg, #74b9ff, {bar_color});'></div>"
    f"</div>"
    f"<p style='text-align:center; margin: 8px 0 0 0; font-weight:700; color:#2d3436;'>현재 온도: {temperature}°C — 물의 움직임이 달라져요!</p>"
    f"</div>",
    unsafe_allow_html=True,
)

st.markdown(
    "<div style='display:flex; justify-content:center; gap:12px; flex-wrap:wrap;'>"
    "<span style='padding:14px 18px; border-radius:18px; background:#74b9ff; color:#ffffff; font-weight:700;'>0°C 이하 → 얼음</span>"
    "<span style='padding:14px 18px; border-radius:18px; background:#38ada9; color:#ffffff; font-weight:700;'>1°C~99°C → 물</span>"
    "<span style='padding:14px 18px; border-radius:18px; background:#ff6b6b; color:#ffffff; font-weight:700;'>100°C 이상 → 수증기</span>"
    "</div>",
    unsafe_allow_html=True,
)

st.write("\n")

st.info(
    "온도가 0도 아래로 내려가면 고체인 얼음이 되고, 100도 이상이 되면 기체인 수증기로 변해요. "
    "20도는 우리 주변에서 가장 친숙한 물의 온도예요."
)

st.write("---")

st.caption("온도 슬라이더를 움직이면 물의 상태가 어떻게 변하는지 눈으로 확인해 보세요!")
