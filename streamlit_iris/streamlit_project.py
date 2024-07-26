import streamlit as st
with open('style/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

about = st.Page(
    page = 'Pages/about.py',
    title = 'About',
    icon = ':material/account_circle:',
    default = True
)

model = st.Page(
    page = 'Pages/iris_predictor.py',
    title = 'Iris_predictor',
    icon = ':material/yard:'
)

pg = st.navigation(
    {
        'About' : [about],
        'Project' : [model]
    }
)

pg.run()