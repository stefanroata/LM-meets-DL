import streamlit as st

st.set_page_config(
    page_title="Introduction",
    page_icon="👋",
    layout='wide'
)

st.title("Landscape Modification Meets Deep Learning")

st.markdown("""In the context of machine learning, optimization is the process of gradually 
         adjusting the parameters of a loss function with the aim to minimize it. 
         Landscape modification is a new optimization acceleration technique introduced 
         by Choi that proposes modifying the loss landscape of a given cost function through 
         a state-dependent transformation. 
         In this thesis, we will explore its theoretical and empirical effect on the loss landscape 
         of common deep learning architectures (MobileNetV2, VGG16, ResNet110), using a novel, 
         dimensionality-reducing visualization technique introduced by Li et al.""".replace('\n', ''))