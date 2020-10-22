import matplotlib.pyplot as plt
from kedro.config import ConfigLoader
from kedro.io import DataCatalog
from kedro.pipeline import Pipeline, node
from kedro.runner import SequentialRunner

# Find the configuration (catalog.yaml) in the current working directory and load it
conf_loader = ConfigLoader(".")
conf_catalog = conf_loader.get("catalog*")

# Create the Data Catalog from the catalog.yml file
io = DataCatalog.from_config(conf_catalog)
df = io.load("titanic_training_data")


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
    clean_raw_data, inputs="titanic_training_data", outputs="df_clean"
)
plot_survival_breakdown_node = node(
    plot_survival_breakdown, inputs="df_clean", outputs="survival_breakdown_chart"
)

# Assemble nodes into a pipeline
pipeline = Pipeline([clean_data_node, plot_survival_breakdown_node])

# Create a runner to run the pipeline
runner = SequentialRunner()

# Run the pipeline
print(runner.run(pipeline, io))
