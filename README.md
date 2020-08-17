# Common utilities for EpiGraphDB infrastructure

Common utilities shared by the following components of the infrastructure:

- `epigraphdb_compose`
- `epigraphdb_api`
- `epigraphdb_web`

At the moment, the common utils contain the following

- environment variable usage by various components,
  i.e. python servers and docker containers.

## Environment variable configs

When setting up the API, check the following configs:

- `api_env_configs.py` for the main python server
- `docker_api_env_configs.py` for the docker container
- `api_docs_env_configs.py` for generating metrics documents

When setting up the web app, check the following configs

- `backend_env_configs.py` for the main python server
- `docker_web_env_configs.py` for the docker containers

When setting up the whole infrastructure (`epigraphdb_compose`),
check the following configs

- `api_env_configs.py`
- `docker_api_env_configs.py`
- `backend_env_configs.py`
- `docker_web_env_configs.py`
- `docker_compose_extra_env_configs.py`
