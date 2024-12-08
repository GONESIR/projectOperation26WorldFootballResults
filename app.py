import pandas as pd
import numpy as np
import altair as alt
import streamlit as st


stops_pdf = pd.read_csv("Officer_Traffic_Stops.csv")

stops_pdf


stops_df['Month_of_Stop'] = stops_df['Month_of_Stop'].astype('datetime64[ns]')

