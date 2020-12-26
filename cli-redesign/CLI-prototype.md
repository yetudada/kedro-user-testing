## Introduction
This issue looks interrogates the user experience of the CLI for global commands using a grouped `noun-first` approach with alias commands for frequently used commands. 

At a high-level, this CLI uses the following pattern: 
```commandline
Usage:
  kedro [OPTIONS] [VERB]
  kedro [OPTIONS] [NOUN] [VERB]
```

## What are the biggest changes for the CLI? 
- The user experience of `kedro new` and `kedro starter` are merged
- The entry of a single project name instead of:
  - Project name
  - Repository name
  - Python package name
- Introduction of a `kedro project` group
- Ease of viewing improvements, you will see a lot of groups
- New commands including `kedro catalog delete`

## The Global CLI 
We can see a redesigned CLI that appears when you run `kedro`. It has space for where you can find documentation, get help and share feedback. 

### Run `kedro`

#### Current view
```bash
(my-virtual-environment) ➜  ~ kedro
Usage: kedro [OPTIONS] COMMAND [ARGS]...

  Kedro is a CLI for creating and using Kedro projects For more information,
  type ``kedro info``.

  When inside a Kedro project (created with `kedro new`) commands from the
  project's `cli.py` file will also be available here.

  Visualize the pipeline using kedroviz.

Options:
  -V, --version  Show version and exit
  -h, --help     Show this message and exit.

Global commands from Kedro
Commands:
  docs     See the kedro API docs and introductory tutorial.
  info     Get more information about kedro.
  new      Create a new kedro project.
  starter  Commands for working with project starters.

Global commands from Kedro-Viz
Commands:
  viz  Visualize the pipeline using kedroviz.
```

#### Future view
```bash
(my-virtual-environment) ➜  ~ kedro
Usage: kedro [OPTIONS] COMMAND [ARGS]...

  A Python framework for reproducible, maintainable and modular data science code.

  Read the documentation - https://kedro.readthedocs.io/en/stable/
  Ask questions on Discourse - https://discourse.kedro.community/
  Provide feedback about Kedro - https://feedback.quantumblack.com/kedro

Global commands from Kedro
Commands:
  docs     See the Kedro tutorials and API docs.
  info     Get more information about Kedro.
  starter  Create a new project or find examples.

Global commands from Kedro-Viz
Commands:
  viz  Visualize a pipeline using Kedro-Viz.

Options:
  -V, --version  Show version and exit
  -v, --verbose  See extensive logging and error stack traces.
  -h, --help     Show this message and exit.
```

### Run `kedro docs` 

#### Curent view
```bash
(my-virtual-environment) ➜  ~ kedro docs
Opening file:///Users/yetunde_dada/opt/anaconda3/envs/my-virtual-environment/lib/python3.7/site-packages/kedro/framework/html/index.html
```

#### Future view
```bash
(my-virtual-environment) ➜  ~ kedro docs

Opening file:///Users/yetunde_dada/opt/anaconda3/envs/my-virtual-environment/lib/python3.7/site-packages/kedro/framework/html/index.html
```

### Run `kedro info`

#### Current view
```bash
(my-virtual-environment) ➜  ~ kedro info

 _            _
| | _____  __| |_ __ ___
| |/ / _ \/ _` | '__/ _ \
|   <  __/ (_| | | | (_) |
|_|\_\___|\__,_|_|  \___/
v0.17.1

kedro allows teams to create analytics
projects. It is developed as part of
the Kedro initiative at QuantumBlack.

Installed plugins:
kedro_viz: 3.8.0 (hooks:global,line_magic)
```

#### Future view

```
(my-virtual-environment) ➜  ~ kedro info
 _            _
| | _____  __| |_ __ ___
| |/ / _ \/ _` | '__/ _ \
|   <  __/ (_| | | | (_) |
|_|\_\___|\__,_|_|  \___/
v0.17.1

Kedro is a Python framework for 
creating reproducible, maintainable 
and modular data science code. It 
borrows concepts from software 
engineering and applies them to 
machine-learning code. It was 
developed and open-sourced by 
QuantumBlack, a McKinsey Company.

Installed plugins:
kedro_viz: 3.8.0 (hooks: global, line_magic)
```

### Running `kedro new`, `kedro starter` and `kedro starter list`

#### Current view
```bash
(my-virtual-environment) ➜  ~ kedro new
Project Name:
=============
Please enter a human readable name for your new project.
Spaces and punctuation are allowed.
 [New Kedro Project]: Example Project

Repository Name:
================
Please enter a directory name for your new project repository.
Alphanumeric characters, hyphens and underscores are allowed.
Lowercase is recommended.
 [example-project]: 

Python Package Name:
====================
Please enter a valid Python package name for your project package.
Alphanumeric characters and underscores are allowed.
Lowercase is recommended. Package name must start with a letter or underscore.
 [example_project]: 

Change directory to the project generated in /Users/yetunde_dada/example-project

A best-practice setup includes initialising git and creating a virtual environment before running `kedro install` to install project-specific dependencies. Refer to the Kedro documentation: https://kedro.readthedocs.io/
```

```bash
(my-virtual-environment) ➜  ~ kedro starter
Usage: kedro starter [OPTIONS] COMMAND [ARGS]...

  Commands for working with project starters.

Options:
  -h, --help  Show this message and exit.

Commands:
  list  List all official project starters available.

(my-virtual-environment) ➜  ~ kedro starter list
- mini-kedro: https://github.com/quantumblacklabs/kedro-starters/tree/master/mini-kedro
- pandas-iris: https://github.com/quantumblacklabs/kedro-starters/tree/master/pandas-iris
- pyspark: https://github.com/quantumblacklabs/kedro-starters/tree/master/pyspark
- pyspark-iris: https://github.com/quantumblacklabs/kedro-starters/tree/master/pyspark-iris
- spaceflights: https://github.com/quantumblacklabs/kedro-starters/tree/master/spaceflights
```

#### Future view

```bash
(my-virtual-environment) ➜  ~ kedro starter
Usage: kedro starter [OPTIONS] COMMAND [ARGS]...

  Commands working with project templates and examples.

Options:
  -h, --help  Show this message and exit.

Commands:
  list  List all project templates or examples.
  pull  Pull a project template or example. 

(my-virtual-environment) ➜  ~ kedro starter list
- blank: A blank project template
- mini-kedro: Use the Data Catalog and a Jupyter notebook
- nhs: A healthcare dataset example with a PySpark workflow
- pandas-iris: An Iris dataset example with a pandas workflow
- pyspark: A blank project template configured with PySpark
- pyspark-iris: An Iris dataset example with a PySpark workflow
- spaceflights: A spaceflights example with a pandas workflow

To pull the example, type: 
kedro starter pull "template-name"

(my-virtual-environment) ➜  ~ kedro starter pull "blank"
Please enter a name for your project: Example Project
```

```
Change directory to the project generated in /Users/yetunde_dada/new-kedro-project by entering `cd /Users/yetunde_dada/new-kedro-project`

The project name "Example Project" has been applied to:
- The project title in /Users/yetunde_dada/example-project/README.md
- The folder created for your project in /Users/yetunde_dada/example-project
- The project's python package in /Users/yetunde_dada/example-project/src/example_project

A best-practice setup includes initialising git and creating a virtual environment, refer to the documentation: https://kedro.readthedocs.io/
```

## The Project-Level CLI 

### Run `kedro`
#### Current view
```bash
(my-virtual-environment) ➜  example-project kedro
Usage: kedro [OPTIONS] COMMAND [ARGS]...

  Kedro is a CLI for creating and using Kedro projects For more information,
  type ``kedro info``.

  When inside a Kedro project (created with `kedro new`) commands from the
  project's `cli.py` file will also be available here.

  Visualize the pipeline using kedroviz.

  Command line tools for manipulating a Kedro project.

Options:
  -V, --version  Show version and exit
  -h, --help     Show this message and exit.

Global commands from Kedro
Commands:
  docs     See the kedro API docs and introductory tutorial.
  info     Get more information about kedro.
  new      Create a new kedro project.
  starter  Commands for working with project starters.

Global commands from Kedro-Viz
Commands:
  viz  Visualize the pipeline using kedroviz.

Project specific commands from /Users/yetunde_dada/example-project/src/example_project/cli.py
Commands:
  activate-nbstripout  Install the nbstripout git hook to automatically...
  build-docs           Build the project documentation.
  build-reqs           Build the project dependency requirements.
  catalog              Commands for working with catalog.
  install              Install project dependencies from both...
  ipython              Open IPython with project specific variables loaded.
  jupyter              Open Jupyter Notebook / Lab with project specific...
  lint                 Run flake8, isort and black.
  package              Package the project as a Python egg and wheel.
  pipeline             Commands for working with pipelines.
  run                  Run the pipeline.
  test                 Run the test suite.
```

#### Future view
```bash
(my-virtual-environment) ➜  ~ kedro
Usage: kedro [OPTIONS] COMMAND [ARGS]...

  A Python framework for reproducible, maintainable and modular data science code.

  Read the documentation - https://kedro.readthedocs.io/en/stable/
  Ask questions on Discourse - https://discourse.kedro.community/
  Provide feedback about Kedro - https://feedback.quantumblack.com/kedro

Global commands from Kedro
Commands:
  docs     See the Kedro tutorials and API docs.
  info     Get more information about Kedro.
  starter  Create a new project or find examples.

Global commands from Kedro-Viz
Commands:
  viz  Visualize a pipeline using Kedro-Viz.

Options:
  -V, --version  Show version and exit.
  -v, --verbose  See extensive logging and error stack traces.
  -h, --help     Show this message and exit.

Project commands from /Users/yetunde_dada/example-project/src/example_project/cli.py
Command groups for project components:
  project               Access commands that apply to the project. 
  pipeline              Access commands that apply to a pipeline or modular pipeline.
  catalog               Access commands that apply to the Data Catalog.

Execution commands for the project:
  build-docs            Build documentation for the project.
  build-reqs            Build dependency requirements for the project.
  install               Install project dependencies.
  lint                  Lint the project with Black, Flake8 and Isort.
  run                   Run the project's default pipeline.
  test                  Run the project's test suite.

Prototyping commands:
  ipython               Open a kedro-instance of IPython.
  jupyter               Access commands for Jupyter Notebook.

Activation hooks and scripts:
  completion            Activate the tab autocompletion script for the CLI.
  nbstripout         Activate the nbstripout git hook.
```

### Run `kedro project`

```
(my-virtual-environment) ➜  ~ kedro project
Usage: kedro project [OPTIONS] COMMAND...

  Access commands that apply to the project.

Commands:
  build-docs            Build documentation for the project.
  build-reqs            Build dependency requirements for the project.
  install               Install project dependencies.
  lint                  Lint the project with Black, Flake8 and Isort.
  package               Package the project as a Python egg and wheel.
  test                  Run the project's test suite.
  run                   Run the project's default pipeline.

Options:
  -h, --help         Show this message and exit.
```

### Run `kedro pipeline`

#### Current view
```bash
(my-virtual-environment) ➜  example-project kedro pipeline 
Usage: kedro pipeline [OPTIONS] COMMAND [ARGS]...

  Commands for working with pipelines.

Options:
  -h, --help  Show this message and exit.

Commands:
  create    Create a new modular pipeline by providing the new pipeline
            name...

  delete    Delete a modular pipeline by providing the pipeline name as an...
  describe  Describe a pipeline by providing the pipeline name as an...
  list      List all pipelines defined in your hooks.py file.
  package   Package up a pipeline for easy distribution.
  pull      Pull a modular pipeline package, unpack it and install the
            files...
```

#### Future view
```bash
(my-virtual-environment) ➜  example-project kedro pipeline 
Usage: kedro pipeline [OPTIONS] COMMAND [ARGS]...

  Access commands that apply to a pipeline or modular pipeline.

Options:
  -h, --help  Show this message and exit.

Commands for pipelines registered on the CLI:
  describe  List nodes and datasets in a pipeline. 
  list      List all pipelines registered to display on the CLI.
  run       Run a pipeline.
  
Modular pipeline commands: 
  create    Create a new modular pipeline.
  delete    Delete a modular pipeline.
  package   Package a modular pipeline for easy distribution.
  pull      Pull a modular pipeline package into your project.
```

### Run `kedro catalog`
#### Current view
```bash
(my-virtual-environment) ➜  example-project kedro catalog
Usage: kedro catalog [OPTIONS] COMMAND [ARGS]...

  Commands for working with catalog.

Options:
  -h, --help  Show this message and exit.

Commands:
  create  Create Data Catalog YAML configuration with missing datasets.
  delete  Delete datasets that are not used in any pipeline.
  list    Show datasets per type.
```

#### Future view
```bash
(my-virtual-environment) ➜  example-project kedro catalog
Usage: kedro catalog [OPTIONS] COMMAND [ARGS]...

  Access commands that apply to the Data Catalog.

Options:
  -h, --help  Show this message and exit.

Commands:
  create  Create Data Catalog YAML configuration for missing datasets.
  list    Show datasets per type.
```

### Run `kedro jupyter` 

#### Current view
```bash
(my-virtual-environment) ➜  example-project kedro jupyter
Usage: kedro jupyter [OPTIONS] COMMAND [ARGS]...

  Open Jupyter Notebook / Lab with project specific variables loaded, or
  convert notebooks into Kedro code.

Options:
  -h, --help  Show this message and exit.

Commands:
  convert   Convert selected or all notebooks found in a Kedro project to...
  lab       Open Jupyter Lab with project specific variables loaded.
  notebook  Open Jupyter Notebook with project specific variables loaded.
```

#### Future view
```bash
(my-virtual-environment) ➜  example-project kedro jupyter
Usage: kedro jupyter [OPTIONS] COMMAND [ARGS]...

  Access commands for Jupyter Notebook.

Options:
  -h, --help  Show this message and exit.

Commands:
  lab                Open Jupyter Lab with project-specific variables loaded.
  notebook           Open Jupyter Notebook with project-specific variables loaded. 
  convert            Convert selected or all notebooks into Python script.
```
