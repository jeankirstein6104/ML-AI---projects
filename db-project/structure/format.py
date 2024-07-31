from pydantic import BaseModel

# class created to perform data validation and to reject invalid data
class Predict(BaseModel):
    sepal_length_cm: float
    sepal_width_cm: float
    petal_length_cm: float
    petal_width_cm: float