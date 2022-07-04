import json
import streamlit as st
import pandas as pd
import base64
import streamlit.components.v1 as components
from PIL import Image
import pandas as pd

import io
from PIL import Image
from pprint import pprint
from zipfile import ZipFile
import os
from os.path import basename


def app_section_button(option1, option2, option3, option4):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        # current page
        col1.markdown(option1) 
    with col2:
        st.markdown(option2, unsafe_allow_html=True) 
    with col3:
        st.markdown(option3, unsafe_allow_html=True) 
    with col4:
        st.markdown(option4, unsafe_allow_html=True) 
      

def app_meta(icon):

    # Set website details
    st.set_page_config(page_title ="Data Quality Wrapper", 
                       page_icon=icon, 
                       layout='centered')
    
    # set sidebar width
    st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 300px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 300px;
        margin-left: -300px;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )

def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
    The bg will be static and won't take resolution of device into account.
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# set background, use base64 to read local file
def get_base64_of_bin_file(bin_file):
    """
    function to read png file 
    ----------
    bin_file: png -> the background image in local folder
    """
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    """
    function to display png as bg
    ----------
    png_file: png -> the background image in local folder
    """
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    st.App {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

# display app header and sidebar
# use HTML code to set div
def display_app_header(main_txt,sub_txt,is_sidebar = False):
    """
    function to display major headers at user interface
    ----------
    main_txt: str -> the major text to be displayed
    sub_txt: str -> the minor text to be displayed 
    is_sidebar: bool -> check if its side panel or major panel
    """

    html_temp = f"""
    <h2 style = "color:#F74369; text_align:center; font-weight: bold;"> {main_txt} </h2>
    <p style = "color:#BB1D3F; text_align:center;"> {sub_txt} </p>
    </div>
    """
    if is_sidebar:
        st.sidebar.markdown(html_temp, unsafe_allow_html = True)
    else: 
        st.markdown(html_temp, unsafe_allow_html = True)
        
def display_app_header_1(sub_txt,is_sidebar = False):
    """
    function to display major headers at user interface
    ----------
    main_txt: str -> the major text to be displayed
    sub_txt: str -> the minor text to be displayed 
    is_sidebar: bool -> check if its side panel or major panel
    """

    html_temp = f"""
    <p style = "color:#BB1D3F; text_align:center;"> {sub_txt} </p>
    </div>
    """
    if is_sidebar:
        st.sidebar.markdown(html_temp, unsafe_allow_html = True)
    else: 
        st.markdown(html_temp, unsafe_allow_html = True)

def _get_default_augmentations() -> dict:
    augmentations = {
        'resize': {
            'width': None,
            'height': None
        },
        'grayscale': False,
        'contrast': {'value':None},
        'brightness': {'value':None},
        'sharpness': {'value':None},
        'color': {'value':None},
        'denoise': False,
    }
    return augmentations

# def get_augmentations() -> dict:
#     if 'augmentations' not in st.session_state:
#         st.session_state.augmentations = _get_default_augmentations()
#     return st.session_state.augmentations

# def update_augmentations(augmentations) -> None:
#     st.session_state.augmentations = augmentations


def sub_text(text):
    '''
    A function to neatly display text in app.
    Parameters
    ----------
    text : Just plain text.
    Returns
    -------
    Text defined by html5 code below.
    '''
    
    html_temp = f"""
    <p style = "color:#1F4E79; text_align:justify;"> {text} </p>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html = True)
    
def open_html(file_name, height, width):

    """
    Open a local html file with streamlit components
    """

    pipe = open(file_name, 'r', encoding='utf-8')
    source_code = pipe.read() 
    components.html(source_code, height = height, width = width, scrolling=True)