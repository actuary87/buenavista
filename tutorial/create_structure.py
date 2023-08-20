import duckdb
import pandas as pd


dump_information_schema_sql = \
"""
select
    table_schema,
    table_name,
    column_name,
    case
        when data_type = 'BLOB' then 'BYTEA'
        when data_type = 'DOUBLE' then 'DOUBLE PRECISION'
		when data_type = 'FLOAT' then 'REAL'
		when data_type = 'TINYINT' then 'SMALLINT'
        -- Notes about the following data types:
		-- no exact match but map all these to BIGINT
		-- there is a possible value loss
		when data_type = 'HUGEINT' then 'BIGINT'
		when data_type = 'UBIGINT' then 'BIGINT'
		when data_type = 'UINTEGER' then 'BIGINT'
		when data_type = 'USMALLINT' then 'BIGINT'
		when data_type = 'UTINYINT' then 'BIGINT'
        else data_type
    end as "data_type"
from information_schema.columns
order by
	table_schema,
    table_name,
    ordinal_position
"""

con = duckdb.connect('test.db', read_only=True)

df = con.sql(dump_information_schema_sql).df() \
        .assign(schema_table = lambda df: df['table_schema'] + '.' + df['table_name']) \
        .assign(column_columntype = lambda df: '    "' + df['column_name'] + '" ' + df['data_type'])
con.close()


sql = ''

for schema in df['table_schema'].unique():
    sql += f'CREATE SCHEMA IF NOT EXISTS {schema};\n\n'

for schema_table in df['schema_table'].unique():
    columns = ',\n'.join(df.query(f'schema_table == "{schema_table}"') \
                            ['column_columntype'] \
                            .to_list())
    query = f'''CREATE TABLE IF NOT EXISTS {schema_table} (\n{columns}\n);\n\n'''
    sql += query

with open('create_structure.sql', 'w') as f:
    f.write(sql)