#importing in libraries

import pandas as pd 
import matplotlib.pyplot as plt

#base dataframe in pandas
df = pd.read_csv('IT_motives_2013.csv')

#quick overview
df.head()

df.info()
