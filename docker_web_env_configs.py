"""
Environment variables used in the docker-compose services of EpiGraphDB web app.

# required
- backend: python backend
- frontned: vuejs frontend
- mongodb: caching
- elasticsearch: search

# optional
- dashboard: vuejs dashboard for internal analytics
- kibana: ELK UI
"""
from .env_utils import EnvConfigs, EnvVar

env_configs = EnvConfigs(
    docker_backend_port=EnvVar(
        "DOCKER_BACKEND_PORT",
        default="8010",
        desc="""
        backend: Port of the web backend docker container
        """,
    ),
    docker_frontend_port=EnvVar(
        "DOCKER_FRONTEND_PORT",
        default="8011",
        desc="""
        frontend: Port of the web frontend docker container
        """,
    ),
    docker_dashboard_port=EnvVar(
        "DOCKER_DASHBOARD_PORT",
        default="8012",
        desc="""
        dashboard: Port of the web dashboard docker container
        """,
    ),
    frontend_backend_url=EnvVar(
        "FRONTEND_BACKEND_URL",
        default="localhost:8010",
        desc="""
        frontend, dashboard:
        URL of a running backend service that for the frontend
        to connect to.
        """,
    ),
    frontend_gtag_id=EnvVar(
        "FRONTEND_GTAG_ID",
        secret=True,
        desc="""
        frontend: Google analytics ID
        NOTE: Only include this variable in a production server.
        """,
    ),
    mongo_passwd=EnvVar(
        "MONGO_PASSWD",
        secret=True,
        desc="""
        mongodb: Password of the mongodb service
        """,
    ),
    mongo_port=EnvVar(
        "DOCKER_MONGO_PORT",
        default="6570",
        desc="""
        mongodb: Container port
        """,
    ),
    es_port=EnvVar(
        "DOCKER_ES_PORT",
        default="6550",
        desc="""
        elasticsearch: Container port
        """,
    ),
    kibana_port=EnvVar(
        "DOCKER_KIBANA_PORT",
        default="6555",
        desc="""
        kibana: Container port
        """,
    ),
)
