"""
Environment variables used in the EpiGraphDB API documentation
"""
from .env_utils import EnvConfigs, EnvVar

configs = EnvConfigs(
    api_url=EnvVar(
        "API_URL",
        default="https://api.epigraphdb.org",
        desc="""
        URL to a running EpiGraphDB API
        (either a local instance or a remote one).

        Used for generating documentation.
        """,
    )
)
