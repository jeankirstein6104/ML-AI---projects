import streamlit as st

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
