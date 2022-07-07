import streamlit as st
import json
import requests as re

st.title("Book Recommendations Web App")


st.write("""
## About
This App using machine learning algorithms to suggest what book you should read next!
        

""")

input_query = st.text_input("Input the Book you last read: ")
values = {"book": input_query}

res = re.post(
    f"http://backend.docker:8000/books", json=values)
json_str = json.dumps(res.json())
resp = json.loads(json_str)

st.write(f"""### These are the book you should read next: {resp[0]}.""")
