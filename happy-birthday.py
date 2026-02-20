import streamlit as st
import time
from PIL import Image
import os

st.set_page_config(page_title="Happy Birthday Sukriti 🎉", page_icon="💌")

# 🌙 GLOBAL ANIMATED NIGHT SKY (ALL PAGES)
st.markdown("""
<style>

/* ===== NIGHT SKY GRADIENT ===== */
.stApp {
    background: linear-gradient(to bottom, #0b1d3a 0%, #142850 40%, #27496d 100%);
    overflow: hidden;
}

/* ===== SMALL GLOWING MOON ===== */
.moon {
    position: fixed;
    top: 120px;
    right: 60px;
    width: 90px;
    height: 90px;
    background: radial-gradient(circle at 30% 30%, #fff 40%, #f5f3ce 60%, #e0d8a7 100%);
    border-radius: 50%;
    box-shadow: 0 0 25px 10px rgba(255,255,200,0.6);
    animation: moonGlow 4s ease-in-out infinite;
    z-index: 0;
}

@keyframes moonGlow {
    0% { box-shadow: 0 0 25px 10px rgba(255,255,200,0.6); }
    50% { box-shadow: 0 0 45px 20px rgba(255,255,220,0.9); }
    100% { box-shadow: 0 0 25px 10px rgba(255,255,200,0.6); }
}

/* ===== FLOATING CLOUDS ===== */
.cloud {
    position: fixed;
    bottom: 0;
    width: 300px;
    height: 120px;
    background: radial-gradient(circle, rgba(255,255,255,0.8) 40%, rgba(255,255,255,0.1) 70%);
    border-radius: 50%;
    filter: blur(25px);
    animation: floatClouds 70s linear infinite;
    z-index: 0;
}

@keyframes floatClouds {
    0% { left: -400px; }
    100% { left: 110%; }
}

/* ===== SHOOTING STAR ===== */
.shooting-star {
    position: fixed;
    top: 100px;
    left: -100px;
    width: 150px;
    height: 2px;
    background: linear-gradient(90deg, white, transparent);
    opacity: 0;
    animation: shoot 8s linear infinite;
    z-index: 0;
}

@keyframes shoot {
    0% { transform: translateX(0) translateY(0); opacity: 1; }
    70% { opacity: 1; }
    100% { transform: translateX(1200px) translateY(400px); opacity: 0; }
}

/* ===== FADE-IN CONTENT ===== */
.block-container {
    position: relative;
    z-index: 1;
    color: white;
    animation: fadeIn 1.5s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* ===== MAIN TITLE ===== */
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: white;
    text-shadow: 0 0 15px rgba(255,255,255,0.9),
                 0 0 30px rgba(255,255,255,0.6);
    margin-top: 40px;
}

/* ===== SUB TITLE ===== */
.sub-title {
    text-align: center;
    font-size: 22px;
    color: #f8f8f8;
    text-shadow: 0 0 10px rgba(255,255,255,0.6);
    margin-bottom: 40px;
}

</style>

<div class="moon"></div>
<div class="cloud" style="left:-300px;"></div>
<div class="cloud" style="left:-700px;"></div>
<div class="shooting-star"></div>

""", unsafe_allow_html=True)

# --- Session State ---
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_home():
    st.session_state.page = "home"
    st.rerun()

def show_home_button():
    if st.session_state.page != "home":
        if st.button("🏠 Return to Home"):
            go_home()

# ---------------- HOME PAGE ---------------- #
if st.session_state.page == "home":

    st.markdown("""
    <h1 class="main-title">Happy Birthday 
Sukriti </h1>
    <h3 class="sub-title">💌 Open Your Birthday Letters 💌</h3>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🎂 Letter 1"):
            st.session_state.page = "letter1"
            st.rerun()

        if st.button("🎉 Letter 3"):
            st.session_state.page = "letter3"
            st.rerun()

    with col2:
        if st.button("📸 Letter 2"):
            st.session_state.page = "letter2"
            st.rerun()

        if st.button("💖 Letter 4"):
            st.session_state.page = "letter4"
            st.rerun()

# ---------------- LETTER 1 ---------------- #
elif st.session_state.page == "letter1":

    show_home_button()

    st.title("🎂 Letter 1")
    st.write("Ready to blow the candle? 🕯️")

    if st.button("Blow the Candle 🎂"):
        countdown = st.empty()

        for i in range(3, 0, -1):
            countdown.markdown(f"# {i}...")
            time.sleep(1)

        countdown.markdown("## 💨 Candle Blown!")
        time.sleep(1)

        st.markdown("## 🎂 Here’s Your Cake!")
        st.image("IMG_4520.jpeg", use_column_width=True)
        st.balloons()

# ---------------- LETTER 2 ---------------- #
elif st.session_state.page == "letter2":

    show_home_button()

    st.title("📸 Letter 2")
    st.write("A little compilation of beautiful memories 💕")

    photo_path = "IMG_4519.jpeg"

    if os.path.exists(photo_path):
        st.image(photo_path, use_column_width=True)
        st.balloons()
    else:
        st.warning("Memory photo not found 💕")

# ---------------- LETTER 3 ---------------- #
elif st.session_state.page == "letter3":

    show_home_button()

    st.title("🎉 Letter 3")

    st.markdown("""
    ## 🌸 Happy Birthday, Suku 🌸

    You were the best thing that happened at TIET,  
    the best gift in the form of a human I could ask for.

    I may not express much, might even make some blunders,  
    but remember you matter to me.

    I miss you, I miss us.  
    I will always be your greatest cheerleader.

    You deserve all the happiness in the world today and always.
    """)

    st.balloons()

# ---------------- LETTER 4 ---------------- #
elif st.session_state.page == "letter4":

    show_home_button()

    st.title("💖 Letter 4")

    st.markdown("""
    ## To My Dearest Suku,

    No matter where life takes us,  
    just remember one thing…

    ### 💞 I Love You 💞

    Forever and always,  
    Noor.
    """)

    st.snow()
