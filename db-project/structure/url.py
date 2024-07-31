from pymongo import MongoClient

client = MongoClient('mongodb+srv://jeankirstein6104:UaSXsPMMz99Acj9v@basics-projects.buat5ge.mongodb.net/?retryWrites=true&w=majority&appName=basics-projects')
db = client.flowers
iris = db.iris_samples
iris_test = db.iris_testing
#mongodb+srv://jeankirstein6104:<password>@basics-projects.buat5ge.mongodb.net/?retryWrites=true&w=majority&appName=basics-projects