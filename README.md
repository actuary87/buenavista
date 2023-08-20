# Power BI loves DuckDB

This is a fork from https://github.com/jwills/buenavista project.

The aim is to get Power BI to connect to DuckDB through Postgres wire protocal which enables Direct Query on DuckDB. This makes the Power BI file is relatively small as the data resides in the DuckDB file and the queries are sent to it where only results are sent back to Power BI.

Only postgres_proxy.py method is used.

## How does this project work:
It is difficult to be able to process every valid SQL query and sends it DuckDB.

Many of the queries Power BI will send to a real Postgres server won't affect the result (it's not pulling any data).

In this project, the postgres_proxy.py sends those queries to a real Postgres Server to get a real response that makes Power BI happy.

On the other hand, any SQL query that pulls actual data is redirected to the DuckDB file set in buenavista\config.py file.

## To try the example I set in this repo, please do the following:

Real Postgres Server side:

1. execute example\create_test_db_structure.sql on the real Postgres server after creating a database that matches the database name in the buenavista\config.py (test is the default value)
2. The real server won't have any data.

VSCode / Python side:

3. pip install -r requirements.txt (you can use a venv as well if you prefer)
4. Change the default values set in buenavista\config.py to the appropriate values
5. You can open the folder of the project in VSCode and click Ctrl+F5 to run it without debugging (or F5 for debugging mode)
6. Check the console for any errors: if you provide a wrong connection info to the real Postgres server you would see error messages instantly
7. If all is fine you should see Listening on 127.0.0.1:5433 (assuming you kept the default proxy port of 5433)

DuckDB and Power BI side:

8. You can examine the two tables (customers and orders) in the DuckDB file using DBeaver (important: you have to close any connection to the DuckDB file though when you run the proxy server)
9. example\PowerBI_loves_DuckDB.pbix file is already configured to connect to the Proxy server localhost:5433 with credentials postgres/postgres, db = test and it has one visual that summarizes the orders count and sum per person
10. Try to make changes to the DuckDB (insert or update) and refresh Power BI to see the changes coming through

If there are refresh/connection issues in Power BI:

11. In some cases, it's better to kill the Proxy server and re run it again to eliminate those issues

## Tutorial: Connect to your actual DuckDB database:

Let us first understand the tutorial which shows how example\PowerBI_loves_DuckDB.pbix was created:

1. There are 3 screenshots provided in tutorial folder. They demonstrate how to add DuckDB tables (Direct Query mode) to a fresh Power BI. Please follow them including the below steps
2. execute example\create_test_db_structure.sql on the real Postgres server after creating a database that matches the database name in the buenavista\config.py (test is the default value) [you will later use a helper script that dumps the structure of any DuckDB database]
3. The real server won't have any data.
4. In a fresh or existing Power BI file, go to Get Data > Database > PostgreSQL database [1.png]
5. Enter the Postgres Proxy server address:port (I used the default values: change if you changed the config.py file) [2.png]
6. Enter Database name: as in the Real Postgres server (default value is test: change if you changed the config.py file) [2.png]
7. Choose "Direct Query" mode and then click "OK" [2.png]
8. Select all tables that you want to import (in example/test.duckdb, there are only two tables) [3.png]
9. Important: Go to Model View and create relationships
10. You can create visuals now and test the performance

You can repeate all the above steps but in step 2, you can use tutorial/create_structure.py to dump the structure of any DuckDB:

1. Please change the DuckDB file in tutorial/create_structure.py (line 33)
2. After running the script, it will produce create_structure.sql file that you should use in step 2 above if you will connect to your own DuckDB instead of the one in the example folder
3. Read the comments in dump_information_schema_sql variable in create_structure.sql: I replaced certain DuckDB types to their equivalent in PostgreSQL. However, HUGEINT and the Unsigned INT (4 types) do not seem to have an equivalent in PostgreSQL. I mapped them all to BIGINT with a warning of a possible data loss. 

## Known issues
* Numbers and Dates are displayed as "Error" in Power Query or Table Import wizard. But they reflect correctly in Power BI Visuals (for example in Graphs, Table and Matrix visuals).


I will try to post a tutorial on how to connect a new Power BI file to the proxy server/DuckDB with screenshots very soon.
