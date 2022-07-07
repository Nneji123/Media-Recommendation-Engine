# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:04:46 2020

Script with defined app, including styling.

@author: Ifeanyi Nneji
"""

import streamlit as st
from PIL import Image

# app setup
try:

    from streamlit_functions.helper_functions import *

    # app design
    app_meta('📊')
    set_bg_hack('./images/background.png')

    # hide warning for st.pyplot() deprecation
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Main panel setup
    display_app_header(main_txt='Media Recommendation App',
                       sub_txt='Clean, describe, visualise and select data for AI models')

    st.markdown("""---""")

    st.write('Welcome to the MRA! An app for getting media recommendations!')

    st.write('Please select the data format/app section you want to use below. ',
             'Due to the multifunctionality of this app, we have split it into five.',
             'This is the main app. Have fun!')

    # provide options to user to navigate to other dqw apps
    app_section_button('[Movie Recommendations 🖼️](https://share.streamlit.io/soft-nougat/dqw-ivves_images/main/app.py)',
                       '[Music Recommendations 🎶](https://share.streamlit.io/soft-nougat/dqw-ivves_structured/main/app.py)',
                       '[Game Recommendations 🎮](https://share.streamlit.io/soft-nougat/dqw-ivves_audio/main/app.py)',
                       '[Anime Recommendations 📚](https://share.streamlit.io/soft-nougat/dqw-ivves_text/main/app.py)',
                       '[Comics Recommendations 🎶](https://share.streamlit.io/soft-nougat/dqw-ivves_audio/main/app.py)',
                       '[Manga Recommendations 🎶](https://share.streamlit.io/soft-nougat/dqw-ivves_audio/main/app.py)',
                       '[Book Recommendations 🎶](https://share.streamlit.io/soft-nougat/dqw-ivves_audio/main/app.py)')
    st.markdown("""---""")

    intro_text = """


    """
    intro = st.expander(
        "Click here for more info on Media Recommendation Engine ✨")

    with intro:
        sub_text(intro_text)


except KeyError:
    st.error("Please select a key value from the dropdown to continue.")

except ValueError:
    st.error(
        "Oops, something went wrong. Please check previous steps for inconsistent input.")

except TypeError:
    st.error(
        "Oops, something went wrong. Please check previous steps for inconsistent input.")
