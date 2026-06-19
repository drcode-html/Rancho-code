import streamlit as st 

st.title("My fun app")

name = st.text_input("Entern your name")
mood = st.selectbox("How do you feel?" , ["Happpy" , "Tired" , "Excited" , "Hungry"])

if "visits" not in st.session_state:
 st.session_state.visits += 1
 st.write(f"")
