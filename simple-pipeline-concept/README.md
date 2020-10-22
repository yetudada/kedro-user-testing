# Simple Pipeline Concept 
_Almost a single pipeline, but I just couldn't let go of configuration_

It also shows how to use Kedro as a library, with library components. 

## What is this thing? 
When you work with a more complex workflow in Kedro you have to interact with the following files:
- `catalog.yaml` for your data sources in configuration 
- `nodes.py` for your Python functions
- `pipline.py` for your pipeline
- `hooks.py` to register your pipeline so that it appears on the CLI (not used)
- `parameters.yaml` for your parameters in configuration (not used)

This design proposes introducing users to a two file workflow: 
- `catalog.yaml` for data source configuration
- A single `pipeline.py` file that merges the `pipeline.py` and `nodes.py` file into one thing

It dodges the KedroContext and just uses the library components of Kedro, but like this, you cannot access the CLI to run or visualise this pipeline. 

## Goals of this design
- Teach users that they don't have to use the whole framework if they don't want to
- Show them how to use Kedro as a libary

## Prototype

_pipeline.py_
```
import matplotlib.pyplot as plt
from kedro.config import ConfigLoader
from kedro.io import DataCatalog
from kedro.pipeline import Pipeline, node
from kedro.runner import SequentialRunner

conf_loader = ConfigLoader(".")
conf_catalog = conf_loader.get("catalog*", "catalog*/**")

# Create the Data Catalog
io = DataCatalog.from_config(conf_catalog)


# Create nodes by writing Python functions
# Remove NaN values
def clean_raw_data(df):
    df = df.drop(["Ticket", "Cabin"], axis=1)
    df = df.dropna()
    return df


# Plot the amount of people who survived and who died.
def plot_survival_breakdown(df):
    plt.figure(figsize=(6, 4))
    fig, ax = plt.subplots()
    df.Survived.value_counts().plot(kind="barh", color="blue", alpha=0.65)
    ax.set_ylim(-1, len(df.Survived.value_counts()))
    plt.title("Survival Breakdown (1 = Survived, 0 = Died)")
    return fig


# Create nodes
clean_data_node = node(
    func=clean_raw_data, 
    inputs="titanic_training_data", 
    outputs="df_clean"
)

plot_survival_breakdown_node = node(
    func=plot_survival_breakdown, 
    inputs="df_clean", 
    outputs="survival_breakdown_chart"
)

# Assemble nodes into a pipeline
pipeline = Pipeline([clean_data_node, plot_survival_breakdown_node])

# Create a runner to run the pipeline
runner = SequentialRunner()

# Run the pipeline
print(runner.run(pipeline, io))
```

_catalog.yml_
```
# Input Dataset
titanic_training_data:
  type: pandas.CSVDataSet
  filepath: train.csv

# Chart Output
survival_breakdown_chart:
  type: matplotlib.MatplotlibWriter
  filepath: survival_breakdown.png
```

## Usage instructions
- Create a Python virtual environment with Python 3.7 and activate it
- Run `pip install "kedro[pandas.CSVDataSet]" && pip install matplotlib"`
- Use the terminal to run `pipeline.py` by typing `python pipeline.py`


## Credits
I used part of [Tam Nguyen's](https://github.com/tamsanh/kedro-introduction-tutorial) introductory tutorial to make this. And he credits:
- @agconti for their work that was used in the tutorial
- And Kaggle.com, the provider of this titanic dataset in the competition Titanic: Machine Learning from Disaster
