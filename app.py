import numpy as np
import pandas as pd
url = 'kc_house_data.csv'
df = pd.read_csv(url)
columns = ['bedrooms','bathrooms','sqft_living','sqft_lot','floors','price']
df = df.loc[:, columns]
df = df.head(15)
df.sample(n = 15, replace = True, random_state = 2)
print(df.sample)