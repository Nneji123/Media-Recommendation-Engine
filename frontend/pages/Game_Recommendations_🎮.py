import streamlit as st
import json
import requests as re

st.title("Games Recommendations Web App")


st.write("""
## About
This App using machine learning algorithms to suggest what Games you should play next!

The API was built with FastAPI and can be found [here.](https://credit-fraud-ml-api.herokuapp.com/)

The notebook, model and documentation(Dockerfiles, FastAPI script, Streamlit App script) are available on [GitHub.](https://github.com/Nneji123/Media-Recommendation-Engine)        

""")

input_query = st.text_input("Input the game you last played: ")
values = {"game": input_query}

res = re.post(
    f"http://backend.docker:8000/games", json=values)
json_str = json.dumps(res.json())
resp = json.loads(json_str)

st.write(f"""### These are the Games you should play next: {resp[0]}.""")
