# Telemetry

## Current view

### `kedro new` workflow

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
 
Usage Statistics: 
=================
As an open source project, we collect usage statistics. We cannot see and do
not store information contained in Kedro projects. You can find out more by
reading our privacy policy at: 
https://github.com/quantumblacklabs/kedro/blob/master/PRIVACY_POLICY.md 
And you can look at the source code of our telemetry plugin: 
https://github.com/quantumblacklabs/kedro-telemetry

Would you like to share usage statistics with the Kedro team to improve Kedro? [yN]
```

```
Change directory to the project generated in /Users/yetunde_dada/example-project

A best-practice setup includes initialising git and creating a virtual environment before running `kedro install` to install project-specific dependencies. Refer to the Kedro documentation: https://kedro.readthedocs.io/
```

### `kedro starter` workflow
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

## Problems
This user journey:
- Asks a lot of questions
- Has a disjoint user workflow for `kedro starter` 

Can we reduce the number of questions and have a unified workflow for `kedro new` and `kedro starter`? 
