import streamlit as st
from voicebot import run_voicebot
from datetime import datetime
import base64

# ---------- REQUIRED FOR AUTOPLAY ----------
def get_base64_audio(file_path):
    with open(file_path, "rb") as audio_file:
        return base64.b64encode(audio_file.read()).decode()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="QueryBot — Simplotel AI", layout="centered", page_icon="🎙️")

st.markdown("""
<style>

/* GENERAL */
html, body, [data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top, #08172f, #020617);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background: transparent;
}

/* ORB CONTAINER */
.glass-box {
    background: rgba(255,255,255,0.05);
    border-radius: 25px;
    padding: 30px 10px;
    text-align: center;
    box-shadow: 0 0 30px rgba(0, 153, 255, 0.2);
    backdrop-filter: blur(12px);
}

/* RESPONSIVE ORB */
.orb {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    margin: auto;
    background: radial-gradient(circle at top right, #3cf0ff, #0044ff, #11001a);
    box-shadow: 0 0 40px #0099ff, inset 0 0 20px #00eaff;
    animation: pulse 5s infinite;
}

/* MOBILE */
@media (max-width: 600px) {
    .orb {
        width: 100px;
        height: 100px;
    }

    h1 {
        font-size: 26px !important;
    }

    .voice-text {
        font-size: 16px !important;
    }
}

@keyframes pulse {
  0% { transform: scale(0.95); }
  50% { transform: scale(1.05); }
  100% { transform: scale(0.95); }
}

h1 {
    text-align: center;
    font-size: 40px;
    margin-bottom: 30px;
}

.voice-text {
    font-size: 18px;
    margin-top: 15px;
    color: #cceeff;
}

/* CENTER BUTTON + CLEAN COLOR */
.stButton {
    display: flex;
    justify-content: center;
}

.stButton > button {
    background: rgba(0, 153, 255, 0.15);
    color: #cceeff;
    border-radius: 60px;
    height: 50px;
    font-size: 18px;
    padding: 10px 40px;
    border: 1px solid rgba(0, 153, 255, 0.4);
    margin-top: 25px;
    box-shadow: 0 0 15px rgba(0, 153, 255, 0.4);
    width: 260px;
    backdrop-filter: blur(10px);
}

/* Hover effect - subtle */
.stButton > button:hover {
    background: rgba(0, 153, 255, 0.25);
    box-shadow: 0 0 20px rgba(0, 153, 255, 0.7);
}


/* CHAT */
.chat-card {
    margin-top: 20px;
    padding: 15px;
    border-radius: 15px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
}

.user {
    color: #00eaff;
    font-weight: bold;
}

.bot {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1>🎙️ QueryBot – Simplotel AI Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>A Voice-Enabled Assistant for the Hotel Industry</p>", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- MAIN UI ----------------
st.markdown("""
<div class="glass-box">
    <div class="orb"></div>
    <div class='voice-text'>Tap the button & speak to QueryBot</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🎤 Start Talking"):
    with st.spinner("Listening..."):
        user_text, response, audio = run_voicebot()

        st.session_state.messages.append({
            "time": datetime.now().strftime("%H:%M"),
            "user": user_text,
            "bot": response
        })

        st.success("✅ Response generated!")


# ---------------- CHAT HISTORY ----------------
st.markdown("## 💬 Conversation")

for chat in reversed(st.session_state.messages[-10:]):
    st.markdown(f"""
    <div class="chat-card">
        <div class="user">You ({chat['time']}):</div>
        {chat['user']}
        <br><br>
        <div class="bot"><b>QueryBot:</b></div>
        {chat['bot']}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{get_base64_audio('audio/output.mp3')}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )
