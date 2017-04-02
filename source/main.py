# Imports

# pandas
import pandas as pd

# get titanic & test csv files as a DataFrame
titanic_df = pd.read_csv("../data/input/train.csv")
test_df    = pd.read_csv("../data/input/test.csv")

# preview the data
print(titanic_df.head())
