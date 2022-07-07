import streamlit as st
import json
import requests as re

st.title("Anime Recommendations Web App")


st.write("""
## About
This App using machine learning algorithms to suggest what anime you should watch next!

The API was built with FastAPI and can be found [here.](https://credit-fraud-ml-api.herokuapp.com/)

The notebook, model and documentation(Dockerfiles, FastAPI script, Streamlit App script) are available on [GitHub.](https://github.com/Nneji123/Media-Recommendation-Engine)        

""")

input_query = st.text_input("Input the Anime you last watched: ")
values = {"anime": input_query}

res = re.post(
    f"http://backend.docker:8000/anime", json=values)
json_str = json.dumps(res.json())
resp = json.loads(json_str)

st.write(f"""### These are the anime you should watch next: {resp[0]}.""")
