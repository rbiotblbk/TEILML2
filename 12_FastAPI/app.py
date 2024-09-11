# pip install "fastapi[standard]"
# pip install "uvicorn[standard]"


# Automated Software Documentation
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

import uvicorn
from fastapi import FastAPI

import pickle

import os
from pathlib import Path
os.chdir(Path(__file__).parent)


# Create an APP
app = FastAPI()


@app.get("/")
def root() -> dict:
    """Home Page greeting Mohamed

    Returns:
        dict: return of hello Mohamed
    """
    return {"hello": "Mohamed"}


@app.get("/wbs")
def wbs_greeting() -> dict:
    """Greeting WBS

    Returns:
        dict: return of hello WBS
    """
    return {"hello": "WBS"}


# http://127.0.0.1:8000/getproduct/1
# http://127.0.0.1:8000/getproduct/2
# http://127.0.0.1:8000/getproduct/5
# http://127.0.0.1:8000/getproduct/apfel  ---> ERROR
@app.get("/getproduct/{product_id}")
def show_info(product_id: int) -> dict:
    """Get Product Title based on ID otherwise Not found

    Args:
        product_id (int): Product ID 

    Returns:
        dict: Product Title
    """
    if product_id == 1:
        return {"product_title": "Milch"}
    elif product_id == 2:
        return {"product_title": "Brot"}
    else:
        return {"product_title": "Not found"}

# http://127.0.0.1:8000/getuserinfo?id=1&name=thomas
# http://127.0.0.1:8000/getuserinfo?id=apfel&name=sven  ---> ERROR
# http://127.0.0.1:8000/getuserinfo?id=1&name=2  --> OK, because 2 can be converted to "2"


@app.get("/getuserinfo")
def get_user_info(id: int, name: str) -> dict:
    """Gets user Infromation based on ID and Name

    Args:
        id (int): Employee ID
        name (str): Employee First Name

    Returns:
        dict: Eimployee Card
    """

    return {
        "id": 1,
        "first_name": name
    }


@app.get("/predict/{area}")
def predict(area: int):

    # Get the model
    model = load_model()

    # Use for prediction
    predicted_value = int(model.predict([[area]]))

    return {"price": predicted_value}


def load_model():
    with open("./model_linear_reg_v1.pkl", mode="rb") as file:
        model = pickle.load(file)

    return model


if __name__ == "__main__":
    uvicorn.run(app)
