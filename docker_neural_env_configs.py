"""
Environment variables used in the main api service
for epigraphdb_neural
"""
from .env_utils import EnvConfigs, EnvVar

env_configs = EnvConfigs(
    docker_neural_port=EnvVar(
        "DOCKER_NEURAL_PORT",
        default="8015",
        desc="""
        port used by `neural`
        """,
    ),
)
