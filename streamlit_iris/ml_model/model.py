import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import warnings

warnings.filterwarnings('ignore')

iris = load_iris()
iris_names = \
{
    0 : 'Setosa',
    1 : 'Vesicolor',
    2 : 'Virginica'
}

x = pd.DataFrame(iris.data, columns = iris.feature_names)
y = iris.target

xtr, xte, ytr, yte = train_test_split(x, y, test_size = 0.2)
model = SVC()
model.fit(xtr, ytr)

def iris_predict(iris_params):
    result = model.predict([iris_params])
    return iris_names[result[0]]






