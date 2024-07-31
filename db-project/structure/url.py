from pymongo import MongoClient

#mongodb cloud database connection link
client = MongoClient('mongodb+srv://jeankirstein6104:UaSXsPMMz99Acj9v@basics-projects.buat5ge.mongodb.net/?retryWrites=true&w=majority&appName=basics-projects')
db = client.flowers

#iris_test is the name of the collection in which flower parameters are stored
iris_test = db.iris_testing
