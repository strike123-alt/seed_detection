import streamlit as st
import numpy as np
import pickle
model = ''
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
ch = list()

st.markdown("<h1 style='text-align: center;'>Seed Detection</h1>",
            unsafe_allow_html=True)
nav = st.sidebar.radio("Navigation", ['Input Section'])
#  A       210 non-null    float64
#  1   P       210 non-null    float64
#  2   C       210 non-null    float64
#  3   LK      210 non-null    float64
#  4   WK      210 non-null    float64
#  5   A_Coef  210 non-null    float64
#  6   LKG
if nav == 'Input Section':

    st.subheader("Please Enter the given values")
    col1, col2 = st.columns(2)
    bal = col1.number_input(
        "A", format="%.4f")

    bal_freq = col2.number_input(
        "P", format="%.4f")

    purchases = col1.number_input(
        "C",  format="%.4f")

    one_off_pur = col2.number_input(
        "LK",  format="%.4f")

    install_pur = col1.number_input(
        "WK", format="%.4f")

    cash_advance = col2.number_input(
        "A_Coef",  format="%.4f")

    pur_freq = col1.number_input(
        "LKG", format="%.4f")

    if st.button('submit'):
        ch.append(bal)
        ch.append(bal_freq)
        ch.append(purchases)
        ch.append(one_off_pur)
        ch.append(install_pur)
        ch.append(cash_advance)
        ch.append(pur_freq)

        y_pred = model.predict(np.array(ch).reshape(1, -1))
        st.info(f'Input:  {ch}')
        st.success(f'Result: {y_pred}')
