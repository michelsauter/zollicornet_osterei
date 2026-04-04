import streamlit as st
import time
import base64
import os

# --- 1. CONFIGURATION & SETUP ---
st.set_page_config(page_title="Magische Ice Cream Macher", page_icon="🍦", layout="centered")

# --- HIDE STREAMLIT STYLE ---
st.markdown("""
    <style>
        /* 1. Hide the standard footer and menu */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* 2. Nuke the 'Created by' badge and the toolbar wrapper */
        .viewerBadge_container__1QS1n {display: none !important;}
        .stAppDeployButton {display: none !important;}
        
        /* 3. Target the Streamlit Cloud toolbar specifically */
        [data-testid="stStatusWidget"] {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        
        /* 4. This targets the 'intercom' and host-injected elements */
        iframe[title="notification"] {display: none !important;}
        
        /* 5. Force the app to cover the full height and hide overflow from the host */
        #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
        
        /* 6. Try to hide the floating 'Manage app' button for the owner */
        div[class^="st-emotion-cache"] > button {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)


# --- 2. SOUND ENGINE ---
def play_local_sound(file_name):
    """Reads a local MP3 file and plays it in the browser using Base64."""
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay="true">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(md, unsafe_allow_html=True)
    else:
        # Minimal feedback if file is missing
        st.write("🔈 (S'Sound-File fählt no)")

# --- 3. INITIAL NAME GATE ---
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

if st.session_state.user_name == "":
    st.title("🍦 Willkomme bi dr magische Glace-Maschine!")
    name_input = st.text_input("Wie heissisch du?", placeholder="Schriib do din Name...")
    
    if name_input:
        st.session_state.user_name = name_input
        st.rerun() 
    st.stop() 

# --- 4. SESSION STATE FOR CHOICES ---
if 'flavor_score' not in st.session_state:
    st.session_state.flavor_score = 0
if 'chosen_flavor' not in st.session_state:
    st.session_state.chosen_flavor = None

# --- 5. DELIVERY FUNCTION ---
def deliver_ice_cream(flavor, topping):
    play_local_sound("egg-crack.mp3")
    st.toast(f"Hooray! A super {flavor} Glacer mit {topping} kunt!", icon="🍨")
    st.balloons()
    st.snow()  
    
    msg_slot = st.empty()
    msg_slot.info(f"Diiiiiing! Dini {flavor} Glace {topping} isch parat!")
    time.sleep(3)
    msg_slot.success(f"Das isch doch e Zollicornet!! 🍦")
    time.sleep(2)
    st.write(f"### Bis bald mol, Michel 👋")
    st.markdown("### 🦄🍦🌈")

# --- 6. THE MAIN UI ---
st.title(f"🌈 Hallo {st.session_state.user_name}, wär wot e Glace!")
st.write(f"Sali {st.session_state.user_name}! Kum, mir mixe uns öppis!")

st.markdown("---")

# --- INTERACTION 1: Flavor ---
st.subheader("1. Welle Gschmagg wotsch? 🥛")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Vanille 🍦"):
        st.session_state.chosen_flavor = "Vanille"
        st.session_state.flavor_score = 1
with col2:
    if st.button("Schoggi 🍫"):
        st.session_state.chosen_flavor = "Schoggi"
        st.session_state.flavor_score = 1
with col3:
    if st.button("Himbeeri 🩷"):
        st.session_state.chosen_flavor = "Himbeeri"
        st.session_state.flavor_score = 5 # Key for Easter Egg

if st.session_state.chosen_flavor:
    st.info(f"Yum! **{st.session_state.chosen_flavor}** isch e gueti Wahl.")

# --- INTERACTION 2: Toppings ---
st.markdown("---")
st.subheader("2. Und obe druf, e Topping 🍬?")
chosen_topping = st.selectbox("Wähl e Topping:", ["None", "Rägetröpfli", "Smarties", "Schoggistreusel"])
sprinkle_amount = st.slider("Sprinkle Level", 0, 100, 20)

if sprinkle_amount > 95:
    st.warning("WOAH! soooo viel!")
    st.markdown("# 🤩🍬🤩✨🤩🧁🤩")

# --- INTERACTION 3: Easter Egg (Chaos Mode) ---
if sprinkle_amount > 90 and st.session_state.flavor_score >= 5:
    st.markdown("---")
    st.subheader("🤫 Psssst... Du hesch dr SECRET Knopf gfunde!")
    st.write("Dä Knopf gits nume mit Himbeeri und vieel Toppings!")
    
    secret_code = st.text_input("Schrib es magischs Wort (Hiwiis: 'YUM'):", "").upper()
    
    if secret_code == "YUM":
        st.info("D'Maschine macht komischi Grüsch... 🎶")
        if st.button("ACTIVATE CHAOS CONE!"):
            play_local_sound("rabbit-sounds.mp3")
            st.snow()
            st.toast("CHAOS MODE!", icon="🎉")
            st.write("Das git a riese Glace!")
            st.markdown("### 🦄🍦🌈💩")
            st.balloons()

# --- INTERACTION 4: Final Order ---
st.markdown("---")
st.subheader("3. Esse mir! 😋")

if st.button("Ich bin parat zum Glace esse!"):
    if st.session_state.chosen_flavor and chosen_topping != "None":
        final_topping_str = f"mit {sprinkle_amount} {chosen_topping} obe druf."
        deliver_ice_cream(st.session_state.chosen_flavor, final_topping_str)
    else:
        st.error("Wait! D'Glace isch no nid fertig! Wähl bitte zersch e Gschmagg und e Topping!")