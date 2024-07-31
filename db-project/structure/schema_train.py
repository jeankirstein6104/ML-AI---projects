
# function to parse ObjectId from mongodb to a dictionary that can be read by python
def get_info(flower): 
    return {
            '_id' : str(flower["_id"]),
            'sepal_length_cm': str(flower['sepal_length_cm']),
            'sepal_width_cm': str(flower['sepal_width_cm']),
            'petal_length_cm': str(flower['petal_length_cm']),
            'petal_width_cm': str(flower['petal_width_cm'])   
           }

# extends get_info() to a list of dictionary
def get_list(flowers):
    return [get_info(flower) for flower in flowers ]

# function to convert flower features in dictionary to a list to be processed by the ml model
def get_data(flower):
    return [
            flower['sepal_length_cm'],
            flower['sepal_width_cm'],
            flower['petal_length_cm'], 
            flower['petal_width_cm']
           ]