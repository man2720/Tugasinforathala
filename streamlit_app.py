import streamlit as st

st.title("--Welcome--")
st.write("Tugas website informatika Muhammad Athala Putra Margana.")
st.image("IMG-20250505-WA0000.jpg",width=500)

st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah bilangan Ganjil")
