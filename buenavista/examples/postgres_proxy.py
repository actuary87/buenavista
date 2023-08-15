import buenavista.config as config

from buenavista.postgres import BuenaVistaServer
from buenavista.backends.postgres import PGConnection

address = ("localhost", config.postgres_proxy_server_port)
server = BuenaVistaServer(
    address,
    PGConnection(
        conninfo="",
        host=config.real_postgres_server_address,
        port=config.real_postgres_server_port,
        user=config.real_postgres_server_user,
        password=config.real_postgres_server_password,
        dbname=config.database_name,
    ),
)
ip, port = server.server_address
print(f"Listening on {ip}:{port}")
server.serve_forever()
