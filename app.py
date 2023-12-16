import streamlit as st
import numpy as np
import scipy as sc 
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')
st.title("Modelo SIR")

beta = 0.00003
gamma = 5

S = 1000000
I = 1
R = 0

SS = []
II = []
RR = []

h = 0.001

T = 1400

for _ in range(T):
  SS.append(S)
  II.append(I)
  RR.append(R)


  S -= h * (beta * S * I)
  if S < 0:
    S = 0
  I += h * (beta * S * I - gamma * I)
  R += h * (gamma * I)

col1, col2 = st.columns([5, 2])

with col1:
    fig, ax = plt.subplots(1, 1)
    ax.plot(SS, label='s')
    ax.plot(II, label='s')
    ax.plot(RR, label='s')
    ax.legend()

    st.pyplot(fig)

with col2:

    beta = st.number_input("Seleccione tasa de contagio", 0, 1)
    gamma = st.number_input("Seleccione tasa de recuperación", 0, 10) 

