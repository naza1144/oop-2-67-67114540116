import streamlit as st
import random as choice

# if 'count' not in st.session_state:
#     st.session_state.count = 0

# def countbutton():
#     st.session_state.count += 1
#     st.write(f"You clicked {st.session_state.count} times")

# st.title("Hello streamlit")
# st.button("Click me", on_click=countbutton)

n = 1000
data = {
    'name': [ choice.choice(['Anna', 'Bob', 'Charlie']) for i in range(n) ],
    'age': [ choice.choice([25, 30, 35]) for i in range(n) ],
    'city': [ choice.choice(['New York', 'Paris', 'London']) for i in range(n) ],
}
st.table(data)

#streamlit run  app01.py