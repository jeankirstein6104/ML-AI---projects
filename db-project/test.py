from fastapi import FastAPI
from structure.schema import get_list
from structure.url import iris
from structure.format import Item, Predict
from models.iris_model import iris_predict
from bson.objectid import ObjectId



app = FastAPI()

# to get all the available flower data in the database
@app.get('/get_all')
async def get_all():
    data = [flower for flower in iris.find()]
    return get_list(data)

# to insert a flower parameters in the database 
@app.post('/insert')
async def add_flower(flowers :Item):
    iris.insert_one(dict(flowers))
    return {'message' : 'flower inserted'}

# to predict the given flower from the features
@app.post('/predict')
async def predict_flower(params: Predict):
    data = [float(params.sepal_length_cm), float(params.sepal_width_cm), float(params.petal_length_cm), float(params.petal_width_cm)]
    return iris_predict(list(data))

# to retrieve the features with an  id
@app.put('/return/{obj_id}')
async def id_get(obj_id:str):
    data = [iris.find_one({'_id':ObjectId(obj_id)})]
    return get_list(data)

# to update a flower with an id
@app.put('/update/{obj_id}')
async def id_update(obj_id:str, updated_item:Item):
    iris.update_one({'_id' : ObjectId(obj_id)},{'$set' : dict(updated_item)})
    return {'message' : 'flower updated'}

# to delete a flower with an id
@app.put('/delete/{obj_id}')
async def id_delete(obj_id:str):
    iris.delete_one({'_id' : ObjectId(obj_id)})
    return {'message' : 'flower deleted'}
