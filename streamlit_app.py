import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="용해 마스터: 실시간 데이터 랩",
    layout="wide",
)

# 과학 계산 함수
def calculate_solubility(solute: str, temperature: int, water_ml: int) -> float:
    """물의 온도와 양에 따라 용해 가능한 용질(g)을 계산합니다."""
    base_water = 100
    water_ratio = water_ml / base_water

    if solute == "설탕":
        max_per_100ml = 180 + (temperature - 10) * 2.5
        max_per_100ml = max(0, max_per_100ml)
    else:
        max_per_100ml = 35 + (temperature - 10) * 0.04
        max_per_100ml = max(0, max_per_100ml)

    return max_per_100ml * water_ratio

# 앱 제목 및 설명
st.title("🔬 용해 마스터: 실시간 데이터 랩")
st.markdown("물과 용질의 마법 같은 만남을 직접 조작해 보세요!")

# 사이드바 입력
with st.sidebar:
    st.header("실험 조작판")
    solute = st.selectbox("어떤 용질을 녹일까요?", ["설탕", "소금"])
    temperature = st.slider("물의 온도 (°C)", min_value=10, max_value=80, value=20)
    water_ml = st.slider("물의 양 (mL)", min_value=50, max_value=300, value=100)
    input_mass = st.slider("투입할 용질의 양 (g)", min_value=0, max_value=300, value=10)

# 계산
max_dissolved = calculate_solubility(solute, temperature, water_ml)
dissolved = min(input_mass, max_dissolved)
undissolved = max(0.0, input_mass - dissolved)

total_water_ratio = water_ml / 300
water_height = 20 + total_water_ratio * 70
water_height = min(92, max(20, water_height))
sediment_height = min(28, undissolved / 10)
particle_count = int(4 + (dissolved / max_dissolved) * 28) if max_dissolved > 0 else 4
particle_count = min(32, max(4, particle_count))
particle_html = "".join(["<span>✨</span>" for _ in range(particle_count)])
block_count = int(min(20, undissolved / 5))
block_html = "".join(["<span>🧊</span>" for _ in range(block_count)])

# 캐릭터 반응
if undissolved == 0 and input_mass > 0.95 * max_dissolved and input_mass > 0:
    pig_message = "🐷 꿀꿀! 완벽하게 다 녹았어! 투명하고 맛있는 물약 완성!"
    success_trigger = True
elif undissolved >= 1:
    pig_message = "🐷 앗! 바닥에 가루가 가라앉고 있어. 물이 더 필요하거나 온도를 높여야 할까?"
    success_trigger = False
else:
    pig_message = "🐷 슬라이더를 움직여서 용해의 비밀을 찾아보자!"
    success_trigger = False

# 메인 화면 출력
col1, col2, col3 = st.columns(3)
col1.metric("총 투입량", f"{input_mass:.1f} g")
col2.metric("완벽하게 녹은 양", f"{dissolved:.1f} g")
col3.metric("바닥에 가라앉은 양", f"{undissolved:.1f} g")

st.markdown("---")

beaker_html = f"""
<div class='beaker-area'>
  <div class='beaker-wrapper'>
    <div class='speech-box'>{pig_message}</div>
    <div class='beaker'>
      <div class='beaker-glass'></div>
      <div class='liquid' style='height: {water_height:.1f}%;'>
        <div class='particles'>{particle_html}</div>
      </div>
      <div class='sediment' style='height: {sediment_height:.1f}%;'>
        {block_html}
      </div>
    </div>
  </div>
</div>
"""

beaker_style = """
<style>
.beaker-area {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px 0;
}
.beaker-wrapper {
  position: relative;
  width: 320px;
}
.speech-box {
  position: absolute;
  top: -90px;
  left: 0;
  right: 0;
  background: #fff9e0;
  border: 2px solid #ffd966;
  border-radius: 20px;
  padding: 12px 16px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.14);
  font-size: 1rem;
  line-height: 1.4;
  color: #333;
}
.speech-box::after {
  content: '';
  position: absolute;
  bottom: -14px;
  left: 40px;
  border-width: 14px 12px 0 12px;
  border-style: solid;
  border-color: #fff9e0 transparent transparent transparent;
}
.beaker {
  position: relative;
  width: 100%;
  height: 420px;
  margin: 0 auto;
}
.beaker-glass {
  position: absolute;
  inset: 0;
  border: 6px solid rgba(80, 145, 205, 0.9);
  border-radius: 40px 40px 60px 60px;
  background: rgba(255, 255, 255, 0.08);
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.18);
}
.liquid {
  position: absolute;
  left: 12px;
  right: 12px;
  bottom: 22px;
  border-radius: 0 0 32px 32px;
  background: linear-gradient(180deg, rgba(165, 220, 255, 0.95), rgba(60, 140, 215, 0.95));
  overflow: hidden;
  transition: height 0.4s ease;
}
.particles {
  position: absolute;
  top: 10px;
  left: 6px;
  right: 6px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-content: flex-start;
  padding: 8px;
  gap: 4px;
}
.particles span {
  display: inline-block;
  font-size: 18px;
  animation: float 5s ease-in-out infinite;
}
@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}
.sediment {
  position: absolute;
  left: 12px;
  right: 12px;
  bottom: 22px;
  background: rgba(255, 255, 255, 0.92);
  border-radius: 0 0 28px 28px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: flex-end;
  padding-bottom: 6px;
  overflow: hidden;
  transition: height 0.4s ease;
}
.sediment span {
  font-size: 20px;
  margin: 1px;
}
</style>
"""

col_main, col_sidebar = st.columns([2, 1])
with col_main:
    st.subheader("🔎 가상의 3D 비커 실험")
    st.markdown(beaker_style + beaker_html, unsafe_allow_html=True)

with col_sidebar:
    st.subheader("실험 요약")
    st.write(f"- 선택된 용질: **{solute}**")
    st.write(f"- 물 온도: **{temperature}°C**")
    st.write(f"- 물의 양: **{water_ml} mL**")
    st.write("- 이 물에서 녹을 수 있는 최대 용질 수치는 숨겨졌어요. 직접 추리해 보세요!")

# 상호작용 피드백
if undissolved == 0 and input_mass > 0.95 * max_dissolved and input_mass > 0:
    st.success("🎉 포화 상태 달성! 완벽한 황금 비율입니다!")
    st.balloons()
elif undissolved >= 1:
    st.error(
        "⚠️ 용해 실패! 바닥에 용질이 가라앉기 시작했습니다. 물을 더 넣거나 온도를 높여 보세요!"
    )
else:
    st.info("슬라이더를 조정하면서 물과 용질의 관계를 직접 확인해 보세요.")
