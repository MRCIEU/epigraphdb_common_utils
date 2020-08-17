"""
Environment variables used in the docker-compose services of EpiGraphDB API.
service name: api_private
"""
from .env_utils import EnvConfigs, EnvVar

env_configs = EnvConfigs(
    docker_api_port_private=EnvVar(
        "DOCKER_API_PORT_PRIVATE",
        default="8006",
        desc="""
        Port of the API docker container
        """,
    )
)
