import streamlit as st
import base64
#st.set_page_config(layout="wide")
st.title('Dynamic Visualization')


option_mapping = {'CIFAR10': 'cifar10', 
                  'ResNet 110, no skip connections': 'resnet110_noshort',
                  'SGD': 'SGD',
                  'f(x) = x': 'x',
                  'f(x) = x^2': 'x^2'}

col1, col2 = st.columns(2, gap="large")
with col1:
    st.header("Regular Optimizer")
    col11, col12 = st.columns(2)
    with col11:
        regular_dataset_selection = st.selectbox('Dataset', ('CIFAR10',), key=11)
    with col12:
        regular_network_architecture_selection = st.selectbox('Network Architecture', ('ResNet 110, no skip connections',), key=12)
    col13, col14 = st.columns(2)
    with col13:
        regular_optimizer_selection = st.selectbox('Optimizer', ('SGD',), key=13)
    with col14:
        regular_epochs_selection = st.selectbox('Number of Epochs', ('100',), key=14)
    col15, col16 = st.columns(2)
    with col15:
        regular_batch_size_selection = st.selectbox('Batch Size', ('128',), key=15)
    with col16:
        regular_learning_rate_selection = st.selectbox('Learning Rate', ('0.05',), key=16)
    col17, col18 = st.columns(2)
    with col17:
        regular_momentum_selection = st.selectbox('Momentum', ('0.9',), key=17)
    with col18:
        regular_weight_decay_selection = st.selectbox('Weight Decay', ('0',), key=18)
    FILE_NAME_1 = f"""./ImageMagick/GIF_{option_mapping[regular_dataset_selection]}_
                  {option_mapping[regular_network_architecture_selection]}_{
                      regular_optimizer_selection}_
                      epochs={regular_epochs_selection}_
                      BS={regular_batch_size_selection}_
                      LR={regular_learning_rate_selection}_
                      MOM={regular_momentum_selection}_
                      WD={regular_weight_decay_selection}.gif""".replace('\n', '').replace(' ', '')
                      
    file_1 = open(FILE_NAME_1, 'rb')
    contents1 = file_1.read()
    data_url_1 = base64.b64encode(contents1).decode('utf-8')
    file_1.close()
    st.markdown(f'<img src = "data:image/gif;base64,{data_url_1}" width="500" height="500" alt="normal">',
                unsafe_allow_html=True)
    
with col2:
    st.header("Landscape Modification")
    col21, col22 = st.columns(2)
    with col21:
        lm_dataset_selection = st.selectbox('Dataset', ('CIFAR10',), key=21)
    with col22:
        lm_network_architecture_selection = st.selectbox('Network Architecture', 
                                                         ('ResNet 110, no skip connections',),
                                                         key=22)
    col23, col24, col25 = st.columns(3)
    with col23:
        lm_optimizer_selection = st.selectbox('Optimizer', ('SGD_IKSA',), key=23)
    with col24:
        lm_epochs_selection = st.selectbox('Number of Epochs', ('100',), key=24)
    with col25:
        lm_batch_size_selection = st.selectbox('Batch Size', ('128',), key=25)
    col26, col27, col28 = st.columns(3)
    with col26:
        lm_seed_selection = st.selectbox('Seed for Data Loading', ('1234', ), key=26)
    with col27:
        lm_learning_rate_selection = st.selectbox('Learning Rate', ('0.05',), key=27)
    with col28:
        lm_momentum_selection = st.selectbox('Momentum', ('0.9',), key=28)
    col29, col210, col211 = st.columns(3)
    with col29:
        lm_weight_decay_selection = st.selectbox('Weight Decay', ('0',), key=29)
    with col210:
        lm_C_selection = st.selectbox('C for LM', ('2','1', 'adaptive'), key=210)
    with col211:
        lm_f_selection = st.selectbox('f', ('f(x) = x', 'f(x) = x^2'), key=211)
    
    FILE_NAME_2 = f"""./ImageMagick/GIF_{option_mapping[lm_dataset_selection]}_
                  {option_mapping[lm_network_architecture_selection]}_{
                      lm_optimizer_selection}_
                      epochs={lm_epochs_selection}_
                      BS={lm_batch_size_selection}_
                      SEED={lm_seed_selection}_
                      LR={lm_learning_rate_selection}_
                      MOM={lm_momentum_selection}_
                      WD={lm_weight_decay_selection}_
                      C={lm_C_selection}_
                      f={option_mapping[lm_f_selection]}.gif""".replace('\n', '').replace(' ', '')
    file_2 = open(FILE_NAME_2, 'rb')
    #file_2 = open('./ImageMagick/GIF_cifar10_resnet110_noshort_SGD_IKSA_epochs=100_BS=128_SEED=1234_LR=0.05_MOM=0.9_WD=0_C=2_f=x.gif', 'rb')
    contents2 = file_2.read()
    data_url_2 = base64.b64encode(contents2).decode('utf-8')
    file_2.close()

    st.markdown(f'<img src = "data:image/gif;base64,{data_url_2}" width="500" height="500" alt="LM">',
                unsafe_allow_html=True)