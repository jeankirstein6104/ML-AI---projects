from fastapi import FastAPI, HTTPException
from structure.schema_train import get_list, get_data
from  structure.url import iris_test
from structure.format import Predict
from models.iris_model import iris_predict
from bson.objectid import ObjectId


app = FastAPI()


# the following endpoints provide certain tasks like retrieving, updating and deleting info along with taking care of exceptions and errors

# to get all the available flower data in the database
@app.get('/get_all')
async def get_all():
    data = [flower for flower in iris_test.find()]
    if not data:
        return {'the document is empty'}
    return get_list(data)


# to insert a flower parameters in the database 
@app.post('/insert')
async def add_flower(flowers :Predict):
    iris_test.insert_one(dict(flowers))
    return {'message' : 'flower parameters added'}


# to predict the given flower from the features using id
@app.put('/predict/{obj_id}')
async def predict_flower(obj_id: str):
    
    try:
        data = iris_test.find_one({'_id' : ObjectId(obj_id)})
        return {'The flower belongs to the class' : iris_predict(get_data(data))}
    
    except Exception as e:
        return HTTPException(status_code = 500, detail = f"error occured {e}")


# to retrieve the features with an id
@app.put('/return/{obj_id}')
async def id_get(obj_id:str):
    
    try:
        data = iris_test.find_one({'_id':ObjectId(obj_id)})
        if not data:
            return HTTPException(status_code = 404, detail = "Id doesn't exist")
        return get_data(data)
    
    except Exception as e:
        return HTTPException(status_code = 500, detail = f"error occured {e}")
    
    
# to update a flower with an id
@app.put('/update/{obj_id}')
async def id_update(obj_id:str, updated_item:Predict):
    
    try:
        
        if not iris_test.find_one({'_id' : ObjectId(obj_id)}):
            return HTTPException(status_code = 404, detail = "Id doesn't exist")
        
        iris_test.update_one({'_id' : ObjectId(obj_id)},{'$set' : dict(updated_item)})
        return {'message' : 'flower parameters updated'}
    
    except Exception as e:
        return HTTPException(status_code = 500, detail = f"error occured {e}")


# to delete a flower with an id
@app.put('/delete/{obj_id}')
async def id_delete(obj_id:str):
    
    try:
        if not iris_test.find_one({'_id' : ObjectId(obj_id)}):
            return HTTPException(status_code = 404, detail = "Id doesn't exist")
        
        iris_test.delete_one({'_id' : ObjectId(obj_id)})
        return {'message' : 'flower parameters deleted'}

    except Exception as e:
        return HTTPException(status_code = 500, detail = f"error occured {e}")