import streamlit as st
import base64
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
st.title('Interactive 3-D Visualization')


option_mapping = {'CIFAR10': 'cifar10', 
                  'ResNet 110, no skip connections': 'resnet110_noshort',
                  'ResNet56, no skip connections': 'resnet56_noshort',
                  'VGG16': 'vgg16',
                  'SGD': 'SGD',
                  'f(x) = x': 'x',
                  'f(x) = x^2': 'x^2',
                  'f(x) = arctan(x^2)': 'arctan(x^2)'}

col1, col2 = st.columns(2, gap="large")
with col1:
    st.header("Regular Optimizer")
    col11, col12 = st.columns(2)
    with col11:
        regular_dataset_selection = st.selectbox('Dataset', ('CIFAR10',), key=111)
    with col12:
        regular_network_architecture_selection = st.selectbox('Network Architecture', ('ResNet 110, no skip connections', 'ResNet56, no skip connections', 'VGG16'), key=121)
    col13, col14 = st.columns(2)
    with col13:
        regular_optimizer_selection = st.selectbox('Optimizer', ('SGD',), key=131)
    with col14:
        regular_epochs_selection = st.selectbox('Number of Epochs', ('100',), key=141)
    col15, col16 = st.columns(2)
    with col15:
        regular_batch_size_selection = st.selectbox('Batch Size', ('128',), key=151)
    with col16:
        regular_learning_rate_selection = st.selectbox('Learning Rate', ('0.05', '0.1', '0.001'), key=161)
    col17, col18 = st.columns(2)
    with col17:
        regular_momentum_selection = st.selectbox('Momentum', ('0.9',), key=171)
    with col18:
        regular_weight_decay_selection = st.selectbox('Weight Decay', ('0','0.0005'), key=181)
    FILE_NAME_1 = f"""{option_mapping[regular_dataset_selection]}_
                  {option_mapping[regular_network_architecture_selection]}_{
                      regular_optimizer_selection}_
                      epochs={regular_epochs_selection}_
                      BS={regular_batch_size_selection}_
                      LR={regular_learning_rate_selection}_
                      MOM={regular_momentum_selection}_
                      WD={regular_weight_decay_selection}.npy""".replace('\n', '').replace(' ', '')
    X_FILE = './ImageMagick/XX_' + FILE_NAME_1
    Y_FILE = './ImageMagick/YY_' + FILE_NAME_1
    Z_FILE = './ImageMagick/ZZ_' + FILE_NAME_1
    
    try:
        XX = np.load(X_FILE)
        YY = np.load(Y_FILE)
        ZZ = np.load(Z_FILE)
        fig = go.Figure(data=[go.Surface(x=XX, y=YY, z=ZZ)])
        # fig.show()
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.warning("GIF not available/not generated yet. Please choose a different parameter configuration.", icon='🚨')
    
with col2:
    st.header("Landscape Modification")
    col21, col22 = st.columns(2)
    with col21:
        lm_dataset_selection = st.selectbox('Dataset', ('CIFAR10',), key=211)
    with col22:
        lm_network_architecture_selection = st.selectbox('Network Architecture', 
                                                         ('ResNet 110, no skip connections','ResNet56, no skip connections', 'VGG16'),
                                                         key=221)
    col23, col24, col25 = st.columns(3)
    with col23:
        lm_optimizer_selection = st.selectbox('Optimizer', ('SGD_IKSA',), key=231)
    with col24:
        lm_epochs_selection = st.selectbox('Number of Epochs', ('100',), key=241)
    with col25:
        lm_batch_size_selection = st.selectbox('Batch Size', ('128',), key=251)
    col26, col27, col28 = st.columns(3)
    with col26:
        lm_seed_selection = st.selectbox('Seed for Data Loading', ('1234', ), key=261)
    with col27:
        lm_learning_rate_selection = st.selectbox('Learning Rate', ('0.05','0.1', '0.001'), key=271)
    with col28:
        lm_momentum_selection = st.selectbox('Momentum', ('0.9',), key=281)
    col29, col210, col211 = st.columns(3)
    with col29:
        lm_weight_decay_selection = st.selectbox('Weight Decay', ('0','0.0005'), key=291)
    with col210:
        lm_C_selection = st.selectbox('C for LM', ('2','1', 'adaptive'), key=2101)
    with col211:
        lm_f_selection = st.selectbox('f', ('f(x) = x', 'f(x) = x^2', 'f(x) = arctan(x^2)'), key=2111)
    
    FILE_NAME_2 = f"""{option_mapping[lm_dataset_selection]}_
                  {option_mapping[lm_network_architecture_selection]}_{
                      lm_optimizer_selection}_
                      epochs={lm_epochs_selection}_
                      BS={lm_batch_size_selection}_
                      SEED={lm_seed_selection}_
                      LR={lm_learning_rate_selection}_
                      MOM={lm_momentum_selection}_
                      WD={lm_weight_decay_selection}_
                      C={lm_C_selection}_
                      f={option_mapping[lm_f_selection]}.npy""".replace('\n', '').replace(' ', '')
    X_FILE = './ImageMagick/XX_' + FILE_NAME_2
    Y_FILE = './ImageMagick/YY_' + FILE_NAME_2
    Z_FILE = './ImageMagick/ZZ_' + FILE_NAME_2
    try:
        XX = np.load(X_FILE)
        YY = np.load(Y_FILE)
        ZZ = np.load(Z_FILE)
        fig = go.Figure(data=[go.Surface(x=XX, y=YY, z=ZZ)])
        # fig.show()
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.warning("GIF not available/not generated yet. Please choose a different parameter configuration.", icon='🚨')