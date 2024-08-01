Flower API with FastAPI and MongoDB

This project is a FastAPI backend service built with Python that interfaces with a cloud MongoDB database. 
It is designed to store and manage flower parameters, including sepal length, sepal width, petal length, 
and petal width. Additionally, it incorporates a machine learning model to predict the type of flower based
on these parameters.

Features

*	Add Flower Parameters: Insert new flower data into the database.
*	Retrieve Flower Parameters: Access stored flower data using the ObjectId.
*	Update Flower Parameters: Modify existing flower data.
*	Delete Flower Parameters: Remove flower data from the database.
*	Predict Flower Type: Utilize a pre-trained iris prediction model from sklearn to classify the type of
  flower based on its parameters.

Technology Stack

1. Backend Framework: FastAPI
2. Database: Cloud MongoDB
3. Machine Learning Model: Sklearn
