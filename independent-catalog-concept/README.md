# An Independent `DataCatalog`

## Install

Install the Data Catalog with the following:
```commandline
pip install kedro
```

This installs the Data Catalog and provides a way to use the Data Catalog with both the code and YAML APIs.

## Usage

### Using the YAML API

#### What needs to happen?
- Create a configuration file specifying your data sources, see `catalog.yml`
- Load configuration
- Create your Data Catalog
- Install dependencies related to the `CSVDataSet` with `pip install "kedro[pandas.CSVDataSet]"`
- In the terminal run `python3 yaml_example.py`

#### Example
_catalog.yml_
```yaml
titanic_training_data:
  type: pandas.CSVDataSet
  filepath: train.csv
```

*yaml_example.py*
```python
from kedro.config import ConfigLoader
from kedro.io import DataCatalog

# Find the configuration (catalog.yaml) in the current working directory and load it
conf_loader = ConfigLoader(".")
conf_catalog = conf_loader.get("catalog*")

# Create the Data Catalog from the catalog.yml file
io = DataCatalog.from_config(conf_catalog)

# Load your file and print the output
df = io.load("titanic_training_data")
print(df.head())
```

The output of running *yaml_example.py*:

```commandline
   PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C
2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S
```

### Using the Python API

#### What needs to happen?
- Create a file called `example_.py`
- Create your Data Catalog
- Install dependencies related to the `CSVDataSet` with `pip install "kedro[pandas.CSVDataSet]"`
- In the terminal run `python3 code_example.py`

#### Example
*code_example.py*
```python
from kedro.io import DataCatalog
from kedro.extras.datasets.pandas import CSVDataSet

io = DataCatalog({"titanic_training_data": CSVDataSet(filepath="train.csv")})

# Load your file and print the output
df = io.load("titanic_training_data")
print(df.head())
```

The output of running _code_example.py_:

```commandline
   PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C
2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S
```