import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

#Setting up layout
st.set_page_config(layout="wide")

#Setting up data
@st.cache_data
def load_data(url):
    df = pd.read_csv(url, encoding='ISO-8859-1')
    return df

# read in data
df = load_data("https://raw.githubusercontent.com/GONESIR/projectOperation26WorldFootballResults/main/Data/FIFA%20Results.csv")

# read in dataset 2
df = load_data("https://raw.githubusercontent.com/GONESIR/projectOperation26WorldFootballResults/main/Data/decision.csv")

# read in dataset 3
df = load_data("https://raw.githubusercontent.com/GONESIR/projectOperation26WorldFootballResults/main/Data/penalty kick.csv")

st.title("The Outcomes Of Every International Football Game")

video_path = "Videos/The Official FIFA World Cup 26™ Theme [HmpzUm5j4OE].mp4"

with open(video_path, "rb")as video_file:
    video_bytes = video_file.read()


# st.video(video_bytes)

# st.button("Rerun")


# # Embed YouTube video URL with controls hidden
# youtube_video_url = "https://www.youtube.com/watch?v=HmpzUm5j4OE"

# Embed the video using an iframe
# st.markdown(f'<iframe width="100%" height="400" src="{video_bytes}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)


# CSS to hide the video controls
st.markdown("""
    <style>
        .streamlit-expanderHeader {
            display: none !important;
        }
        .stVideo video::-webkit-media-controls {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# Embed your video (URL example)
st.video("https://www.youtube.com/watch?v=HmpzUm5j4OE")


