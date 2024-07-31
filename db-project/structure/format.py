from pydantic import BaseModel

class Item(BaseModel):
    name: str

class Predict(BaseModel):
    sepal_length_cm: float
    sepal_width_cm: float
    petal_length_cm: float
    petal_width_cm: float