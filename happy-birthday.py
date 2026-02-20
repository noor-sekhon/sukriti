import streamlit as st
import time
from PIL import Image
import os

st.set_page_config(page_title="Happy Birthday Noor 🎉", page_icon="💌")

# --- Session State ---
if "page" not in st.session_state:
    st.session_state.page = "home"

# --- Function: Go Home ---
def go_home():
    st.session_state.page = "home"
    st.rerun()

# --- Function: Show Home Button ---
def show_home_button():
    if st.session_state.page != "home":
        if st.button("🏠 Return to Home"):
            go_home()

# ---------------- HOME PAGE ---------------- #
if st.session_state.page == "home":

    st.markdown(
        "<h1 style='text-align:center;'>💌 Open Your Birthday Letters 💌</h1>",
        unsafe_allow_html=True
    )

    st.write(" ")
    st.write("Choose a letter to open 💖")

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
        st.image("cake.png", use_column_width=True)
        st.balloons()

# ---------------- LETTER 2 ---------------- #
elif st.session_state.page == "letter2":

    show_home_button()

    st.title("📸 Letter 2")
    st.write("A little compilation of beautiful memories 💕")

    photo_folder = "photos"

    if os.path.exists(photo_folder):
        photos = os.listdir(photo_folder)
        for photo in photos:
            image = Image.open(os.path.join(photo_folder, photo))
            st.image(image, use_column_width=True)
            time.sleep(1)
    else:
        st.warning("Add a folder named 'photos' with your pictures inside!")

# ---------------- LETTER 3 ---------------- #
elif st.session_state.page == "letter3":

    show_home_button()

    st.title("🎉 Letter 3")

    st.markdown("""
    ## 🌸 Happy Birthday, Noor 🌸

    May your day be filled with  
    ✨ Laughter  
    💖 Love  
    🎂 Sweet surprises  
    🌟 Dreams coming true  

    You deserve all the happiness in the world today and always.
    """)

    st.balloons()

# ---------------- LETTER 4 ---------------- #
elif st.session_state.page == "letter4":

    show_home_button()

    st.title("💖 Letter 4")

    st.markdown("""
    ## To My Dearest Noor,

    No matter where life takes us,  
    just remember one thing…

    ### 💞 I Love You 💞

    Forever and always.
    """)

    st.snow()
