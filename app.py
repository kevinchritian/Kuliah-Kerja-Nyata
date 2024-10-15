import streamlit as st

# st.title("Hello world")

home = st.Page(
    page = "views/home.py",
    title='Home',
    icon= "😎",
    default= True
)

about = st.Page(
    page = "views/about.py",
    title='About',
    icon= "😎",
)

sampah = st.Page(
    page = "views/sampah.py",
    title='Sampah',
    icon= "😎",
)



pg = st.navigation(
    pages= [home, about, sampah]
)

# {
#     "info" : [home],
#     "projects" :[about],
#     }



pg.run()


hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden; }
    </style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)