import streamlit as st
import sys

sys.path.append('D:\Ml_projects\streamlit_iris')
from ml_model import model


st.title('FLOWER PREDICTOR')

col1, col2 = st.columns(2, vertical_alignment = 'center')

with col1:
    sepal_len = st.number_input('Enter the sepal length (cm)', min_value = 0)
    print('\n')
    sepal_width = st.number_input('Enter the sepal width (cm)', min_value = 0)

with col2:
    petal_len = st.number_input('Enter the petal length (cm)', min_value = 0 )
    petal_width = st.number_input('Enter the petal width (cm)', min_value = 0)

input = [sepal_len, sepal_width, petal_len, petal_width]

result = model.iris_predict(input)

if st.button('PREDICT'):
    st.write('The flower is ', result)