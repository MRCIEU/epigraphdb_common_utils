"""
Environment variables used in the python fastapi backend of EpiGraphDB web app
"""
from .env_utils import EnvConfigs, EnvVar

env_configs = EnvConfigs(
    # backend
    use_cache=EnvVar(
        "USE_CACHE",
        default=True,
        desc="""
        Enable caching.
        """,
    ),
    # paired private API
    api_url=EnvVar(
        "API_URL",
        desc="""
        Paired EpiGraphDB private API: URL
        """,
    ),
    api_key=EnvVar(
        "API_KEY",
        secret=True,
        desc="""
        Paired EpiGraphDB private API: API key
        """,
    ),
    # paired mongodb
    mongo_passwd=EnvVar(
        "MONGO_PASSWD",
        secret=True,
        desc="""
        Paired mongodb: password
        """,
    ),
    mongo_host=EnvVar(
        "BACKEND_MONGO_HOST",
        default="localhost",
        desc="""
        Paired mongodb: server name
        either localhost, server name, or docker service name
        """,
    ),
    mongo_port=EnvVar(
        "BACKEND_MONGO_PORT",
        default="27017",
        desc="""
        Paired mongodb: port
        NOTE: when connecting to a paired service inside docker-compose,
        this port should be the internal port, not the exposed port.
        """,
    ),
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
)
