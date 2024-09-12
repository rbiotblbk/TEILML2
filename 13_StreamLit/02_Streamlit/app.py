# pip install streamlit
# > streamlit run app.py
#  https://www.webfx.com/tools/emoji-cheat-sheet/
import os
import streamlit as st
from pathlib import Path
import pandas as pd

os.chdir(Path(__file__).parent)


def get_dataframe():
    df = pd.read_csv("./multivariat.csv")
    return df


# Get the whole Datasource
df = get_dataframe()

############################################
# Sidebar
############################################
st.sidebar.header("Filter the data")
area = st.sidebar.multiselect(
    "Select the area:", options=df["Area"].unique(), default=df["Area"].unique())
room_count = st.sidebar.multiselect(
    "Select the room count:", options=df["RoomCount"].unique(), default=df["RoomCount"].unique())

df_selected = df.query("Area == @area & RoomCount == @room_count")


############################################
# Web Page
############################################
st.title("📈 Area Price Dashboard")
st.markdown("## Information")

# Aggregation value
total_area = int(df_selected["Area"].sum())
average_price = round(df_selected["Mietpreis"].mean(), 2)
message = "This is important"


# Split the area to 3x columns
left_col, middle_col, right_col = st.columns(3)

with left_col:
    st.subheader("Total Area:")
    st.subheader(total_area)

with middle_col:
    st.subheader("AVG Price:")
    st.subheader(average_price)

with right_col:
    st.subheader("MSG:")
    st.subheader(message)


st.markdown("---")

############################################
# Show the Data Frame
############################################
st.markdown("## Data Frame")
st.dataframe(df_selected)
