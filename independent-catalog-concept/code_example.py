from kedro.io import DataCatalog
from kedro.extras.datasets.pandas import CSVDataSet

io = DataCatalog({"titanic_training_data": CSVDataSet(filepath="train.csv")})

# Load your file and print the output
df = io.load("titanic_training_data")
print(df.head())