import streamlit as st

st.set_page_config(
     page_title="BCN RS Study",
     page_icon=":house:",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.filmaffinity.com/es/film160882.html',
         'About': "*Ezequiel 25:17*. The path of the righteous man is beset on all sides by the inequities of the selfish and the tyranny of evil men. Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness. For he is truly his brother's keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy my brothers. And you will know I am the Lord when I lay my vengeance upon you."
     }
 )

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Methodologies", "Other Page"])

if page == "Home":
    st.title("Barcelona Real Estate Study")
    st.header("IronHack Final Project")
    st.write(
        "This project is designed to empower users with a comprehensive understanding of the dynamic Real Estate market in Barcelona, Spain. Divided into three distinct components, it offers an insightful exploration of the city's property landscape.")
    project_info = {
        "Title": "Real Estate Study",
        "Location": "Barcelona, Spain",
        "This project is powered by a combination of tools and technologies. Here are some of the key tools used": 
        "Python-Jupyter Notebooks-Git and GitHub-Tableau-h2o-Streamlit.",
        "Last update": "07/12/2023",
        "Acknowledgments": "IronHack Team(Fernando Costa, Santiago Aguilar and Begoña Ripoll)"
    }
    Project_Overview = """
    This multifaceted project delves into the intricate dynamics of the real estate market in Barcelona, Spain. 
    Offering users a comprehensive understanding through distinct components: different Tableau visualizations and a predictive modeling framework.
    """
    col1, col2 = st.columns(2)
    col1.subheader("**General Information**")
    for key, value in project_info.items():
        col1.write(f"**{key}:** {value}")
    col2.subheader("*Project Overview*")
    col2.write(Project_Overview)
elif page == "Methodologies":
    import pages.methodologies
else:
    import pages.other_page
