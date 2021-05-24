"""
Environment variables used in the docker-compose services of EpiGraphDB DOCS.
service name: docs
"""
from .env_utils import EnvConfigs, EnvVar

env_configs = EnvConfigs(
    docker_docs_port=EnvVar(
        "DOCS_PORT",
        default="8011",
        desc="""
        Port of the docs docker container
        """,
    )
)
