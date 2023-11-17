# real Postgres connection info
real_postgres_server_address = "localhost"
real_postgres_server_port = 5432
real_postgres_server_user = "postgres"
real_postgres_server_password = "postgres"
#database_name = "test"
database_name = "test_data_types"

# postgres_proxy_server_port must be different than the real_postgres_server_port
postgres_proxy_server_port = 5433

# DuckDB file
#duckdb_file = "example/test.duckdb"
duckdb_file = "test_data_types/test_data_types.duckdb"