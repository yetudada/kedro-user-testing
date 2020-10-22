from kedro.config import ConfigLoader
from kedro.io import DataCatalog

# Find the configuration (catalog.yaml) in the current working directory and load it
conf_loader = ConfigLoader(".")
conf_catalog = conf_loader.get("catalog*")

# Create the Data Catalog from the catalog.yml file
io = DataCatalog.from_config(conf_catalog)
df = io.load("titanic_training_data")
print(df.head())