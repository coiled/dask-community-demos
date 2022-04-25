# dask-community-demos

Reproducers and demos for community issues.

## Creating a local environment

The `environment.yml` and `conda-lock.yml` file in this repository can be used to create a local Conda environment to debug issues.

### `conda-lock.yml`

`conda-lock.yml` has all the versions of packages solved so should install faster. However, dependencies may be out-of-date. You can create an environment with `conda-lock.yml` by installing `conda-lock` (this will install into the `base` environment, but that's not strictly necessary):

```shell
mamba install -n base -c conda-forge conda-lock
```

Then, you can run `conda-lock` to create an environment:

```shell
conda-lock install --name dask-community-demos conda-lock.yml
```

Since the environment has already been solved, this is a relatively fast operation.

#### Updating `conda-lock.yml`

If you want to update package versions in `conda-lock.yml`, you can do so by:

1. Updating/adding the pin in `environment.yml` and creating a new `conda-lock.yml` file, `conda-lock -f environment.yml -p osx-arm64 -p linux-64 -p linux-aarch64 -p win-64 -p osx-64`. This will also update all the packages specified in `environment.yml`.
2. Running `conda-lock --update <dependency>`. I _think_ this will only update that one dependency and any of its dependencies that become incompatible, but I haven't tried it.

### `environment.yml`

`environment.yml` is the base file used to create `conda-lock.yml`, but does not have the solution for any package versions. Using `environment.yml` will get you the most up-to-date dependencies but make take longer to solve the environment. To create an environment with `environment.yml` run:

```shell
mamba env create -f environment.yml
```

which will create an environment named `dask-community-demos`. You can update an existing environment by running:

```shell
mamba env update -n <name-of-environment> -f environment.yml
```

The `-n <name-of-environment>` can be omitted if the environment is activated.
