
def get_info(flower): 
    return {'_id' : str(flower["_id"]),\
            'name' : str(flower["name"])}

def get_list(flowers):
    return [get_info(flower) for flower in flowers ]

#print((get_list([{'_id' : '123','name' : 'setosa'}, {'_id' : '124', 'name' : 'versicolor'}, {'_id' : '125', 'name' : 'virginica'}])))

