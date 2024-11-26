import streamlit as st

st.title('menghitung :blue[volume tabung] :rocket:')

r = st.number_input("Masukkan jari-jari (cm): ",0)
t = st.number_input("masukkan tinggi (cm): ",0)

if st.button("Hitung volume", type="primary"):
  v = math.pi*(r**2)*t
  st.succes(f'volume tabung adalah (v:.2f)')
