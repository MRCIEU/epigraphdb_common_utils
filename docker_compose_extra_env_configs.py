"""
Environment variables used in the extra components in epigraphdb_compose.

Components in epigraphdb_compose are based on epigraphdb_web,
with a few extra (apis, graphs, etc)
"""
from .env_utils import EnvConfigs, EnvVar

env_configs = EnvConfigs(
    # api_public
    docker_api_port_public=EnvVar(
        "DOCKER_API_PORT_PUBLIC",
        default="8005",
        desc="""
        api_public: Port
        """,
    ),
    # graph
    graph_http_port=EnvVar(
        "GRAPH_HTTP_PORT",
        default="37474",
        desc="""
        graph: http port to the neo4j browser
        """,
    ),
    graph_bolt_port=EnvVar(
        "GRAPH_BOLT_PORT",
        default="37687",
        desc="""
        graph: Bolt port
        """,
    ),
    graph_https_port=EnvVar(
        "GRAPH_HTTPS_PORT",
        default="37473",
        desc="""
        graph: https port to the neo4j browser
        """,
    ),
    graph_user=EnvVar(
        "GRAPH_USER",
        secret=True,
        desc="""
        graph: User name
        """,
    ),
    graph_passwd=EnvVar(
        "GRAPH_PASSWD",
        secret=True,
        desc="""
        graph: Password
        """,
    ),
    graph_server=EnvVar(
        "GRAPH_SERVER",
        desc="""
        graph: Server name
        """,
    ),
    graph_readonly=EnvVar(
        "GRAPH_READONLY",
        default=True,
        desc="""
        graph: Override to enable writability.
        """,
    ),
    graph_heap_max=EnvVar("GRAPH_HEAP_MAX", default="40G"),
    graph_heap_initial=EnvVar("GRAPH_HEAP_INITIAL", default="10G"),
    graph_pagecache=EnvVar("GRAPH_PAGECACHE", default="10G"),
)
