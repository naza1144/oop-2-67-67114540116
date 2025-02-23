import streamlit as st

st.title("Interactive widgets")
clicked = st.button("Click me")
if clicked:
    name = st.text_input("Enter your name")
    if name:
        st.write(f"Hello {name}")
        st.image("https://picsum.photos/200/300")