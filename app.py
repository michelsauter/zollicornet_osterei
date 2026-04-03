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
        st.rerun()  # Refresh the app to show the ice cream maker
    st.stop() # Prevents the rest of the code from running until name is entered

# --- THE REST OF THE APP (Only runs if name is entered) ---

# Initialize Session State for the game
if 'flavor_score' not in st.session_state:
    st.session_state.flavor_score = 0
if 'waffle_cone' not in st.session_state:
    st.session_state.waffle_cone = False
if 'special_code_active' not in st.session_state:
    st.session_state.special_code_active = False

# Function to "send" the ice cream
def deliver_ice_cream(flavor, topping):
    st.toast(f"Hooray! A super {flavor} Glacer mit {topping} kunt!", icon="🍨")
    st.balloons()
    st.snow()  # THE MAIN ICE CREAM CELEBRATION
    time.sleep(5)
    st.success(f"Diiiiiing! Dini {flavor} Glace mit {topping} isch parat!")
    time.sleep(2)
    st.success(f"Das isch doch e Zollicornet!!🍦")
    time.sleep(2)
    st.success(f"Bis bald mol, Michel")

    st.markdown("### 🦄🍦🌈")

# --- THE UI STARTS HERE ---
st.title(f"🌈 Hallo {st.session_state.user_name}, wär wot e Glace!")
st.write(f"Sali {st.session_state.user_name}! Kum, mir mixe uns öppis!")

st.markdown("---")

# --- INTERACTION 1: The Magic Flavor Mixer ---
st.subheader("1. Welle Gschmagg wotsch?🥛")
col1, col2, col3 = st.columns(3)

with col1:
    vanilla = st.button("Vanille 🍦")
with col2:
    choco = st.button("Schoggi 🍫")
with col3:
    himbeeri = st.button("Himbeeri 🩷")

chosen_flavor = None
if vanilla:
    chosen_flavor = "Vanille"
    st.session_state.flavor_score += 1
elif choco:
    chosen_flavor = "Schoggi"
    st.session_state.flavor_score += 1
elif himbeeri:
    chosen_flavor = "Himbeeri"
    st.session_state.flavor_score += 5 # Special flavor bonus

if chosen_flavor:
    st.write(f"Yum! **{chosen_flavor}** isch e gueti Wahl.")

# --- INTERACTION 2: The Secret Topping Slider ---
st.markdown("---")
st.subheader("2. Und obe druf 🍬?")
st.write("Hi und her fahre für e Topping! Wenns ganz rechts isch passirt öppis...")

sprinkle_amount = st.slider("Sprinkle Level", 0, 100, 20)

if sprinkle_amount > 95:
    st.warning("WOAH! soooo viel!")
    st.markdown("# 🤩🍬🤩✨🤩🧁🤩")
elif sprinkle_amount == 0:
    st.write("Moment, nüt obe druf, das isch doch langwilig! 😕")
else:
    st.write(f"Nume {sprinkle_amount} das isch doch z wenig obe druf")

chosen_topping = st.selectbox("Wähl e Topping:", ["None", "Rägetröpfli", "Smarties", "Schoggistreusel"])

# --- THE INTERACTIVE EASTER EGG (The 'Hidden' Button) ---
if sprinkle_amount > 90 and st.session_state.flavor_score >= 5:
    st.markdown("---")
    st.subheader("🤫 Psssst... Du hesch dr SECRET Knopf gfunde!")
    st.write("Dä Knopf gits nume mit Himbeeri und vieel Toppings!")
    
    # Text input inside the Easter egg area
    secret_code = st.text_input("Schrib es magischs Wort (Hiwiis: 'YUM'):", "").upper()
    
    if secret_code == "YUM":
        st.session_state.special_code_active = True
        st.info("D'Maschine macht komischi Grüsch... 🎶")
        if st.button("ACTIVATE CHAOS CONE!"):
            st.snow() # Double snow
            st.toast("CHAOS MODE!", icon="🎉")
            st.write("Das git a riese Glace!")
            st.markdown("### 🦄🍦🌈💩")

# --- DELIVERY SYSTEM ---
st.markdown("---")
st.subheader("3. Esse mir! 😋")

ready = st.checkbox("Ich bin parat zum Glace esse!")

if ready and chosen_flavor and chosen_topping:
    # We combine the selections
    final_flavor = chosen_flavor
    final_topping = f"mit {sprinkle_amount} {chosen_topping} obe druf."
    
    # Use our function to 'send' the treats
    deliver_ice_cream(final_flavor, final_topping)

elif ready and (not chosen_flavor or chosen_topping == "None"):
    st.error("Wait! Die Glace isch no nid fertig! Mir bruche nomol en Gschmagg und es Topping!")