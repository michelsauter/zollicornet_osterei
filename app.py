import streamlit as st
import random
import time

# --- CONFIGURATION & SETUP ---
st.set_page_config(page_title="Magical Ice Cream Maker", page_icon="🍦", layout="centered")

# Initialize Session State
if 'flavor_score' not in st.session_state:
    st.session_state.flavor_score = 0
if 'waffle_cone' not in st.session_state:
    st.session_state.waffle_cone = False
if 'special_code_active' not in st.session_state:
    st.session_state.special_code_active = False

# Function to "send" the ice cream
def deliver_ice_cream(flavor, topping):
    st.toast(f"Hooray! A super {flavor} ice cream with {topping} is coming!", icon="🍨")
    st.balloons()
    st.snow()  # THE MAIN ICE CREAM CELEBRATION
    time.sleep(1)
    st.success(f"Diiiiiing! Your {flavor} {topping} cone is ready! 🍦")

# --- THE UI STARTS HERE ---
st.title("🌈 Welcome to the Magical Ice Cream Maker!")
st.write("Let's mix up a virtual treat. But watch out for the secret buttons!")

st.markdown("---")

# --- INTERACTION 1: The Magic Flavor Mixer ---
st.subheader("1. Choose Your Base Flavor 🥛")
col1, col2, col3 = st.columns(3)

with col1:
    vanilla = st.button("Classic Vanilla 🍦")
with col2:
    choco = st.button("Super Chocolate 🍫")
with col3:
    alien = st.button("Alien Green Apple 👽🍏")

chosen_flavor = None
if vanilla:
    chosen_flavor = "Vanilla"
    st.session_state.flavor_score += 1
elif choco:
    chosen_flavor = "Super Chocolate"
    st.session_state.flavor_score += 1
elif alien:
    chosen_flavor = "Alien Green Apple"
    st.session_state.flavor_score += 5 # Special flavor bonus

if chosen_flavor:
    st.write(f"Yum! **{chosen_flavor}** is a great choice.")

# --- INTERACTION 2: The Secret Topping Slider ---
st.markdown("---")
st.subheader("2. Add Toppings 🍬")
st.write("Slide to add sprinkles! If you slide it too far, something funny might happen...")

sprinkle_amount = st.slider("Sprinkle Level", 0, 100, 20)

if sprinkle_amount > 95:
    st.warning("WOAH! Too many sprinkles! The machine is getting goofy!")
    st.markdown("# 🤩🍬🤩✨🤩🧁🤩")
elif sprinkle_amount == 0:
    st.write("Wait, zero sprinkles? You must like it simple.")
else:
    st.write(f"Adding {sprinkle_amount} tiny sprinkles!")

chosen_topping = st.selectbox("Pick a bonus topping:", ["None", "Rainbow Drops", "Cookie Dust", "Unicorn Magic"])

# --- THE INTERACTIVE EASTER EGG (The 'Hidden' Button) ---
if sprinkle_amount > 90 and st.session_state.flavor_score >= 5:
    st.markdown("---")
    st.subheader("🤫 Psssst... You unlocked the SECRET button!")
    st.write("This button only appears if you chose Alien Apple and maximized the sprinkles!")
    
    # Text input inside the Easter egg area
    secret_code = st.text_input("Enter the magic word (Hint: 'YUM'):", "").upper()
    
    if secret_code == "YUM":
        st.session_state.special_code_active = True
        st.info("The machine is humming a funny tune... 🎶")
        if st.button("ACTIVATE CHAOS CONE!"):
            st.snow() # Double snow
            st.toast("CHAOS MODE ENGAGED!", icon="🎉")
            st.write("The machine made a giant, floating, rainbow-pooping unicorn ice cream!")
            st.markdown("### 🦄🍦🌈💩")

# --- DELIVERY SYSTEM ---
st.markdown("---")
st.subheader("3. Let's Eat! 😋")

ready = st.checkbox("I am ready for my ice cream!")

if ready and chosen_flavor and chosen_topping:
    # We combine the selections
    final_flavor = chosen_flavor
    final_topping = f"with {sprinkle_amount} sprinkles and {chosen_topping}"
    
    # Use our function to 'send' the treats
    deliver_ice_cream(final_flavor, final_topping)

elif ready and (not chosen_flavor or chosen_topping == "None"):
    st.error("Wait! You didn't finish designing your ice cream! We need flavors and toppings!")

# --- A FINAL GIGGLE ---
st.sidebar.title("Machine Settings ⚙️")
if st.sidebar.checkbox("Show 'How it Works'"):
    st.sidebar.write("1. Magic happens.")
    st.sidebar.write("2. Streamlit is basically code magic.")
    st.sidebar.write("3. You eat virtual ice cream.")
    st.sidebar.write("4. We avoid brain freeze.")