from pydantic import BaseModel
from models.iris_model import iris_predict
from structure.url import iris_test
from bson.objectid import ObjectId

class Item(BaseModel):
    name: str
    price: float
# objects =  ObjectId('6a89a71844954173a987e9a')
# data = iris.find_one({'_id' : objects})
id = ObjectId('66a9bc7824527cc6d489d65e')

data = iris_test.find_one({'_id' : id})

print(type(data['sepal_length_cm']))