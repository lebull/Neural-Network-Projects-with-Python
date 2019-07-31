import pandas as pd
URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
df = pd.read_csv(URL, names = [
    'sepal_length', 
    'sepal_width', 
    'petal_length', 
    'petal_width', 
    'class'
])
print(df.info())