import streamlit as st
import random as choice
if 'counter' not in st.session_state:
    st.session_state.counter = 0

clear = st.button("Clear")
add = st.button("Add")
addx2 = st.button("Add x2")
minus = st.button("Minus")

if add:
    st.session_state.counter += 1
if addx2:
        st.session_state.counter += 2
if minus:
    st.session_state.counter -= 1
if clear:
    st.session_state.counter = 0

st.title("Session State")
st.header(f'counter: {st.session_state.counter}')


n = st.session_state.counter
data = {
    'name': [ choice.choice(['Anna', 'Bob', 'Charlie']) for i in range(n) ],
    'age': [ choice.choice([25, 30, 35]) for i in range(n) ],
    'city': [ choice.choice(['New York', 'Paris', 'London']) for i in range(n) ],
}
st.table(data)