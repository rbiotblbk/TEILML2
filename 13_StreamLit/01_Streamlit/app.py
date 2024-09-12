# pip install streamlit
# > streamlit run app.py

import os
import pickle
import streamlit as st
from pathlib import Path
os.chdir(Path(__file__).parent)


# Load Model Phase
def load_model():
    with open("./models/model_linear_reg_v1.pkl", mode="rb") as file:
        model = pickle.load(file)

    return model


def main():
    model = load_model()

    # Write a title
    st.write("Welcome by Area Prediction Application")

    # Write a Text Paraghraph
    st.write("""
            ### Project description
             We have trained several models to predict the price of a house area
            """)

    # Add input field
    area = int(st.text_input("Area", 50))  # 50 is the default value

    # Add a button
    if st.button("Predict"):
        predicted_price = round(float(model.predict([[area]])), 2)

        st.success(f"The price of the provided area is: {predicted_price} €")


if __name__ == "__main__":
    main()
