"""
Environment variables used in the EpiGraphDB API (public) container.
service name: api_public
"""
from .env_utils import EnvConfigs, EnvVar

configs = EnvConfigs(
    docker_api_port_public=EnvVar(
        "DOCKER_API_PORT_PUBLIC",
        default="8005",
        desc="""
        Port of the API docker container
        """,
    )
)
