"""
Environment variables used in the main api service
for epigraphdb_neural
"""
from .env_utils import EnvConfigs, EnvVar

env_configs = EnvConfigs(
    # paired elasticsearch
    es_host=EnvVar(
        "BACKEND_ES_HOST",
        default="localhost",
        desc="""
        Paired elasticsearch: server name
        either localhost, server name, or docker service name
        """,
    ),
    es_port=EnvVar(
        "BACKEND_ES_PORT",
        default="9200",
        desc="""
        Paired elasticsearch: port
        NOTE: when connecting to a paired service inside docker-compose,
        this port should be the internal port, not the exposed port.
        """,
    ),
    # paired models api
    models_api_url=EnvVar(
        "NEURAL_MODELS_API_URL",
        default="localhost:8015",
        desc="""
        url to the models api.
        """,
    ),
)
