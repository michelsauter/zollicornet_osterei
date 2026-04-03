import streamlit as st
import time
import random

st.set_page_config(page_title="Nothing to see here", page_icon="🥚")

# --- SECRET STATE ---
if 'click_count' not in st.session_state:
    st.session_state.click_count = 0
if 'chaos_mode' not in st.session_state:
    st.session_state.chaos_mode = False

# --- THE UI ---
st.title("Just a Productivity App™")
st.write("This is a very serious tool for serious people. Please interact with it professionally.")

# --- THE BAIT ---
col1, col2 = st.columns(2)

with col1:
    if st.button("Do NOT Click Me"):
        st.session_state.click_count += 1
        
        if st.session_state.click_count == 1:
            st.warning("I said 'Do NOT'. Please respect my boundaries.")
        elif st.session_state.click_count == 2:
            st.error("Okay, that's twice. Stop it.")
        elif st.session_state.click_count == 3:
            st.info("I'm going to start counting to three... oh wait.")
        elif st.session_state.click_count >= 5:
            st.session_state.chaos_mode = True
            st.balloons()
            st.toast("Look what you've done.", icon="🫠")

with col2:
    suspicious_slider = st.slider("Reality Distortion Level", 0, 100, 0)
    if suspicious_slider > 90:
        st.write("🌌 *The fabric of the app is thinning...*")

# --- THE EASTER EGGS ---

# 1. The Low-Key Sass
if st.session_state.chaos_mode:
    st.markdown("---")
    st.subheader("⚠️ SYSTEM COMPROMISED")
    
    # 2. Interactive Glitch
    user_input = st.text_input("Type 'Sorry' to fix it:", "")
    if user_input.lower() == "sorry":
        st.success("Apology accepted. (Not really, but I'll hide the mess.)")
        if st.button("Reset Reality"):
            st.session_state.click_count = 0
            st.session_state.chaos_mode = False
            st.rerun()
    
    # 3. Random Humor Generator
    if st.button("Push for a bad tech joke"):
        jokes = [
            "Why did the web developer walk out of the restaurant? Because of the table layout.",
            "A SQL query walks into a bar, walks up to two tables, and asks... 'Can I join you?'",
            "Hardware: The parts of a computer that you can kick.",
            "There are 10 types of people: those who understand binary, and those who don't."
        ]
        st.code(random.choice(jokes), language="markdown")

# 4. The "Invisible" Interaction
st.sidebar.title("Settings")
if st.sidebar.checkbox("Show 'The Secret'"):
    st.sidebar.write("2026 Prediction: Streamlit will eventually develop sentience. This checkbox is the first step.")
    st.sidebar.image("https://pillows.com/cdn/shop/products/standard-white-pillow_1024x1024.jpg?v=1571438591", 
                     caption="A picture of a 'Cloud' for tech enthusiasts.", width=150)

# 5. Hidden Math (Using LaTeX because why not)
if st.session_state.click_count > 10:
    st.write("You've clicked too much. Here is the formula for your boredom:")
    st.latex(r"B_{ore} = \sum_{i=1}^{clicks} \frac{TimeLost}{Productivity^2}")