import streamlit as st
from database import connect

def signup():

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Signup"):

        conn = connect()
        cur = conn.cursor()

        cur.execute(
        "INSERT INTO users VALUES (?,?)",
        (email,password)
        )

        conn.commit()

        st.success("Account created")


def login():

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        conn = connect()
        cur = conn.cursor()

        cur.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email,password)
        )

        user = cur.fetchone()

        if user:
            st.success("Login success")
        else:
            st.error("Invalid login")