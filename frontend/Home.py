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
    app_meta('🖼️')
    set_bg_hack('./images/background.png')

    # hide warning for st.pyplot() deprecation
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Main panel setup
    display_app_header(main_txt='Media Recommendation App',
                       sub_txt='Get suggestions on what to read, watch or listen to next using this recommendations web app!')

    st.markdown("""---""")

    st.write('Welcome to the MRA! An app for getting media recommendations!')

    st.write('Please select the recommendation app you would like to use from the sidebar!',
             'Due to the multifunctionality of this app, we have split it into 7 different apps.',
             'This is the main app. Have fun!')

    # provide options to user to navigate to other dqw apps
    app_section_button('[Movie Recommendations 🖼️](https://share.streamlit.io/soft-nougat/dqw-ivves_images/main/app.py)',
                       '[Music Recommendations 🎶](https://share.streamlit.io/soft-nougat/dqw-ivves_structured/main/app.py)',
                       '[Game Recommendations 🎮](https://share.streamlit.io/soft-nougat/dqw-ivves_audio/main/app.py)',
                       '[Anime Recommendations 📚](https://share.streamlit.io/soft-nougat/dqw-ivves_text/main/app.py)',
                       '[Comics Recommendations 📚](https://share.streamlit.io/soft-nougat/dqw-ivves_audio/main/app.py)',
                       '[Manga Recommendations 📚](https://share.streamlit.io/soft-nougat/dqw-ivves_audio/main/app.py)',
                       '[Book Recommendations 📚](https://share.streamlit.io/soft-nougat/dqw-ivves_audio/main/app.py)')
    st.markdown("""---""")

    intro_text = """


    """
    intro = st.expander(
        "Click here for more info on Media Recommendation Engine ✨")

    with intro:
        sub_text(intro_text)


except KeyError:
    st.error("Please select a key value from the dropdown to continue.")

# except ValueError:
#     st.error(
#         "Oops, something went wrong. Please check previous steps for inconsistent input.")

except TypeError:
    st.error(
        "Thanks for using this App.")
