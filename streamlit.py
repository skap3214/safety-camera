import streamlit as st
import time



st.title("Safety Camera")
with st.container():
    st.camera_input('Live Video Capture')
    col1, col2 = st.columns(2,gap = 'large')
    col1.button('Start Safety Cam')
    col2.button('Stop Safety Cam')