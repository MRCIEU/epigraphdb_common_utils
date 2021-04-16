"""
Environment variables used in the EpiGraphDB API python server
"""
from .env_utils import EnvConfigs, EnvVar

env_configs = EnvConfigs(
    api_private_access=EnvVar(
        "API_PRIVATE_ACCESS",
        default=True,
        desc="""
        If True, will enable several endpoints that are restricted to
        an internal / private API instance.
        """,
    ),
    api_key=EnvVar(
        "API_KEY",
        secret=True,
        desc="""
        API key to access restricted endpoints

        NOTE: this only applies to the private API instance.
        """,
    ),
    # epigraphdb graph
    epigraphdb_server=EnvVar(
        "EPIGRAPHDB_SERVER",
        default="0.0.0.0",
        desc="""
        EpiGraphDB graph: server name / ip address
        """,
    ),
    epigraphdb_port=EnvVar(
        "EPIGRAPHDB_PORT",
        default="7687",
        desc="""
        EpiGraphDB graph: bolt port
        """,
    ),
    epigraphdb_user=EnvVar(
        "EPIGRAPHDB_USER",
        secret=True,
        desc="""
        EpiGraphDB graph: User name
        """,
    ),
    epigraphdb_passwd=EnvVar(
        "EPIGRAPHDB_PASSWD",
        secret=True,
        desc="""
        EpiGraphDB graph: Password
        """,
    ),
    epigraphdb_db_version=EnvVar(
        "EPIGRAPHDB_DB_VERSION",
        default="1.0",
        desc="""
        EpiGraphDB graph: version number

        Also used as the overall platform version
        """,
    ),
    # public epigraphdb graph
    public_epigraphdb_server=EnvVar(
        "PUBLIC_EPIGRAPHDB_SERVER",
        default="0.0.0.0",
        desc="""
        EpiGraphDB graph (public): server name / ip address
        """,
    ),
    public_epigraphdb_port=EnvVar(
        "PUBLIC_EPIGRAPHDB_PORT",
        default="7687",
        desc="""
        EpiGraphDB graph (public): bolt port
        """,
    ),
    # pqtl graph
    pqtl_server=EnvVar(
        "PQTL_SERVER",
        desc="""
        PQTL graph: server name / ip address
        """,
    ),
    pqtl_port=EnvVar(
        "PQTL_PORT",
        desc="""
        PQTL graph: bolt port
        """,
    ),
    pqtl_user=EnvVar(
        "PQTL_USER",
        secret=True,
        desc="""
        PQTL graph: User name
        """,
    ),
    pqtl_passwd=EnvVar(
        "PQTL_PASSWD",
        secret=True,
        desc="""
        PQTL graph: Password
        """,
    ),
    pqtl_db_version=EnvVar(
        "PQTL_DB_VERSION",
        default="3.0",
        desc="""
        PQTL graph: version number
        """,
    ),
)
