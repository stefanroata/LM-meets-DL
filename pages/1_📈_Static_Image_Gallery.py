import streamlit as st
import base64

st.title('Static Image Gallery')
error_msg = 'Temporarily Unavailable'
option_mapping = {'CIFAR10': 'cifar10', 
                  'ResNet 110, no skip connections': 'resnet110_noshort',
                  'ResNet56 no skip connections': 'resnet56_noshort',
                  'SGD': 'SGD'}

gallery_selection = st.selectbox('Select gallery of images', ('VGG16, SGD, LR = 0.001',
                                                              'VGG16, Adam, LR = 0.001',
                                                              'VGG16, Adam, LR = 0.005',
                                                              'ResNet56 no skip connections, SGD, LR = 0.1',
                                                              'ResNet110 no skip connections, SGD, LR = 0.05'))

if 'VGG16' in gallery_selection:
    if 'SGD' in gallery_selection:
        if '0.001' in gallery_selection:
            model_name1 = 'StaticGallery/vgg_sgd/loss_surface_cifar10_vgg16_SGD_epochs=100_BS=128_SEED=1234_LR=0.001_MOM=0.9_WD=0_axes=ON_log=ON.png'
            model_name2 = 'StaticGallery/vgg_sgd/loss_surface_cifar10_vgg16_SGD_IKSA_epochs=100_BS=128_SEED=1234_LR=0.001_MOM=0.9_WD=0_'
    elif 'Adam' in gallery_selection:
        if '0.001' in gallery_selection:
            model_name1 = 'StaticGallery/vgg_adam/LR=0.001/loss_surface_cifar10_vgg16_Adam_epochs=100_BS=128_LR=0.001_BETA1=0.9_BETA2=0.999_WD=0_axes=ON_log=ON.png'
            model_name2 = 'StaticGallery/vgg_adam/LR=0.001/loss_surface_cifar10_vgg16_Adam_IKSA_epochs=100_BS=128_SEED=1234_LR=0.001_BETA1=0.9_BETA2=0.999_WD=0_'
        elif '0.005' in gallery_selection:
            model_name1 = 'StaticGallery/vgg_adam/LR=0.005/loss_surface_cifar10_vgg16_Adam_epochs=100_BS=128_LR=0.005_BETA1=0.9_BETA2=0.999_WD=0_axes=ON_log=ON.png'
            model_name2 = 'StaticGallery/vgg_adam/LR=0.005/loss_surface_cifar10_vgg16_Adam_IKSA_epochs=100_BS=128_SEED=1234_LR=0.005_BETA1=0.9_BETA2=0.999_WD=0_'
elif 'ResNet56' in gallery_selection:
    model_name1 = 'StaticGallery/resnet56_noshort/loss_surface_cifar10_resnet56_noshort_SGD_epochs=100_BS=128_LR=0.1_MOM=0.9_WD=0.0005_axes=ON_log=ON.png'
    model_name2 = 'StaticGallery/resnet56_noshort/loss_surface_cifar10_resnet56_noshort_SGD_IKSA_epochs=100_BS=128_SEED=1234_LR=0.1_MOM=0.9_WD=0.0005_'
elif 'ResNet110' in gallery_selection:        
    model_name1 = 'StaticGallery/resnet110_noshort/loss_surface_cifar10_resnet110_noshort_SGD_epochs=100_BS=128_LR=0.05_MOM=0.9_WD=0_axes=ON_log=ON.png'
    model_name2 = 'StaticGallery/resnet110_noshort/loss_surface_cifar10_resnet110_noshort_SGD_IKSA_epochs=100_BS=128_SEED=1234_LR=0.05_MOM=0.9_WD=0_'

def display_caption(caption):
    partial = caption.find('loss_surface')
    subset = caption[partial + 13:]
    return ", ".join(subset.split('_'))[:-4]

st.markdown(f'<h2 style="text-align: center;">{gallery_selection}</h2>', unsafe_allow_html=True)

def display_gallery():
    col11, col12, col13 = st.columns(3, gap='large')
    with col12:
        try:
            st.image(model_name1, 
                     caption=display_caption(model_name1), 
                     output_format='PNG', 
                     use_column_width='always')
        except Exception as e:
            st.write(error_msg)
        
    # row for f(x) = x, C = 2, 1, adaptive
    col21, col22, col23 = st.columns(3, gap='large')
    with col21:
        image_name = model_name2 + 'C=2_f=x_axes=ON_log=ON.png'
        try:
            st.image(image_name, 
                     caption=display_caption(image_name),
                     output_format='PNG',
                     use_column_width='always')
        except Exception as e:
            st.write(error_msg)
        
    with col22:
        image_name = model_name2 + 'C=1_f=x_axes=ON_log=ON.png'
        try:
            st.image(image_name, 
                     caption=display_caption(image_name),
                     output_format='PNG',
                     use_column_width='always')
        except Exception as e:
            st.write(error_msg)
        
    with col23:
        image_name = model_name2 + 'C=adaptive_f=x_axes=ON_log=ON.png'
        try:
            st.image(image_name, 
                     caption=display_caption(image_name),
                     output_format='PNG',
                     use_column_width='always')
        except Exception as e:
            st.write(error_msg)
        
    # row for f(x) = x^2, C = 2, 1, adaptive
    col31, col32, col33 = st.columns(3, gap='large')
    with col31:
            image_name = model_name2 + 'C=2_f=x^2_axes=ON_log=ON.png'
            try:
                st.image(image_name, 
                         caption=display_caption(image_name),
                         output_format='PNG',
                         use_column_width='always')
            except Exception as e:
                st.write(error_msg)
        
    with col32:
        image_name = model_name2 + 'C=1_f=x^2_axes=ON_log=ON.png'
        try:
            st.image(image_name, 
                     caption=display_caption(image_name),
                     output_format='PNG',
                     use_column_width='always')
        except Exception as e:
            st.write(error_msg)
        
    with col33:
        image_name = model_name2 + 'C=adaptive_f=x^2_axes=ON_log=ON.png'
        try:
            st.image(image_name, 
                     caption=display_caption(image_name),
                     output_format='PNG',
                     use_column_width='always')
        except Exception as e:
            st.write(error_msg)
        
    # row for f(x) = arctan(x^2), C = 2, 1, adaptive
    col41, col42, col43 = st.columns(3, gap='large')
    with col41:
        image_name = model_name2 + 'C=2_f=arctan(x^2)_axes=ON_log=ON.png'
        try:
            st.image(image_name, 
                     caption=display_caption(image_name),
                     output_format='PNG',
                     use_column_width='always')
        except Exception as e:
            st.write(error_msg)
        
    with col42:
        image_name = model_name2 + 'C=1_f=arctan(x^2)_axes=ON_log=ON.png'
        try:
            st.image(image_name, 
                     caption=display_caption(image_name),
                     output_format='PNG',
                     use_column_width='always')
        except Exception as e:
            st.write(error_msg)
        
    with col43:
        image_name = model_name2 + 'C=adaptive_f=arctan(x^2)_axes=ON_log=ON.png'
        try:
            st.image(image_name, 
                     caption=display_caption(image_name),
                     output_format='PNG',
                     use_column_width='always')
        except Exception as e:
            st.write(error_msg)

display_gallery()
            