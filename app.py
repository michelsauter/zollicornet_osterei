import streamlit as st
import random
import time

# --- CONFIGURATION & SETUP ---
st.set_page_config(page_title="Magische Ice Cream Macher", page_icon="🍦", layout="centered")

# --- INITIAL NAME GATE ---
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

if st.session_state.user_name == "":
    st.title("🍦 Willkomme bi dr magische Glace-Maschine!")
    name_input = st.text_input("Wie heissisch du?", placeholder="Schriib do dine Name...")
    
    if name_input:
        st.session_state.user_name = name_input
        st.rerun() 
    st.stop() 

# --- SESSION STATE FOR SELECTIONS ---
if 'flavor_score' not in st.session_state:
    st.session_state.flavor_score = 0
if 'chosen_flavor' not in st.session_state:
    st.session_state.chosen_flavor = None
if 'chosen_topping' not in st.session_state:
    st.session_state.chosen_topping = "None"

# Function to "send" the ice cream
def deliver_ice_cream(flavor, topping):
    st.toast(f"Hooray! A super {flavor} Glacer mit {topping} kunt!", icon="🍨")
    st.balloons()
    st.snow()  
    
    # We use a placeholder so the messages appear one after another nicely
    msg_slot = st.empty()
    
    msg_slot.info(f"Diiiiiing! Dini {flavor} Glace {topping} isch parat!")
    time.sleep(3)
    msg_slot.success(f"Das isch doch e Zollicornet!! 🍦")
    time.sleep(2)
    st.balloons()
    st.write(f"### Bis bald mol, Michel 👋")
    st.markdown("### 🦄🍦🌈")

# --- THE UI ---
st.title(f"🌈 Hallo {st.session_state.user_name}, wär wot e Glace!")
st.write(f"Sali {st.session_state.user_name}! Kum, mir mixe uns öppis!")

st.markdown("---")

# --- 1. FLAVOR ---
st.subheader("1. Welle Gschmagg wotsch? 🥛")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Vanille 🍦"):
        st.session_state.chosen_flavor = "Vanille"
        st.session_state.flavor_score += 1
with col2:
    if st.button("Schoggi 🍫"):
        st.session_state.chosen_flavor = "Schoggi"
        st.session_state.flavor_score += 1
with col3:
    if st.button("Himbeeri 🩷"):
        st.session_state.chosen_flavor = "Himbeeri"
        st.session_state.flavor_score = 5 # Trigger for easter egg

if st.session_state.chosen_flavor:
    st.info(f"Yum! **{st.session_state.chosen_flavor}** isch e gueti Wahl.")

# --- 2. TOPPINGS ---
st.markdown("---")
st.subheader("2. Und obe druf 🍬?")
sprinkle_amount = st.slider("Sprinkle Level", 0, 100, 20)

# FIX: Store the selectbox choice directly into session_state
st.session_state.chosen_topping = st.selectbox(
    "Wähl e Topping:", 
    ["None", "Rägetröpfli", "Smarties", "Schoggistreusel"]
)

if sprinkle_amount > 95:
    st.warning("WOAH! soooo viel!")
    st.markdown("# 🤩🍬🤩✨🤩🧁🤩")

# --- EASTER EGG ---
if sprinkle_amount > 90 and st.session_state.flavor_score >= 5:
    st.markdown("---")
    st.subheader("🤫 Psssst... Du hesch dr SECRET Knopf gfunde!")
    secret_code = st.text_input("Schrib es magischs Wort (Hiwiis: 'YUM'):", "").upper()
    
    if secret_code == "YUM":
        st.info("D'Maschine macht komischi Grüsch... 🎶")
        if st.button("ACTIVATE CHAOS CONE!"):
            st.snow()
            st.toast("CHAOS MODE!", icon="🎉")
            st.write("Das git a riese Glace! 🦄🍦🌈💩")

# --- 3. DELIVERY ---
st.markdown("---")
st.subheader("3. Esse mir! 😋")

if st.button("Ich bin parat zum Glace esse!"):
    # Check if they actually picked something
    if st.session_state.chosen_flavor and st.session_state.chosen_topping != "None":
        final_topping_str = f"mit {sprinkle_amount} {st.session_state.chosen_topping}"
        deliver_ice_cream(st.session_state.chosen_flavor, final_topping_str)
    else:
        st.error("Wait! D'Glace isch no nid fertig! Wähl bitte e Gschmagg UND e Topping!")