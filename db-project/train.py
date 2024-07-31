from fastapi import FastAPI
from structure.schema_train import get_list, get_data
from structure.url import iris_test
from structure.format import Item, Predict
from models.iris_model import iris_predict
from bson.objectid import ObjectId



app = FastAPI()

# to get all the available flower data in the database
@app.get('/get_all')
async def get_all():
    data = [flower for flower in iris_test.find()]
    return get_list(data)

# to insert a flower parameters in the database 
@app.post('/insert')
async def add_flower(flowers :Predict):
    iris_test.insert_one(dict(flowers))
    return {'message' : 'flower inserted'}

# to predict the given flower from the features using id
@app.put('/predict/{obj_id}')
async def predict_flower(obj_id: str):
    data = iris_test.find_one({'_id' : ObjectId(obj_id)})
    return iris_predict(get_data(data))


# to retrieve the features with an  id
# @app.put('/return/{obj_id}')
# async def id_get(obj_id:str):
#     data = [iris.find_one({'_id':ObjectId(obj_id)})]
#     return get_list(data)

# # to update a flower with an id
# @app.put('/update/{obj_id}')
# async def id_update(obj_id:str, updated_item:Item):
#     iris.update_one({'_id' : ObjectId(obj_id)},{'$set' : dict(updated_item)})
#     return {'message' : 'flower updated'}

# # to delete a flower with an id
# @app.put('/delete/{obj_id}')
# async def id_delete(obj_id:str):
#     iris.delete_one({'_id' : ObjectId(obj_id)})
#     return {'message' : 'flower deleted'}
